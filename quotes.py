import json
import requests


def get_quote() -> tuple | None:
    """
    Return a quote from a database.
    """
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        quote = data[0]["q"]
        author = data[0]["a"]

        return quote, author

    # to catch http/network errors
    except requests.exceptions.RequestException as error:
        print(f"Error while fetching data from url: {error}")

    # to catch error if response is json
    except json.JSONDecodeError as error:
        print(f"Error while decoding file: {error}")
        return None
