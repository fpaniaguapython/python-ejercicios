class Pelicula:
    pass

def obtener_rendimiento(pelicula : Pelicula, recaudacion : int):
    if not isinstance(pelicula, Pelicula):
        raise TypeError("La película no es una película")
    if not isinstance(recaudacion, int):
        raise TypeError("La recaudación debe ser un número entero")
    if recaudacion < 0 :
        raise ValueError("La recaudación debe ser un número positivo")
    return 1000

try:
    #obtener_rendimiento("patata",5000)
    #obtener_rendimiento(Pelicula(),"diez mil euros")
    #obtener_rendimiento(Pelicula(),-5000)
    obtener_rendimiento(Pelicula(),1050)
except Exception as e:
    print(e)