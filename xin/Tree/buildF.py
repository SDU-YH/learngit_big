import numpy as np
import Data_manage as Dm
import random
import math
import tree

#选择数据集
def select_data_set(data_train_set):
    
    tree_number = 2
    data_ture_number = 10
    all_tree_data_set = []
    
    for i in range(tree_number):
        tree_data_set = []
        
        while len(tree_data_set) < data_ture_number:
            index = random.randrange(len(data_train_set))
            tree_data_set.append(data_train_set[index])
            
        all_tree_data_set.append(tree_data_set)
        
    return all_tree_data_set

#选择特征集
def select_class_set(data_train_set):
    all_tree_class = []
    class_set = [0,1,2,4]
    for i in range(2):
        one_tree_class = []
        while len(one_tree_class) < 3:
            n = random.randrange(len(class_set))
            if class_set[n] not in one_tree_class:
                one_tree_class.append(class_set[n])
        all_tree_class.append(one_tree_class)
    return all_tree_class

#每次把数据集二分,class_value选出的最优特征值，class_index要与最优特征值比较的特征的指针
def spilt_op(tree_data_set, class_value, class_index):
    right_tree = []
    left_tree = []
    for data in tree_data_set:
        if data[class_index] < class_value:
            left_tree.append(data)
        else:
            right_tree.append(data)
    return [left_tree, right_tree]

'''
#计算基尼系数
def Gini(data_set, class_index):
    class_number = Dm.sort_count(data_set, class_index)
    ck = Dm.class_dif_value(data_set, class_index)
    all_p = 0
    for i in range(class_number):
        p2 = math.pow(ck[i] / len(data_set), 2)
        all_p = all_p + p2
    gini_i = 1 - all_p
    return gini_i


#gini系数和对应的特征编号
def Gini_dictionary(data_set, one_tree_class):
    dictionary = {}
    for i in range(len(one_tree_class)):
        value = Gini(data_set, one_tree_class[i])
        key = one_tree_class[i]
        dictionary[key] = value
    return dictionary
'''

def select_best_gini(data_set, class_set, gini_limit):
    all_gini = []
    gini_index = []
    class_index = []
    print('start')
    for i in range(len(class_set)):
        my_count = Dm.sort_count(data_set,class_set[i])
        my_number_set = Dm.class_dif_value(data_set, class_set[i])
        print('f')
        for j in range(my_count):
            print('s')
            D1_number = 0
            D2_number = 0
            for l in range(j):
                print('t')
                D1_number = D1_number + my_number_set[l]
            D2_number = len(data_set) - D1_number
            if D1_number == 0 or D2_number == 0:
                gini_i = 1
            else:
                avg_set = Dm.avg(data_set, D1_number)
                D1_avg = avg_set[0]
                D2_avg = avg_set[1]
                D1_vace = Dm.variance(data_set[0:D1_number], D1_avg)
                D2_vace = Dm.variance(data_set[D1_number:len(data_set)], D2_avg)
                gini_i = D1_vace + D2_vace
            all_gini.append(gini_i)
            gini_index.append(data_set[class_set[i]][D1_number])
            class_index.append(class_set[i])
    #best_gini = min(all_gini)
            '''
    test_all_gini = all_gini
    test_all_gini = Dm.easy_sort(test_all_gini)
    test_gini = gini_limit
    for y in range(len(test_all_gini)):
        if test_all_gini[y] > gini_limit:
            if test_all_gini[y] > test_gini:
                test_gini = test_all_gini[y]
                '''
    test_all_gini = [gini_limit]
    for t in range(len(all_gini)):
        if all_gini[y] > gini_limit:
            test_all_gini.append(all_gini[y])
    best_gini = min(test_all_gini)
    if best_gini == gini_limit:
        best_gini_index = -1
        best_class_index = -1
    else:
        for g in all_gini:
            if all_gini[g] == best_gini:
                best_gini_index = g
        best_gini_index = gini_index[g]
        best_class_index = class_index[g]
    return best_gini_index, best_class_index#相当于class_value和class_index

#建树
def build_tree(data_limit, data_set, class_set, gini_limit):
    best_set = select_best_gini(data_set, class_set, gini_limit)
    class_value = best_set[0]
    class_index = best_set[1]
    root = data_set[]
    if len(data_set) > data_limit and class_index != -1:
        son_tree_set = spilt(data_set, class_value, class_index)
        left_tree = son_tree_set[0]
        right_tree = son_tree_set[1]
        return
    else:
        return 

#建造森林
def build_forest(data_train_set, tree_number):
    all_tree_data_set = select_data_set(data_train_set)
    all_tree_class_set = select_class_set(data_train_set)
    for i in 

    
'''
对于每个特征计算基尼系数Gini(),选出最优的特征,循环判断，利用最优的特征进行二分spilt_op()
对于符合样本个数和基尼系数的二分后的子集继续划分，防止过拟合
'''

Data_all_set = Dm.loaddata("D:\文档\亚马逊spot实例数据.txt")
All_set = Dm.cut_data(Data_all_set)
'''
All_tree_data_set = select_data_set(All_set[0])
print(All_tree_data_set[0])

All_tree_class = select_class_set(All_set[0])
print(All_tree_class[1])

Spilt_set = spilt_op(All_tree_data_set[0], 'us-east-1d', 0)
print(Spilt_set[0])

Gini = Gini(All_tree_data_set[0], 0)
print(Gini)
'''

'''
dictionary = Gini_dictionary(All_tree_data_set[0], All_tree_class[0])
dictionary.items()


myc = Dm.sort_count(Data_all_set, 0)
'''
