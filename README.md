# Documentación para el proyecto T2O: Intrucciones de uso

<div>Para poder ejecutar el proyecto, en primer lugar debemos activar el environment, por lo que nos situaremos en t2o/t2o/venv/Scripts y ejecutaremos el comando "activate".</div>
<div>Una vez activado este environment podremos proceder a iniciar el proyecto en local. Para ello, simplemente deberemos posicionarnos en t2o/t2o/ y ejecutar el comando "python manage.py runserver". Una vez ejecutado este comando podremos consumir la API que genera.</div>
<div>En concreto, son tres las llamadas que estan disponibles para su consumo:</div>
<ol>
  <li>La primera de ellas es 'blockchain/save_orders/"crypto"-"fiat"', donde "crypto" y "fiat" representan la relación entre la criptodivisa y la moneda fiat (e.g. "BTC-USD"). Un ejemplo de esta llamada (suponiendose que se ha iniciado el proyecto en local) sería: 'http://127.0.0.1:8000/blockchain/save_orders/BTC-USD/'. En esta llamada, es posible tanto ver la información sin insertarla (a través del método GET) como insertándola (a través del método PUT). En este último caso, la información será guardada en base de datos para poderse consumir posteriormente.</li>
  <li>La segunda de las llamadas disponibles está relacionada tanto con la funcionalidad 2 como con la 3. Para su llamada bastaría con ingresar una url del tipo 'blockchain/specific_statistics/"type_of_order"/"crypto"-"fiat"/' donde el parametro 'type_of_order' puede ser "bids" o "asks", en función del tipo de orden sobre la que queramos obtener información. Por otra parte, y al igual que anteriormente, "crypto" y "fiat" representan la relación entre la criptodivisa y la moneda fiat. Un ejemplo de esta llamada sería: 'http://127.0.0.1:8000/blockchain/specific_statistics/bids/BTC-USD/' </li>
  <li>La tercera de las llamadas disponibles devuelve las estadísticas generales, tal y como propone la funcionalidad 4. En este caso debería seguir la forma, '/blockchain/general_statistics/', por lo que un ejemplo sería: 'http://127.0.0.1:8000/blockchain/general_statistics/'.</li>
</ol>
<div> Por otra parte, también se han generado algunos test, que podran ejecutarse con el comando "manage.py test" una vez nos situemos sobre t2o/t2o/.

# Apartados pendientes de mejora/modificación
 <div>Fundamentalmente hay dos apartados pendientes de mejora.</div>
 <ol>
  <li>El primer apartado pendiente de mejora sería la realización de un mayor número de test y una validación más completa de las respuestas.</li>
  <li>Otro apartado que se podría mejorar sería el paso del tratamiento de datos a queryset en lugar de Pandas Dataframe, esto provocaría mejoras en el rendimiento de los cálculos.</li>
</ol>
