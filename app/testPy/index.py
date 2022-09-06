
import pandas
from sklearn.tree import DecisionTreeClassifier
from sklearn2pmml.pipeline import PMMLPipeline
from sklearn2pmml import sklearn2pmml


iris_df = pandas.read_csv("./data/Iris.csv")

iris_X = iris_df[iris_df.columns.difference(["Species"])]
iris_y = iris_df["Species"]

pipeline = PMMLPipeline([
    ("classifier", DecisionTreeClassifier())
])
pipeline.fit(iris_X, iris_y)

sklearn2pmml(pipeline, "DecisionTreeIris.pmml", with_repr=True)
