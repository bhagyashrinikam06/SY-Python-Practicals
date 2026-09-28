# 5 days × 5 hour slots
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
schedule = [["-" for _ in days] for _ in range(5)]

while True:
    print("\nSchedule:")
    print("   ", *days)
    for i in range(5):
        print(i, schedule[i])

    h = int(input("Hour (0-4): "))
    d = int(input("Day (0=Mon ... 4=Fri): "))
    schedule[h][d] = input("Enter subject: ")

    if input("Update more? (y/n): ").lower() != "y":
        break
