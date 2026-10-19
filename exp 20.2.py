questions = {
    "Follow company policies?": True,
    "Share confidential data without permission?": False,
    "Follow safety rules?": True,
    "Is bribery acceptable?": False,
    "Report compliance violations?": True
}

score = 0

for q, ans in questions.items():
    print(q)
    if input("True/False: ").strip().lower() == str(ans).lower():
        score += 1

accuracy = score / 5 * 100
print("\nScore:", score, "/ 5")
print("Accuracy:", accuracy, "%")
print("Result:", "PASS" if accuracy >= 80 else "FAIL")