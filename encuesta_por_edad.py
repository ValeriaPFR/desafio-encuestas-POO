from encuesta import Encuesta

class EncuestaPorEdad(Encuesta):
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
    #en este metodo, los parentesis vacios indican que o acepta ningun otro argumento ademas de 'self', 
    # este metodo actualmente no hace nada, pero está diseñado para agregar un listado de respuestas a 'agregar_listado_respuesta'.
    def agregar_listado_resp(self, ):
        pass

