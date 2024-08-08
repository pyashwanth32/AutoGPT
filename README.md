# AutoGPT - Automatic Essay Writer using Google Gemini API Key

## 1 Introduction
The AutoGPT Essay Creator is a web-based application designed to automatically generate essays on any given topic. By leveraging advanced language models and external resources like Wikipedia, the application provides users with coherent and informative essays, enhancing both productivity and creativity in writing tasks.

## 2 Dependencies
Please Note: Make sure you have added money into your OpenAI Account for API key usage, else the prompts won't work.

Make sure the set the environment variables to:
set GOOGLE_API_KEY=insert_your_gemini_api_key_here
![Setting the Environment Variable in your PC](https://github.com/pyashwanth32/AutoGPT/blob/main/Additional_Pictures/Environment_Variable_Setting.png)

Install the following libraries
1. pip install langchain-google-genai
2. pip install streamlit langchain openai wikipedia chromadb tiktoken

Got this error while installing chromadb:
```
error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": 
https://visualstudio.microsoft.com/visual-cpp-build-tools/ [end of output] note: This error originates from a subprocess, and is likely not a problem with pip. ERROR: Failed building wheel for chroma-hnswlib Failed to build chroma-hnswlib ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (chroma-hnswlib).
```
So I used the following website instructions (along with installing MSVC Build Tools):
```
https://stackoverflow.com/questions/73969269/error-could-not-build-wheels-for-hnswlib-which-is-required-to-install-pyprojec
```

To run the application:
```
streamlit run app.py
```

## 3 Objectives
1. Automate Essay Writing: Enable users to generate essays on a wide range of topics with minimal input.
2. Utilize AI and External Resources: Combine AI models with Wikipedia research to produce well-informed content.
3. User-Friendly Interface: Provide a simple interface for users to input topics and receive essays.

## 4 Technology Stack
1. Streamlit: A popular Python library for creating interactive web applications. It is used to build the user interface of the application.
2. LangChain: A framework designed to build applications powered by language models. It facilitates the integration of different models and utilities.
3. OpenAI: Previously commented out, indicating potential use of OpenAI's models.
4. Google Generative AI: Utilized via the langchain_google_genai library, specifically the Gemini model, to generate essay content.
5. Wikipedia: Used to fetch research content related to the topic provided by the user.
6. ChromaDB and Tiktoken: Installed but not directly used in this script. They might be intended for more advanced data handling or tokenization processes.

## 5 System Architecture
### 5.1 Components
1. User Interface (UI): 
    Built using Streamlit to capture user input and display results.
    Users enter a topic prompt, and the application generates an essay based on this input.

2. Language Model Chains:
    Title Chain: Generates an essay title based on the input topic using Google Generative AI.
    Script Chain: Produces the essay content by utilizing the generated title and Wikipedia research.

3. Memory Management:
    Utilizes ConversationBufferMemory from LangChain to store conversation history for both titles and scripts, enhancing the application's contextual understanding over time.

4. External Research:
    Uses WikipediaAPIWrapper to fetch relevant information from Wikipedia, ensuring that the generated essays are well-informed.

### 5.2 Process Flow
1. Input Handling:
    The user provides a topic via a text input field.

2. Title Generation:
    The title_chain uses the topic to generate a suitable essay title, storing the history in title_memory.

3. Research Integration:
    Wikipedia API is queried for information related to the topic to inform the essay.

4. Essay Generation:
    The script_chain uses both the generated title and Wikipedia research to produce a comprehensive essay.

5. Output and History:
    The application displays the essay title and content.
    Users can view historical data for titles, scripts, and Wikipedia research using expandable sections.

## Future Enhancements
1. Expand Model Options: Enable switching between different language models (e.g., OpenAI's GPT models).
2. Advanced Research: Incorporate more external data sources or databases for richer content generation.
3. User Customization: Allow users to specify essay length, tone, or specific points to be covered.

## Conclusion
The AutoGPT Essay Creator represents a significant step towards automating the essay writing process. By integrating cutting-edge AI models with a simple and intuitive interface, it provides a valuable tool for anyone needing quick, coherent, and informative written content.
