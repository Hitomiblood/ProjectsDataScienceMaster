import cv2 as cv
from Util import * 

class FrameVideo():

    def __init__(self, img, number_frame):
        self.circles_opencv = []
        self.number_frame = number_frame
        self.frame = img
        
    @staticmethod
    def analyzeFrame(frame_and_options):
        frame, options = frame_and_options
        filterKernel = Utils.filterKernel()
        (minRadius, maxRadius, _, _, _, _, _, _) = options


        height, width, depth = frame.frame.shape
        w = width + 50
        h = height + 50

        image = cv.cvtColor(frame.frame, cv.COLOR_BGR2GRAY)
        cv.normalize(image, image, 0, 255, cv.NORM_MINMAX)
        image = cv.filter2D(image, -1, filterKernel)
        img_border = cv.copyMakeBorder(image, 50, 50, 50, 50, cv.BORDER_REFLECT)
        circles = cv.HoughCircles(img_border, cv.HOUGH_GRADIENT, 1, 25, param1=80, param2=35, minRadius=minRadius,
                                  maxRadius=maxRadius)
        circles = np.uint16(np.around(circles))
        # I choose the circles that are inside the image
        circles2 = []
        for (x, y, r) in circles[0, :]:
            if ((x >= 50) and x <= w and (y >= 50) and y <= h):
                mask = np.zeros((height, width), np.uint8)
                cv.circle(mask, (x, y), r, 255, -1)
                points = np.transpose(np.where(mask == 255))
                sum = 0
                for (a, b) in points:
                    sum = sum + img_border[a][b]
                # suma = suma + img_border[a][b][0] + img_border[a][b][1] + img_border[a][b][2] # Aqui mejor poner algo como que > 50% pixeles tienen alta intensidad
                if (sum <= 128 * 0.6 * len(points)):
                    circles2.append([x - 50, y - 50, r])

        frame.circles_opencv = circles2
        frame.frame=image
        return frame