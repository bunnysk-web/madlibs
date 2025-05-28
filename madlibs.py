def story_bestfriend():
    print("\nYou've chosen: Spending time with your best friend 👫")
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")
    adverb1 = input("Enter an adverb: ")
    place = input("Enter a place: ")

    story = f"""
    Once upon a time in {place}, there was a {adjective1} {noun1}.
    It loved to {verb1} with its best friend, the {noun2}.
    Every day, they would go on adventures and do everything {adverb1}.
    Their friendship was known all across the land!
    """
    print(story)


def story_resort():
    print("\nYou've chosen: Going to a resort 🏖️")
    name = input("Enter a proper noun: ")
    place = input("Enter a resort name: ")
    adjective = input("Enter an adjective: ")
    activity = input("Enter a fun activity: ")
    adverb = input("Enter an adverb: ")
    food = input("Enter your favorite food: ")

    story = f"""
    {name} went to the beautiful resort called {place}.
    It was a {adjective} place filled with joy and peace.
    {name} would {activity} {adverb} and then relax with some delicious {food}.
    It was truly a vacation to remember!
    """
    print(story)


def main():
    print("🎉 Welcome to the Mad Libs Generator!")
    print("Choose a story type:")
    print("1. Spending time with best friend")
    print("2. Going to a resort")

    choice = input("Enter the number of your choice (1 or 2): ")

    if choice == "1":
        story_bestfriend()
    elif choice == "2":
        story_resort()
    else:
        print("Invalid choice. Please run the program again and choose 1 or 2.")

# Run the program
main()
