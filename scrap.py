import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import hashlib
import json
def gravatar(username):
    response = requests.get(f'https://en.gravatar.com/{username}.json')
    # print(response.text)
    if response.status_code == 200:
        # Parse the JSON data
        data = json.loads(response.text)

        # Extract the fields
        entry = data.get("entry", [{}])[0]
        hash_value = entry.get("hash", "")
        profile_url = entry.get("profileUrl", "")
        preferred_username = entry.get("preferredUsername", "")
        thumbnail_url = entry.get("thumbnailUrl", "")
        name = entry.get("name", {})
        given_name = name.get("givenName", "")
        family_name = name.get("familyName", "")
        formatted_name = name.get("formatted", "")
        display_name = entry.get("displayName", "")
        about_me = entry.get("aboutMe", "")
        current_location = entry.get("currentLocation", "")

        # Create a list of lists for tabulating
        table_data = [
            ["Hash", hash_value],
            ["Profile URL", profile_url],
            ["Preferred Username", preferred_username],
            ["Thumbnail URL", thumbnail_url],
            ["Given Name", given_name],
            ["Family Name", family_name],
            ["Formatted Name", formatted_name],
            ["Display Name", display_name],
            ["About Me", about_me],
            ["Current Location", current_location]
        ]

        # Display the table
        print(tabulate(table_data, headers=["Field", "Value"], tablefmt="grid"))
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
gravatar('shan')
email = "MyEmailAddress@example.com"
email = email.strip().lower()
md5_hash = hashlib.md5(email.encode()).hexdigest()

print(md5_hash)
