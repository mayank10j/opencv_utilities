
import cv2
import numpy as np

class Image_Utils:
    def __init__(self):
        '''
        '''

    def image_resize(self, image, width = None, height = None, inter = cv2.INTER_AREA):
        '''[Resizes the image]
            
            Arguments:
            image {Image} --  [Image to be resized]
            width = None {String} -- [When image width is none]
            height = None {String} -- [When image height is none]
            inter = cv2.INTER_AREA {String} -- [Using open cv library to resample using pixel area relation]

            Returns:
            image {image} -- [Resized Image]
        '''
        # initialize the dimensions of the image to be resized and
        # grab the image size
        dim = None
        (h, w) = image.shape[:2]

        # if both the width and height are None, then return the
        # original image
        if width is None and height is None:
            return image

        # check to see if the width is None
        if width is None:
            # calculate the ratio of the height and construct the
            # dimensions
            r = height / float(h)
            dim = (int(w * r), height)

        # otherwise, the height is None
        else:
            # calculate the ratio of the width and construct the
            # dimensions
            r = width / float(w)
            dim = (width, int(h * r))

        # resize the image
        resized = cv2.resize(image, dim, interpolation = inter)

        # return the resized image
        return resized


    def combine_img_horz(self, img1, img2):
        '''[Combines two images horizontally]
            
            Arguments:
            img1 {Image} -- [First image to be combined]
            img2 {Image} -- [Second image to be combined]

            Returns:
            result_image {Image} -- [Horizontally combined image with spacing]
        '''
        h1, w1 = img1.shape[:2]
        h2, w2 = img2.shape[:2]
        spacing = int(10) #provides spacing

        result_image_height = min(h1,h2) #provides minimum height among the two images
        img1 = self.image_resize(img1,height=result_image_height) #resizing according to result_image_height
        img2 = self.image_resize(img2,height=result_image_height)

        result_image = np.concatenate((img1, img2), axis=1) #concatenating img1 along with spacing with img2
        return result_image

    def combine_img_vert(self, img1, img2):
        '''[Combines two vertically]
            
            Arguments:
            img1 {Image} -- [First image to be combined]
            img2 {Image} -- [Second image to be combined]

            Returns:
            result_image {Image} -- [Vertically combined image with spacing]
        '''

        h1, w1 = img1.shape[:2]
        h2, w2 = img2.shape[:2]
        spacing = int(10) #provides spacing

        result_image_width = min(w1,w2) #provides minimum width among the two images
        img1 = self.image_resize(img1,width=result_image_width) #resizing according to result_image_width
        img2 = self.image_resize(img2,width=result_image_width)

        result_image = np.concatenate((img1, img2), axis=0) #concatenating img1 along with spacing with img2
        return result_image
