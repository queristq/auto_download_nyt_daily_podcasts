## Background
I wanted to download all the latest mp3 files of NYT Daily podcasts to listen while running. 

## Goal 
This python code opens NYT Daily podcast webpage (https://www.nytimes.com/column/the-daily) and get the links of the all episodes. Then automatilcally download the mp3 files. 

## Parameters
- download location: you can change the download location (variable name: foldername). e.g., I am using a cloud folder. 
- number of episodes: you can change the max number to download (Variable name: max_download_number)

## Add to Windows Task Scheduler

I have added a task in Windows Task scheduler to repetitively execute this Python file to update the podcast episodes. 

You will need to add two parameters - Program and Argument - in Windows Task Scheduler. 

Progoram: Your python path. e.g., C:/Users/abc/AppData/Local/Programs/Python/Python311/python.exe
Argument: D:\dev\auto_daily_podcast_downloader\download_all_daily_podcasts.py




