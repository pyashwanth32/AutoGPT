import os 
from apikey import apikey
import streamlit as st
#from langchain.llms import OpenAI
#from langchain.llms import ChatGoogleGenerativeAI
#from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_google_genai.llms import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
os.environ['GOOGLE_API_KEY'] = apikey

st.title('Essay Creator using Google Gemini API Key')
prompt = st.text_input('Please add your prompt here!')
style = st.selectbox('Choose the writing style:', ['Formal', 'Informal', 'Persuasive'])

title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='Write me an essay title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='write me an essay based on this title: {title} using Wikipedia Research:{wikipedia_research} in a {style} style.'
)

citation_template = PromptTemplate(
    input_variables=['title', 'wikipedia_citation'],
    template='Generate a citation list for the following sources used in an essay titled {title}. Wikipedia: {wikipedia_citation}.'
)


title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

#llm = OpenAI(temperature=0.9)
llm = GoogleGenerativeAI(
    api_key=os.environ["GOOGLE_API_KEY"],
    model="gemini-pro"
)   

title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)
citation_chain = LLMChain(llm=llm, prompt=citation_template, verbose=True, output_key='citations')
wiki = WikipediaAPIWrapper()

if prompt: 
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt) 
    script = script_chain.run(title=title, wikipedia_research=wiki_research, style = style)
    citations = citation_chain.run(
        title=title, 
        wikipedia_citation=f"Wikipedia: {wiki_research[:50]}... (Retrieved from Wikipedia)"
    )

    st.write(title) 
    st.write(script) 

    with st.expander('Title History'): 
        st.info(title_memory.buffer)

    with st.expander('Script History'): 
        st.info(script_memory.buffer)

    with st.expander('Wikipedia Research'): 
        st.info(wiki_research)

    with st.expander('Citations'): 
        st.write(citations)

