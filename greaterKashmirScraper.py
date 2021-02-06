import requests, bs4, webbrowser

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    res = requests.get(
        'https://www.greaterkashmir.com/latest/', headers=headers)

    gkSoup = bs4.BeautifulSoup(res.text, 'html.parser')

    latestHeadlines = gkSoup.select(
        'h2.m-article-first-large-listing__title.entry-title > a')

    open('gk.txt', 'w').close()

    for i in latestHeadlines:
        gk = open('gk.txt', 'a')
        gk.write('**' + i.string + '**\n\n\n')
        gk.close()

    webbrowser.open('gk.txt')
except:
    print('Something went wrong, Check Your Internet Connection and make sure you haven\'t deleted a necessary file')









