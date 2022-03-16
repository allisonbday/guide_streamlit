import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Wizards - Taxi Machine")
    st.write(
        """
        *Following this [tutorial](https://www.youtube.com/watch?v=-IM3531b1XU&list=PLM8lYG2MzHmRpyrk9_j9FW0HiMwD9jSl5)*
        """
    )


with dataset:
    st.header("US Zipcodes Dataset")
    st.text("")

    zip_data = pd.read_csv("data/uszips.csv")
    st.write(zip_data.head(5))

    # density plot (basic)
    st.subheader("Average zipcode density per State in the US")
    density_mean = pd.DataFrame(zip_data.groupby("state_name")["density"].mean())
    st.bar_chart(density_mean)

with features:
    st.header("The features I created")

    st.markdown(
        """
        * ** first feature** I created this feature because of this... I calculated it using this logic....
        * ** second feature** I created this feature because of this... I calculated it using this logic....
        """
    )


with model_training:
    st.header("Time to train the model!")

    sel_col, disp_col = st.columns(2)

    max_depth = sel_col.slider(
        "What should be the max_depth of the model?",
        min_value=10,
        max_value=100,
        value=50,
        step=10,
    )

    n_estimators = sel_col.selectbox(
        "How many trees should there be?", options=[100, 200, 300, "No Limit"], index=1
    )

    input_feature = sel_col.text_input("Which feature should we use?", "PU")
