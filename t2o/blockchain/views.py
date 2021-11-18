import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializer import L3Serializer
from .utils import *


# Create your views here.
@api_view(['GET', 'PUT'])
def save_orders(request, crypto, fiat):
    # Request
    resp = requests.get(f'https://api.blockchain.com/v3/exchange/l3/{crypto}-{fiat}')

    if request.method == 'GET':
        return Response(resp.json())

    if request.method == 'PUT':
        if resp.status_code == 200:
            # get or create both currencies
            cryptocurrency, create_crypto = CryptoCurrencies.objects.get_or_create(name=crypto)
            fiatcurrency, created_fiat = FiatCurrencies.objects.get_or_create(name=fiat)
            # fix the data
            data_dict = fix_request_data(resp.json())
            # check if data is valid
            l3_serialized = L3Serializer(data=data_dict, many=True)
            # if data is valid, insert data in database
            if l3_serialized.is_valid():
                # create version id
                l3_version = L3Version.objects.create()
                # add both currencies to the received data and save
                l3_serialized.save(cryptocurrencies=cryptocurrency,
                                   fiatcurrencies=fiatcurrency,
                                   version=l3_version,)

                return Response(l3_serialized.data, status=status.HTTP_200_OK)
            else:
                return Response(l3_serialized.errors(), status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(resp.json(), status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def order_statistics(request, type_of_order, crypto, fiat):
    if type_of_order in ['bids', 'asks']:
        crypto_obj = get_object_or_404(CryptoCurrencies, name=crypto)
        fiat_obj = get_object_or_404(FiatCurrencies, name=fiat)

        qs = L3.objects.filter(order_type=type_of_order,
                               cryptocurrencies=crypto_obj,
                               fiatcurrencies=fiat_obj)
        if len(qs) == 0:
            return Response('Empty data', status=status.HTTP_404_NOT_FOUND)
        else:
            df = prepare_specific_l3(qs)
            dict_to_response = calculate_specific_statistics(df, type_of_order)
        return Response(dict_to_response, status=status.HTTP_200_OK)
    else:
        return Response('Wrong URL', status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def general_statistics(request):
    qs = L3.objects.all()
    df = prepare_general_l3(qs)
    if len(qs) == 0:
        return Response('Empty data', status=status.HTTP_404_NOT_FOUND)
    else:
        dict_to_response = calculate_general_statistics(df)
        return Response(dict_to_response, status=status.HTTP_200_OK)

