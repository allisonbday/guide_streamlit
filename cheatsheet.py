import streamlit as st

import pandas as pd
import numpy as np

import altair as alt

# Add a selectbox to the sidebar:
with st.sidebar:
    st.markdown("[Display Text](http://localhost:8501/#display-text)", unsafe_allow_html=True)
    st.markdown("[Display Data](http://localhost:8501/#display-data)", unsafe_allow_html=True)
    st.markdown("[Dataframe or Write](http://localhost:8501/#why-choose-dataframe-table-over-write)", unsafe_allow_html=True)





df = pd.read_csv('data/iris.csv')

st.title('CheatSheet')

st.markdown('There are a variety of ways to display information inside of streamlit')

st.header('Display Text')


st.code('st.markdown()')
st.markdown('This is in markdown')

st.code('st.latex()')
st.latex(r''' \underbrace{\overbrace{\ b_0 \ }^\text{y-intercept} + \overbrace{b_1}^\text{slope} X_i \ }_\text{estimated regression relation}
 ''')

st.code('st.write()')
st.write('Allows you to display all types of data and information. Streamlit just knows...')





st.header('Display Data')

st.markdown('Dataframes')

st.markdown('Using Magic')
st.code('df')
df


st.code('st.dataframe()')
st.dataframe(df)

st.code('st.table()')

if st.checkbox('Show table'):
  
    st.table(df)



st.code('st.write()')


st.write(df)

st.markdown('Charts')

st.code('st.write()')
sepal = alt.Chart(data=df, title='Flower Sepal Measurements').encode(
    x = 'sepal length (cm)',
    y = 'sepal width (cm)',
    color = 'Type',
    tooltip = ['sepal length (cm)','sepal width (cm)']
).mark_circle().interactive()
st.write(sepal)

st.header('Why choose dataframe/table over Write?')


st.markdown('1. datarame/table allows for the data to be added or replaced')
st.markdown('2. datarame/table have various arguements that can be used to customize table')


if "df" not in st.session_state:
#st.session_state.df =df
    st.session_state.df = pd.DataFrame(columns=["Sepal Length", 
                                                "Sepal Width", 
                                                "Petal Length", 
                                                "Petal Width", 
                                                "Variety"])

st.subheader("Add Record")

num_new_rows = st.sidebar.number_input("Add Rows",1,50)
ncolumns = st.session_state.df.shape[1]  # col count

rw = -1

with st.form(key="add form", clear_on_submit= True):
    cols = st.columns(ncolumns)
    rwdta = []

    for i in range(ncolumns):
        rwdta.append(cols[i].text_input(st.session_state.df.columns[i]))

    # you can insert code for a list comprehension here to change the data (rwdta) 
    # values into integer / float, if required

    if st.form_submit_button("Add"):
        if st.session_state.df.shape[0] == num_new_rows:
            st.error("Add row limit reached. Cant add any more records..")
        else:
            rw = st.session_state.df.shape[0] + 1
            st.info(f"Row: {rw} / {num_new_rows} added")
            st.session_state.df.loc[rw] = rwdta

            if st.session_state.df.shape[0] == num_new_rows:
                st.error("Add row limit reached...")

st.dataframe(st.session_state.df)