
import cv2
import sys
import csv
import numpy as np


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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.00001)

import tensorflow as tf
feats = tf.contrib.learn.infer_real_valued_columns_from_input(X_train)
classifier_tf = tf.contrib.learn.DNNClassifier(feature_columns=feats, hidden_units=[50, 50, 50], n_classes=3)
classifier_tf.fit(X_train, y_train, steps=50)

ct1=pd.read_csv("C:\\Users\\Lenovo\\.spyder-py3\\test.csv")
xx_test=ct1

predictions = list(classifier_tf.predict(xx_test, as_iterable=True))


if(predictions==[0]):
    print('Predicted color:RED')
elif(predictions==[1]):
    print('Predicted color:GREEN')
elif(predictions==[2]):
    print('Predicted color:BLUE')
else:
    print('wrong outupt')
#print(predictions)
