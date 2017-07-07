# Youtube-music (English Instructions)
A simple python program to download Youtube music. Usase **Pydub** and **ffmpeg** to convert files.
## Required packages
- [pafy](https://github.com/mps-youtube/pafy)
- [Youtube-dl](https://github.com/rg3/youtube-dl)
- [pydub](https://github.com/jiaaro/pydub/)
- [ffmpeg](https://ffmpeg.org/)
## Installation and Run
* Download or clone repository
* Open Youtube-music folder and execute `pip install -r requirements.txt`
* Download ffmpeg
  * **Linux:** `sudo apt-get install ffmpeg`
  * **Windows and Mac:** Download [here](https://www.ffmpeg.org/download.html)

Now run the program: `python download.py` to create songs.txt and directories

Paste your links in "songs.txt" separated to a line break **(Example in songs.example)**

The music files save in music directory. Have fun!
## Configuration
Change bitrate and extension in **download.py line 43**: 

`audio.export('music/'+name[0]+'.mp3',format="mp3",bitrate="160k")`

**Example, export files with format .wav:**

`audio.export('music/'+name[0]+'.wav',format="wav",bitrate="320k")`

See available formats: `ffmpeg -formats`

# Youtube-music (Instrucciones en español)
Un simple programa en python para descargar musica de Youtube. Utiliza **Pydub** y **ffmpeg** para convertir los archivos.
## Paquetes requeridos
- [pafy](https://github.com/mps-youtube/pafy)
- [Youtube-dl](https://github.com/rg3/youtube-dl)
- [pydub](https://github.com/jiaaro/pydub/)
- [ffmpeg](https://ffmpeg.org/)
## Instalación y ejecución
* Abre la carpeta Youtube-music y ejecuta `pip install -r requirements.txt`
* Descarga ffmpeg
  * **Linux:** `sudo apt-get install ffmpeg`
  * **Windows y Mac:** Descarga [aquí](https://www.ffmpeg.org/download.html)
Ahora ejecuta el programa: `python download.py` para crear el archivo "songs.txt" y los directorios.

Pega tus links en "songs.txt" separadas por un salto de línea **(Ejemplo en songs.example)**

Los archivos de musica se guardaran en el directorio de musica ¡Diviertete!
## Configuración
Cambia el bitrate y la extensión en **download.py line 43**: 

`audio.export('music/'+name[0]+'.mp3',format="mp3",bitrate="160k")`

**Ejemplo,exportar archivos con formato .wav**

`audio.export('music/'+name[0]+'.wav',format="wav",bitrate="320k")`

Mira los formatos disponibles: `ffmpeg -formats`
## Credits / Créditos
Developer/ Desarrollador: Deadblast ([@JackCloudman](https://t.me/JackCloudman))
