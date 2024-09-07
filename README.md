# Terminal Drive Downloader

This script allows you to download individual files or multiple files from Google Drive using Terminal and Google Drive API.

## Features

- Download individual files from Google Drive.
- Download multiple files from Google Drive.
- Handle multiple file downloads in one session.
- User-friendly command-line prompts for input.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Zkryy/terminal-drive-downloader.git

   cd terminal-drive-downloader
   ``` 
2. **Install Required Packages**
   
   ```bash
   pip install gdown google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client tqdm
   ```
3. **Obtain Google API Credentials**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/apis).
   - Create a new project or select an existing one.
   - Navigate to the Credentials tab and create OAuth 2.0 Client IDs.
   - Download the `client_secrets.json` file and place it in the project directory.
  
## How to Use

1. **run the script**
    in the terminal, navigate to  the project and execute:
    ```bash
    python GDownloader.py
    ```
2. **Follow the Prompts**
   - Enter the directory where you want to save the downloaded files.
   - Choose the download type (single file or multiple files).
   - Paste the Google Drive file links.
3. **Monitor the Download Progress**
   The script will download the files based on your input. It provides progress updates and error messages as needed. **Don't close your terminal window and quit the script**, or the download will be interrupted and failed.

## How it Works

1. **Authentication**
   - The script uses OAuth 2.0 to authenticate with Google Drive. It will prompt you to log in and authorize access to your Google Drive account.
   - Authentication credentials are saved in `token.json` file for future use.
2. **Single and Multiple Files Passing**
   - The script parses the provided Google Drive link to determine if it's a Single or Multiple files.
   - For single files, it constructs a download URL and uses `gdown` to download the file.
   - For multiple files, it lists all the links that user provided, and downloads them one by one.

## Acknowledgements

- [gdown](https://github.com/wkentaro/gdown) for handling Google Drive file downloads.
- [Google API Client Library for Python](https://github.com/googleapis/google-api-python-client) for interacting with Google Drive API.
- [tqdm](https://github.com/tqdm/tqdm) for displaying progress bars.

## Contact

For questions or support, please open an issue on the [Github Repository](https://github.com/Zkryy/terminal-drive-downloader/issues). or email me at [dzikrimaulana1511@gmail.com](mailto:dzikrimaulana1511@gmail.com)