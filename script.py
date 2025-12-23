import os
import requests
from git import Repo

# --- CONFIGURATION ---
API_TOKEN = 'gb_api_aCaXjTYV070bkz9BFZyiLhxmhI3PBJgAVqOLqs9Q'
ORG_ID = 'UqB26ZsUCCuLBAdK2gwL' # Replace with your actual ID from the URL
BACKUP_DIR = './backups'

headers = {'Authorization': f'Bearer {API_TOKEN}'}

def run_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # 1. Get all spaces from Roadcast Docs
    print("Fetching spaces from GitBook...")
    url = f'https://api.gitbook.com/v1/orgs/{ORG_ID}/spaces'
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching spaces: {response.text}")
        return

    spaces = response.json().get('items', [])

    for space in spaces:
        title = space['title'].replace(" ", "_").lower()
        space_id = space['id']
        print(f"Backing up: {title}...")

        # 2. Download content as Markdown
        # Note: This is a simplified example of fetching the primary content
        content_url = f'https://api.gitbook.com/v1/spaces/{space_id}/content'
        content_res = requests.get(content_url, headers=headers)
        
        space_path = os.path.join(BACKUP_DIR, title)
        if not os.path.exists(space_path):
            os.makedirs(space_path)

        with open(os.path.join(space_path, 'content.json'), 'w') as f:
            f.write(content_res.text)

    # 3. Git Operations
    try:
        repo = Repo('.') # Assumes your bolt_v2_docs is a git repo
        repo.git.add(BACKUP_DIR)
        repo.index.commit("Backup: Roadcast Docs updated")
        origin = repo.remote(name='origin')
        origin.push()
        print("Successfully pushed to GitHub!")
    except Exception as e:
        print(f"Git Error: {e}")

if __name__ == "__main__":
    run_backup()