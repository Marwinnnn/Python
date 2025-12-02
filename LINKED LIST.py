class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next_song = None
        self.previous_song = None

class Playlist:
    def __init__(self):
        self.first_song = None
        self.current_song = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if self.first_song is None:
            self.first_song = new_song
            self.first_song.next_song = self.first_song
            self.first_song.previous_song = self.first_song
            self.current_song = self.first_song
        else:
            last_song = self.first_song.previous_song
            new_song.next_song = self.first_song
            new_song.previous_song = last_song
            self.first_song.previous_song = new_song
            last_song.next_song = new_song

    def play_next(self):
        if self.current_song is not None:
            self.current_song = self.current_song.next_song
            print("---------------------------")
            print("Now Playing:", self.current_song.title, "by", self.current_song.artist)
            print("---------------------------")
            if self.current_song == self.first_song:
                print("(End of Playlist - Going Back to Start...)")

    def play_previous(self):
        if self.current_song is not None:
            self.current_song = self.current_song.previous_song
            print("---------------------------")
            print("Now Playing:", self.current_song.title, "by", self.current_song.artist)
            print("---------------------------")

    def show_playing(self):
        if self.current_song is not None:
            print("Current Song:", self.current_song.title, "by", self.current_song.artist)
        else:
            print("Playlist is empty.")

    def show_all_songs(self):
        if self.first_song is None:
            print("Playlist is empty.")
            return
        current = self.first_song
        print("Current Playlist:")
        while True:
            print("-", current.title, "by", current.artist)
            current = current.next_song
            if current == self.first_song:
                break

def main_player():
    my_playlist = Playlist()
    my_playlist.add_song("Stig", "Bugoy na Koykoy")
    my_playlist.add_song("Rapstar", "Gwolf")
    my_playlist.add_song("Hayaan mo sila", "XB")
    my_playlist.add_song("Ediwow", "V-Ganda")

    print("===========================")
    print("Music Playlist Player")
    print("===========================")

    while True:
        my_playlist.show_playing()
        print("Choose an option:")
        print("1. Next Song")
        print("2. Previous Song")
        print("3. Show Playlist")
        print("4. Exit")

        user_choice = input("Enter choice: ")

        if user_choice == '1':
            my_playlist.play_next()
        elif user_choice == '2':
            my_playlist.play_previous()
        elif user_choice == '3':
            my_playlist.show_all_songs()
        elif user_choice == '4':
            print("Exiting player. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main_player()