# k-近邻算法
import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def k_near():
    """
        2个样本，3个特征
        a(a1,a2,a3),b(b1,b2,b3)
        欧式距离：
             ____________________________________
        p = √(a1 -b1)^2 + (a2-b2)^2 + (a3 - b3)^2
    """
    # 1、原始数据
    # 读取数据
    train_data = pandas.read_csv("k_near/train.csv")
    # print(train_data.head(10))

    # 2、数据处理
    # 数据筛选
    train_data = train_data.query("x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75")

    # 转换时间
    time_value = pandas.to_datetime(train_data["time"], unit="s")
    # 转换成字典
    time_value = pandas.DatetimeIndex(time_value)
    # print(time_value)

    # 构造特征
    data = train_data.copy()
    data["day"] = time_value.day
    data["hour"] = time_value.hour
    data["weekday"] = time_value.weekday
    # print(train_data.head(10))

    # 删除影响特征的数据,axis为1纵向删除
    data = data.drop(["time"], axis=1)

    # 删除小于目标值的数据
    place_count = data.groupby("place_id").count()
    # print(place_count)
    # 过滤数量大于5的地点ID，并且加入列中
    tf = place_count[place_count.x > 5].reset_index()
    # print(tf)
    data = data[data["place_id"].isin(tf.place_id)]

    # 取特征值和目标值
    y = data["place_id"]
    x = data.drop(["place_id", "row_id"], axis=1)

    # 数据分割
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 3、特征工程
    # 特征工程(标准化)
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 4、算法
    # 算法计算
    """
        优点：
            简单、易于理解、易于实现、无需估计参数、无需训练
        缺点：
            懒惰算法，对测试样本分类时的计算量大，内存开销大
            必须指定K值，K值选择不当则分类精度不能保证
        问题：
            k值比较小：容易受异常点影响
            k值比较大：容易受K值影响(类别)影响
            性能问题：每一个数据都要循环计算
    """
    # k值就是n_neighbors，也就是通过多少个邻近数据确认分类
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(x_train, y_train)
    y_predict = knn.predict(x_test)
    print("预测值：", y_predict)

    # 5、评估
    # 评估
    score = knn.score(x_test, y_test)
    print("准确率：", score)