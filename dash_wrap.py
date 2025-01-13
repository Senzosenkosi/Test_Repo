import pandas as pd
import streamlit as st
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker 

st.title("Regression Model")

fake =Faker()

st.write(fake.nationality())

data = {
    'X': [1,2,3,4,56,66],
    'Y': [2,3,4,5,6,7]
}


df = pd.DataFrame(data)

X = df[['X']]
Y=df[['Y']]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)
mse = mean_squared_error(Y_test,Y_pred)

st.markdown("## Regression Model Results : Very basic my friend")
st.write(f"Mean Squared Error: {mse}")
st.write("Predictions:", Y_pred)
st.write("Actual:", Y_test)

fig, ax = plt.subplots()
sns.regplot(x='X', y='Y', data=df, ax=ax)
st.pyplot(fig)