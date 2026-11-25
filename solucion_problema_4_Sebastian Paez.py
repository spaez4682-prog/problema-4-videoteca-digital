# Problema 4 - Videoteca digital
 
# Matriz: [titulo, anio de lanzamiento, calificacion, genero]
videoteca = [
    ["Conexion final", 2024, 10, "Ciencia ficcion"],
    ["El ultimo viaje", 2019, 9, "Aventura"],
    ["Planeta en pausa", 2023, 8, "Documental"],
    ["Voces del bosque", 2021, 7, "Drama"],
    ["La ruta del manana", 2020, 8, "Drama"],
    ["Memorias de invierno", 2018, 8, "Drama"],
    ["Codigo azul", 2022, 9, "Accion"]
]
 
def contar_titulos(matriz, umbral_calificacion, anio_limite):
    contador = 0
 
    for registro in matriz:
        if registro[2] >= umbral_calificacion and registro[1] >= anio_limite:
            contador += 1
 
    return contador
 
 
# Criterios definidos para la consulta
umbral_calificacion = 8
anio_limite = 2020
 
# Ejecucion de la funcion y presentacion del resultado
total = contar_titulos(videoteca, umbral_calificacion, anio_limite)
print("Cantidad de titulos que cumplen ambos criterios:", total)
