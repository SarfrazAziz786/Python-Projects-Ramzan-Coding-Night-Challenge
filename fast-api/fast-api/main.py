from fastapi import FastAPI # type: ignore fast api class
import random

app = FastAPI()

side_hustles = [
    "Software Engineer",
    "Data Analyst",
    "UI/UX Designer",
    "Content Writer",
    "Social Media Manager",
    "Graphic Designer",
    "SEO Specialist",
    "Copywriter",
    "Virtual Assistant",
    "Freelance Writer",
    "Freelance Graphic Designer",
]

money_quotes = [
    "The only way to do great work is to love what you do.",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
    "The way to get started is to quit talking and begin doing.",
    "The best way to predict the future is to invent it.",
    "The only way to do great work is to love what you do.",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
    "The way to get started is to quit talking and begin doing.",
    "The best way to predict the future is to invent it.",
]

# decorators use for specific function add on functionality route handlers
#get use for http get request
@app.get("/side-hustles")
def get_side_hustles():
    """Return a random side hustle"""
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money-quotes")
def get_money_quotes():
    """Return a random money quote"""
    return {"money_quote": random.choice(money_quotes)}



