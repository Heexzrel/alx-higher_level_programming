#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
"""
if __name__ == '__main__':
        import requests
            import sys
                res = requests.get(sys.argv[1])
                    print(res.headers.get('X-Request-Id'))
