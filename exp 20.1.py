# Vocabulary Flashcard Application

flashcards = {
    "Abundant": "Available in large quantities",
    "Brave": "Showing courage",
    "Rapid": "Very fast",
    "Ancient": "Very old",
    "Honest": "Truthful"
}

score = 0

for word, meaning in flashcards.items():
    print("\nWord:", word)
    answer = input("Enter the definition: ")

    if answer.strip().lower() == meaning.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect! Definition:", meaning)

total = len(flashcards)
print("\nFinal Score:", score, "/", total)
print("Accuracy:", round(score / total * 100, 2), "%")