import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

# Connet to the Groq API and generate text based on the user's input
def DeepSeektext(request):
    try :
        prompt = request["Question"]
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        completion = client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=[{"role": "system", "content": "You are a friendly AI assistant."}, {"role": "user", "content": prompt}],
            temperature=0.6,
            max_completion_tokens=4096,
            top_p=0.95,
            stream=True,
            stop=None,
        )
        data=[]
        for chunk in completion:
            data.append(chunk.choices[0].delta.content )
        return data
    except Exception as e:
        print("Error generating text: ", e)
        return str(e)