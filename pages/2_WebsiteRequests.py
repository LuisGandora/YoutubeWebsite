import streamlit as st
import toml

data = "/home/lewis/CodingStuff/PythonTester/WebsiteStuff/.streamlit/secrets.toml"

st.set_page_config(page_title="Website Requests", page_icon=":computer:")


st.title("Website Requests")
st.markdown("""
    I can make streamlit websites in a reasonably long time, send your specifications for a website you request below along with a personal email so I can send you the final results
    pls dont say make it reactive

""")

user_input = st.text_area("Your Request: ", "")
if user_input and user_input != "":
    temp_data = toml.load(data)
    temp_data["numofWebsites"]["num2"] += 1
    temp_data["numofWebsites"]["WebsiteRequests"].append(user_input)
    with open(data, "w") as f:
        toml.dump(temp_data, f)
st.success("Wait for 1-2 weeks for the request to be processed")
