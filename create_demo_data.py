import requests
import random
import threading

names = ["Bob", "Joe", "Harry", "Sam", "Lemon", "Gabby", "Pat", "Luca", "Trixie", "Jacob", "Pumpkin", "Smokey", "Garfield", "Oscar", "Winnie", "Millie", "Alvin", "Cocoa", "Harry", "Crookshanks"]
breeds = ["Orange", "Black", "Tabby", "American Shorthair", "British Shorthair", "Scottish Fold", "Birman", "Maine Coon", "British Longhair"]

def create_cats():
    for i in range(10000):
        response = requests.post("http://localhost:8000/api/v1/cat/", data={
            "name": random.choices(names),
            "breed": random.choices(breeds),
            "age": random.randint(1, 18),
            "weight": random.randint(1, 20),
            "sex": "Male" if random.randint(1, 2) == 1 else "Female",
            "adopted": True if random.randint(1, 2) == 1 else False
        })
        print(i)

if __name__ == "__main__":
    threads = []
    for _ in range(8):
        t = threading.Thread(target=create_cats)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
        
    