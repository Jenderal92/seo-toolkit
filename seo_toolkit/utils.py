import requests

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print "Error fetching HTML: {}".format(e)
        return ""
