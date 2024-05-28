from multiprocessing import Pool
import matplotlib.pyplot as plt
import os
import random
import shutil
from Video import *
from Util import *

class VideoAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.output_dir = os.path.join(os.path.dirname(file_path), "Output_" + os.path.splitext(os.path.basename(file_path))[0])
        os.makedirs(self.output_dir, exist_ok=True)
        self.frames = []

    def videoSpermDetection(self, options):
            self.frames = [] # Reiniciamos por si acaso
            video = self.file_path

            # Creamos las carpetas de salida
            output_dir_images_rect = os.path.join(self.output_dir, "Images_Rectangles")
            output_dir_labels = os.path.join(self.output_dir, "Labels")
            output_dir_images_original = os.path.join(self.output_dir, "Images_Original")
            os.makedirs(output_dir_images_rect, exist_ok=True)
            os.makedirs(output_dir_labels, exist_ok=True)
            os.makedirs(output_dir_images_original, exist_ok=True)

            morphKernel = Utils.morphKernel()

            th = 70
            (minRadius, maxRadius, param1, param2, mediumCellSize, micronsPerPixel, cameraDepth, diluent) = options

            vidcap = cv.VideoCapture(video)
            success, image = vidcap.read()

            circleList = []
            cimgList = []

            if success:
                height, width, depth = image.shape
                iimg = np.full((height, width), 255, np.uint8)
                w = width + 50
                h = height + 50
            i = 0

            while success:
                f = FrameVideo(image, i)
                i += 1
                self.frames.append(f)
                cimgList.append(image)
                success, image = vidcap.read()

            vidcap.release()

            # Execute in .py
            jobs = [(frame, options) for frame in self.frames] #Tengo que hacer esto para poder pasar multiples argumentos
            with Pool() as p:
                self.frames = p.map(FrameVideo.analyzeFrame, jobs)
                p.close()
            # # Execute in Jupyter
            # for frame in self.frames:
            #     frame_and_options = (frame, options)
            #     analyzed_frame = FrameVideo.analyzeFrame(frame_and_options)
            #     self.frames[frame.number_frame] = analyzed_frame

            for frame in self.frames:
                circleList.append(frame.circles_opencv)
                _, img_umb = cv.threshold(frame.frame, th, 255, cv.THRESH_BINARY)
                img_umb = cv.dilate(img_umb, morphKernel)
                img_umb = cv.dilate(img_umb, morphKernel)
                img_umb = cv.dilate(img_umb, morphKernel)
                iimg = cv.bitwise_and(iimg, img_umb)

            # I compute the static sperms
            img = cv.erode(iimg, morphKernel)
            img_umb = img

            circles = cv.HoughCircles(img_umb, cv.HOUGH_GRADIENT, 1, 25, param1=50, param2=20, minRadius=10,
                                    maxRadius=maxRadius)
            if circles is not None:
                circles = np.uint16(np.around(circles))

                for (x, y, r) in circles[0, :]:
                    cv.circle(img_umb, (x, y), r - 3, 0, 13)

            # I compute the indices of the circles in each frame
            indices = []
            circles0 = circleList[0]
            for k in range(0, len(circles0)):
                indices.append([k])

            i = 0
            for (x1, y1, r1) in circles0:

                for m in range(1, len(cimgList)):
                    circles1 = circleList[m - 1]
                    circles2 = circleList[m]

                    jointCircles = []

                    p1 = np.array([x1, y1], dtype=np.int64)
                    j = 0
                    for (x2, y2, r2) in circles2:

                        p2 = np.array([x2, y2], dtype=np.int64)

                        if (np.sqrt(np.sum(np.square(p1 - p2))) <= r1):
                            jointCircles.append(j)
                        j = j + 1
                    if len(jointCircles) == 1:
                        indices[i].append(jointCircles[0])
                        circle = circles2[jointCircles[0]]
                        x1 = circle[0]
                        y1 = circle[1]
                        r1 = circle[2]
                    elif len(jointCircles) >= 2:
                        circle0 = circles2[jointCircles[0]]
                        p2 = np.array([circle0[0], circle0[1]], dtype=np.int64)
                        dmin = np.sqrt(np.sum(np.square(p1 - p2)))
                        imin = 0
                        for k in range(1, len(jointCircles)):
                            circle20 = circles2[jointCircles[k]]

                            p2 = np.array([circle20[0], circle20[1]], dtype=np.int64)
                            if np.sqrt(np.sum(np.square(p1 - p2))) < dmin:
                                dmin = np.sqrt(np.sum(np.square(p1 - p2)))
                                imin = k
                        indices[i].append(jointCircles[imin])
                        circle = circles2[jointCircles[imin]]
                        x1 = circle[0]
                        y1 = circle[1]
                        r1 = circle[2]
                    else:
                        indices[i].append(-1)

                i = i + 1
            # In each colored image, I draw the circles
            good_indices = []
            final_indices = []
            i = 0
            for l in indices:
                if l.count(-1) < (len(l) / 2):  # I consider those that appear at least in half of the frames
                    j = len(l) - 1
                    while l[j] == -1:
                        j = j - 1
                    final_indices.append([j, l[j]])
                else:
                    final_indices.append([-1, -1])
                i = i + 1
            i = 0
            for l in indices:
                if (final_indices[i][0] != -1) and (l.count(-1) < (len(l) / 2)):
                    j = final_indices[i][0]
                    k = final_indices[i][1]
                    rep = []
                    for s in range(i + 1, len(indices)):
                        if (final_indices[s][0] == j and final_indices[s][1] == k):
                            rep.append(s)
                    if len(rep) > 0:
                        max = l.count(-1)
                        for s in rep:
                            l2 = indices[s].count(-1)
                            if l2 > m:
                                m = l2
                                i = s
                        for s in rep:
                            final_indices[s][0] = -1
                    good_indices.append(indices[i])
                i = i + 1
            self.number_circles = len(good_indices)
            i = 1
            cmap = plt.get_cmap('tab20c')
            final_circles = []
            for k in range(0,len(good_indices[0])):
                final_circles.append([])
            for l in good_indices:
                colorVal = cmap(i%20)
                for k in range(0,len(cimgList)):
                    cimagek = cimgList[k]
                    circlesk = circleList[k]
                    indice = l[k]
                    if (indice != -1):
                        circle = circlesk[indice]
                        x = circle[0]
                        y = circle[1]
                        r = circle[2]
                    final_circles[k].append(circle)
                    cv.circle(cimagek,(x,y),r+10,(colorVal[0]*255,colorVal[1]*255,colorVal[2]*255),2)
                            # draw the center of the circle
                    cv.circle(cimagek,(x,y),2,(255,0,255),3)

                    cimagek = cv.putText(cimagek, str(i), (int(x)-10,int(y)+10), cv.FONT_HERSHEY_SIMPLEX, 1, (colorVal[0]*255,colorVal[1]*255,colorVal[2]*255), 2, cv.LINE_AA)
                i = i+1

            #Con esto ponemos las listas de círculos buenas (de lo que realmente se pinta).
            for frame, circles in zip(self.frames, final_circles):
                frame.circles_opencv = circles
            
            for frame in self.frames:
                # Convertir el marco a color
                frame.frame = cv.cvtColor(frame.frame, cv.COLOR_GRAY2BGR)

                # Guardar la imagen original
                image_filename_original = os.path.join(output_dir_images_original, f"frame_{frame.number_frame}.jpg")
                cv.imwrite(image_filename_original, frame.frame)

                # Dibujar cuadrados alrededor de los círculos y guardar la imagen con los cuadrados dibujados
                for i, circle in enumerate(frame.circles_opencv, start=1):
                    x, y, r = circle
                    # Aumentar el radio en 2 píxeles
                    r += 2
                    x_left = x - r
                    y_top = y - r
                    x_right = x + r
                    y_bottom = y + r
                    cv.rectangle(frame.frame, (x_left, y_top), (x_right, y_bottom), (0, 255, 0), 2)
                    cv.putText(frame.frame, str(i), (x_left + 5, y_bottom - 5), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                image_filename_rect = os.path.join(output_dir_images_rect, f"frame_{frame.number_frame}.jpg")
                cv.imwrite(image_filename_rect, frame.frame)

                # Guardar las etiquetas YOLO en un archivo
                label_filename = os.path.join(output_dir_labels, f"frame_{frame.number_frame}.txt")
                with open(label_filename, "w") as f:
                    for i, circle in enumerate(frame.circles_opencv, start=1):
                        x, y, r = circle
                        # Aumentar el radio en 2 píxeles
                        r += 2
                        # Normalizar las coordenadas X y Y y calcular el ancho y alto del cuadro
                        img_width = frame.frame.shape[1]
                        img_height = frame.frame.shape[0]
                        x_center = x / img_width
                        y_center = y / img_height
                        box_width = (2 * r) / img_width
                        box_height = (2 * r) / img_height
                        f.write(f"{i} {x_center:.3f} {y_center:.3f} {box_width:.3f} {box_height:.3f} {i}\n")
                    
    