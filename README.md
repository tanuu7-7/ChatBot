Interactive AI Chatbot with Memory

This project is an interactive chatbot built with Streamlit that leverages LLaMA 2 and LangChain to provide context-aware conversations. The chatbot remembers previous user inputs to respond more accurately, making it ideal for applications that require continuous dialogue.

Features:

Contextual Memory: Remembers recent user inputs to deliver context-aware responses.

Streamlit UI: Provides a simple and interactive web-based interface for easy user interaction.

Customizable Models: Utilizes the LLaMA 2 model for language processing and can be configured with other compatible models.

Directory Structure:

MyChatbotProject/

│

├── app.py                   # Main application script for Streamlit

├── requirements.txt         # Project dependencies

├── .gitignore               # Specifies files to ignore in Git

├── models/                  # Directory for model binaries

│   └── llama-2-7b-chat.ggmlv3.q8_0.bin  # LLaMA model binary

└── README.md                # Project description and setup instructions

Setup Instructions:

1.Clone the Repository:

git clone <repository-url>

cd MyChatbotProject

2.Install Required Dependencies:

pip install -r requirements.txt

3.Download the LLaMA Model:

Download the LLaMA model binary  llama-2-7b-chat.ggmlv3.q8_0.bin from 'https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML'

4.Run the Streamlit App:

streamlit run app.py

Usage:

Once the app is running, you can interact with the chatbot by typing your questions in the input box. The chatbot maintains a memory of the last few interactions, allowing it to provide contextually relevant responses.

Future Enhancements:

Extended Memory Management: Implement a more scalable way to store conversation history.

Multi-Model Support: Extend compatibility to include more language models beyond LLaMA.

Fine-tuned Responses: Adjust model parameters to customize conversational tones and styles.

License

This project is licensed under the MIT License - see the LICENSE file for details.
