artists = []

def add_artist():
    name = input("Enter the name of the artist: ")
    genre = input("Enter the genre of the artist: ")
    duration = input("Enter the duration of the performance: ")
    artist_info = {"name": name, "genre": genre, "duration": duration}
    artists.append(artist_info)
    print(f"Artist {name} has been added to the list.")
    main()

def edit_artist():
    name = input("Enter the name of the artist to edit: ")
    for artist in artists:
        if artist["name"] == name:
            print(f"Artist found: {artist}")
            choice = input("What do you want to change? 1: Name, 2: Genre, 3: Duration: ")
            if choice == "1":
                new_name = input("Enter the new name: ")
                artist["name"] = new_name
                print(f"Name changed to {new_name}")
            elif choice == "2":
                new_genre = input("Enter the new genre: ")
                artist["genre"] = new_genre
                print(f"Genre changed to {new_genre}")
            elif choice == "3":
                new_duration = input("Enter the new duration: ")
                artist["duration"] = new_duration
                print(f"Duration changed to {new_duration}")
            else:
                print("Invalid choice")
            main()
            return
    print(f"Artist {name} not found in the system.")
    main()

def remove_artist():
    name = input("Enter the name of the artist to remove: ")
    for artist in artists:
        if artist["name"] == name:
            artists.remove(artist)
            print(f"Artist {name} has been removed.")
            main()
            return
    print(f"Artist {name} not found in the system.")
    main()

def view_artists():
    print("Artists in the system:")
    for artist in artists:
        print(artist)
    main()

def main():
    print("1: Add an Artist")
    print("2: Edit an Artist")
    print("3: Remove an Artist")
    print("4: View all Artists")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_artist()
    elif choice == "2":
        edit_artist()
    elif choice == "3":
        remove_artist()
    elif choice == "4":
        view_artists()
    else:
        print("Invalid choice")
        main()

main()