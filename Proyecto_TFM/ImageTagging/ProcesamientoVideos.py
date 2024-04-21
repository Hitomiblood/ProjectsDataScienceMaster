from Util import *
import os
import shutil
from Options import *
from VideoAnalyzer import *

def procesarVideos():


    Utils.split_videos("D:\OneDrive - Universidad de La Rioja\RepositoriosPersonales\TrabajosMaestriaCienciadeDatos\Proyecto_TFM\Prueba\Videos")
    video_files = Utils.get_video_files("D:\OneDrive - Universidad de La Rioja\RepositoriosPersonales\TrabajosMaestriaCienciadeDatos\Proyecto_TFM\Prueba\Train")
    print(video_files)
    print(len(video_files))


    options = OptionsHough()

    # Carpeta externa a la contenedora de los videos
    external_folder = os.path.dirname(os.path.dirname(video_files[0]))

    # Carpeta "Procesado" en la carpeta externa
    procesado_folder = os.path.join(external_folder, "Procesado")
    os.makedirs(procesado_folder, exist_ok=True)

    # Procesar cada video
    for video_file in video_files:
        video = VideoAnalyzer(video_file)
        video.videoSpermDetection(options.return_options())
        
        # Mover el video procesado a la carpeta "Procesado"
        video_name = os.path.basename(video_file)
        processed_video_path = os.path.join(procesado_folder, video_name)
        shutil.move(video_file, processed_video_path)

    print("Proceso completado. Los videos han sido procesados y movidos a la carpeta 'Procesado'.")

    video_files = Utils.get_video_files("D:\OneDrive - Universidad de La Rioja\RepositoriosPersonales\TrabajosMaestriaCienciadeDatos\Proyecto_TFM\Prueba\Test")
    print(video_files)
    print(len(video_files))



    # Carpeta externa a la contenedora de los videos
    external_folder = os.path.dirname(os.path.dirname(video_files[0]))

    # Carpeta "Procesado" en la carpeta externa
    procesado_folder = os.path.join(external_folder, "Procesado")
    os.makedirs(procesado_folder, exist_ok=True)

    # Procesar cada video
    for video_file in video_files:
        video = VideoAnalyzer(video_file)
        video.videoSpermDetection(options.return_options())
        
        # Mover el video procesado a la carpeta "Procesado"
        video_name = os.path.basename(video_file)
        processed_video_path = os.path.join(procesado_folder, video_name)
        shutil.move(video_file, processed_video_path)

    print("Proceso completado. Los videos han sido procesados y movidos a la carpeta 'Procesado'.")


    video_files = Utils.get_video_files("D:\OneDrive - Universidad de La Rioja\RepositoriosPersonales\TrabajosMaestriaCienciadeDatos\Proyecto_TFM\Prueba\Validation")
    print(video_files)
    print(len(video_files))



    # Carpeta externa a la contenedora de los videos
    external_folder = os.path.dirname(os.path.dirname(video_files[0]))

    # Carpeta "Procesado" en la carpeta externa
    procesado_folder = os.path.join(external_folder, "Procesado")
    os.makedirs(procesado_folder, exist_ok=True)

    # Procesar cada video
    for video_file in video_files:
        video = VideoAnalyzer(video_file)
        video.videoSpermDetection(options.return_options())
        
        # Mover el video procesado a la carpeta "Procesado"
        video_name = os.path.basename(video_file)
        processed_video_path = os.path.join(procesado_folder, video_name)
        shutil.move(video_file, processed_video_path)

    print("Proceso completado. Los videos han sido procesados y movidos a la carpeta 'Procesado'.")


