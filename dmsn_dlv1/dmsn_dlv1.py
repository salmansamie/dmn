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
ep1_user = api.me()._json                                   # alt: api.get_user('samie21s')
with open('./output/Profile.json', 'w') as fp1:
    json.dump(ep1_user, fp1, sort_keys=True, indent=4)

print(ep1_user)


# Collecting Data : Timeline
