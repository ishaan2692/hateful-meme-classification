import streamlit as st
import requests
import json
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PIL.Image
from PIL import UnidentifiedImageError


def generate_text(uploaded_file, prompt):
    try:
        if uploaded_file is not None:
            image = PIL.Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)

        model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')

        with st.spinner('Generating...'):
            response = model.generate_content([prompt, image], stream=True)
            response.resolve()
            st.markdown(response.text)

    except UnidentifiedImageError:
        error_message = "Invalid image file. Please upload a valid image."
        st.write(f"<div style='padding: 10px; border-radius: 5px;'> {error_message} </div>", unsafe_allow_html=True)

    except ValueError:
        error_message = "The given image might contain hateful or nsfw content. Processing failed."
        st.write(f"<div style='padding: 10px; border-radius: 5px;'> {error_message} </div>", unsafe_allow_html=True)
    
    except UnboundLocalError:
        error_message = "There's no image file. Please upload a valid image."
        st.write(f"<div style='padding: 10px; border-radius: 5px;'> {error_message} </div>", unsafe_allow_html=True)



def chatbot(prompt):
    try:
        model = genai.GenerativeModel('gemini-1.0-pro-latest')
        response = model.generate_content(prompt)
        return response.text
    except ValueError as e:
        return f"I apologize, I'm currently encountering some issues and cannot process your request. " \
               f"The error message is: {str(e)}."
    except Exception as e:
        return f"An unexpected error occurred. Please try again later. (Error: {str(e)})"


def get_random_meme():

    try:
        response = requests.get("https://meme-api.com/gimme")
        response.raise_for_status()  

        data = json.loads(response.text)

        if not all(field in data for field in ("title", "url")):
            raise ValueError("Missing required meme data")

        return data
    except Exception as e:
        print(f"Error fetching meme: {e}")
        return None


def get_random_joke():

    try:
        response = requests.get("https://v2.jokeapi.dev/joke/Any?format=txt")
        response.raise_for_status() 
        joke_text = response.text.strip()  
        return joke_text
    except Exception as e:
        print(f"Error fetching joke: {e}")
        return None


st.set_page_config(page_title="Hateful Meme Classification, Chatbot, Research Papers, Random Jokes, and Random Memes")

st.sidebar.header("Navigation")
selected_page = st.sidebar.selectbox("Select a page", [
    "Home",
    "Hateful Meme Classification",
    "Chatbot",
    "Random Jokes",
    "Random Memes",
    "About",
])

if selected_page == "Home":
    st.title("Welcome to our multimodal AI-powered App!")

    html_temp = f"""
    <div style="text-align: center">
      <img src="https://cdn3.emoji.gg/emojis/9228-kiwicatrun.gif" width="200" />
    </div>
    """
    st.write(html_temp, unsafe_allow_html=True)

    st.write("This app offers a variety of functionalities to help you with:")
    st.write("- Identifying hateful content in memes")
    st.write("- Engaging in conversations with a chatbot")
    st.write("- Enjoying a stream of random memes")
    st.write("- Getting a good laugh with random jokes")
    st.write("- Exploring research papers on relevant topics") 


elif selected_page == "Hateful Meme Classification":
    st.header("Hateful Meme Classification")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    prompt = st.text_area("Prompt (Optional)", "Is the given image hateful or nsfw? Consider various aspects that spread hate and nsfw.")

    if st.button('Classify'):
        generate_text(uploaded_file, prompt)

elif selected_page == "Chatbot":
    st.header("Chatbot")
    user_input = st.text_input("Enter your message:")

    if user_input:
        bot_response = chatbot(user_input)
        st.write("Chatbot:", bot_response)

elif selected_page == "Random Jokes":
    st.title("Random Joke Generator")
    if st.button("Get a Random Joke"):
        joke_text = get_random_joke()
        if joke_text:
            st.write(joke_text)
        else:
            st.error("Failed to retrieve joke.")

elif selected_page == "Random Memes":
    st.title("Random Meme Generator")
    if st.button("Get a Random Meme"):
        meme_data = get_random_meme()
        if meme_data:
            st.subheader(meme_data["title"])
            st.image(meme_data["url"])
        else:
            st.error("Failed to retrieve meme.")

elif selected_page == "About":
    st.title("Abstract")
    st.write("""
  Hateful memes are an escalating issue in the digital-landscape, demanding innovative solutions for their effective detection and classification. 
  These memes often employ subtlety, sarcasm, and symbolism, presenting formidable challenges for automated detection systems. 
  Moreover, the linguistic and cultural diversity of the internet, transcending geographical and language boundaries, further complicates the task.

  This project presents a comprehensive approach to hateful meme detection, utilizing a Dual Stream Transformer Model, real-world knowledge integration, characteristic detection, and cultural reference understanding. 
  We emphasize the importance of ethics and responsible usage in deploying such technology, underscoring its potential for positive societal impact.
  """)
    st.write("Here are some links to our research papers on the relevant topic:")
    st.write("- [Hateful Meme Classification using Hateful Content Segregator](https://www.ijaresm.com/hateful-meme-classification-using-hateful-content-segregator)")
    st.write("- [Unmasking Hate: A Multimodal Approach to Hateful Meme Detection](https://ijarsct.co.in/A13192.pdf)")
    