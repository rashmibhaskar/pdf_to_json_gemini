# Resources- https://ai.google.dev/gemini-api/docs/document-processing?lang=python

#Step 1: Get Gemini API key
#Step 2: pip install -U google-generativeai
#Step 3: Configure your API : Relace with "YOUR API"
#Step 4: Define the path of your df file
#Step 5: Run the following code using : python3.9 pdf_to_json_gemini.py
import os
import google.generativeai as genai

genai.configure(api_key="YOUR API")

model = genai.GenerativeModel("gemini-1.5-flash")


model = genai.GenerativeModel("gemini-1.5-flash")
sample_file = genai.upload_file(path="./standard_application.pdf", display_name="Sample file")
response = model.generate_content(["Generate the all form fields in this pdf document in a json format", sample_file])
print(response.text)