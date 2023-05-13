
import os

import googleapiclient.discovery
import googleapiclient.errors


regions = ["US","GB"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDTKyBWPeUkcddV47Y5Y0D-4KgvzVVcZGo"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)
    
    # First obtain the video category id for the categories "Music" & "News and Politics"

    regionCategoryComb =[]
    for region in regions:
        request = youtube.videoCategories().list(
            part="snippet",
            regionCode=region,
            fields="items(id,snippet/title)"
        )
        response = request.execute()

        for item in response["items"]:
            categoryTitle = item["snippet"]["title"] 
            categoryId = item["id"]

            if categoryTitle == "Music" or categoryTitle == "News & Politics":
                combination = {"regionCode":region, "categoryId":categoryId, "title":categoryTitle}
                regionCategoryComb.append(combination)

    
    # Second, for each region get videoIDs belonging to the "Music" and "News & Politics" video category
    for combination in regionCategoryComb:
        regionCode = combination["regionCode"]
        categoryId = combination["categoryId"]
        regionCategoryComb = combination["title"]

        fileName = "videoIds_"+regionCode+"_"+categoryId+".txt"

        fileObj = open("./rawComments/"+fileName,"w")


        request = youtube.search().list(
            part="snippet",
            maxResults=50,
            regionCode=regionCode,
            relevanceLanguage="en",
            type="video",
            videoCategoryId=categoryId,
            fields="nextPageToken,items/id/videoId"
        )

        print("Writing to file: ",fileName)
        videoCounts = 0
        while True:
            response = request.execute()
            
            for videoItem in response["items"]:
                fileObj.write(videoItem["id"]["videoId"]+"\n")
                videoCounts+=1

            

            if(videoCounts>=300):
                break

            if "nextPageToken" not in response.keys():
                break
            nextToken = response["nextPageToken"]

            request = youtube.search().list(
                part="snippet",
                maxResults=50,
                regionCode=regionCode,
                relevanceLanguage="en",
                type="video",
                videoCategoryId=categoryId,
                fields="nextPageToken,items/id/videoId",
                pageToken = nextToken
            )

        fileObj.close()

        print("No of videos Ids extrated and wrtiiten: ",videoCounts)

if __name__ == "__main__":
    main()