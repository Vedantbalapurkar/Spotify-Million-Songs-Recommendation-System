# Spotify-Million-Songs-Recommendation-System 
This is data for songs and the most reflective thing about the song is the name of the track and album.
Also, the artist name which is categorized according to the type of songs the artist sings.
We depended on the track name , album name, and artist name.

### Understanding the Dataset
The dataset we are working on is a combination of four json files
('mpd.slice.0-999.json’, 'mpd.slice.1000-1999.json', 'mpd.slice.2000-2999.json', ' mpd.slice.3000-3999.json')
Each data set contained different playlists.


## EDA


- **merged_data** dataset comprises of 144276 rows and 33 columns.
- Dataset comprises of continious variable and float data type. 
- Dataset column varaibales 'danceability','energy'|'key'|'loudness'|mode'|'speechiness'|'acousticness'|'instrumentalness'|'liveness'|
are the columns that descripe many things of each song


**Univariate Analysis:**

Plotted histogram to see the distribution of data for each column and found that few variables are normally distributed and others was skewed
we did log and power transformation for each skewed column

**Descriptive Statistics:**

Using **describe()** we could get the following result for the numerical features

duration_song_ms	danceability	energy	key	loudness	mode	speechiness	acousticness	instrumentalness	liveness	valence	tempo	time_signature
count	1.44e+05	144276.00	1.44e+05	144276.00	144276.00	144276.00	144276.00	144276.00	1.44e+05	144276.00	144276.00	144276.00	144276.00
mean	2.32e+05	0.63	6.56e-01	5.16	-6.80	0.65	0.10	0.20	2.69e-02	0.18	0.51	121.93	3.96
std	5.36e+04	0.15	1.91e-01	3.64	3.02	0.48	0.10	0.25	1.24e-01	0.14	0.23	28.51	0.29
min	2.06e+02	0.00	3.79e-04	0.00	-39.47	0.00	0.00	0.00	0.00e+00	0.00	0.00	0.00	0.00
25%	2.01e+05	0.53	5.31e-01	2.00	-8.17	0.00	0.04	0.02	0.00e+00	0.09	0.33	99.93	4.00
50%	2.25e+05	0.63	6.80e-01	5.00	-6.19	1.00	0.05	0.09	1.16e-06	0.12	0.50	120.46	4.00
75%	2.55e+05	0.73	8.05e-01	8.00	-4.79	1.00	0.11	0.30	1.56e-04	0.23	0.68	140.05	4.00
max	1.81e+06	0.99	1.00e+00	11.00	2.77	1.00	0.96	1.00	9.91e-01	1.00	1.00	219.30	5.00

**Correlation Plot of Numerical Variables:**

some variables are correlated with each other with correlation coefficient of .99 such as **duration_ms** and **num_tracks**
 
 

# Model Building


### Spotify_Recommendation class 


###### search-function
Function that search the song in the dataframe by its name
   --parameters
take the **song name** and the **amount** of songs that you want to view


###### recommend-function

Function that recommend songs by its name and other features
   --parameters
take the **song name** and the **amount** of songs that you want to view


**First:- move into each feature**

*Compare the 
    Trake_Name
between recommended songs and users songs*


*Results:- Recommended songs with the same name of the song*


**artist_name**--------**track_name**-----------------------------------**album_name**
Blackmill--------------Don't Let Me Down (feat. Cat Martin--------------Miracle
The Chainsmokers-------Don't Let Me Down--------------------------------The Chainsmokers- Japan Special Edition
Keith Urban------------Sun Don't Let Me Down----------------------------Ripcord
The Chainsmokers-------Don't Let Me Down - Illenium Remix---------------Don't Let Me Down (Remixes)
The Beatles------------Don't Let Me Down - Remastered-------------------The Beatles 1967 - 1970
The Chainsmokers-------Don't Let Me Down - W&W Remix--------------------Don't Let Me Down (Remixes)
The Chainsmokers-------Don't Let Me Down - Hardwell & Sephyx Remix------The Chainsmokers- Japan Special Edition



**Second:- move into each *numeric* feature**

*Compare the 
    danceability ,energy ,loudness,mode ,speechiness ,acousticness ,instrumentalness, liveness, valence and tempo
between recommended songs and users songs
And make new column called distance that include the distance between our song and the song in dataframe and sort these songs*


Results:- Recommended the least 10 songs by distance with required song


**artist_name**-------**track_name**-----------------------------**album_name**
    Blackmill---------Don't Let Me Down (feat. Cat Martin)-------Miracle
    Blackmill---------Don't Let Me Down (feat. Cat Martin)-------Miracle
    Jamie xx----------Far Nearer---------------------------------Far Nearer
    DJ Shadow---------Building Steam With A Grain Of Salt--------Endtroducing.....
    DJ Shadow---------Building Steam With A Grain Of Salt--------Endtroducing.....
    TwoThirds---------Epiphany-----------------------------------Epiphany
    Passion Pit-------The Reeling - Calvin Harris Remix----------Manners
    Bonobo------------Nothing Owed-------------------------------Dial 'M' for Monkey
    Cut Chemist-------The Garden---------------------------------The Audience's Listening
    Pretty Lights-----Change Is Gonna Come-----------------------Filling up the City Skies (Disc 1)



## Deployment
you can access our app by following this link [Spotify-playlist-recommendation-system-streamlit](https://vedantbalapurkar-spotify-million-songs-recommendati-main-i82kn2.streamlitapp.com/)
### Streamlit
- It is a tool that lets you creating applications for your machine learning model by using simple python code.
- We write a python code for our app using Streamlit; the app asks the user to enter the following data (**song title**, **number of recommendations**).
- The outcome of our application will be the recommendations of the song is based on the danceability, energy, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence and tempo of the song that the user enters.
- The app runs on local host.

