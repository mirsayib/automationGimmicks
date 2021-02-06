import requests, bs4, re, webbrowser

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

res = requests.get(
    'https://www.reddit.com/r/manga/?f=flair_name%3A%22DISC%22', headers=headers)

redditSoup = bs4.BeautifulSoup(res.text, 'html.parser')

newReleases = redditSoup.select('h3._eYtD2XCVieq6emjKBH3m')

titleRegex = re.compile(r'\s.+\d')

open('manga.txt', 'w').close()

for i in newReleases:
    matchObj = titleRegex.search(i.string)
    manga = open('manga.txt', 'a')
    manga.write(matchObj.group() + '\n')
    manga.close()

webbrowser.open('manga.txt')









