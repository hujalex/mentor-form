from fuzzywuzzy import fuzz
from fastapi import FastAPI, app, HTTPException
import pandas
from pydantic import BaseModel
import numpy as np

app = FastAPI()

class user_list(BaseModel):
    user_list_info: dict
    target_name: str

@app.post("/api")
async def read_item(message : user_list):
    try:
        user_list_info: dict = message.user_list_info
        target_name = message.target_name

        user_names = user_list_info.keys()
        fuzzy_ratios = np.empty(len(user_names))

        for i in enumerate(user_names):
            fuzzy_ratios[i] = fuzz.ratio(user_names, target_name)
    
        max_ratio_idx = np.argmax(fuzzy_ratios)

        return user_list_info[user_names[max_ratio_idx]]
        
    except Exception as e:
        raise HTTPException(status_code = 500, detail = f"Error in processing Post Request {e}")



