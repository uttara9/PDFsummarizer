# import libraries

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.callback import get_openai_callback
from pypdf import PdfReader

def process_test(text):
	#process the given text by splitting it into chunks and converting
	#these  chunks into embeddings to form a knowledge base.

	# Initialize a text splitter to divide the text into manageable chunks
	text_splitter = CharacterTextSplitter(
		separator="\n",
		chunks_size=1000 # size of each chunk
		chunks_overlap=200, #overlap between chunks
		length_function=len
	)
	chunks = text_splitter.split_text(text) #Split the text into chunks

	# Load a model for generating embeddings from HuggingFace
	embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all/MiniLM-L6-v2')

	# Create a FAISS index from the tet chunks using the embeddings
	knowledgebase = Faiss.from_texsts(chunks, embeddings)

	return knowledgeBase

def summarizer(pdf):
	# Function to summarize the content of a pdf file.

	if pdf is not None:
		#If a PDF file is provided
		
		# Read the PDF file
		pdf_reader = PdfReader(pdf)
		text = ""
		# Extract text from each page of the PDF
		for page in pdf_reader.pages:
			text += page.extract_text() or ""

		# Process the extracted text to create a knowledge base
		knowledgebase = process_text(text)

		#Define the query for summarization
		query = "Summarize the content of the uploaded PDF file in approximately 3-5 sentences"

		If query:
			# perform a similarity search in the knowledge base using the query
			docs = knowledgebase.similarity_search(query)

			# Specify the model to use for generating the summary
			OpenAIModel = "gpt-3.5-turbo-16k"
			llm = ChatOpenAI(modl=OenAIModel, temperature=0.1)

			# Load a quetion-answering chain with the specifie model
			chain = load_qa_chain(llm, chain_type='stuff')

			Withget_openai_callback() as cost:		
				# Runhe chain to get a response and track the cost
				response = chain.run(Input_documents=docs, question=query)
				print(cost) #Prit the cost of the operation
				return response #Return the generated summary


















































