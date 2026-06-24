import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as file:
        return json.load(file)

def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_memory(user, jarvis):
    memory = load_memory()
    memory.append({"user": user, "jarvis": jarvis})
    save_memory(memory)