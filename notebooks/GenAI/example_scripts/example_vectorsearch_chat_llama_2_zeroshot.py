from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
#from langchain_google_vertexai import VertexAIModelGarden
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_google_vertexai import VectorSearchVectorStore
from langchain_google_vertexai import ChatVertexAI
from langchain_google_vertexai import VertexAI
import sys
import json
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

MAX_HISTORY_LENGTH = 1

def build_chain():
    #if using model from uncomment Model Garden
    
    PROJECT_ID = os.environ["PROJECT_ID"]
    LOCATION_ID = os.environ["LOCATION_ID"]
    #ENDPOINT_ID = os.environ["ENDPOINT_ID"]
    BUCKET = os.environ["BUCKET"]
    VC_INDEX_ID = os.environ["VC_INDEX_ID"]
    VC_ENDPOINT_ID = os.environ["VC_ENDPOINT_ID"]
    
    
    #llm = VertexAIModelGarden(project=PROJECT_ID, endpoint_id=ENDPOINT_ID, location=LOCATION_ID)
    llm = VertexAI(
    model_name="gemini-2.0-flash",
    max_output_tokens=1024,
    temperature=0.2,
    top_p=0.8,
    top_k=40,
    verbose=True,
)
    embeddings = VertexAIEmbeddings(model_name="textembedding-gecko@003")

    vector_store = VectorSearchVectorStore.from_components(
        project_id=PROJECT_ID,
        region=LOCATION_ID,
        gcs_bucket_name=BUCKET,
        embedding=embeddings,
        index_id=VC_INDEX_ID,
        endpoint_id=VC_ENDPOINT_ID
    )
    

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k":3}
    )
  
    prompt_template = """
    Ignore everything before.
    Instructions:
    I will provide you with research papers on a specific topic in English, and you will create a cumulative summary. 
    The summary should be concise and should accurately and objectively communicate the takeaway of the papers related to the topic. 
    You should not include any personal opinions or interpretations in your summary, but rather focus on objectively presenting the information from the papers. 
    Your summary should be written in your own words and ensure that your summary is clear, concise, and accurately reflects the content of the original papers. First, provide a concise summary then citations at the end.
    {question} Answer "don't know" if not present in the document. 
    {context}
    Solution:"""

    
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"],
    )

    condense_qa_template = """
    Chat History:
    {chat_history}
    Here is a new question for you: {question}
    Standalone question:"""
    standalone_question_prompt = PromptTemplate.from_template(condense_qa_template)

    #RetrievalQA.from_chain_type(llm=llm, chain_type="stuff"
    qa = ConversationalRetrievalChain.from_llm(
        llm=llm, 
        retriever=retriever, 
        condense_question_prompt=standalone_question_prompt, 
        return_source_documents=True, 
        combine_docs_chain_kwargs={"prompt":PROMPT},
        )
    return qa

def run_chain(chain, prompt: str, history=[]):
    print(prompt)
    return chain({"question": prompt, "chat_history": history})

if __name__ == "__main__":
  chat_history = []
  qa = build_chain()
  print(bcolors.OKBLUE + "Hello! How can I help you?" + bcolors.ENDC)
  print(bcolors.OKCYAN + "Ask a question, start a New search: or CTRL-D to exit." + bcolors.ENDC)
  print(">", end=" ", flush=True)
  for query in sys.stdin:
    if (query.strip().lower().startswith("new search:")):
      query = query.strip().lower().replace("new search:","")
      chat_history = []
    elif (len(chat_history) == MAX_HISTORY_LENGTH):
      chat_history.pop(0)
    result = run_chain(qa, query, chat_history)
    chat_history.append((query, result["answer"]))
    print(bcolors.OKGREEN + result['answer'] + bcolors.ENDC)
    if 'source_documents' in result:
        print(bcolors.OKGREEN + 'Sources:')
        for idx, ref in enumerate(result["source_documents"]):
            print(ref.page_content)            
    print(bcolors.ENDC)
    print(bcolors.OKCYAN + "Ask a question, start a New search: or CTRL-D to exit." + bcolors.ENDC)
    print(">", end=" ", flush=True)
  print(bcolors.OKBLUE + "Bye" + bcolors.ENDC)
