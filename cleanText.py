import os
import re
from langdetect import detect
from cleantext import clean

def cleanText(inputStr):
    try:
        cleanedtext = clean(inputStr,
            fix_unicode=True,               # fix various unicode errors
            to_ascii=True,                  # transliterate to closest ASCII representation
            lower=True,                     # lowercase text
            no_line_breaks=True,           # fully strip line breaks as opposed to only normalizing them
            no_urls=True,                  # replace all URLs with a special token
            no_emails=True,                # replace all email addresses with a special token
            no_phone_numbers=True,         # replace all phone numbers with a special token
            no_numbers=True,               # replace all numbers with a special token
            no_digits=True,                # replace all digits with a special token
            no_currency_symbols=True,      # replace all currency symbols with a special token
            no_punct=True,                 # remove punctuations
            replace_with_punct=" ",          # instead of removing punctuations you may replace them
            replace_with_url=" ",
            replace_with_email=" ",
            replace_with_phone_number=" ",
            replace_with_number=" ",
            replace_with_digit=" ",
            replace_with_currency_symbol=" ",
            lang="en"                       # set to 'de' for German special handling
        )
    except:
        return {"status":-1,"cleanedText":""}
    return {"status":1,"cleanedText":cleanedtext}

rawCommentFileObj = open("rawComments.txt","r")
rawCommentsText = rawCommentFileObj.read()
rawComments = rawCommentsText.split("--\n--")
cleanCommentFileObj = open("cleanComments.txt","w")

commentsEncountered = 0
commentsIgnored=0
commentsWritten = 0

for rawComment in rawComments:
    commentsEncountered +=1
    rawComment=rawComment.strip()

    if rawComment == "":
        commentsIgnored +=1
        continue
    
    if not rawComment:
        commentsIgnored +=1
        continue

    try:
        language = detect(rawComment)
    except:
        # print("***Ignoring comment***")
        # print("Reason: langdetect error")
        # print("Comment: ",rawComment)
        commentsIgnored +=1
        continue

    if(language != 'en'):
        # print("***Ignoring comment***")
        # print("Reason: Language not english")
        # print("Comment: ",rawComment)
        commentsIgnored +=1
        continue

    cleanedObj = cleanText(rawComment)
    # print(cleanedObj)
    if(cleanedObj["status"] == -1):
        commentsIgnored +=1
        continue

    cleanedText = cleanedObj["cleanedText"]
    emojiFreeText = re.sub('[^a-zA-Z0-9 \n\.]', ' ', cleanedText)
    if emojiFreeText == "":
        commentsIgnored +=1
        continue

    cleanCommentFileObj.write(emojiFreeText+"\n")
    commentsWritten+=1

rawCommentFileObj.close()
cleanCommentFileObj.close()

print("Statistics:")
print("Total Comments encountered: ",commentsEncountered)
print("Total Comments ignored", commentsIgnored)
print("Total Comments written", commentsWritten)




