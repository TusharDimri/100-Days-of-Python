import spotify

date = input("Enter the date for which you want to create the playlist for. Format-YYYY-MM-DD: ")

spotify.add_to_playlist(date=date)