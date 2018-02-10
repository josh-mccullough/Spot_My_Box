#!/usr/bin/env python
import spotipy.util as util
import spotipy


class DropBoxSpottedSetLists:

    def __init__(self):
        self._username = self.get_credentials()
        self.log_into_spotify()

    @property
    def username(self):
        return self._username

    @property
    def token(self):
        return self._token

    @staticmethod
    def get_credentials():
        username = raw_input("Enter Username: ")
        return username

    def log_into_spotify(self):
        # here we set up the token/scopes for the desired username
        scope = 'user-library-read playlist-modify-public playlist-modify-private', 'playlist-read-private playlist-read-collaborative user-read-private'
        token = util.prompt_for_user_token(self.username, scope, client_id, client_secret, redirect_uri='https://127.0.0.1/')
        if token is None:
            raise Exception('failed to authenticate')
        self.SpotPlayer = spotipy.Spotify(auth=self.token)

    def get_track_uri(self, track):
        song_details = self.SpotPlayer.search(q=('track:{0}'.format(track)))
        return song_details['tracks']['items'][0]['uri']

    def get_playlist_id(self, playlist):
        all_playlists = self.SpotPlayer.user_playlists(self.username)
        results = filter(lambda i: i['name'] == playlist, all_playlists['items'])
        if len(results) > 0:
            result = results[0]
            print 'Play list found'
            print result
            return result['uri']
        else:
            print Exception("Didn't find playlist id")
            print 'creating a new playlist'
            self.create_a_public_playlist(newone=True)

    def create_track_list(self, track_list):
        track_id_list = []
        for tracks in track_list:
            song_details = self.SpotPlayer.search(q=('track:{0}'.format(tracks)))
            track_id_list.append(song_details['tracks']['items'][0]['uri'])
        return track_id_list

    def create_a_public_playlist(self):
        playlistname = raw_input("What do you want to  name your public playlist: ")
        self.SpotPlayer.user_playlist_create(self.username, playlistname, public=True)


    def create_a_private_playlist(self):
        playlistname = raw_input("What do you want to name your private playlist: ")
        self.SpotPlayer.user_playlist_create(self.username, playlistname, public=False)

    def add_to_playlist(self, playlist=None, tracklist=None):
        self.SpotPlayer.user_playlist_add_tracks(self.username, playlist, tracklist, position=None)
        print 'tracks added'


if __name__ == "__main__":
    OnYourMarks = DropBoxSpottedSetLists()
    OnYourMarks.log_into_spotify()
