import os
import groq
from anthropic import Anthropic
from openai import OpenAI
from groq import Groq

# struct Agent {
#     provider
#     called_agents : []Agents
# } 

# important this should primarily work like a game
# get the most reliable answer with the cheapest cost

class Agent:
    def __init__(self, prev_state) -> None:
        self.
    # providers
    agents: []
    


# client = Groq(
#     # This is the default and can be omitted
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

# client = Groq()

# try:
#     with client.chat.completions.with_streaming_response.create(
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a helpful assisstant.",
#             },
#             {
#                 "role": "user",
#                 "content": "Explain the importance of low latency LLMs",
#             },
#         ],
#         model="mixtral-8x7b-32768",
#     ) as response:
#         print(response.headers.get("X-My-Header"))

#     for line in response.iter_lines():
#         print(line)

# \
# except groq.APIConnectionError as e:
#     print("The server could not be reached")
#     print(e.__cause__)  # an underlying Exception, likely raised within httpx.
# except groq.RateLimitError as e:
#     print("A 429 status code was received; we should back off a bit.")
# except groq.APIStatusError as e:
#     print("Another non-200-range status code was received")
#     print(e.status_code)
#     print(e.response)
    
    
    
"""
model_name

provider (entity that provided this model)
- Anthropic, OpenAI, Groq, Gemini, Mistral

input context window : u64
output context window : u64

cost per input_token : float
cost per output token: float

open_source : boolean
"""