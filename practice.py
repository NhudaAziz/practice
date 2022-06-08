import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = pd.read_csv("https://raw.githubusercontent.com/NhudaAziz/practice/main/IRIS.csv")
feature_cols = ['sepal_length','sepal_width','petal_length','petal_width']
X = iris[feature_cols]
Y = iris.species

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
#y_label = ['setosa','versicolor','virginica']
st.write(pd.DataFrame({
     'Species': ['setosa','versicolor','virginica'],
 }))

st.subheader('Prediction')
#st.write(iris.target_names[prediction])
st.write(prediction)
st.image(
    "https://miro.medium.com/max/1000/1*nfK3vGZkTa4GrO7yWpcS-Q.png"
)

st.subheader('Prediction Probability')
st.write(prediction_proba)
