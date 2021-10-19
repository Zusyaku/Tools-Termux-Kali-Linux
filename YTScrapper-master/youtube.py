import requests
from dotenv import load_dotenv
import os
import json
import isodate
# import csv
import re
import unicodecsv as csv
import sys

load_dotenv()

KEY=os.environ.get("KEY")
BASE_URL="https://www.googleapis.com/youtube/v3"

def get_channel_info(id=None,name=None):
    
    PAYLOAD = dict()
    if id:
        PAYLOAD['id']=id
    elif name:
        PAYLOAD['forUsername']=name
    else:
        return None
    PAYLOAD['part']="snippet,contentDetails,statistics"
    PAYLOAD['key']=KEY
    try:
        response = requests.get(BASE_URL+"/channels", params=PAYLOAD).json()
    except:
        print("Conection Error")
        sys.exit()
    info = dict()
    response=response['items'][0]    
    info['id']=response['id']
    info['title']=response['snippet']['title']
    info['description']=response['snippet']['description']
    info['upload_id']=response['contentDetails']['relatedPlaylists']['uploads']
    info['total_videos']=response['statistics']['videoCount']
    return info


def parse_iso_date(date=None,duration=None):
    if date:
        return str(isodate.parse_datetime(date))
    elif duration:
        return str(isodate.parse_duration(duration))
    else:
        return None


def write_data(json_data,file="youtube_data.csv"):
    WATCH_PREFIX="https://www.youtube.com/watch?v="
    keys = json_data[0].keys()
    csv_data_list=[keys]
    for x in json_data:
        x['url']=WATCH_PREFIX+x.pop('id')
        csv_data_list.append( x.values())
    with open(file, "wb") as output_file:
        writer = csv.writer(output_file, encoding='utf-8')
        writer.writerows(csv_data_list)
    print("[+] Data Saved to ",file)

def get_all_videos(id):
    
    PAYLOAD = [{},{}]
    PAYLOAD[0]={'part':"snippet",'maxResults':50,'playlistId':id,'key':KEY}
    PAYLOAD[1]={'part':"contentDetails",'key':KEY}
    full_videos_dump=[]
    while True:
        response = requests.get(BASE_URL+"/playlistItems", params=PAYLOAD[0]).json()
        videos_list=response['items']
        nextPageToken=response.get('nextPageToken',None)
        videos_dump=[]
        for video in videos_list:
            video=video['snippet']
            videos_dump.append({"title":video['title'],
                                "description":video['description'],
                                "id":video['resourceId']['videoId'],
                                "thumbnail":video['thumbnails']['default']['url'],
                                "published_on":parse_iso_date(date=video["publishedAt"])})
        videos_id=[video['id'] for video in videos_dump ]
        PAYLOAD[1]['id']=",".join(videos_id)
        response = requests.get(BASE_URL+"/videos", params=PAYLOAD[1]).json()['items']
        for x in range(len(videos_dump)):
            videos_dump[x]['duration']=parse_iso_date(duration=response[x]['contentDetails']['duration'])
        full_videos_dump+=videos_dump
        print('\rScrapped {current} Videos of {total} videos'.format(current=len(full_videos_dump),total=channel_info['total_videos']),end='\r')
        if nextPageToken:
            PAYLOAD[0]['pageToken']=nextPageToken
        else:
            break
    return full_videos_dump


while True:
    channel = input("Enter Full Channel URL: ")
    if re.search(r"^.*youtube.com\/channel\/.{24}$",channel):
        channel=channel.split('/')[-1]
        break
    else:
        print("[!] Put a valid URL")
        print("    Example: https://www.youtube.com/channel/UC6CwdVj9ztWzJtO3q43isfg ")

channel_info = get_channel_info(id=channel)
try:
    print("Channel Name: ",channel_info['title'])
    print("Channel Description: ",channel_info['description'])
    input("\n\nPress Enter To Confirm And Start Scrapping")
    print("\n\n")
    all_video=get_all_videos(channel_info['upload_id'])
    write_data(all_video)
except:
    print("Conection Error")
    sys.exit()