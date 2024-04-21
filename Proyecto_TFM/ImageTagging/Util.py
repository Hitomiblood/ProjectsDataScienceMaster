# Definiendo la clase utils para usar funciones genericas
import numpy as np
import cv2 as cv
import random
import shutil
import os

class Utils:

    @staticmethod
    def filterKernel():
        return np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    
    @staticmethod
    def morphKernel():
        return np.ones((3, 3), np.uint8)
    
    @staticmethod
    def split_videos(source_folder, min_val_videos=1, min_test_videos=1, seed=42):
        # Obtener la lista de videos en la carpeta de origen
        videos = os.listdir(source_folder)
        random.seed(seed)
        random.shuffle(videos)

        # Calcular la cantidad de videos para cada conjunto
        total_videos = len(videos)
        train_size = int(0.8 * total_videos)
        val_size = max(min_val_videos, int(0.1 * total_videos))
        test_size = max(min_test_videos, total_videos - train_size - val_size)

        # Crear las carpetas de train, validation y test
        train_folder = os.path.join(os.path.dirname(source_folder), "Train")
        val_folder = os.path.join(os.path.dirname(source_folder), "Validation")
        test_folder = os.path.join(os.path.dirname(source_folder), "Test")

        os.makedirs(train_folder, exist_ok=True)
        os.makedirs(val_folder, exist_ok=True)
        os.makedirs(test_folder, exist_ok=True)

        # Mover los videos a las carpetas correspondientes
        for video in videos[:train_size]:
            shutil.move(os.path.join(source_folder, video), os.path.join(train_folder, video))

        for video in videos[train_size:train_size + val_size]:
            shutil.move(os.path.join(source_folder, video), os.path.join(val_folder, video))

        for video in videos[train_size + val_size:]:
            shutil.move(os.path.join(source_folder, video), os.path.join(test_folder, video))

        # Verificar si la carpeta de validación tiene más videos que la de test
        val_videos_count = len(os.listdir(val_folder))
        test_videos_count = len(os.listdir(test_folder))
        if test_videos_count > val_videos_count:
            print("La carpeta de test tiene más videos que la de validación. Renombrando las carpetas...")
            # Renombrar la carpeta de validación a "Test" y la de test a "Validation"
            os.rename(val_folder, os.path.join(os.path.dirname(val_folder), "Test1"))
            os.rename(test_folder, os.path.join(os.path.dirname(test_folder), "Validation"))
            os.rename(os.path.join(os.path.dirname(source_folder), "Test1"), os.path.join(os.path.dirname(val_folder), "Test"))

        print("Videos divididos en conjuntos de entrenamiento, validación y prueba.")
    
    @staticmethod
    def get_video_files(folder):
            video_files = []
            for file in os.listdir(folder):
                if file.endswith(('.mp4', '.avi', '.mov', '.mkv')):  
                    video_files.append(os.path.join(folder, file))
            return video_files
    
    
