from encuestas import Encuesta

class EncuestaPorRegion(Encuesta):   
    """
    Clase para representar una encuesta especifica por region.

    Attributes:
        region (int): La region asociada a la encuesta.
        listado_region (list): La lista de regiones validas para la encuesta.

    Methods:
        agregar_listado_respuestas(): Verifica si la region de la encuesta esta en la lista de regiones validas.
    """
    def __init__(self, region: int, listado_region=None):
        """
        Constructor de la clase 'EncuestaPorRegion'.

        Args:
            region (int): La region asociada a la encuesta.
            listado_region (list, opcional): La lista de regiones validas para la encuesta. Si no se proporciona, se inicializa como una lista vacia.
        """
        super().__init__()  # Llama al constructor de la clase base
        self.region = region
        self.listado_region = listado_region if listado_region is not None else []

    def agregar_listado_respuesta(self):
        """
        Verifica si la region de la encuesta está en la lista de regiones validas.
        """
        if self.region in self.listado_region:
            print("Las respuestas registradas son:", self.listado_region)
        else:
            print("No pertenece a la región de esta encuesta")

regiones = [8, 9, 10]  # Lista de regiones validas

if __name__ == "__main__":
    encuesta_region = EncuestaPorRegion(8, regiones)
    encuesta_region.agregar_listado_respuesta()
