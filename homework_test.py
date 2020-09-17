#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import sys
import os
from math import sqrt
import jieba.analyse
from functools import reduce
class Similarity():                                  #初始化，给定要比对的文本和关键字
    def __init__(self, target1, target2, topK=10):
        self.target1 = target1
        self.target2 = target2
        self.topK = topK

    def vector(self):                                
        self.vdict1 = {}
        self.vdict2 = {}
        top_keywords1 = jieba.analyse.extract_tags(self.target1, topK=self.topK, withWeight=True)  #self.target 为代提取的文本
                                                                                                   #topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
                                                                                                   #withWeight 为是否一并返回关键词权重值，默认值为 False
        top_keywords2 = jieba.analyse.extract_tags(self.target2, topK=self.topK, withWeight=True)
        for k, v in top_keywords1:
            self.vdict1[k] = v
        for k, v in top_keywords2:
            self.vdict2[k] = v

    def mix(self):
        for key in self.vdict1:
            self.vdict2[key] = self.vdict2.get(key, 0)
        for key in self.vdict2:
            self.vdict1[key] = self.vdict1.get(key, 0)

        def mapminmax(vdict):
            #计算相对词频
            _min = min(vdict.values())
            _max = max(vdict.values())
            _mid = _max - _min
            # print _min, _max, _mid
            for key in vdict:
                vdict[key] = (vdict[key] - _min) / _mid  #计算相对词频
            return vdict

        self.vdict1 = mapminmax(self.vdict1)   
        self.vdict2 = mapminmax(self.vdict2)

    def similar(self):  #余弦算法
        self.vector()
        self.mix()
        sum = 0
        for key in self.vdict1:
            sum += self.vdict1[key] * self.vdict2[key]   #计算分子
        A = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict1.values())))
        B = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict2.values())))
        return sum / (A * B)


if __name__ == '__main__':
    # t1 = '"D:\Python\Firstcode\orig.txt"'
    # t2 = '"D:\Python\Firstcode\orig_0.8.add.txt"'
    x1 = input('请输入原文本文件路径:')
    x2 = input('请输入抄袭文本文件路径:')
    if x1.endswith('.txt')==False:
        print("原文件路径输入错误!")
    elif x2.endswith('.txt')==False:
        print("抄袭文件路径输入错误!")
    else:
        try:
            f0 =open(x1,encoding="utf-8")
            f1 =open(x2,encoding="utf-8")
            t0=f0.read()
            t1=f1.read()
            f0.close()
            f1.close()
            topK = 888
            s = Similarity(t0, t1, topK)
            result = s.similar()
            result = round(result,2)
            #print(result)
            x3 = input("请输入存放结果文件的路径:")
            with open(x3,'w') as f:
                f.write(str(result))    
                print(result)
                print("答案已经成功写入!")
        except Exception as err:
            print(err)

    
   
    
