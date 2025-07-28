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
dt_pst = datetime(2025, 7, 28, 10, 0, tzinfo=pst)
publish_at = dt_pst.isoformat()
# => "2025-07-15T15:30:00-07:00"

# put the path of the video that you want to upload
media_file = "kittySLIME.mp4"

def upload_video(youtube):
    request_body = {
        "snippet": {
            "categoryId": "24",
            "title": "Kitty plays with GREEN SLIME ASMR #ai #shorts #funny #cat #compilation",
            "description": "These hyper-realistic AI cats are just so cute — they live through tiny cinematic stories. "
            "From getting trapped in claw machines to surviving spooky nights, every short is packed with "
            "expressive emotion, unexpected twists, and soft kitty chaos.\n\n"
            "🎬 Ultra-realistic AI visuals\n"
            "📖 Mini stories in under 60 seconds\n"
            "🐾 Expressive, lifelike reactions that feel too real\n\n"
            "Watch, feel, and fall into the world of these story-driven kitties.\n"
            "#RealisticCats #AIKittyShorts #CinematicCats #FunnyCatVideos "
            "#AIPets #EmotionalShorts #MeowMoments",
            "tags": ["ai","cat","shorts","funny","kitty","compilation", "stories", "realistic kittens","claw machine"
                     ,"funny cat short","ai generated video","ai shorts","meta ai","kitten chaos",
                     "short cat video","cute cats","photorealistic cats","viral cat short","realistic animal ai",
                     "cat videos","hyperrealistic kitten","cat" "animation","realistic ai cat"]
        },
        "status":{
            "privacyStatus": "private",
            "publishAt": publish_at,
        },
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


