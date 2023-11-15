# Laboratorio de IA AREP-2023-2


Hecho por : David Eduardo Valencia Cardona

## Como Ejecutar
Para ejecutar el proyecto basta con hacer 

```bash
git clone https://github.com/DavidVal6/repoIAArep.git
```
y una vez se hace el clone con hacer:
```bash
cd REPOIAAREP
```
una vez dentro se debe de disponer las variables de entonrno requeridas es decir las variables de entorno que se necesitan tener es la de la:\

- PINECONE_API_KEY
- PINECONE_ENVIRONMENT
- OPENAI_API_KEY

Las dos primeras keys se consiguen en la aplicacion de pinecone y la tercera fue la facilitada por los directores del taller la cual se cerro en la misma clase que se hizo el taller.
Con esto basta ejecutar el programa taller.py

```bash
py taller.py
```
y ya fuincionara

## Como Funciona

1. Importaciones:
os: Funcionalidad específica del sistema operativo (utilizada para acceder a variables de entorno).
pinecone: Un servicio para la búsqueda de similitud en datos vectoriales.
langchain.chat_models.ChatOpenAI: Una clase para interactuar con el modelo de lenguaje de OpenAI (ChatGPT).
langchain.agents: Módulo para funcionalidades relacionadas con agentes.
langchain.tools: Módulo para funcionalidades relacionadas con herramientas.
langchain.embeddings.OpenAIEmbeddings: Clase para manejar embeddings utilizando el modelo de lenguaje de OpenAI.
langchain.vectorstores.pinecone.Pinecone: Integración con Pinecone para la búsqueda de similitud en vectores.

2. Función: pinecone_stuff:
Inicializa Pinecone con la clave API y el entorno.
Crea una instancia de OpenAIEmbeddings para manejar embeddings.
Define una lista de rutas de archivos en la variable directory.
Itera sobre cada archivo, lee su contenido e indexa los datos de texto en Pinecone bajo el nombre de índice "documentos."

4. Función de herramienta: say_hello:
Una función registrada como una herramienta utilizando el decorador @tool.
Recibe un parámetro name y devuelve un mensaje de saludo.

5. Función de herramienta: search_pinecone:
Una función registrada como una herramienta utilizando el decorador @tool.
Recibe query y k (número de resultados) como parámetros.
Inicializa un índice de Pinecone y realiza una búsqueda de similitud utilizando la consulta proporcionada.

6. Función principal: main:
Crea una instancia de ChatOpenAI (ChatGPT) con una configuración de temperatura de 0.0 (lo que hace que las respuestas sean más determinísticas).
Define una lista de funciones de herramientas (say_hello y search_pinecone).
Inicializa un agente utilizando initialize_agent del módulo langchain.agents, proporcionando las herramientas, la instancia de ChatGPT y especificando el tipo de agente como AgentType.OPENAI_FUNCTIONS.
Ejecuta el agente con dos entradas de ejemplo: un saludo y una consulta de búsqueda.


