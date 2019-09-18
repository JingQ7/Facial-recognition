import PIL.Image
from os import listdir
import numpy
from .ImageToTXT import img_txt
from .KNNAlogrithm import knn

#1. Loading data and convert into array
def txt_to_array():
    array = []
    for each in range(0, 100):
        data = open(img_txt())
        for i in range(0, 32):
            each_line = data.readline()
            for j in range(0, 32):
               array.append(int(each_line[j]))
        return array


#2. Create traning set

# Get lables
def sep_label(file_name):
    notxt = file_name.split('.')[0]
    lable = str(notxt.split('_')[0])
    return lable

# Training
def train():
    label_array= []
    file = listdir('/Users/jingjing/Documents/Python_file/DS/Algorithm/KNN/traindata')
    n = len(file)
    data_array = numpy.zeros((n, 1024))
    for i in range (0, n):
        this_file = file[i]
        this_lable = sep_label(this_file)
        label_array.append(this_lable)
        data_array[i,:] = data_array('/traindata/'+this_file)
    return label_array, data_array


#3. Testing data by KNNAlgorithm
def test():
    train_label, train_data = train()
    test_file = listdir('/test/data/path.txt')
    n = len(test_file)
    for i in range(0, n):
        this_test_file = test_file[i]
        this_test_data = txt_to_array('/test/data/path'+this_test_file)
        result = knn(k=3, test_data=this_test_data, train_data=train_data, lables=train_label)
    return result
