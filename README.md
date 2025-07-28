# YouTube Video Upload Script

This repository contains a Python script for uploading videos to YouTube using the YouTube Data API v3. The script manages authentication, video metadata setup, and the upload process.

## Prerequisites

Before using this script, make sure you have the following:

1. **Google Developer Console Project**: Set up a project and activate the YouTube Data API v3.
2. **OAuth 2.0 Credentials**: Get your OAuth 2.0 Client ID and Client Secret.
3. **Python Environment**: Make sure Python is installed on your system.

## Getting Started

### Step 1: Configure Google Developer Console

1. **Go to the Developer Console**: Visit [Google Developer Console](https://console.developers.google.com/).
2. **Set Up a New Project**: Click "Select Project" at the top, then "New Project". Name it and create the project.
3. **Activate YouTube Data API v3**: Navigate to "API & Services Dashboard" and click "Enable APIs and Services". Search for "YouTube Data API v3" and activate it.
4. **Configure OAuth Consent Screen**: Go to "OAuth consent screen" on the sidebar, choose "External", and complete the required information.
5. **Generate OAuth 2.0 Credentials**: Navigate to "Credentials", click "Create Credentials", and choose "OAuth 2.0 Client IDs". Download the JSON credentials file and store it safely.

### Step 2: Install Required Dependencies

Install the necessary packages using pip:

`pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client`

### Step 3: Set Up and Execute the Script

1. **Position the Credentials File**: Make sure the `client_secrets_file` path in the script references your downloaded credentials JSON file.
2. **Customize the Script**: Adjust the script as necessary for your video upload requirements. The script includes authentication and upload capabilities.

### Step 4: Execute the Script

Launch the script from your terminal or command prompt:

`python run.py`

The script will ask you to authenticate using your Google account. After authentication, it will upload the designated video to your YouTube channel.

## Script Overview

The script accomplishes these tasks:

1. **Google Authentication**: Utilizes OAuth 2.0 for authentication with the YouTube Data API v3.
2. **Video Upload**: Uploads videos to YouTube with the designated metadata.

## Troubleshooting

If you experience problems, verify that:

- The credentials file is properly positioned and the path is accurate.
- You have activated the YouTube Data API v3 in your Google Developer Console.
- The required packages are installed in your Python environment.

## License

This project uses the MIT License. Refer to the LICENSE file for more information.
