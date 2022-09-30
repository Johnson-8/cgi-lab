#!/usr/bin/env python3

import os
import json
import templates


# Create an empty dictionary
env = {}

print("Content-Type: application/json")     # HTML is following
print()                                     # blank line, end of headers

# Iterate through environment variables and add them to env
for env_key, env_value in os.environ.items():
    env[env_key] = env_value
    #print('{} -> {}'.format(env_key,env_value))
    print(env_key, env_value)

# Print env dictionary in json format
print(json.dumps(env))

# pt3
#print('Content-Type: text/html; charset=UTF-8')
print(env["HTTP_USER_AGENT"])


print(templates.login_page())   