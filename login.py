#!/usr/bin/env python3

import cgi
import os
from templates import login_page
from templates import secret_page

def get_env():
    env = {}
    env_str = ''
    for env_key, env_value in os.environ.items():
        env[env_key] = env_value
        new_str = str(env_key) + ' | ' + str(env_value) + '<br>'
        env_str += new_str
    return str(env_str)

def parse_cookies(cookie_string):
    result = {}
    if cookie_string == "":
        return result
        
    cookies = cookie_string.split(";")
    for cookie in cookies:
        split_cookie = cookie.split("=")
        result[split_cookie[0]] = split_cookie[1]
    return result

cookies = parse_cookies(os.environ["HTTP_COOKIE"])  # get all cookies as dictionary
env_variables = get_env()  # enviroment variable as one string

# get username and pass from prev page submit
form = cgi.FieldStorage()
username = form.getfirst("username")
password = form.getfirst("password")

header = ""
header += "Content-Type: text/html\r\n"    # HTML is following
body = ""
    
# if ("newCookie" in cookies):
#     body += '<h6>You still have this cookie</h5><br>'
# else:
#     header += 'Set-Cookie: newCookie=new; Max-Age=5'

if username is not None or ('logged' in cookies and cookies['logged'] == "true"):
    header += "Set-Cookie: logged=true; Max-Age=60\r\n" #keeps track if user is logged in expires after 60s
    body += secret_page(username, password)
    body += "<h1>A terrible secret</h1>"
    body += "<hr> <h4> Env variables </h4>"
    body += "<p>" + env_variables + "</p>"
else:
    header += 'Set-Cookie: visited=true'
    body += login_page()

print(header)
print()
print(body)