import random

while True:

    hero = input("Enter hero name: ")
    topic = input("Enter story topic: ")

    places = [
        "a mysterious forest",
        "a distant planet",
        "an ancient kingdom",
        "a hidden island"
    ]

    place = random.choice(places)

    stories = [
        hero + " discovered a secret about " + topic + " in " + place + ".",
        hero + " fought enemies while searching for " + topic + " in " + place + ".",
        hero + " solved the mystery of " + topic + " in " + place + "."
    ]

    story = random.choice(stories)

    print("\nGenerating story...\n")
    print(story)

    file = open("story.txt", "a")
    file.write(story + "\n")
    file.close()

    choice = input("\nDo you want another story? (yes/no): ")

    if choice.lower() == "no":
        break
