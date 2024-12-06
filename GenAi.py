import google.generativeai as genai

genai.configure(api_key="AIzaSyDzSK_VNYgRjKtocL29voSQdOuw44iMNVQ")
model = genai.GenerativeModel("gemini-1.5-flash")
prompt= f"""short description into something more actionable for blind person  : a man with glasses on taking a self
            do or die rules: 
            --------------------------------------
            1. just give the description about the objects seen in caption
            2. keep the description simple may be within 30 characters
            3. Do not include the description about the surface

            example output 1: 
            ---------------------------------------
            computer screen with a picture of person on it.

            example output 2:
            ---------------------------------------
            A chair infront of a table.

            Strictly follow the given instruction and provide the output

"""
response = model.generate_content(prompt)
print(response.text)
