from encuestas import Encuestas

class EncuestaPorEdad(Encuestas):
    """
Una clase para manejar encuestas basadas en grupos de edad.

Args:
- edad_min (int): edad minima para el grupo de edad.
- edad_max (int): edad maxima para el grupo ed edad

Returns:
None
"""
    def __init__(self, edad_min: int, edad_max: int):
        
        self.__edad_min = edad_min
        self.__edad_max = edad_max 
    #en este metodo, los parentesis vacios indican que o acepta ninun otro argumento ademas de 'self', 
    # este metodo actualmente no hace nada, pero está diseñado para agregar un listado de respuestas a 'agregar_listado_respuestas'.
    def agregar_listado_resp(self, ):
        pass

