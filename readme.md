## Background
I wanted to download all the latest mp3 files of NYT Daily podcasts to listen while running. 

## Goal 
This python code open Daily podcast webpage (https://www.nytimes.com/column/the-daily) and get the links of the all episodes. Then automatilcally download the mp3 files. 

## Parameters

- download location: you can change the download location. e.g., I am using a cloud folder. 
- number of episodes: you can change the max number to download

## Add to task scheduler

I have added this python file in Windows Task scheduler to continuously update the podcast episodes. 

You need to create a task and add Program and Argument in Task Scheduler. 

Progoram: Your python path. e.g., C:/Users/abc/AppData/Local/Programs/Python/Python311/python.exe
Argument: D:\dev\auto_daily_podcast_downloader\download_all_daily_podcasts.py




