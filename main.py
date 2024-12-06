import instaloader

def save_reels_links(username, limit):
    # Initialize Instaloader
    loader = instaloader.Instaloader()

    # Get profile information
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")
        return

    # Add Reels links to a list
    reels_links = []
    
    # Iterate through the posts
    for post in profile.get_posts():
        if post.is_video and post.typename == 'GraphVideo':  # Select Reels videos
            url = f"https://www.instagram.com/reel/{post.shortcode}/"
            reels_links.append(url)

        # Stop if we have reached the limit
        if len(reels_links) >= limit:
            break

    # Check if any Reels links were found
    if reels_links:
        # Write links to a text file
        with open("reels_links.txt", "w") as f:
            for link in reels_links:
                f.write(link + "\n")
        print(f"A total of {len(reels_links)} Reels links were found and saved to 'reels_links.txt'.")
    else:
        print("No Reels links were found for this user.")

# Enter the Instagram username and limit for the number of Reels
target_username = input("Enter the Instagram username: ")
limit = int(input("Enter the number of Reels links you want to fetch: "))
save_reels_links(target_username, limit)
