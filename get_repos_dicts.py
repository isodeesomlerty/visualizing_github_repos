import requests

def get_repos(language='Python', min_stars='10000'):
    """
    Make an API call to get GitHub repositories,
     with a given language and minimum stars.
    """
    url = "https://api.github.com/search/repositories"
    url += f"?q=language:{language.lower()}+sort:stars+stars:>{min_stars}"

    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)

    return response


def get_response_dict(response_object):
    """
    Convert an API response object to a dictionary.
    Return a tuple containing both the response dictionary 
     and repository dictionaries.
    """
    response_dict = response_object.json()
    repo_dicts = response_dict['items']
    return response_dict, repo_dicts