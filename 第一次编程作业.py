#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
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
    f0 =open('sim_0.8/orig.txt',encoding="utf-8")
    f1 =open('sim_0.8/orig_0.8_add.txt',encoding="utf-8")
    f2 =open('sim_0.8/orig_0.8_del.txt',encoding="utf-8")
    f3 =open('sim_0.8/orig_0.8_dis_1.txt',encoding="utf-8")
    f4 =open('sim_0.8/orig_0.8_dis_3.txt',encoding="utf-8")
    f5 =open('sim_0.8/orig_0.8_dis_7.txt',encoding="utf-8")
    f6 =open('sim_0.8/orig_0.8_dis_10.txt',encoding="utf-8")
    f7 =open('sim_0.8/orig_0.8_dis_15.txt',encoding="utf-8")
    f8 =open('sim_0.8/orig_0.8_mix.txt',encoding="utf-8")
    f9 =open('sim_0.8/orig_0.8_rep.txt',encoding="utf-8")
    t0=f0.read()
    t1=f1.read()
    t2=f2.read()
    t3=f3.read()
    t4=f4.read()
    t5=f5.read()
    t6=f6.read()
    t7=f7.read()
    t8=f8.read()
    t9=f9.read()
    f0.close()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
    topK = 888
    s = Similarity(t0, t1, topK)
    result1 = s.similar()
    print('%.2f' % result1)
    s = Similarity(t0, t2, topK)
    result3=s.similar()
    print('%.2f' %result3)
    s = Similarity(t0, t3, topK)
    result4 = s.similar()
    print('%.2f' % result4)
    s = Similarity(t0, t4, topK)
    result5 = s.similar()
    print('%.2f' % result5)
    s = Similarity(t0, t5, topK)
    result6 = s.similar()
    print('%.2f' % result6)
    s = Similarity(t0, t6, topK)
    result7 = s.similar()
    print('%.2f' % result7)
    s = Similarity(t0, t7, topK)
    result8 = s.similar()
    print('%.2f' % result8)
    s = Similarity(t0, t8, topK)
    result9 = s.similar()
    print('%.2f' % result9)
    s = Similarity(t0, t9, topK)
    result10 = s.similar()
    print('%.2f' % result10)
    
    
