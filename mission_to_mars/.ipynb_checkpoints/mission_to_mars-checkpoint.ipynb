{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import requests\n",
    "import bs4\n",
    "import urllib.parse\n",
    "import pymongo\n",
    "from splinter import Browser"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://mars.nasa.gov/news/'\n",
    "url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "url3 = 'https://twitter.com/marswxreport?lang=en'\n",
    "url4 = 'https://space-facts.com/mars/'\n",
    "url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "executable_path={'executable_path':'chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = bs4.BeautifulSoup(browser.html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "headlines_and_more = soup.find_all(class_= 'content_title', limit=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "headlines_and = []\n",
    "\n",
    "for headline in headlines_and_more:\n",
    "    headlines_and.append(headline.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Two of a Space Kind: Apollo 12 and Mars 2020',\n",
       " 'Mars Scientists Investigate Ancient Life in Australia',\n",
       " \"NASA's Mars 2020 Will Hunt for Microscopic Fossils\",\n",
       " 'With Mars Methane Mystery Unsolved, Curiosity Serves Scientists a New One: Oxygen',\n",
       " \"NASA's Mars 2020 Heads Into the Test Chamber\",\n",
       " \"Screening Soon: 'The Pathfinders' Trains Lens on Mars\",\n",
       " \"InSight's 'Mole' Team Peers into the Pit\",\n",
       " \"Common Questions about InSight's 'Mole'\",\n",
       " 'Mars 2020 Stands on Its Own Six Wheels',\n",
       " 'New Selfie Shows Curiosity, the Mars Chemist',\n",
       " 'Naming a NASA Mars Rover Can Change Your Life',\n",
       " 'Mars 2020 Unwrapped and Ready for More Testing',\n",
       " \"HiRISE Views NASA's InSight and Curiosity on Mars\",\n",
       " \"NASA's Curiosity Rover Finds an Ancient Oasis on Mars\",\n",
       " \"NASA's Mars 2020 Rover Tests Descent-Stage Separation\",\n",
       " \"NASA's Push to Save the Mars InSight Lander's Heat Probe\",\n",
       " \"NASA's InSight 'Hears' Peculiar Sounds on Mars\",\n",
       " 'NASA Mars Mission Connects With Bosnian and Herzegovinian Town',\n",
       " \"Deadline Closing for Names to Fly on NASA's Next Mars Rover\",\n",
       " 'NASA Wins Two Emmy Awards for Interactive Mission Coverage',\n",
       " \"NASA's Mars 2020 Comes Full Circle\",\n",
       " 'NASA Invites Students to Name Mars 2020 Rover',\n",
       " \"NASA's Mars Helicopter Attached to Mars 2020 Rover \",\n",
       " \"What's Mars Solar Conjunction, and Why Does It Matter?\",\n",
       " 'Scientists Explore Outback as Testbed for Mars ',\n",
       " \"NASA-JPL Names 'Rolling Stones Rock' on Mars\",\n",
       " \"Robotic Toolkit Added to NASA's Mars 2020 Rover\",\n",
       " \"Space Samples Link NASA's Apollo 11 and Mars 2020\",\n",
       " 'Small Satellite Mission of the Year',\n",
       " \"NASA 'Optometrists' Verify Mars 2020 Rover's 20/20 Vision\",\n",
       " 'New Finds for Mars Rover, Seven Years After Landing',\n",
       " 'MEDLI2 Installation on Mars 2020 Aeroshell Begins',\n",
       " \"NASA's Mars 2020 Rover Does Biceps Curls \",\n",
       " \"Fueling of NASA's Mars 2020 Rover Power System Begins\",\n",
       " 'What Does a Marsquake Look Like?',\n",
       " 'Mars 2020 Rover: T-Minus One Year and Counting ',\n",
       " 'NASA Racks Up Two Emmy Nominations for Mission Coverage',\n",
       " 'Want to Colonize Mars? Aerogel Could Help',\n",
       " 'A Rover Pit Stop at JPL',\n",
       " 'Mars 2020 Rover Gets a Super Instrument',\n",
       " '\\n\\nNASA Garners 7 Webby Award Nominations\\n\\n',\n",
       " \"\\n\\nNASA's Opportunity Rover Mission on Mars Comes to End\\n\\n\",\n",
       " \"\\n\\nNASA's InSight Places First Instrument on Mars\\n\\n\",\n",
       " '\\n\\nNASA Invites Students to Name Mars 2020 Rover\\n\\n',\n",
       " \"\\n\\nNASA's Curiosity Mars Rover Finds a Clay Cache\\n\\n\",\n",
       " '\\n\\nWhy This Martian Full Moon Looks Like Candy\\n\\n',\n",
       " '\\n\\nNASA Garners 7 Webby Award Nominations\\n\\n',\n",
       " \"\\n\\nNASA's Opportunity Rover Mission on Mars Comes to End\\n\\n\",\n",
       " \"\\n\\nNASA's InSight Places First Instrument on Mars\\n\\n\",\n",
       " '\\n\\nNASA Invites Students to Name Mars 2020 Rover\\n\\n',\n",
       " \"\\n\\nNASA's Curiosity Mars Rover Finds a Clay Cache\\n\\n\",\n",
       " '\\n\\nWhy This Martian Full Moon Looks Like Candy\\n\\n']"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "headlines_and"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "headlines = []\n",
    "\n",
    "for h in headlines_and:\n",
    "    h = h.replace('\\n','')\n",
    "    headlines.append(h)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "news_title = headlines[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "info_and_more = soup.find_all(class_= 'article_teaser_body', limit=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "info_and = []\n",
    "\n",
    "for info in info_and_more:\n",
    "    info_and.append(info.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "info = []\n",
    "\n",
    "for i in info_and:\n",
    "    i = i.replace('\\n','')\n",
    "    info.append(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "news_p = info[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Two of a Space Kind: Apollo 12 and Mars 2020'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Apollo 12 and the upcoming Mars 2020 mission may be separated by half a century, but they share several goals unique in the annals of space exploration.'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.visit(url2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "soup2 = bs4.BeautifulSoup(browser.html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.click_link_by_partial_text('FULL IMAGE')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "img_info = soup2.find('div', {'class': 'img'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"img\">\n",
       "<img alt=\"Phlegethon Catena\" class=\"thumb\" src=\"/spaceimages/images/wallpaper/PIA23563-640x350.jpg\" title=\"Phlegethon Catena\"/>\n",
       "</div>"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img_info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "img_url = img_info.contents[1]\n",
    "featured_img_url = img_url['src']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/spaceimages/images/wallpaper/PIA23563-640x350.jpg'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "featured_img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.visit(url3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "soup3 = bs4.BeautifulSoup(browser.html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "tweet_info = soup3.find(class_ = 'js-tweet-text-container')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "tweet = tweet_info.contents[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'InSight sol 348 (2019-11-19) low -102.5ºC (-152.5ºF) high -23.2ºC (-9.8ºF)\\nwinds from the SSE at 5.1 m/s (11.5 mph) gusting to 18.9 m/s (42.3 mph)\\npressure at 6.80 hPa'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_weather = tweet.contents[0]\n",
    "mars_weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_html(url4)\n",
    "len(df)\n",
    "table_data = df[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>0</th>\\n      <th>1</th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>0</th>\\n      <td>Equatorial Diameter:</td>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>1</th>\\n      <td>Polar Diameter:</td>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>2</th>\\n      <td>Mass:</td>\\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\\n    </tr>\\n    <tr>\\n      <th>3</th>\\n      <td>Moons:</td>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>4</th>\\n      <td>Orbit Distance:</td>\\n      <td>227,943,824 km (1.38 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>5</th>\\n      <td>Orbit Period:</td>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>6</th>\\n      <td>Surface Temperature:</td>\\n      <td>-87 to -5 °C</td>\\n    </tr>\\n    <tr>\\n      <th>7</th>\\n      <td>First Record:</td>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>8</th>\\n      <td>Recorded By:</td>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_facts = table_data.to_html()\n",
    "mars_facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.visit(url5)\n",
    "soup5 = bs4.BeautifulSoup(browser.html)\n",
    "\n",
    "descriptions = soup5.find_all(class_='description', limit = 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/cerberus_enhanced\"><h3>Cerberus Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 21 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Cerberus hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of 104 Viking Orbiter images acquired…</p></div>,\n",
       " <div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/schiaparelli_enhanced\"><h3>Schiaparelli Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 35 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Schiaparelli hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The images were acquired in 1980 during early northern…</p></div>,\n",
       " <div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/syrtis_major_enhanced\"><h3>Syrtis Major Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 25 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Syrtis Major hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of about 100 red and violet…</p></div>,\n",
       " <div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/valles_marineris_enhanced\"><h3>Valles Marineris Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 27 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Valles Marineris hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The distance is 2500 kilometers from the surface of…</p></div>]"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "descriptions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "images_list = []\n",
    "\n",
    "for desc in descriptions:\n",
    "    browser.visit(url5)\n",
    "    soup5 = bs4.BeautifulSoup(browser.html)\n",
    "    header = desc.find('h3').contents[0]\n",
    "    browser.click_link_by_partial_text(header)\n",
    "    soup6 = bs4.BeautifulSoup(browser.html)\n",
    "    img_url = soup6.find(class_='wide-image')['src']\n",
    "    images_list.append({'title':header, 'img_url':img_url})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': '/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': '/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': '/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': '/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "images_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
