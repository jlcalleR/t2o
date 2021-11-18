import pandas as pd


def fix_request_data(data: dict) -> dict:
    """Transform input data from the request to data available to be serialized and saved"""
    output_list = list()
    for e in ['bids', 'asks']:
        for i in data[e]:
            i['type_of_order'] = e
            output_list.append(i)
    return output_list


def prepare_specific_l3(qs) -> pd.DataFrame:
    """Get the necessary columns to created a dataframe to operate later"""
    df = pd.DataFrame(qs.values(
        'quantity',
        'price',
        'number')
    )
    df['value'] = df['quantity'] * df['price']
    return df


def prepare_general_l3(qs) -> pd.DataFrame:
    """Get the necessary columns to created a dataframe to operate later"""
    df = pd.DataFrame(
        qs.values('cryptocurrencies__name',
                  'fiatcurrencies__name',
                  'quantity',
                  'price',
                  'order_type')
    )

    df['symbols'] = df['cryptocurrencies__name'] + '-' + df['fiatcurrencies__name']
    df['value'] = df['quantity'] * df['price']
    df = df[['symbols', 'quantity', 'price', 'order_type', 'value']]
    return df


def calculate_specific_statistics(df: pd.DataFrame, type_of_order: str) -> dict:
    """Process all the information needed for specific statistics"""
    greater_value = df.loc[df['value'] == df['value'].max(), :]
    lesser_value = df.loc[df['value'] == df['value'].min(), :]

    dict_to_response = {
        type_of_order: {
            "average_value": df['value'].mean(),
            "greater_value": greater_value.to_dict('records')[0],
            "lesser_value": lesser_value.to_dict('records')[0],
            "total_qty": df['quantity'].sum(),
            "total_px": df['price'].sum(),
        }
    }

    return dict_to_response


def calculate_general_statistics(df: pd.DataFrame) -> dict:
    """Process all the information needed for general statistics"""
    df = df.groupby(
        ['symbols', 'order_type']
    ).agg(
        {"quantity": ['sum'], "value": ['sum'], 'order_type': ['count']}
    )
    df.columns = ['qty', 'value', 'count']
    dict_to_response = df.groupby(level=0).apply(lambda df: df.xs(df.name).to_dict('index')).to_dict()

    return dict_to_response
