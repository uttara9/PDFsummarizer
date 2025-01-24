import streamlit as st # Importing the SteamLit Library
import os # Importing the os module for environment variable management
from utils import *



# Main function to run the Steamlit app.

def main():
	# Set page configurations
	st.set_page_config(page_title="PDF Summarizer")
	# Some changes

	st.title("PDF Summarizing App") # Setting the title of the app
	st.write("Summarize your pdf files in just a few seconds.") # Displaying a description
	st.divider() # Inserting a divider for better layout

	# creating a file uploader widget to upload PDF files
	pdf = st.file_uploader('Upload your PDF Document, type='pdf')

	# Creating a button for users to submit their PDF for summarization
	submit= st.button("Generate Summary")

	# Setting the OpenAI API key as an environment variable
	os.environ["OEPNAI_API_KEY"] = "sk_WPe76XLtM3w79qeS7HDyT3BlbkFj4emKQXseVEsSTKsUjnxN"

	If submit:
	# If the submit button is pressed
	# Calling the summarizer function from utils module with the uploaded PDF
	response = summarizer(pdf)	


	# Displaying the summary of the PDF file
	st.subheader('Summary of File:)
	st.write(response)

#Python script execution starts hear
if __name__ == '__main__":
	main() # calling the main function to start the Streamlit app












