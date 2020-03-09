name = input("Write the name: ")

def two_fer(name = ""):
    if name != "":
        return f"One for {name}, one for me."
    else :
        return "One for you, one for me."


two_fer(name)
