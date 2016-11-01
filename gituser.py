#Pulls public Pull public information for a user's github
import requests
import json

def get_user():
    '''
    user the Github - User Data API to
    pull public information for a user guthub account

    API_URL = https://api.github.com/users/hackeryou
    '''

    username = input("What is your user name: >>")
    profile_info = requests.get('https://api.github.com/users/'+ username)
    #data = json.loads(profile_info)

    print(profile_info)
    '''
    Go through the profile_info and only returns their
    location, email, followers and public repos
    '''
    for info in profile_info:
        pass
    #print(profile_info.json())
get_user()
