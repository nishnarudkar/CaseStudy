import google.generativeai as genai
import os

def generate_response(query, data):
    try:
        # Convert data to JSON or formatted string
        data_str = data.to_csv(index=False)
        
        # Initialize Gemini model
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        
        generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        }
        safety_settings = [
        {   "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"       },
        {   "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"       },
        {   "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"       },
        {   "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"       },
        ]
        
        model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
        
        convo = model.start_chat(history=[])
        
        # Create prompt for the LLM
        prompt = f"""
        Based on the following data, answer the query in detail:
        
        Data:
        {data_str}
        
        Query:
        {query}
        """
        
        convo.send_message(prompt)
        
        # Generate response
        response = convo.last.text
        return response
    except Exception as e:
        return f"Error generating response: {e}"
