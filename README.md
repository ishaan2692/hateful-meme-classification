# hateful-meme-classification
An AI-powered App's - Code Documentation

Introduction

This documentation provides a comprehensive overview of the code for the AI-powered Streamlit application. It details the functionalities offered, technical dependencies, and code structure, serving as a valuable resource for developers and users alike.

Functionalities

The application leverages Google GenerativeAI to deliver a range of functionalities:

 Hateful Meme Classification: Identify and classify potentially offensive or NSFW content within images using image classification techniques.
 Chatbot Interaction: Engage in stimulating conversations with a chatbot that utilizes natural language processing for responsive interactions.
 Random Joke Generation: Generate laughter on demand with the random joke generator.
 Random Meme Stream: Immerse yourself in a continuous stream of entertaining memes retrieved from a dedicated online API.
 Research Paper Exploration: Gain valuable insights into relevant research papers through informative summaries and readily accessible links.

Technical Dependencies

The application relies on the following Python libraries:

 Streamlit: Streamlines the creation of interactive web app interfaces.
 Requests: Facilitates communication with external services like APIs.
 JSON: Enables parsing of JSON-formatted data received from APIs.
 Google GenerativeAI: Provides pre-trained models for image classification and text generation.
 OS (Optional): May be used for environment variable management.
 Dotenv (Optional): Enables secure loading of environment variables from a `.env` file (likely for API tokens).
 Pillow (PIL.Image): Provides functionalities for image processing.

Code Breakdown

The code is structured to handle various functionalities and user interactions:

 Functionalities:
     `generate_text(uploaded_file, prompt)`: Manages image upload, prompt input, image classification using a pre-trained model, and error handling for hateful/NSFW content and invalid images.
     `chatbot(prompt)`: Processes user prompts and generates responses using a pre-trained model, with exception management for potential errors.
     `get_random_meme()` and `get_random_joke()`: Fetch random memes and jokes from external APIs, respectively, and handle potential errors during the process.
 User Interface (Streamlit):
     `st.set_page_config`: Sets the title of the app.
     `st.sidebar` components: Create a navigation menu for users to select functionalities.
     Conditional statements (`if selected_page == "Home"` etc.): Dynamically display content based on user selection.
     Various Streamlit elements (`st.title`, `st.text_area`, `st.button`, `st.image`, etc.): Build an informative and interactive user interface.
