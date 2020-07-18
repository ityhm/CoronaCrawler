# CoronaCrawler: Archiving Israel's total covid-19 confirmed cases by media sources

**CoronaCrawler** is a script that runs a few crawlers periodically, based on spiders and selenium scrapers, searching for the most updated number of confirmed covid-19 cases (total, not current) in Israel and saves it in a local db.

## Why was CoronaCrawler created?
Well, I was at home for a few days during the first wave of the corona in Israel, when a lot of people had to work from home. In my case, I just got paid vacation since I was in the army, and other than a few days of work for a project we built in my unit that helped hospitals communicating with rooms of covid-19 patients (the doctors can't bring their phones inside), I was doing nothing at home - so I got bored.
I was watching the news at home, following the different updates and numbers and I saw that almost every channel/website/other media source was publishing different numbers, so I decided to see which ones are the most updated and which sources are falling behind.
So I decided to remove the rust I had on my Python skills, and learn some new things like crawlers, DB and more.
Beware - I was still rusty when I wrote it.

## What do we have here?
For each selected website, wether israeli or international, there is a specific script that uses a technique that fits the website's format:
  - **Spiders**: For websites that upload the information for the first html request for the original URL.
  - **Selenium scrapers**: For websites that either need time to load the data or use scripts to get the data from another source.

### How do I use it?
The main script is **coronaDataFetcher.py** and that is the script you'll run when you want to look for new data.
There's also a script called **printDB.py** which is very self-explanatory.
The script creates a **log output file** (output.txt) and there is a **log folder** (Logs) for success/failure information.
All of the data is saved in a **local DB** (using mysql), in the future I might make it non-local.

### How do I add a new website?
Well first you need to read the website's source. You can open it in a browser, but it will give you the final result of all html requests. So actualy you should download the source using a scrapy's spider shell.
After downloading the actual first source page that you get as a response, look for the number of the sick people in Israel.
If you find it - try to find the correct xpath in order to locate it, and save it for later.
If you can not find the number in the html file, try open the URL in a browser and use the browser's inspect tools (F12 in chrome for example) in order to inspect the URL's source.
If you find the number in the final loaded source at the inspect tool - try to find the correct xpath and save it for later.
Some websites use javascript in order to load the data from other sources and that makes our job difficult. It's on you to decide how hard you'll work for a certain website's data, but remember - they might change their format and then your code will not get the data.

Great, we got the xpath for the data.
  - If we got it using the original html response - create a new **spider** script for the website in the spiders folder, use the abstract class the same way the other spiders do.
  - If we got it using the inspect tool or following dynamic data - try to filter out the wanted data by using selenium and the xpath you saved. Afterwards, create a new **selenium** script for the website in the scrapers folder, use the abstract class the same way the other scrapers do.

After finishing with the new website script, use it in the main script coronaDataFetcher.py

If the explanation above was not enough, I suggest reading more about crawling using spiders/selenium. 

### I added a new website! What now?
It is very important to **keep all scripts updated** according to the websites formats. Unfortunatly the websites tend to be updated and changed, and we have to do the dirty work and change out scripts to get the data out of the new format.

### How do I know if a website's format has changed?
The script's output file (output.txt) and log folder (Logs) will have the information you need.
The script will print logs for success and failure and will create a log file for websites that it failed to fetch the wanted data. In addition, the source page of the page will be downloaded to the htmls folder (htmls) in order for you to understand the new format of the website and update the script.



