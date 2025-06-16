import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}


def get_github_rate_limits():
    """Get the current GitHub API rate limits"""
    response = requests.get("https://api.github.com/rate_limit")
    return response.json()


# LOOK FOR PUBLIC REPOSITORIES
def search_repositories(query, per_page=10, page=1):
    url = f"https://api.github.com/search/repositories?q={query}&per_page={per_page}&page={page}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
        print("Success")
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


# OBTAIN REPOSITORY CONTENT
def get_commits(owner, repo, per_page=5, page=1):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page={per_page}&page={page}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


# LIST CONTENT FORM A REPOSITORY
def get_repo_contents(owner, repo, path=""):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None



