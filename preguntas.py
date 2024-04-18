from alternativas import Alternativas

class Pregunta:
    """
    Clase para representar las preguntas en una encuesta.

    Attributes:
        enunciado (str): El enunciado de la pregunta.
        ayuda (str): La ayuda asociada a la pregunta.
        requerido (bool): Indica si la pregunta es requerida o no.
        alternativas (list): Una lista de instancias de la clase 'Alternativas', representando las alternativas de respuesta.

    Methods:
        mostrar_pregunta(): Muestra el enunciado de la pregunta, la ayuda (si está disponible) y las alternativas de respuesta.
    """
    def __init__(self, enunciado: str, ayuda: str, requerido: bool, alternativas: list):
        """
        Constructor de la clase 'Pregunta'.

        Args:
            enunciado (str): El enunciado de la pregunta.
            ayuda (str): La ayuda asociada a la pregunta.
            requerido (bool): Indica si la pregunta es requerida o no.
            alternativas (list): Una lista de diccionarios que representan las alternativas de respuesta.
        """
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerido = requerido
        self.alternativas = [Alternativas(d["contenido"], d["pista"]) for d in alternativas]

    def mostrar_pregunta(self):
        """
        Muestra el enunciado de la pregunta, la ayuda (si está disponible) y las alternativas de respuesta.
        """
        print(self.enunciado)
        print("Ayuda:", self.ayuda) if self.ayuda else None
        for alternativa in self.alternativas:
            print(alternativa.mostrar_alternativas())

if __name__ == "__main__":
    alternativas = [
        {"contenido": "contenidos_1", "pista": "pista_1"},
        {"contenido": "contenidos_2", "pista": "pista_2"},
        {"contenido": "contenidos_3", "pista": "pista_3"}
    ]

    pregunta = Pregunta("enunciado1", "pista_1", True, alternativas)

    for dicc in alternativas:
        print(dicc)
