from preguntas import Preguntas  # Importa la clase Preguntas desde el módulo preguntas

class Encuestas:
    def __init__(self, nombre: str, listado_preguntas: list, listado_respuestas=None):
        """
        Constructor de la clase 'Encuestas'.
        
        Args:
            nombre (str): El nombre de la encuesta.
            listado_preguntas (list): Una lista de diccionarios que representan las preguntas de la encuesta.
            listado_respuestas (list, opcional): Una lista de respuestas para la encuesta, inicialmente vacía si no se proporciona.

        Inicializa los atributos 'nombre', 'listado_preguntas' y 'listado_respuestas' de la encuesta.
        """
        self.nombre = nombre  # Asigna el nombre de la encuesta
        # Crea una lista de instancias de la clase 'Pregunta' a partir de los diccionarios de las preguntas
        self.listado_preguntas = [Preguntas(dicc["enunciado"], dicc["ayuda"]) for dicc in listado_preguntas]
        
        # Inicializa la lista de respuestas como vacía si no se proporciona
        self.listado_respuestas = listado_respuestas if listado_respuestas is not None else []

    def mostrar_encuesta(self):
        """
        Metodo para mostrar la encuesta.

        Imprime el nombre de la encuesta, seguido de las preguntas y respuestas (si las hay).
        """
        print(f"Encuestas: {self.nombre}")  # Imprime el nombre de la encuesta
        print("Preguntas:")
        for pregunta in self.listado_preguntas:
            print(f"- {pregunta}")  # Imprime cada pregunta en la lista de preguntas
        
        print("Respuestas:")
        if self.listado_respuestas:
            for respuesta in self.listado_respuestas:
                print(f"- {respuesta}")  # Imprime cada respuesta en la lista de respuestas 
                #El guion previo a {preguntas} indica que tel texto esta relacionado con algun tipo de elemento de una lista o enumeracion
        else:
            print("Por favor ingrese respuesta.")  # Imprime un mensaje si no hay respuestas
