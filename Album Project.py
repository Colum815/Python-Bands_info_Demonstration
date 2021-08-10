albums = [
    {'band': 'Dave Matthews Band', 'album': 'Crash', 'producer': 'Steve LilyWhite'},
    {'band': 'Gregory Alan Isakov', 'album': 'Evening machines', 'producer': 'Andrew Berlin'},
    {'band': 'John Butler Trio', 'album': 'April Uprising', 'producer': 'John Butler'}
]

user_input = "Press a to add a band,Press s to show the list,Press f to find a band Press q to quit"
choose_option = input(user_input)

#------------------------------------------------FUNCTIONS SECTION------------------------------------------------------
def add_album():
    band_name = input("Enter a band ").title()
    album_name = input("Enter an album ").title()
    producer = input("Enter a producer ").title()

    albums.append(
        {
        "band":band_name,
        "album":album_name,
        "producer":producer
        }
    )
    print("-----------------------")
    print(f"Band: {band_name}\nAlbum: {album_name}\nProducer:{producer}\nhas been added to the list")
    print("-----------------------")
def album_info(i):
    print("-----------------------------")
    print(f"Band: {i['band']}")
    print(f"Album: {i['album']}")
    print(f"Producer: {i['producer']}")
    print("-----------------------------")


def show_albums():
    for album in albums:
        album_info(album)

def find_album():
    user = input("Enter a band you want to look for").title()

    for i in albums:
        if user == i['band']:
            album_info(i)

#-----------------------------------------END OF FUNCTIONS SECTION------------------------------------------------------


while choose_option != "q":
    if choose_option == "a":
        add_album()
        choose_option = input(user_input)
    elif choose_option =="s":
        show_albums()
        choose_option = input(user_input)
    elif choose_option == "f":
        find_album()
        choose_option = input(user_input)
    else:
        print("Not valid try again")
        choose_option = input(user_input)

print("Program Ended")