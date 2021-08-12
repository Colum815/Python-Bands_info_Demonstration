bands = [
    {'band': 'Dave Matthews Band', 'album': 'Crash', 'producer': 'Steve LilyWhite'},
    {'band': 'Gregory Alan Isakov', 'album': 'Evening machines', 'producer': 'Andrew Berlin'},
    {'band': 'John Butler Trio', 'album': 'April Uprising', 'producer': 'John Butler'}
]

user_input = """------------------------------------------------------------
Press 'a' to add a band     Press 's' to show the list
Press 'f' to find a band    Press 'q' to quit
------------------------------------------------------------ """


# ------------------------------------------------FUNCTIONS SECTION-----------------------------------------------------
def add_info():
    band_name = input("Enter a band ").title()
    album_name = input("Enter an album ").title()
    producer = input("Enter a producer ").title()
    bands.append({
        "band": band_name,
        "album": album_name,
        "producer": producer
    })

    print("-----------------------")
    print(f"Band: {band_name}\nAlbum: {album_name}\nProducer:{producer}\nhas been added to the list")
    print("-----------------------")


def format_info(i):
    print("---------------------------")
    print(f"Band {i['band']}")
    print(f"Album {i['album']}")
    print(f"Producer {i['producer']}")
    print("---------------------------")



def show_info():
    for band in bands:
        format_info(band)


def find_info():
    user = input("Enter a band to search ").title()
    if any(user in value.values() for value in bands):
        for band in bands:
            if user == band['band'].title():
                format_info(band)
    else:
        print("Not found")


# --------------------------------------------END OF FUNCTIONS SECTION--------------------------------------------------

choose_option = input(user_input).lower()

while choose_option != "q":
    if choose_option == "a":
        add_info()
        choose_option = input(user_input)
    elif choose_option == "s":
        show_info()
        choose_option = input(user_input)
    elif choose_option == "f":
        find_info()
        choose_option = input(user_input)
    else:
        print("Not a valid selection")
        choose_option = input(user_input)


print("Program Ended")