#!/usr/bin/env python
# coding=utf-8

import urllib
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def top10():
	data1=[]
	data2=[]
	data3=[]
	resp = urllib.urlopen("https://movie.douban.com/top250?start=0&filter=10").read()
	res1 = r'<img alt="(.+)"\s+?src'
	res2 = r'property="v:average">(.+)</span>'
	res3 = r'<span property="v:best" content="10.0"></span>\s+?<span>(.+)人评价</span>'
	data1.extend(re.findall(res1, resp))
	data2.extend(re.findall(res2, resp))
	data3.extend(re.findall(res3, resp))
	dicts = {
		"mname":data1,
		"mscore":data2,
		"mcount":data3
	}
	return pd.DataFrame(dicts)

top = top10()
score_max = top.mscore.max()
score_min = top.mscore.min()
count_max = top.mcount.max()
count_min = top.mcount.min()

# score_range = score_max - score_min
# count_range = count_max - count_min

print score_max
plt.scatter(top.mscore.astype(float), top.mcount.astype(float))
plt.show()
