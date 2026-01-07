import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # active api key
genai.configure(api_key= os.getenv("GOOGLE_GEMINI_API"))

# Movie Recommendation system
st.title(" 🍿🎥✮⋆˙ Movie Recommendation system")
user_input = st.text_input("Enter the movie name")
submit = st.button("click here..")

#if submit and user_input.strip:
 #   st.markdown("Movie name has been entered")
    
#else:
 #   st.warning("No movie name has been entered yet...")    
 
model = genai.GenerativeModel("gemini-2.5-flash-lite")

if submit and user_input.strip:
    st.markdown(f"Movie Name entered :{user_input}")
    response = model.generate_content(f"Generative Movie Recommendations related to : {user_input}")
    #st.write(f"Recommendation: \n {response}")
    st.write(f"Releated recom ,endations for similar movies: \n{response.text}")
    
else:
    st.write(f"you need to enter the movie name")