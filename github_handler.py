import os
from github import Github
from dotenv import load_dotenv
load_dotenv()

# Set your GitHub Personal Access Token
github_token = os.getenv('GITHUB_TOKEN')
github = Github(github_token)

def get_permissions(organization_name):
    org = github.get_organization(organization_name)

    # Dictionary to store repository access data
    repo_access_data = {}

    # Fetch all repositories in the organization
    for repo in org.get_repos():
        repo_access_data[repo.name] = {"collaborators": {}}
        # Get Collaborators and their access levels
        try:
            for collaborator in repo.get_collaborators():
                permissions = {
                    "admin": collaborator.permissions.admin,
                    "write": collaborator.permissions.push,
                    "read": collaborator.permissions.pull
                }
                repo_access_data[repo.name]["collaborators"][collaborator.login] = permissions
        except Exception as e:
            repo_access_data[repo.name]["collaborators"] = {}
    return repo_access_data
