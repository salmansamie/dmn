import os
import configparser
import tweepy
import json


__author__ = "salmansamie"


# Parse configuration file and get keys, tokens and secrets
config = configparser.ConfigParser()
config.read(os.path.join('tw_config.ini'))
cons_key = config['DEFAULT']['cons_key']
cons_sec = config['DEFAULT']['cons_sec']
accs_tok = config['DEFAULT']['accs_tok']
accs_sec = config['DEFAULT']['accs_sec']


# tweepy auth and api object
auth = tweepy.OAuthHandler(cons_key, cons_sec)
auth.set_access_token(accs_tok, accs_sec)
api = tweepy.API(auth)


# Collecting Data : Profile
def get_profile():
    ep1_user = api.me()._json                                   # alt: api.get_user('samie21s')
    with open('./output/Profile.json', 'w') as fp1:
        json.dump(ep1_user, fp1, sort_keys=True, indent=4)
    print(ep1_user)


# Collecting Data : Timeline
def get_timeline():
    ep2_timeline = api.user_timeline('samie21s')[0]._json
    with open('./output/Timeline.json', 'w') as fp2:
        json.dump(ep2_timeline, fp2, sort_keys=True, indent=4)
    print(ep2_timeline)


# Collecting Data : Followers
def get_followers():
    ep3_followers = []
    for user in tweepy.Cursor(api.followers, screen_name="samie21s").items():
        ep3_followers.append({"id": user.id,
                              "id_str": user.id_str,
                              "name": user.name,
                              "screen_name": user.screen_name,
                              "location": user.location,
                              "description": user.description,
                              "url": user.url,
                              "entities": user.entities,
                              "protected": user.protected,
                              "followers_count": user.followers_count,
                              "friends_count": user.friends_count,
                              "listed_count": user.listed_count,
                              "created_at": user.created_at,
                              "favourites_count": user.favourites_count,
                              "geo_enabled": user.geo_enabled,
                              "lang": user.lang,
                              "profile_image_url": user.profile_image_url,
                              "profile_background_image_url": user.profile_background_image_url,
                              "profile_image_url_https": user.profile_image_url_https,
                              "default_profile": user.default_profile,
                              "follow_request_sent": user.follow_request_sent,
                              "notifications": user.notifications,
                              "muting": user.muting,
                              "blocking": user.blocking,
                              "blocked_by": user.blocked_by
                              })

    with open('./output/Followers.json', 'w') as fp3:
        fp3.write(str(ep3_followers))
    print(ep3_followers)


# Collecting Data : Friends/Following
def get_friends():
    s = api.friends_ids('samie21s')
    print(s)


if __name__ == '__main__':
    print("PROFILE:")
    get_profile()
    print("\n\n\nTIMELINE:")
    get_timeline()
    print("\n\n\nFOLLOWERS:")
    get_followers()
    print("\n\n\nFRIENDS:")
    get_friends()
