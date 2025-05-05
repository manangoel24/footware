import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class ShoeAdvisorAgent:
    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def recommend(self, purpose, comfort, durability, style, brand):
        prompt = f"""
        You are a helpful AI shoe advisor. Based on the user's preferences, provide a detailed shoe recommendation including features to look for, example types, and reasoning.

        Preferences:
        - Purpose: {purpose}
        - Comfort: {comfort}
        - Durability: {durability}
        - Style: {style}
        - Preferred Brand: {brand if brand else 'None'}

        Respond in markdown format. Use bullet points where useful.
        """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "system", "content": "You are an expert footwear consultant."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
