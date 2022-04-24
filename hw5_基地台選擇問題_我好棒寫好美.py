from math import sqrt

##################################################################################
#https://www.coursera.org/learn/pbc1/exam/wkZ6A/di-wu-zhou-zuo-ye-ji-di-tai-wei-zhi-xuan-ze/attempt
##############################處理input############################################

input_1 = input(" 城鎮數量 , 共要幾個基地台 , 能涵蓋範圍 : ")
list_input_1 = input_1.split()
n=int(list_input_1[0])                        ## n 城鎮數量
p=int(list_input_1[1]) ## n   p   d           ## p 共要幾個基地台
d=int(list_input_1[2]) ## 0 list_input_1      ## d 能涵蓋範圍
 

population_i = []                             ## p [ p1,p2,p3,p4...pn]
x_i=[]                                        ## x [ x1,x2,x3,x4...xn]
y_i=[]                                        ## y [ y1,y2,y3,y4...yn]
for i in range(0,n):                          ## 輸入值
    input_i = input(" xi , yi , pi : ")
    list_input_i = input_i.split()

    x_i.append(int(list_input_i[0]))
    y_i.append(int(list_input_i[1]))
    population_i.append(int(list_input_i[2]))
    

#################################################  建立class  ########################################################################

class town:
    
    def __init__(self,population,x,y,index):
        
        #
        self.p = population
        self.x=x
        self.y=y
        self.index=index
        #
        
    #################################  距離list  ########################################
    
        dis = []
        
        for i in range(0,n):
            distant_math = sqrt((x_i[self.index]-x_i[i])**2+(y_i[self.index]-y_i[i])**2)
            dis.append(distant_math)
        #   
        self.distent_to_other = dis     ## [self-1,self-2,self-3,self-4,self-5,self-6...self-n]##            
        #
        
    #################################  所包到的town的index list  ########################################
    
        towns_is_covered_for_i = []
        
        for index , element in enumerate(self.distent_to_other) :
            #if element<=3 and element!=0:
            if element<=d :
                #towns_is_covered_for_i.append(index+1)
                towns_is_covered_for_i.append(index)
    
        #
        self.covers_town_index = towns_is_covered_for_i      ##[cover1 , cover2 , cover3.....]## 
        ##self.remain_cover = self.covers_town_index[:]        ##[cover1 , cover2 , cover3.....]##
        #
         
#################################################   建立lsit 裡面是town的class  ########################################################################

all_town = []                          ##[town0 , town1 , town2.....]##
for i in range(0,n):
     town_i = town(population_i[i],x_i[i],y_i[i],i)
     all_town.append(town_i)
     
#################################################   定義一些函式  ########################################################################    


def cover_people(indexs):              ##input含到那些town回傳總人數(扣掉已被包過的)##
    town_i = all_town[ indexs ]
    cover_index = town_i.covers_town_index
    ## 這樣寫不對阿 remain_index = cover_index & remain ##我包到的和剩下的取交集
    remain_index = list(set(cover_index)   .    intersection( set(remain) ))
    ##取交集應該這樣寫
    total = 0
    for i in remain_index:
        total += all_town[i].p
    return total

remain = list(range(0,n))             ##input上一個選擇架基地台的index 紀錄還剩那些沒包道##
def remain_cover(last_chose):
    last_chose_cover = all_town[last_chose].covers_town_index
    for i in last_chose_cover:
        if i in remain:
            del remain[remain.index(i)]
        
def max_in_remain(remain_list):      ##回傳下一個要選的town的index
    temp = 0
    max_index = 100000000000000000
    for i in remain_list:
        if(cover_people(i)>temp):
            temp = cover_people(i)
            max_index = i

    return max_index
    
    
    
#################################################    main     ############################################################################

# first_chose =  population_i.index(max(population_i))   ##第一個選人數最多的

# remain_cover(first_chose)                              ##扣掉第一個選，包到的

#chose = [first_chose]                                  ##紀錄選擇 (基地台數-1(first))

chose = []
for i in range(0,p):                                   
    chose_in_remain = max_in_remain(remain)            ##從剩下裡面選包道人數最多的
    remain_cover(chose_in_remain)                      ##扣掉包到的
    chose.append(chose_in_remain)                      ##放進紀錄
    print("i=",chose)
    #if(i==0): print("jajajajaja",remain)
    
all_index = list(range(0,n))
###############################取差及########################################################
all_cover_index = list(set(all_index)   .    difference( set(remain) ))
###############################取差及########################################################
total = 0
for i in all_cover_index:
    population = all_town[i].p
    total+=population
    
    
    
############正確全部加一的方法########################
chose_pls1 = [i+1 for i in chose]
############正確全部加一的方法########################
##print(chose+1,total)
# a = chose_pls1[0]
# b = chose_pls1[1]
# c = chose_pls1[2]


# print(a,b,c,total)

for i in range(0,p):
    print(chose_pls1[i],end=" ")
print(total)




    










 
        
    
    