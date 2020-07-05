import requests
def downloadFile(urlToDownload, fileToWriteTo):
    print('Beginning file download with requests')

    # debug = {'verbose': sys.stderr}
    user_agent = {'User-agent': 'Mozilla/5.0'}
    # url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
    r = requests.get(urlToDownload, headers = user_agent)

    with open(fileToWriteTo, 'wb') as f:
        f.write(r.content)

    # Retrieve HTTP meta-data
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)