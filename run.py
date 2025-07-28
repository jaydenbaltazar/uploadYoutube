import os
import google_auth_httplib2
import google_auth_oauthlib
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.http
from datetime import datetime, timezone, timedelta

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
TOKEN_FILE = 'token.json'

def authenticate_youtube():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)

    # Load client secrets file, put the path of your file
    client_secrets_file = "client.json"

    
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, SCOPES)
    credentials = flow.run_local_server()

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", credentials=credentials)

    return youtube


# PDT in July is UTC‑7
pst = timezone(timedelta(hours=-7))

# “July 15 2025, 3:30 PM Pacific” → 15:30 local
dt_pst = datetime(2025, 7, 29, 10, 0, tzinfo=pst)
publish_at = dt_pst.isoformat()
# => "2025-07-15T15:30:00-07:00"

# put the path of the video that you want to upload
media_file = "ToUpload/roseQuartToast.mp4"


def upload_video(youtube):
    request_body = {
        "snippet": {
            "categoryId": "24", # Category ID for "Entertainment"
            "title": "Spreading GEM CRYSTAL on TOAST ASMR #ai #shorts #relaxing #satisfying",
            "description": "Listen closely... every slice hits different. 🔪🍎 AI-generated precision meets cutting board "
            "ASMR in this ultra-satisfying food prep loop. Perfect for relaxing, zoning out, or oddly calming "
            "motivation while you scroll.\n\n"
            "🎧 Crisp slice sounds\n"
            "🍎 AI-generated food realism\n"
            "🧘 Calming rhythm & soft tension release\n\n"
            "#asmrshorts #satisfying #aiasmr #cuttingboard #relaxing #metaai #aifood"
            ,
            "tags": ["ai","asmr","shorts","relaxing","satisfying","toast", "speading toast", "keyboardasmr", "slime", "slimeasmr","oddlysatisfying","foodasmr","cuttingboard","foodprep","calming","ai generated video","ai shorts"]
        },
        "status":{
            "privacyStatus": "private",
            "publishAt": publish_at,
        }
    }

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=googleapiclient.http.MediaFileUpload(media_file, chunksize=-1, resumable=True)
    )

    response = None 

    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload {int(status.progress()*100)}%")

        print(f"Video uploaded with ID: {response['id']}")

if __name__ == "__main__":
    youtube = authenticate_youtube()
    upload_video(youtube)


