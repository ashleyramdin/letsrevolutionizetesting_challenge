import requests


def follow_challenge_url(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data from {url}")
        return

    # get the json response
    data = response.json()
    print(data)

    if data.get("message") == "This is not the end":
        follow_url = data.get("follow", "")
        if follow_url:
            # get the id parameter for the next url
            new_id = follow_url.split("=")[-1]
            # construct the new follow url
            follow_url = follow_url.replace("challenge", f"challenge.json?id={new_id}")
            follow_challenge_url(follow_url)


if __name__ == "__main__":
    start_url = "https://www.letsrevolutionizetesting.com/challenge.json"
    follow_challenge_url(start_url)
