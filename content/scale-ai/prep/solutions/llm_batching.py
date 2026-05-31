# =============================================================================
# LLM INPUT/OUTPUT BATCHING — Scale AI Backend Practical
# =============================================================================
#
# There is a black-box LLM (synchronous call). Design a system that:
#
# 1. Asynchronously receives user input
# 2. Internally splits the input into hundreds of pieces
#    and calls the LLM black box for each piece
# 3. Sends the aggregated results back to the user via notification
#
# CONSTRAINTS:
#   - LLM call is synchronous (blocking)
#   - Input can be split into hundreds of chunks
#   - Must handle many concurrent user requests
#   - Results must be aggregated and sent back when all chunks are done
#
# THINK ABOUT:
#   - How do you call the LLM for each chunk without blocking the main thread?
#   - How do you know when ALL chunks for a request are done?
#   - How do you send the result back to the user?
#
# KEY CONCEPTS:
#   - ThreadPoolExecutor  → parallelize sync LLM calls
#   - Queue               → decouple input receiving from processing
#   - futures / as_completed → wait for all chunks, aggregate
#   - callback/webhook    → notify user when done
#
# EXAMPLE:
#   user sends: "Summarize this 10,000 word document"
#   system splits into 100 chunks of 100 words each
#   calls LLM(chunk) for each → 100 parallel calls
#   aggregates 100 responses → sends final summary to user
#
# =============================================================================

from queue import Queue
import random
import time
import uuid
import numpy as np 
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# --- Black-box LLM (do not modify) ---
def llm(chunk: str) -> str:
    time.sleep(0.05)  # simulates network latency
    return f"[result for: {chunk[:20]}]"

# --- Your implementation below ---
# TODO: split input into chunks

def split(text, chunk_size=100):
    words = text.split()
    
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words) , chunk_size) ]
# TODO: call llm() for each chunk in parallel using ThreadPoolExecutor
def process(text):
    chunks = split(text, chunk_size=100)
    res = [None] * len(chunks)
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(llm, chunk): i for i, chunk in enumerate(chunks) }
        for future in as_completed( futures ):
            x = futures[future]
            res[x] = future.result()
        
    return res

def notify(result, user_id):
    print(f"{result=} for {user_id=}")

def handle_requests(user_id, text):
    job_id = str(uuid.uuid4())
    def background():
        results = process(text)
        notify(results, user_id) 
    threading.Thread(target=background, daemon=True ).start()
    return job_id
# TODO: aggregate results in order

# TODO: notify user (print for now)

words = np.random.choice(
    ['some', 'example', 'words', 'and', 'sentences', 'are'],
    size=200
    )
text = ' '.join(words)
# split(text)
handle_requests('id', text)
handle_requests('id6', text)
time.sleep(3)


            