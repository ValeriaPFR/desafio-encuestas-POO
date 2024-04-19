from pregunta import Pregunta  # Importa la clase 'Pregunta' desde el modulo pregunta

class Encuesta:
    def __init__(self, nombre: str, listado_pregunta: list, listado_respuesta=None):
        """
        Constructor de la clase 'Encuesta'.
        
        Args:
            nombre (str): El nombre de la encuesta.
            listado_preguntas (list): Una lista de diccionarios que representan las preguntas de la encuesta.
            listado_respuestas (list, opcional): Una lista de respuestas para la encuesta, inicialmente vacía si no se proporciona.

        Inicializa los atributos 'nombre', 'listado_pregunta' y 'listado_respuesta' de la encuesta.
        """
        self.nombre = nombre  # Asigna el nombre de la encuesta
        # Crea una lista de instancias de la clase 'Pregunta' a partir de los diccionarios de las preguntas
        self.listado_pregunta = [Pregunta(dicc["enunciado"], dicc["ayuda"]) for dicc in listado_pregunta]
        
        # Inicializa la lista de respuestas como vacía si no se proporciona
        self.listado_respuesta = listado_respuesta if listado_respuesta is not None else []

    def mostrar_encuesta(self):
        """
        Metodo para mostrar la encuesta.

        Imprime el nombre de la encuesta, seguido de las preguntas y respuestas (si las hay).
        """
        print(f"Encuesta: {self.nombre}")  # Imprime el nombre de la encuesta
        print("Pregunta:")
        for pregunta in self.listado_pregunta:
            print(f"- {pregunta}")  # Imprime cada pregunta en la lista de preguntas
        
        print("Respuesta:")
        if self.listado_respuesta:
            for respuesta in self.listado_respuesta:
                print(f"- {respuesta}")  # Imprime cada respuesta en la lista de respuestas 
                #El guion previo a {preguntas} indica que tel texto esta relacionado con algun tipo de elemento de una lista o enumeracion
        else:
            print("Por favor ingrese respuesta.")  # Imprime un mensaje si no hay respuestas
