import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.datasets import load_boston, load_iris
from autosklearn.classification import AutoSklearnClassifier
from autosklearn.regression import AutoSklearnRegressor
import pandas as pd

def modeling_tab(data):
    st.title("Modeling")

    if data is not None:
        st.write("### Select Target Variable")
        target_variable = st.selectbox("Select the target variable", data.columns)

        st.write("### Select Input Features")
        input_features = st.multiselect("Select the input features", data.columns)

        if st.button("Train Model"):
            if len(input_features) == 0:
                st.error("Please select at least one input feature.")
            else:
                X = data[input_features]
                y = data[target_variable]

                # Train-test split
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Train and evaluate autoML models
                if st.radio("Select Problem Type", ("Classification", "Regression")) == "Classification":
                    automl = AutoSklearnClassifier(time_left_for_this_task=120)
                else:
                    automl = AutoSklearnRegressor(time_left_for_this_task=120)

                automl.fit(X_train, y_train)

                y_pred = automl.predict(X_test)

                if st.radio("Select Problem Type", ("Classification", "Regression")) == "Classification":
                    accuracy = accuracy_score(y_test, y_pred)
                    st.write(f"Model Accuracy: {accuracy}")
                else:
                    rmse = mean_squared_error(y_test, y_pred, squared=False)
                    st.write(f"Model RMSE: {rmse}")
