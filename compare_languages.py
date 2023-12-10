import pandas as pd
import plotly.express as px

from get_repos_dicts import get_repos, get_response_dict

def compare_languages(languages, repos_number=10):
    """
    Create a line chart comparing the popularity of the top GitHub repositories
     across multiple programming languages.
    """

    # Store data for plotting.
    all_repos_data = []

    # Process each language.
    for language in languages:
        r = get_repos(language=language, min_stars=0)
        repo_dicts = get_response_dict(r)[1][:repos_number]

        # Rank repos and collect data
        for rank, repo_dict in enumerate(repo_dicts, start=1):

            hover_text =(
                f"Name: {repo_dict['name']}<br />"
                f"Owner: {repo_dict['owner']['login']}<br />"
                f"Description: {repo_dict['description']}"
                )
            
            all_repos_data.append({
                'Language': language,
                'Rank': rank,
                'Star': repo_dict['stargazers_count'],
                'Info': hover_text,
                })
    
    # Create DataFrame for plotting
    df = pd.DataFrame(all_repos_data)

    # Make visualization.
    title = f"Top {repos_number} GitHub repos star count, by language"
    labels = {'Rank': 'Repository Rank', 'Star': 'Star Count'}
    fig = px.line(df, x='Rank', y='Star', color='Language', 
                  hover_name='Info',
                  title=title, labels=labels)

    fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                    yaxis_title_font_size=20)
    fig.show()