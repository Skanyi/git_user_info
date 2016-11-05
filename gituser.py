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
    data = profile_info.json()
    '''
    Only returns their location, email, followers and public repos
    '''
    info = data['location'], data['followers'], data['email'], data['public_repos']
    info = list(info)
    print("Location: %s Followers: %d Email: %s Public Repository: %d" % (info[0], info[1], info[2], info[3]))

get_user()
