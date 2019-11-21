def scrape():

    import pandas as pd
    import requests
    import bs4
    import urllib.parse
    import pymongo
    from splinter import Browser

    url = 'https://mars.nasa.gov/news/'
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    url3 = 'https://twitter.com/marswxreport?lang=en'
    url4 = 'https://space-facts.com/mars/'
    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    executable_path={'executable_path':'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(url)
    soup = bs4.BeautifulSoup(browser.html)
    headlines_and_more = soup.find_all(class_= 'content_title', limit=None)

    headlines_and = []

    for headline in headlines_and_more:
        headlines_and.append(headline.text)

    headlines = []

    for h in headlines_and:
        h = h.replace('\n','')
        headlines.append(h)

    news_title = headlines[0]
    info_and_more = soup.find_all(class_= 'article_teaser_body', limit=None)

    info_and = []

    for info in info_and_more:
        info_and.append(info.text)

    info = []

    for i in info_and:
        i = i.replace('\n','')
        info.append(i)

    news_p = info[0]

    browser.visit(url2)
    soup2 = bs4.BeautifulSoup(browser.html)
    browser.click_link_by_partial_text('FULL IMAGE')
    img_info = soup2.find('div', {'class': 'img'})
    img_url = img_info.contents[1]
    featured_img_url = img_url['src']

    browser.visit(url3)
    soup3 = bs4.BeautifulSoup(browser.html)
    tweet_info = soup3.find(class_ = 'js-tweet-text-container')
    tweet = tweet_info.contents[1]
    mars_weather = tweet.contents[0]


    df = pd.read_html(url4)
    table_data = df[0]
    mars_facts = table_data.to_html()


    browser.visit(url5)
    soup5 = bs4.BeautifulSoup(browser.html)
    descriptions = soup5.find_all(class_='description', limit = 4)
    hemisphere_image_urls = []

    for desc in descriptions:
        browser.visit(url5)
        soup5 = bs4.BeautifulSoup(browser.html)
        header = desc.find('h3').contents[0]
        browser.click_link_by_partial_text(header)
        soup6 = bs4.BeautifulSoup(browser.html)
        img_url = soup6.find(class_='wide-image')['src']
        hemisphere_image_urls.append({'title':header, 'img_url':img_url})

    return  {'news title':news_title, 'news paragraph':news_p, 
            'featured image url': featured_img_url, 
            'mars weather': mars_weather, 'mars_facts':mars_facts, 
            'hemisphere names/urls': hemisphere_image_urls}