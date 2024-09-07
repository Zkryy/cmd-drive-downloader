import os
import gdown
from tqdm import tqdm
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate_drive():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('drive', 'v3', credentials=creds)

def choose_directory():
    path = input("Enter the directory to save downloaded files (press Enter to use the default directory): ").strip()
    if not path:
        path = os.getcwd()
    if not os.path.exists(path):
        try:
            os.makedirs(path)
            print(f"Directory created at: {path}")
        except Exception as e:
            print(f"Failed to create directory: {str(e)}")
            return choose_directory()
    print(f"Files will be saved in: {path}")
    return path

def parse_drive_id(link):
    if "drive.google.com" in link:
        if "/file/d/" in link:
            return link.split("/file/d/")[1].split("/")[0], 'file'
        elif "/folders/" in link:
            return link.split("/folders/")[1].split("?")[0], 'folder'
    raise ValueError("Invalid Google Drive link. Please provide a valid link.")

def download_file_with_progress(service, file_id, destination, file_index):
    try:
        file_metadata = service.files().get(fileId=file_id, fields="name").execute()
        file_name = file_metadata['name']
        url = f"https://drive.google.com/uc?id={file_id}"
        destination = os.path.join(destination, file_name)
        gdown.download(url, destination, quiet=False)
        print(f"File {file_index} '{file_name}' downloaded successfully.")
    except Exception as e:
        print(f"Download failed for File {file_index}: {str(e)}")

def download_multiple_files(service, links, destination):
    links = [link.strip() for link in links.split(',')]
    
    for index, link in enumerate(links, start=1):
        try:
            file_id, file_type = parse_drive_id(link)
            if file_type == 'file':
                download_file_with_progress(service, file_id, destination, index)
            else:
                print(f"Link {index} is not a file link. Skipping...")
        except ValueError as e:
            print(f"Error parsing link {index}: {str(e)}")
    
    print("All files downloaded successfully.")

def main():
    service = authenticate_drive()
    destination = choose_directory()

    while True:
        download_type = input("Choose download type: (1) Single File, (2) Multiple Files: ").strip()
        
        if download_type == '1':
            link = input("Paste the Google Drive link: ").strip()
            file_id, file_type = parse_drive_id(link)
            if file_type == 'file':
                download_file_with_progress(service, file_id, destination, 1)
            else:
                print("The provided link is not a file link.")
        
        elif download_type == '2':
            links = input("Paste the Google Drive links separated by commas: ").strip()
            download_multiple_files(service, links, destination)
        
        else:
            print("Invalid option selected.")

        # Ask the user
        repeat = input("Do you want to download another file or set of files? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Exiting the script.")
            break

    print("Download process completed.")

if __name__ == "__main__":
    main()
