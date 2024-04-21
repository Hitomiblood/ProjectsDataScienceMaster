import sys
import multiprocessing
from ProcesamientoVideos import procesarVideos


if __name__ == "__main__":
    if sys.platform.startswith('win'):
        # On Windows calling this function is necessary.
        multiprocessing.freeze_support()  # Funcionará con onedir pero no con onefile
        procesarVideos()