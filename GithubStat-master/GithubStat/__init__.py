#!/usr/bin/python
# -*- coding: utf-8 -*-

#  MIT License
#
#  Copyright (c) 2021 Tahmid Rayat
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#
#      Copyright (C) 2021  HTR-TECH (https://github.com/htr-tech)
#

import os
import sys
import json
import six
import requests

info = """
[-] Username  : %s

[-] Name      : %s
[-] Followers : %s
[-] Following : %s

[-] Location  : %s
[-] Email     : %s
[-] Twitter   : %s
[-] Blog      : %s
[-] Company   : %s
[-] Hireable  : %s

[-] Total Repository : %s
[-] Total Gists      : %s
[-] Joined Github at : %s
[-] Recent Activity  : %s

[-] Github URL   : https://github.com/%s
[-] Repositories : https://github.com/%s/repositories
[-] Avatar       : %s
"""

def status(user):
    main = requests.get("https://api.github.com/users/%s" % (user))
    if main.status_code == 200:
        pass
    elif main.status_code == 404:
        print('No Github Account with that Username !')
        sys.exit()
    else:
        print('Try again After Some Time')
        sys.exit()

def stats(user):
    status(user)
    main = requests.get("https://api.github.com/users/%s" % (user))
    dump = json.loads(main.text)

    h1 = dump['login']
    h2 = dump['name']
    h3 = dump['followers']
    h4 = dump['following']
    h5 = dump['location']
    h6 = dump['email']
    h7 = dump['twitter_username']
    h8 = dump['blog']
    h9 = dump['company']
    h10 = dump['hireable']
    h11 = dump['public_repos']
    h12 = dump['public_gists']
    h13 = dump['created_at']
    h14 = dump['updated_at']
    h15 = dump['avatar_url']

    print(info % (h1, h2, h3, h4, h5, h6, h7, h8,
          h9, h10, h11, h12, h13, h14, h1, h1, h15))

    orgs = requests.get("https://api.github.com/users/%s/orgs" % (user))
    orgs_dump = json.loads(orgs.text)
    for hulu in orgs_dump:
        print('[-] Organization : {} '.format(hulu['login']))

    list_repo = six.moves.input(
        '\n[-] Wanna List repositories [Max 100] [Y/n] : ')
    print('')

    if list_repo == "y" or list_repo == "Y":
        repos = requests.get(
            "https://api.github.com/users/%s/repos?per_page=100" % (user))
        repo_dump = json.loads(repos.text)
        for bagh in repo_dump:
            print('[-] Repo Name :: {} \n[-] Stars     :: {} \n[-] Forks     :: {} \n[-] Clone URL :: {}\n'.format(
                bagh['name'], bagh['stargazers_count'], bagh['forks_count'], bagh['clone_url']))

        total_star, total_fork = 0, 0
        for bagh in repo_dump:
            total_star += int(bagh['stargazers_count'])
            total_fork += int(bagh['forks_count'])

        print('[-] Total Stars  : '+str(total_star))
        print('[-] Total Forks  : '+str(total_fork))
        print('')
    else:
        pass

note = """
 GithubStat (c) Tahmid Rayat <https://github.com/htr-tech>

 A Simple Github User Statistics Meter based on Github-API.

 Type GithubStat <your github username>

 Example : GithubStat HTR-TECH

 If you Like this Project then don't Forget to leave a Star :)
"""

def main():
    if len(sys.argv) >= 2:
        try:
            stats(sys.argv[1])
        except Exception as exceptions:
            sys.exit(exceptions)
    else:
        sys.exit(note)

if __name__ == '__main__':
    main()
