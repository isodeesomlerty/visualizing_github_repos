from get_repos_dicts import get_repos, get_response_dict

def test_status_code():
    """Is the value of status_code 200?"""
    response = get_repos()
    assert response.status_code == 200


def test_repos_returned():
    """Is the number of repositories returned 30?"""
    response = get_repos()
    repo_dicts = get_response_dict(response)[1]
    repos_count = len(repo_dicts)
    assert repos_count == 30


def test_complete_results():
    """Does the API call yield complete results?"""
    response = get_repos()
    response_dict = get_response_dict(response)[0]
    incomplete_status = response_dict['incomplete_results']
    assert incomplete_status == False


def test_total_repos():
    """Is the count of total number of repositories returned at least 400?"""
    response = get_repos()
    response_dict = get_response_dict(response)[0]
    total_repos = response_dict['total_count']
    assert total_repos >= 400
