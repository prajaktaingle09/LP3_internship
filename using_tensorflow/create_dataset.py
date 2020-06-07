from PIL import Image
import csv
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import itemfreq

def color_histogram_of_training_image(img_name):

    # detect image color by using image file name to label training data
    if 'red' in img_name:
        data_source = ',0'
  
    elif 'green' in img_name:
        data_source = ',1'
   
    elif 'blue' in img_name:
        data_source = ',2'
    
    # load the image
    image = cv2.imread(img_name)

    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter = 0
    for (chan, color) in zip(chans, colors):
        counter = counter + 1

        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)

        # find the peak pixel values for R, G, and B
        elem = np.argmax(hist)

        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue

    feature_data =feature_data + data_source
    with open('C:\\Users\\Lenovo\\.spyder-py3\\p3.csv', 'a') as myfile:
        myfile.write(feature_data + '\n')
 

def training():
    

    # red color training images
    for f in os.listdir('C:\\Users\\Lenovo\\.spyder-py3\\red'):
        color_histogram_of_training_image('C:\\Users\\Lenovo\\.spyder-py3\\red/' + f)
    for f in os.listdir('C:\\Users\\Lenovo\\.spyder-py3\\green'):
        color_histogram_of_training_image('C:\\Users\\Lenovo\\.spyder-py3\\green/' + f)
    for f in os.listdir('C:\\Users\\Lenovo\\.spyder-py3\\blue'):
        color_histogram_of_training_image('C:\\Users\\Lenovo\\.spyder-py3\\blue/' + f)		
 

#calling the function

training()
with open('C:\\Users\\Lenovo\\.spyder-py3\\p3.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]    
      
with open('C:\\Users\\Lenovo\\.spyder-py3\\p3.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Red','Green','Blue','Class'])
    w.writerows(data)