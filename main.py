def decision(choice: str) -> str:
    """
    this looks at what the user entered and returned a code.
    """
    if choice == "y":
        return "1"
    elif choice == "n":
        return "-1"
    else:
        return "0"

def main():
    while True:
        selection = input("what is your choice: y or n? ").strip().lower()
        code = decision(selection)

        if code == "1":
            print("you chose yes")
            break
        elif code == "-1":
            print("you chose no")
            break
        else:
            print("you did not choose y or n. please try again.")

if __name__ == "__main__":
    main()


