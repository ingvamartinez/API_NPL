# API_NPL

En este repositorio creamos una api el cual tendra como servicio un clasificador de lenguaje natural, que nos permitira clasificar criticas de peliculas de cine, el cual usaremos flask para la api, algo de html y css para el front con el fin de crear un aplicacion amigable con el usuario. 

El model que se utilizo fue el Gradiente Estocatico descendiente, con un loss de log_loss, para que hacer la clasificacion logistica:

# Data Source

Esta data fue extraida desde [stanford_aclimdb](https://ai.stanford.edu/~amaas/data/sentiment/), son 50.000 criticas de peliculas de cine. En el link indicado lo descargas, y extraes, y con el [ Load Data ](https://github.com/ingvamartinez/API_NPL/blob/main/load_data_aclImdb.ipynb), el cual te crea un archivo csv, con las variables review y sentiment. donde review son las 50k criticas y sentiment las etiquetas (0,1), donde "0" son negativas y "1" son positivas.

En el front, realice lo que pude, es funcional, se que se puede mejorar mucho, pero lo importante es que la app cumple la funcion y no clasifica el tipo de critica.

# SQLite

Se realizo una base de datos en sqlite con el fin de poder obtener el feddback del modelo, y asi poder reentrenarlo, solo almacenamos si la prediccion es incorrecta. para asi solo tener que adjuntar los datos de la base de datos con la data original de entrenamiento.

Comparto unas pocas imagenes, cualquier inquietud puedes contactarme. Saludos.

Se introduce la critica:
![imagen1](https://github.com/ingvamartinez/API_NPL/blob/main/images/api_1_aclimdb.png)

Se imprime la prediccion:
![imagen2](https://github.com/ingvamartinez/API_NPL/blob/main/images/api_2_aclimdb.png)

Se agradece el feedback:
![imagen3](https://github.com/ingvamartinez/API_NPL/blob/main/images/api_3_aclimdb.png)

:)

