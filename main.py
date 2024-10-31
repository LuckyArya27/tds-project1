from dotenv import load_dotenv
import requests
import time
from os import getenv
import csv

load_dotenv()
# GitHub API settings
TOKEN = getenv("GITHUB_API_TOKEN") # Add your GitHub API token here or set it as an environment variable
HEADERS = {
    "Authorization": f"token {TOKEN}"
}
BASE_URL = "https://api.github.com"
# Fetch users in Bangalore with over 100 followers
def get_users_in_bangalore(min_followers=100, per_page=30):
    print("Fetching users in Bangalore with over 100 followers")
    users = []
    page = 1
    while True:
        response_users = requests.get(
            f"{BASE_URL}/search/users",
            headers=HEADERS,
            params={
                "q": f"location:Bangalore+followers:>{min_followers}",
                "per_page": per_page,
                "page": page
            }
        )
        data = response_users.json()
        if 'items' not in data:
            break
        users.extend(data['items'])        
        if len(data['items']) < per_page:
            break
        page += 1
        time.sleep(1)  # To avoid rate limiting
    return users

# Fetch repositories for each user
def get_user_repos(username, max_repos=500):
    print(f"Fetching repos for {username}")
    repos = []
    per_page = 100
    pages = min((max_repos // per_page), 5)
    
    for page in range(1, pages + 1):
        url = f"https://api.github.com/users/{username}/repos?per_page={per_page}&page={page}"
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 200:
            repos.extend(response.json())
            if len(response.json()) < per_page:
                break
        else:
            print(f"Error fetching repos for {username}: {response.status_code}")
            break
        time.sleep(1)  # To avoid rate limiting
    return repos
  
#Get user data
def get_user_data(username):
    print(f"Fetching data for {username}")
    response = requests.get(
        f"{BASE_URL}/users/{username}",
        headers=HEADERS
    )
    return response.json()

#Trimming company name
def trim_company_name(company_name):
    if company_name:
        while True:
            if company_name[0] == '@':
                company_name = company_name.lstrip("@")
            if company_name[0] == ' ':
                company_name = company_name.strip()
            if company_name[0] != '@' and company_name[0] != ' ':
                break
        company_name = company_name.upper()
    return company_name
# Save users data to users.csv
def save_users_to_csv(users):
    print("Saving data to users.csv")
    with open("users.csv", mode="w", newline='', encoding="utf-8") as file:
        writer.writerow(["login", "name", "company", "location", "email", "hireable", "bio", "public_repos", "followers", "following", "created_at"])
        writer = csv.writer(file)
        for user in users:
            if user['hireable'] == True:
                user['hireable'] = 'true'
            elif user['hireable'] == False:
                user['hireable'] = 'false'
            writer.writerow([user['login'], user['name'], user['company'], user['location'], user['email'], user['hireable'], user['bio'], user['public_repos'], user['followers'], user['following'], user['created_at']])

# Save repositories data to repositories.csv
def save_repositories_to_csv(repositories):
    print("Saving data to repositories.csv")
    with open("repositories.csv", mode="w", newline='', encoding="utf-8") as file:
        writer.writerow(["login", "full_name", "created_at", "stargazers_count", "watchers_count", "language", "has_projects", "has_wiki", "license_name"])
        writer = csv.writer(file)
        for repo in repositories:
            if repo['has_projects'] == True:
                repo['has_projects'] = 'true'
            elif repo['has_projects'] == False:
                repo['has_projects'] = 'false'
            if repo['has_wiki'] == True:
                repo['has_wiki'] = 'true'
            elif repo['has_wiki'] == False:
                repo['has_wiki'] = 'false'
            writer.writerow([repo['owner']['login'], repo['full_name'], repo['created_at'], repo['stargazers_count'], repo['watchers_count'], repo['language'], repo['has_projects'], repo['has_wiki'], repo['license']['key'] if repo['license'] else ""])

# Main function to gather and save data
def main():
    users = get_users_in_bangalore()
    all_repositories = []
    for user in users:
        username = user['login']
        user_data = get_user_data(username)
        user_data['company'] = trim_company_name(user_data.get('company', ''))
        user.update(user_data)
        repos = get_user_repos(username)
        all_repositories.extend(repos)
    
    save_users_to_csv(users)
    save_repositories_to_csv(all_repositories)
    print("Data saved to users.csv and repositories.csv")

if __name__ == "__main__":
    main()