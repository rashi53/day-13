def str_float(x):#x='4.9','3.0','1.4','0.2','Iris-setosa']
    temp=[]
    for i in range(4):
        x[i]=float(x[i])
    return(x)

import random
training_data=[]
test_data=[]
for line in open("iris.txt",'r'):
##    print(i,type(i))
      temp=line[0:-1].split(',')
##      print(temp)
      if random.random()<=0.8:
          training_data.append(temp)

      else:
          test_data.append(temp)
print("data1",len(training_data))
print("data2",len(test_data))
