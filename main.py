
import pandas as pd
import numpy as np
import streamlit as st
class Spotify_Recommendation():
    def __init__(self, dataset):
        self.dataset = dataset
    def search(self, user_songs, amount):
        same_tracks_lst = []
        columns = ['artist_name', 'track_name', 'album_name']
        for track in df.track_name.str.lower():
            same_tracks_lst.append(((user_songs.lower() == track) or (user_songs.lower() in track)))
        song = self.dataset[same_tracks_lst]
        song = song[columns]
        song = song.drop_duplicates()
        return song[:amount]
    def recommend(self, user_songs, amount=5):
        distance = []
        try:
            # Take the identitcal songs
            same_tracks_lst = []
            for track in df.track_name.str.lower():
                same_tracks_lst.append(((user_songs.lower() == track) or (user_songs.lower() in track)))
            song = self.dataset[same_tracks_lst].head(1).values[0]
            # Take the other songs
            other_tracks_lst = []
            for track in df.track_name.str.lower():
                other_tracks_lst.append(user_songs.lower() != track)
            rec = self.dataset[other_tracks_lst]
        except:
            # if there where any error display this message
            st.write('\nsomething goes wrong...')
            return
        for songs in rec.values:
            d = 0
            for col in np.arange(len(rec.columns)):
                # Take the numerical columns only
                if not col in [0, 1, 2, 3, 10, 11, 12, 13, 14, 15, 16, 28, 29, 30, 31, 32]:
                    '''
                    - Compare the danceability ,energy ,loudness
                      ,mode ,speechiness ,acousticness ,instrumentalness
                      , liveness, valence and tempo between recommended songs and users songs
                    '''
                    d = d + np.absolute(float(song[col]) - float(songs[col]))
            distance.append(d)
        rec['distance'] = distance
        rec = rec.sort_values('distance')
        columns = ['artist_name', 'track_name', 'album_name']
        return rec[columns][:amount]

st.image('spotify.png')

#path = r'C:\Users\hp\Downloads\Spotify_datasets\final df.csv'
df = pd.read_csv('final df.csv')

def main():
    title = st.text_input("- Enter the song title here...").lower()
    
    try:
            amount = int(st.text_input("- How many recommendations do you want (Enter an integer number): ")) #st.slider('Pick a number', 0, 100)
            if st.button("Search"):
                try:
                    st.write('- Search results:')
                    search = Spotify_Recommendation(df)
                    search_songs = search.search(title, amount)
                    st.write(search_songs)
                    st.write('--------------------------------------------')
                    st.write('- Recommended for you:')
                    st.write('These songs have small difference in danceability, energy, loudness,mode, speechiness, '
                         'acousticness, instrumentalness, liveness, valence and tempo.')
                    recomendations = Spotify_Recommendation(df)
                    recommended_songs = recomendations.recommend(title, amount)
                    st.write(recommended_songs)
                    
                except Exception as e:
                    st.write("Something goes wrong..")

    except:
            st.write()
        


if __name__ == '__main__':
    main()
    
#https://vedantbalapurkar-spotify-million-songs-playlist-rec-main-559eq0.streamlitapp.com/    
