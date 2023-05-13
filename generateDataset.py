from textblob import TextBlob
import csv

fileObj = open("cleanComments.txt","r")
csvFileObj = open("commentsDatasetLarge.csv","w")
datawriter = csv.writer(csvFileObj,delimiter=",")

header = ["text","polarity","sentiment"]
datawriter.writerow(header)
rowsWritten = 0

while True:
    # if rowsWritten>50:
    #      break
    comment = fileObj.readline().strip()
    if not comment:
            break
    try:  
        blob = TextBlob(comment)
    except:
         print("Ignoring: ",comment)
         continue
    sentiment = blob.sentiment
    polarity = sentiment.polarity

    label = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"

    datawriter.writerow([comment,polarity,label])
    rowsWritten+=1

csvFileObj.close()
fileObj.close()



    
