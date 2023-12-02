#!/usr/bin/python3
"""
 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
 You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
 Print all commits by: `<sha>: <author name>` (one by line)

Write a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.
"""

if __name__ == '__main__':
        import sys
            import requests
                repo_name = sys.argv[1]
                    owner_name = sys.argv[2]
                        repo_info = owner_name + "/" + repo_name
                            url = "https://api.github.com/repos/" + repo_info + "/commits"
                                r = requests.get(url)
                                    top = r.json()[:10]
                                        for i in top:
                                                    el = i['sha']
                                                            author = i['commit']['author']['name']
                                                                    print('{}: {}'.format(el, author))


