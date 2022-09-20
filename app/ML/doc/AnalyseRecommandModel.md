***对RecommendModel模型的分析***

**import的部分**

1: numpy就不赘述了(做矩阵计算用的)

2: pandas
 参考文档 https://www.pypandas.cn/docs/getting_started/basics.html#head-%E4%B8%8E-tail
3: skkearn，基本的机器学习的框架
4：seaborn, 这是一个基于matplotlib进行高级封装的可视化库，相比之下，绘制图表更为集成化、绘图风格具有更高的定制性
相关参考文档： https://pypi.org/project/seaborn/
https://zhuanlan.zhihu.com/p/342945532
5: scipy相关的 https://www.biaodianfu.com/scipy-sparse.html
是关于创建 稀释的矩阵的内容。细节可以参考文档
6：warning模块 https://blog.csdn.net/low5252/article/details/109334695


***数据部分***

首先是数据部分： 我们有两份可用数据分别是ratings.csv和movies.csv，
rating，部分包括 userId,movieId,rating,timestamp 几个字段的数据
movies，部分包括 movieId,title,genres 三个字段


***coding部分***

1： 读取rating文件并取前5条 (head, tail是末尾5条)
2： movies同理

n_ratings,得到ratings的length
movies
users
同理 (unique 去重，从大到小返回)




 
