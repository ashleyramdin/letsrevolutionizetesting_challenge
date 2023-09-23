import requests


def follow_challenge_url(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch data from {url}")
        return

    # get the json response
    data = response.json()
    print(data)
    
    if data["message"] == "This is not the end":  # end condition
        # update the url to include .json
        json_url = data["follow"].replace("challenge", "challenge.json")

        # split the url into parts to get the id parameter for the next url
        url_parts = json_url.split("=")
        pre_query_string = url_parts[0]  # first part of the url
        new_id = url_parts[1]  # id parameter

        # construct the new follow url
        follow_url = pre_query_string.replace("?id", f"?id={new_id}")

        # print(f"Follow URL: {follow_url}")

        # call the function recursively
        follow_challenge_url(follow_url)


if __name__ == "__main__":
    start_url = "https://www.letsrevolutionizetesting.com/challenge.json"
    follow_challenge_url(start_url)
