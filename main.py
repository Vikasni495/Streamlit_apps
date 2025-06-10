import streamlit as st
from streamlit_option_menu import option_menu

st.title("Hello Students ❤️‍🔥")
st.header("👨🏾‍💻 VCET STUDENTS 👩‍💻")
st.subheader("INTERNSHIP ")
st.write("# WELCOME TO VINSUP 😊")
st.text("GOOD MORNING STUDENTS 😊")
st.code("""
#include <stdio.h>
int main()
{
printf("HOW IS THE INTERNSHIP");
return 0;
}""",language="c")
st.latex(r"E=mc^2")
st.latex(r"Area of Rectangle = l*b")
st.metric(label="Temperature",value="75°",delta="-1.24°")
st.progress(0.5)
st.progress(0.5,text="50%")
st.progress(0.8,text="100%")
st.text_input("ENTER YOUR NAME")
st.text_input("ENTER THE NAME OF COLLEGE")
st.multiselect("SELECT YOUR SKILLS YOU HAVE",["COMMUNICATION","TEAM HANDLING","TECHNICAL IDEAS","SPEAKING"])
st.number_input("ENTER YOUR AGE")
st.slider(label="SELECT YOUR AGE",min_value=0,max_value=100,value=18)
st.date_input("ENTER YOUR DATE OF BIRTH")
st.checkbox(" I AGREE THE TERMS OF CONDITIONS")
st.radio("SELECT YOUR GENDER",["Male 👦🏻","Female 👩🏻","Others ⚧"])
st.multiselect("SELECT YOUR COUNTRY",["INDIA","CANADA","USA","AUSTRALIA"])

with st.sidebar:
    st.title(" MENU BAR 🧾")
    st.title("𝐖𝐄𝐋𝐂𝐎𝐌𝐄 🙏🏻")
    st.title("Hello Students 💜!")

    select = option_menu(
        menu_title="VCET- MADURAI",
        options=['Home','About','Service'],
        menu_icon = ['house-heart-fill','file-earmark-person','gear-wide-connnected']
    )

if select == "Home":
    st.title("Welcome to H♡me  🏠︎")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS04C9ht8a0VHw87UhwArIlXx8hG1crU5G-yw&s")
    st.divider()
    col1,col2 = st.columns(2)
    with col1:
        a = st.text_input("First Name :")
        if st.button("Verified"):
              st.write(a)
              st.balloons()
              st.snow()
    with col2:
        st.text_input("Last Name :")
    st.text_input("Email 📩")

    col3,col4= st.columns(2)
    with col3:
        b = st.text_input("Enter your Password 🔐")
        if st.button("Confirm"):
             st.write(b)
             st.balloons()
elif select == "About":
    st.title("Welcome to About 🤔 ")
elif select == "Service":
    st.title("Welcome to Service ⚙️")

       

    

