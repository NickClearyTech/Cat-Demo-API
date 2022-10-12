import requests
import random
import threading
import numpy

names = ["Bob", "Joe", "Harry", "Sam", "Lemon", "Gabby", "Pat", "Luca", "Trixie", "Jacob", "Pumpkin", "Smokey", "Garfield", "Oscar", "Winnie", "Millie", "Alvin", "Cocoa", "Harry", "Crookshanks"]
breeds = ["Orange", "Black", "Tabby", "American Shorthair", "British Shorthair", "Scottish Fold", "Birman", "Maine Coon", "British Longhair"]

def create_cats():
    for i in range(5000):
        age = numpy.random.choice(numpy.arange(1, 17), 1, p=[0.1, 0.15, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.04, 0.04, 0.03, 0.02, 0.02])[0]
        sex = "Male" if random.randint(1, 2) == 1 else "Female"
        if sex == "Male":
            weight = random.randint(5, 18)
        else:
            weight = random.randint(3, 15) - 2
        response = requests.post("http://localhost:8000/api/v1/cat/", data={
            "name": random.choices(names),
            "breed": random.choices(breeds),
            "age": age,
            "weight": weight,
            "sex": sex,
            "adopted": numpy.random.choice([True, False], 1, p=[0.65, 0.35])[0]
        })
        print(i)

if __name__ == "__main__":
    threads = []
    for _ in range(16):
        t = threading.Thread(target=create_cats)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
