# 1. Download & Open Streamlit

# 2. Basics

# 3. Charts

# 4. Models 

## a) model_making
### model
```python
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]  # Labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    classifier1 = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    classifier1.fit(X_train, y_train)
    y_pred = classifier1.predict(X_test)
```

## b) model_import
### load in pickel
```python
def pickel_load():  # load in saved model
    pickle_in = open("model/classifier.pkl", "rb")
    classifier = pickle.load(pickle_in)
    return classifier
```
### get predictions
```python
def prediction(sepal_length, sepal_width, petal_length, petal_width):
    classifier2 = pickel_load()
    prediction = classifier2.predict(
        [[sepal_length, sepal_width, petal_length, petal_width]]
    )
    print(prediction)
    return prediction
```


# 5. Wrap it up
### cache & functions
```python
def get_data():  # load in the data
    # the data
    iris = datasets.load_iris()
    data = pd.DataFrame(
        {
            "sepal length": iris.data[:, 0],
            "sepal width": iris.data[:, 1],
            "petal length": iris.data[:, 2],
            "petal width": iris.data[:, 3],
            "species": iris.target,
        }
    )
    return data
```

### customize
```python
st.markdown(
    """
<style>
.main {
    background-color: #81B29A;
}
</style>
    """,
    unsafe_allow_html=True,
)
```