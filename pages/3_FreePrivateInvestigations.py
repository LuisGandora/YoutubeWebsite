import streamlit as st
import toml

data = "/home/lewis/CodingStuff/PythonTester/WebsiteStuff/.streamlit/secrets.toml"

st.set_page_config(page_title="Free Private Investigations", page_icon=":jigsaw:")

st.title("Free Private Investigations")
st.markdown("""Thats right, you can request private investigations here, FOR FREE! This site is secure and requests will be handeled in extreme secrecy.
            However, there are some limits: 1. I will not take requests that will lead the the harm of myself, clients or people being harmed. 2. Complete online, I will not physcially stalk people for you
            that is your responsibility. 3. Time between requests will be longer depending on how many requests I have taken. In the case that I have too many requests to handle, I will shut down this webpage.
            Write a memo of the situation and what you want to investigate. Leave some sort of name/social media handle that I can work with, then give me a secure type of connection, gmail, whatsapp etc. so i can return results
            or reject your offer.            
            
""")

user_input = st.text_area("Your Request(press enter): ", "")

if user_input and user_input != "":
    temp_data = toml.load(data)
    temp_data["numofPIrequests"]["num3"] += 1
    temp_data["numofPIrequests"]["PIRequests"].append(user_input)
    with open(data, "w") as f:
        toml.dump(temp_data, f)
st.success("Wait for 1-2 weeks for the request to be processed")