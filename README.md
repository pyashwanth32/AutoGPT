#AutoGPT

Please Note: Make sure you have added money into your OpenAI Account for API key usage, else the prompts won't work.


Make sure the set the environment variables to:
set GOOGLE_API_KEY=insert_your_gemini_api_key_here

Dependencies:
1. pip install langchain-google-genai
2. pip install streamlit langchain openai wikipedia chromadb tiktoken


Got this error while installing chromadb:
error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/ [end of output] note: This error originates from a subprocess, and is likely not a problem with pip. ERROR: Failed building wheel for chroma-hnswlib Failed to build chroma-hnswlib ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (chroma-hnswlib).

So I used the following website instructions (along with installing MSVC Build Tools):
https://stackoverflow.com/questions/73969269/error-could-not-build-wheels-for-hnswlib-which-is-required-to-install-pyprojec![image](https://github.com/user-attachments/assets/3dcab2af-b28c-4123-9d33-466e819d7c94)

To run the application:
```
streamlit run app.py
```
