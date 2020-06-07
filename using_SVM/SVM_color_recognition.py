import cv2
import os
import sys
import numpy as np
import csv
def color_histogram_of_test_image(test_src_image):

    # load the image
    image = test_src_image

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
            #print(feature_data)
        
    with open('C:\\Users\\Lenovo\\.spyder-py3\\test.csv', 'w') as myfile:
        myfile.write(feature_data)
    with open('C:\\Users\\Lenovo\\.spyder-py3\\test.csv',newline='') as f:
        r = csv.reader(f)
        data = [line for line in r]
    with open('C:\\Users\\Lenovo\\.spyder-py3\\test.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['Red','Green','Blue'])
        w.writerows(data)

try:
    source_image = cv2.imread(sys.argv[1])
except:
    source_image = cv2.imread('C:\\Users\\Lenovo\\.spyder-py3\\actual_ip.jpg')
prediction = 'n.a.'


color_histogram_of_test_image(source_image)
##############################################################################################

import pandas as pd

ct = pd.read_csv("C:\\Users\\Lenovo\\.spyder-py3\\p3.csv")
ct.shape
ct.head

X = ct.drop('Class', axis=1)
y = ct['Class']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
ct1=pd.read_csv("C:\\Users\\Lenovo\\.spyder-py3\\test.csv")
xx_test=ct1
y_pred = svclassifier.predict(xx_test)
if(y_pred==[0]):
    print('Predicted color:RED')
elif(y_pred==[1]):
    print('Predicted color:GREEN')
elif(y_pred==[2]):
    print('Predicted color:BLUE')
else:
    print('wrong outupt')