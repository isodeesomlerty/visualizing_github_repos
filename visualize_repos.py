import plotly.express as px

from get_repos_dicts import get_repos, get_response_dict

def visualize_repos(language, min_stars='10000', marker_color='SteelBlue'):
    """
    Create a bar chart showing the most-starred projects on GitHub for
     a given programming language.
    """

    # Make an API call.
    r = get_repos(language=language, min_stars=min_stars)

    # Process repository information.
    repo_dicts = get_response_dict(r)[1]
    repo_links, stars, hover_texts = [], [], []
    for repo_dict in repo_dicts:
        # Turn repo names into active links.
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])

        # Build hover texts.
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        hover_text = f"{owner}<br />{description}"
        hover_texts.append(hover_text)

    # Make visualization.
    title = f"Most-Starred {language} Projects on GitHub"
    labels = {'x': 'Repository', 'y': 'Stars'}
    fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
                hover_name=hover_texts)

    fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                    yaxis_title_font_size=20)

    fig.update_traces(marker_color=marker_color, marker_opacity=0.6)

    fig.show()