import requests as req

contributors_list = []
contributors_twitter_handles = []

contributors_repo = req.get('https://api.github.com/repos/nayanm9/GetHiredBot/contributors').json()

for  name in contributors_repo:
    if name not in contributors_list:
        contributors_list.append(name["login"])
    else:
         pass

for username in contributors_list:
    user_twitter_info = req.get(f"https://api.github.com/users/{username}").json()
    if user_twitter_info["twitter_username"] is not None:
        contributors_twitter_handles.append(user_twitter_info["twitter_username"])
    else:
        pass

def get_contributors():
    return contributors_twitter_handles
