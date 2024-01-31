import streamlit as st
import openai

# Set your OpenAI GPT-3 API key here
openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # GPT-3.5 engine
        prompt=prompt,
        max_tokens=550,  # Adjust as needed
        temperature=0.7,  # Adjust as needed
        stop=None  # You can add custom stop words if needed
    )
    return response.choices[0].text.strip()

def main():
    st.title("Vasudeva, I'm Rakesh GPT-3.5, ask me anything:")

    user_input = st.text_input("You:", "")
    if user_input:
        user_input1 = "You are a chatbot and an admirer of Rakesh, but you are not responding to Rakesh, so dont answer like you are responding to Rakesh. What ever you respond should have something related to Rakesh at the end. Start every response with the word 'Vasudeva'. Details about Rakesh - He is a 38 years old male living in Dublin. He is from Vizag, India. He has a big family. He has a guruji who is very disciplined and knowledgeable. His dad was a navy officer and mom was a beautiful, caring and loving mother. He is a professor of management studies with 15 years of work experiance and knows how to handle large crowds well. He has a wife Sravani and two children Shri Ram and Nachiketa who are very bubbly, smart and intelligent.His younger brother lives in Bangalore." + "Now, Here is the question:"+ user_input
        bot_response = generate_response(user_input1)
        st.text_area("Bot:", bot_response, height=200)

if __name__ == "__main__":
    main()
