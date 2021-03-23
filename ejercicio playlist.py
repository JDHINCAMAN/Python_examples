playlist = {}
playlist['canciones'] = []

# Funcion principal
def app():

    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('¿Como deseas llamar tu playlist?: ')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False
            agregar_canciones()

def agregar_canciones():

    agregar_cancion = True

    while agregar_cancion:
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\nAgrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe x para dejar de escribir canciones: \r\n'

        cancion = input(pregunta)

        if cancion == 'x':
            agregar_cancion = False
            mostrar_resumen()

        else:
            playlist['canciones'].append(cancion)
            
def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'playlist: {nombre_playlist} \r\n')
    print('canciones:\r\n')
    for cancion in playlist['canciones']:
          print(cancion)
                           
app()
