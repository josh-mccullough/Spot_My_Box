#!/usr/bin/env python
import spotipy

class DropBoxSpottedSetLists:

    def __init__(self):
        self._username, self._token = self.get_credentials()
        self.log_into_spotify()

    @property
    def username(self):
        return self._username

    @property
    def token(self):
        return self._token

    @staticmethod
    def get_credentials():
        username = raw_input ("Enter Username: ")
        token = raw_input("Enter Token: ")
        return username, token

    def log_into_spotify(self):
       # here we set up the token/scopes for the desired username
        self.scope = 'user-library-read playlist-modify-public playlist-modify-private' \
                     ' playlist-read-private playlist-read-collaborative user-read-private'
        self.token = util.prompt_for_user_token(self.username, self.scope, client_id, client_secret, redirect_uri='https://127.0.0.1/')

        if self.token is None:
            raise Exception('failed to authenticate')

        # TODO get rid of the hardcoded id and secret
        self.SpotPlayer = spotipy.Spotify(auth=self.token) 


if __name__ == "__main__":
    OnYourMarks = DropBoxSpottedSetLists()

