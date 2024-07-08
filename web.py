import streamlit as st
st.title("Loan approval app")
st.write("This app will help you")
st.header("Kindly enter the details")
st.text_input("Name")
c = st.number_input("Enter your credit score")
if c > 500:
    st.write("Yes sir, congratulations")
    #st.balloons()
    x = st.radio("What type of loan ?",options = ["home loan","car loan","personal loan"])
    if x == "home loan":
        s = st.number_input("Enter your salary")
        y = st.checkbox("Are you looking for loan for more than 20 years?")
        st.write("ok sir, our executive will contact you")
    elif x == "car loan":
        st.number_input("Enter your Annual income")
    elif x == "personal loan":
        st.number_input("Enter your income")
else:
    st.write("Sorry sir")