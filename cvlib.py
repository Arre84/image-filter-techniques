#Import standard libraries
import numpy as np 
import cv2 
import argparse as arg 
from numpy.typing import NDArray

def parse_user_data()->arg.ArgumentParser:
    parser = arg.ArgumentParser() 
    parser.add_argument('--input_image',
                        type=str,
                        required=True,
                        help='Input image to be visualised')
    parser.add_argument('--filter',
                        type=str,
                        required=True,
                        help='filter to apply')
    parser.add_argument('--kernel_size',
                        type=int,
                        required=True,
                        help='Input image to be visualised')
    args = parser.parse_args()
    return args

def load_image(filename:str)->NDArray:
    img = cv2.imread(filename)
    if img is None:
        print(f"The following image:{filename} could not be found!")
        exit (-1)
    return img

def rotate_image(img:NDArray)->NDArray:
    # get heigth and width of image, (we dont need de channel)
    height, width = img.shape[:2]
    # Get the centroid of the image
    centroid = (width / 2, height / 2)
    # Apply some angule to the RotationMatrix    
    rotation_matrix = cv2.getRotationMatrix2D(centroid, 45,1)
    # Apply the rotation to the image.
    image_rotated = cv2.warpAffine(img, rotation_matrix, (width, height))
    return image_rotated

def translate_image(img:NDArray)->NDArray:
    M = np.float32([[1,0,50],[0,1,0]]) #Aplicamos una martríz de traslación
    image_translated = cv2.warpAffine(img,M,(img.shape[1], img.shape[0])) #Aplicamos la matríz
    return image_translated #Retornamos la imágen

def flip_image(img:NDArray)->NDArray:
    img_reflected =cv2.flip(img,1)
    # Return reflected image
    return img_reflected

def visualise_image (img:NDArray, title:str)->None:
    cv2.imshow(title,img)
    return None

def close_windows()->None:
    cv2.waitKey(0) #Comando para que se cierren las ventanas hasta 
    cv2.destroyAllWindows()
    return None