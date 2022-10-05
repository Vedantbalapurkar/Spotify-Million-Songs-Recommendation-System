# Spotify-Million-Songs-Recommendation-System
This is the Dataset for the Spotify Million Playlist.

Dataset Link: https://drive.google.com/file/d/1KiJ9-CCjpRJJWq1UmoDfr9-5giO_j2vk/view?usp=sharing

Hosted Model: https://vedantbalapurkar-spotify-million-songs-playlist-rec-main-559eq0.streamlitapp.com/

This challenge set contains 10,000 incomplete playlists. The challenge is to recommend tracks for each of these playlists.

## Description:
The Data set consists of a single JSON dictionary with three fields:

   * **version** - the version of the challenge set. This should be "v1"
   * **playlists** - an array of 10,000 incomplete playlists. Each element in this array contains the following fields:
      * **pid** - the playlist ID
      * **name** - (optional) - the name of the playlist. For some challenge playlists, the name will be missing.
      * **num_holdouts** - the number of tracks that have been omitted from the playlist
      * **tracks** - a (possibly empty) array of tracks that are in the playlist. Each element of this array contains the following fields:
         * **pos** - the position of the track in the playlist (zero offset)
         * **track_name** - the name of the track
         * **track_uri** - the Spotify URI of the track
         * **artist_name** - the name of the primary artist of the track
         * **artist_uri** - the Spotify URI of the primary artist of the track
         * **album_name** - the name of the album that the track is on
         * **album_uri** -- the Spotify URI of the album that the track is on
         * **duration_ms** - the duration of the track in milliseconds
      * **num_samples** the number of tracks included in the playlist
      * **num_tracks** - the total number of tracks in the playlist.

  Note that len(tracks) == num\_samples and num\_samples + num\_holdouts == num\_tracks

## Playlist Categories
The 10,000 playlists are made up of 10 different categories, with 1,000 playlists in each category:

   1. Predict tracks for a playlist given its title only
   2. Predict tracks for a playlist given its title and the first track
   3. Predict tracks for a playlist given its title and the first 5 tracks
   4. Predict tracks for a playlist given its first 5 tracks (no title)
   5. Predict tracks for a playlist given its title and the first 10 tracks
   6. Predict tracks for a playlist given its first ten tracks (no title)
   7. Predict tracks for a playlist given its title and the first 25 tracks
   8. Predict tracks for a playlist given its title and 25 random tracks
   9. Predict tracks for a playlist given its title and the first 100 tracks
   10. Predict tracks for a playlist given its title and 100 random tracks
   
Thank You
