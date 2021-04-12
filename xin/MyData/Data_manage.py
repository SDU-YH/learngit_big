import csv
import random
#训练
#读取数据
def loaddata(file):
    data_all_set = []
    with open(file, 'r') as newfile:
        csvfile = csv.reader(newfile)
        for line in csvfile:
            data_all_set.append(line)
    return data_all_set
#切分数据
def cut_data(data_all_set):
    data_train_set = []
    data_test_set = []
    data_all_number = len(data_all_set)
    cut_index = int(0.8 * data_all_number)
    data_train_set = data_all_set[0:cut_index]
    data_test_set = data_all_set[cut_index:data_all_number]
    all_set = [data_train_set, data_test_set]
    return all_set
#连续数据离散化
    
'''
    data_all_number = len(T_data_all_set)
    print(data_all_number)
    data_train_number = 0.8 * data_all_number
    data_test_number = 0.2 * data_all_number
    data_train_set = []
    while len(data_train_set) < data_train_number:
        index = random.randrange(data_all_number)
        print(index)
        data_train_set.append(T_data_all_set(index))
    return data_train_set
'''
'''  
Data_all_set = loaddata("")
All_set = cut_data(Data_all_set)
print(All_set[1][1])
'''


def sort_count(data_set, class_index):
    
    data_number = len(data_set)
    for i in range(data_number):
        for j in range(data_number - i - 1):
            if data_set[j][class_index] > data_set[j + 1][class_index]:
                data_set[j], data_set[j + 1] = data_set[j + 1], data_set[j]
    
    T_data = 0
    count = 0
    for i in range(len(data_set)):
        if data_set[i][class_index] != T_data:
            T_data = data_set[i][class_index]
            count = count + 1
    return count #确定特征值有多少个取值情况

def class_dif_value(data_set,class_index):
    number_set = []
    count = 1
    n = 0
    for i in range(len(data_set) - 1):
        if data_set[i][class_index] == data_set[i + 1][0]:
            count = count + 1
        else:
            number_set.append(count)
            count = 1
    for j in range(len(number_set)):
        n = number_set[j] + n
    number_set.append(len(data_set) - n)
    return number_set #确定特征每个值的数量的列表

#除数不为0，在上层限制
def avg(data_set, n):
    '''
    my_sum1 = 0
    my_avg1 = 0
    my_sum2 = 0
    my_sum2 = 0
    '''
    for i in range(n):
        my_sum1 = my_sum1 + data_set[i][3]
    my_avg1 = my_sum1 / n
    for j in range(n,len(data_set)):
        my_sum2 = my_sum2 + data_set[j][3]
    my_avg2 = my_sum2 / (len(data_set) - n)
    return my_avg1, my_avg2

def variance(data_set, avg):
    my_vace = 0
    for i in range(len(data_set)) :
        dif = data_set[i][3] - avg
        va = pow(dif, 2)
        my_vace = my_vace + va
    return my_vace

def easy_sort(data_set):
    data_number = len(data_set)
    for i in range(data_number):
        for j in range(data_number - i - 1):
            if data_set[j] > data_set[j + 1]:
                data_set[j], data_set[j + 1] = data_set[j + 1], data_set[j]
    return data_set
