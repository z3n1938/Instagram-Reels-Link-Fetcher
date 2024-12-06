#
__Instagram Reels Link Fetcher__

Instagram Reels Link Fetcher is a Python script that allows you to automatically retrieve Reels video links from any public Instagram profile. The script uses the Instaloader library to scrape and download Reels links, storing them in a .txt file for easy access. You can specify the number of Reels you want to fetch, and the script will stop collecting once the specified limit is reached.
#
__Features__
Fetch Instagram Reels links from any public profile.

Specify the number of Reels links to fetch.

Save the links in a .txt file (reels_links.txt).

Easy to use with simple user input.
#
__Requirements__

Python 3.x

Instaloader library
#
__Installation__
Clone or download the repository.

Start the __setup.bat__
#
__Usage__
Run the bat:  __start.bat__

Enter the Instagram username of the target account when prompted.

Enter the number of Reels links you want to fetch.

The script will save the Reels links to a text file called reels_links.txt.
#

__Notes__

If the account is private, you will need to log in by adding your Instagram credentials:

loader.login("your_username", "your_password")

The script stops fetching Reels once the specified limit is reached.

The program only fetches Reels and not other types of posts like photos or regular videos.

#
