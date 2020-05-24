# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:20:51 2019

@author: Aaron
"""

mydict={}

mydict={"小明":93,"小華":92}
mydict["小明"]


hisdict={"Name":"Peter","Age":530,"Class":101}
hisdict["Age"]=0.53 #修改
hisdict["school"]="Harvard" #新增

del mydict["小明"] #刪除key
print(mydict)
mydict.clear() #清空字典
print(mydict)

del mydict #刪除字典
print(mydict) #會出錯喔!NameError

