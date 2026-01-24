import google.generativeai as genai
import json

# Replace 'YOUR_API_KEY' with the key you got from AI Studio
genai.configure(api_key="AIzaSyB0Wx_1fdHE3ZXTakH1qPKj3OZEWqzmias")

# This is Step 1 & 4 combined: Setting the persona and the JSON requirement
instructions = (
    "You are a grumpy 1920s Noir Detective. You ONLY provide information if the user provides a 'Clue'. "
    "If no clue is given, stay in character but refuse to cooperate. "
    "Your response must be ONLY a valid JSON object with the keys: "
    "'clue_validity', 'suspect_name', and 'detective_mood'."
)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=instructions
)

# Step 3: Provide the context (Case Evidence)
case_evidence = """
At 10:00 PM, a loud crash was heard in the library. Mr. Boddy was found near the 
bookshelf. A heavy candlestick was lying on the floor. The maid, Sarah, was 
seen polishing silver in the dining room, but her apron had a faint green stain 
from the library's billiard table felt.
"""

user_query = f"The clue is the green stain on the apron. Evidence: {case_evidence}"

# Generate the response
response = model.generate_content(user_query)

# Print the result
print(response.text)