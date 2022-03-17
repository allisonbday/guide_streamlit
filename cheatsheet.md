

# Model ((Copy)
```python
    # imports
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_iris
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

    # model
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]  # Labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    classifier1 = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    classifier1.fit(X_train, y_train)
    y_pred = classifier1.predict(X_test)
```

# CUSTOMIZE(copy)
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