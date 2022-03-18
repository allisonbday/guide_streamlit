

# Data:
data = get_data()

# Chart 1:
chart = (
        alt.Chart(data)
        .encode(
            alt.X("petal length", axis=alt.Axis(title="Petal Length")),
            alt.Y("petal width", axis=alt.Axis(title="Petal Width")),
            color=alt.Color("species", title="Species"),
        )
        .mark_circle()
        .configure_axis(labelFontSize=18, titleFontSize=18)
        .configure_title(fontSize=20)
        .configure_legend(titleFontSize=18, labelFontSize=18)
    )

# Chart 2:
fig = plt.figure(figsize=(10, 4))
sns.lineplot(x="sepal length", y="sepal width", hue="species", data=data)
