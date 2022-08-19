import streamlit as st
import pandas as pd


st.set_page_config(
    page_title='Form Responses Tracker',
    # layout='wide',
    page_icon=':rocket:'
)



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


st.markdown(
            f'''
            <style>
                .reportview-container .sidebar-content {{
                    padding-top: {1}rem;
                }}
                .reportview-container .main .block-container {{
                    padding-top: {1}rem;
                }}
            </style>
            ''',unsafe_allow_html=True)


m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color:#d3413f;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #0a7832;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.image("Nirma Logo.jpeg")

with col3:
    st.write(' ')


flag = 0
flag2 = 0
flag3=0
st.markdown("<h1 style='text-align: center;font-weight:bold; color:#008080'>Form Responses Tracker</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='font-weight:bold; color:#d3413f'>Upload Master Roll Call File</h3>", unsafe_allow_html=True)
input_from_user1 = st.file_uploader("1", type={"csv", "xlsx"})
if input_from_user1 is not None:
    df1 = pd.read_excel(input_from_user1)
    header1 = list(df1.columns)
    option1 = st.selectbox('Choose the column having Roll numbers',header1,key='abc')
    option_name = st.selectbox('Choose the column having Names',header1,key='abcd')
    flag2=1

if flag2==1:
    st.markdown("<h3 style='font-weight:bold;color:#d3413f'>Upload response file</h3>", unsafe_allow_html=True)
    input_from_user2 = st.file_uploader("2", type={"csv", "xlsx"})
    if input_from_user2 is not None:
        df2 = pd.read_excel(input_from_user2)
        header2 = list(df2.columns)
        option2 = st.selectbox('Choose the column having Roll number',header2,key='abcde')
        flag3=1

        if flag3==1:
            if input_from_user1 and input_from_user2 is not None:
                roll_no_master = df1[option1].tolist()
                name = df1[option_name].tolist() 
                roll_no_form = df2[option2].tolist() 

                filled,not_filled = 0,0
                Not_filled_list_Name = []
                Not_filled_list_Email = []
                Filled_list = []
                for i in roll_no_master:
                    found = False
                    for j in roll_no_form:
                        j = j.strip()
                        if (i.upper())==(j.upper()):
                            # Filled_list.append(i.upper())
                            filled = filled+1
                            found = True
                            break
                    if found==False:
                        Not_filled_list_Name.append(i.upper()) 
                        Not_filled_list_Email.append(i.lower()+"@nirmauni.ac.in") 
                        not_filled = not_filled+1
                    
                st.write("Total Students",filled+not_filled)
                st.write("Filled Count",filled)
                st.write("Not Filled Count",not_filled)
                # temp=[]
                

                res = dict(zip(roll_no_master, name))
                emailId_df=pd.DataFrame(Not_filled_list_Email)
                df3 = pd.DataFrame.from_dict(res, orient ='index')
        

        
                col3, col4, = st.columns(2)
                with col3:
                    if st.button('Copy to Clipboard Name & RollNo',key="xyz"):
                        df3.to_clipboard(header=None)

                with col4:
                    if st.button('Copy to Clipboard Email Id',key="xyz1"):
                        emailId_df.to_clipboard(header=None, index=False)
                
                    

                    
                
                col5, col6, = st.columns(2)
                with col5:
                    st.markdown("<h4 '>Roll Number And Name</h4>", unsafe_allow_html=True)
                    for i in Not_filled_list_Name:
                        # temp.append(res[i]+" "+i)
                        st.write(i+" "+res[i])

                with col6:
                    st.markdown("<h4 >Email Ids</h4>", unsafe_allow_html=True)
                    for i in Not_filled_list_Name:
                        st.write(i.lower()+"@nirmauni.ac.in")


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: #d3413f;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
height: 70px;
background-color: #c8ffc8d9;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p style='font-size: 14px;'>© Copyright 2022 by Nirma University. All Rights Reserved.  Privacy policy   |  Disclaimer  |  Copyright  
</br> Mentor: <a href="https://www.linkedin.com/in/dr-sachin-gajjar-805816a/" target="_blank">Dr. Sachin Gajjar</a> 
</br> Developed with ❤ by <a  href="https://www.linkedin.com/in/parth-jain-0804/" target="_blank">Parth Jain</a> | <a href="https://www.linkedin.com/in/anish-gupta-a28a20191/" target="_blank">Anish Gupta</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)