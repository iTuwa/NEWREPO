import streamlit as st

st.title('Steve was here')

num1 = st.number_input('Enter a number')
num2 = st.number_input('Enter another number')

if st.button('Sum'):
    value = num1 + num2
    st.write(F'The sum of the numbers is {value}')
