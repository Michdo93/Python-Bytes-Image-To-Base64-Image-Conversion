import base64
import io
import cv2
from imageio import imread
import matplotlib.pyplot as plt
import numpy as np

with open('testImageBytes', 'r') as file:
    data = file.read()

data = eval(data)

b64_string = base64.b64encode(data)
bytes_string = b64_string.decode()
jpg_as_text = str(bytes_string)

text_file = open("testImage3", "w")
 
#write string to file
text_file.write(jpg_as_text)
 
#close file
text_file.close()
