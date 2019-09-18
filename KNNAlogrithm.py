import numpy
import operator

def knn(k, test_data, train_data, lables):
    train_data.sharp()
    train_data_colm = train_data.sharp[0]
    test_data = numpy.tile(test_data, (train_data_colm, 1))

    diff = test_data - train_data
    sqrdiff = diff**2
    sumsqfdiff = sqrdiff.sum(axis=1)
    dist = sumsqfdiff**0.5
    sortdist = numpy.argsort(dist)

    count = {}
    for i in range(0, k):
        lable_num = lables[sortdist[i]]
        count[lable_num] = count.get(lable_num, 0)+1
    sorted_count = sorted(count.items(), key=operator.itemgetter(1), reverse=True)

    result = sorted_count[0][0]
    return result


