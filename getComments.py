import os

import googleapiclient.discovery
import re
from dotenv import load_dotenv

load_dotenv()
apiKey = os.environ.get("API_KEY")

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = apiKey

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version,developerKey = DEVELOPER_KEY)
    
    path = "./videoIds"
    listDirs = os.listdir(path)
    filenames = [f for f in listDirs if f.endswith(".txt")]
    # print(filenames)
    
    commentFileObj = open("rawComments.txt","w")

    commentsTotal = 0
    commentsEncountered = 0
    for f in filenames:

        fileObj = open("./videoIds/"+f,"r")
        print("Processing file: ",f)
        
        while True:
            id = fileObj.readline()
            if not id:
                break
            id=id.strip()
            request = youtube.commentThreads().list(
                part="snippet",
                fields="items(id,snippet/topLevelComment/snippet/textOriginal)",
                videoId=id,
                maxResults=100
            )

            try:
                response = request.execute()
            except:
                print("Video with id ",id," ignored")
                # print(exp)
                continue


            for commentItem in response["items"]:
                text = commentItem["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
                text=text.lower()
                text = re.sub("--\n--"," ",text)
                commentsEncountered +=1
                commentFileObj.write(text+"--\n--")
                commentsTotal+=1

            # break
            # print("Comments extracted till now:",commentsTotal)

        if commentsTotal > 100000:
            break

        fileObj.close()

    
    commentFileObj.close()

    print("*****Statistics:*****")
    print("Total Comments encountered: ",commentsEncountered)
    print("Total Comments written", commentsTotal)

if __name__ == "__main__":
    main()