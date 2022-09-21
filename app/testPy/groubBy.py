# @Time:2022/9/21 09:54
# @Author:Ray
# @File:groubBy.py.py

import pandas as pd
import numpy as np

# 先创建一个测试table

df = pd.DataFrame({'key1': list('aabba'),
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})

# print("df", df)

# 1： 使用单特征对table进行划分
grouped = df.groupby(["key1"])

for name, group in grouped:
    print(name)
    print(group)

# 打印之后会发现，是根据key1的不同的值，将df分成两个table，第一部分是key1=a,第二部分是key2=b
# 用其他特征划分原理也是一样的


# 2：用key1对表格进行划分，对划分之后的表格求其中的特征的均值，

groupedMean = df.groupby(["key1"]).mean()
# 如果groupby()一个参数的话，也可以是 groupby("key")

print("groupedMean", groupedMean)

# 3：使用多特征对表格进行划分

for name, group, in df.groupby(["key1", "key2"]):
    print("multiple features", name)
    print(group, "\n")

# 具体使用场景 比如
# 有两家商店1和2，每家商店有a，b，c三种商品，每家商店的每种商品都有各自的日销售额，
# 现在要快速得到每家商店每种商品的月销售额，那么我们就可以使用groupby来进行操作。

df2 = pd.DataFrame({'shop_id': list('111111222222'),
                    'item_id': list('abcabcabcabc'),
                    'item_daysales': list('123456123456')})

print("df_field_table", df2[["shop_id", "item_id"]].groupby("shop_id"))

# 计算每家点每月的销售量
# reset_index是保留划分的字段(这里就是shop_id and item_id)
month_grounded = df2.groupby(["shop_id", "item_id"]).sum().reset_index()

print("month_grounded", month_grounded)
