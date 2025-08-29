from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()

FULL_NAME = "john_doe"
DOB = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

class InputData(BaseModel):
    data: List[Any]

def is_number(s):
    try:
        int(s)
        return True
    except:
        return False

def is_alpha(s):
    return isinstance(s, str) and s.isalpha()

def is_special(s):
    return isinstance(s, str) and not s.isalnum()

def process_data(data):
    even_numbers, odd_numbers, alphabets, special_characters = [], [], [], []
    num_sum, concat_letters = 0, []

    for item in data:
        s = str(item)
        if is_number(s):
            n = int(s)
            if n % 2 == 0: even_numbers.append(s)
            else: odd_numbers.append(s)
            num_sum += n
        elif is_alpha(s):
            alphabets.append(s.upper())
            concat_letters.append(s)
        elif is_special(s):
            special_characters.append(s)

    all_letters = "".join(concat_letters)[::-1]
    concat_string = "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(all_letters)])

    return {
        "even_numbers": even_numbers,
        "odd_numbers": odd_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(num_sum),
        "concat_string": concat_string
    }

@app.post("/bfhl")
async def bfhl_api(input_data: InputData):
    result = process_data(input_data.data)
    user_id = f"{FULL_NAME.lower()}_{DOB}"
    return {
        "is_success": True,
        "user_id": user_id,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        **result
    }
