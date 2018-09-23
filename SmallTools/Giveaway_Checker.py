"""[Giveaway_Checker]
    Feature:
    - Login to FB account, without pop-up driver
    - Crawl comments for the specific post.
    - Crawl by characteristic:
        + ALWAYS get time and user's name, chosen number
        + Check for share with hashtag (Optional)
        + Check for tag friend in comment (Optional).
    
    Technology Method: SELENIUM

    Step by step action:
    - Enter username, password (use getpass), post's link.
    - List option:
        + Just crawl and save to csv
            * Use only list to store and writecsv
        + Crawl and check for share
            * Data structure: List in dict, keys is username
            * List: Time, number, share (check mark)
        + Crawl and check for tag
            * Data structure: List in dict, keys is username
            * List: Time, number, tag (check mark only when have enough tags)
"""
