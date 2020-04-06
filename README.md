# GDrive-Streaming-Link
Stream from GDrive link in your favourite video player using your GDrive API_KEY.

# Contents:
* [Requirements](https://github.com/Tweetus-Bot/GDrive-Streaming-Link/blob/master/README.md#requirements)
* [How to?](https://github.com/Tweetus-Bot/GDrive-Streaming-Link/blob/master/README.md#how-to)
* [stream.py](https://github.com/Tweetus-Bot/GDrive-Streaming-Link/blob/master/README.md#streampy)
* [Credits](https://github.com/Tweetus-Bot/GDrive-Streaming-Link/blob/master/README.md#credits)

## Requirements:
1. file_id from GDrive link.
2. api_key from your Google Cloud Console.
       
## How to?
* [How to get file_id?](https://github.com/Tweetus-Bot/GDrive-Streaming-Link/blob/master/README.md#how-to-get-file_id)
* [How to get api_key?](https://github.com/Tweetus-Bot/GDrive-Streaming-Link/blob/master/README.md#how-to-get-api_key)
### How to get file_id?
- file_id can be obtained: 
  - from a GDrive link which is already publicly (or)
  - by making a shareable link from a your GDrive
- For example, here, `https://drive.google.com/open?id=1hpBqbuHQr6UhVawkcsANAe63P70s9Ycu` **1hpBqbuHQr6UhVawkcsANAe63P70s9Ycu** is the file_id.    
       
### How to get api_key?
api_key can be obtained from Google Cloud Console. Following pictures guide you on how to get api_key:

1. Go to [Google Cloud Console](https://console.cloud.google.com) and create a new project.
![Create a Project](https://i.imgur.com/7RRshPa.png)

2. Now click on APIs & Services and go to Credentials.
![Credentials](https://i.imgur.com/Wt24uXa.png)

3. Click on Create Credentials and then on API key and copy.
![API Key](https://i.imgur.com/pCa9SvF.png)

4. Copy and save the api_key somewhere.

## stream.py
This is where you obtain the streamable link. As this is my first project, I thought of writing it in python with just two functions. That is `print` and `input`. You can get the py from [here]()

```python
prompt = "Enter your file_id:" 
file_id = input(prompt)

prompt = "Enter your api_key:"
api_key = input(prompt)

print(f"https://www.googleapis.com/drive/v3/files/{file_id}/?key={api_key}&alt=media")
```

## Credits
Thanks to [Yuno](https://github.com/yunooooo/Google-Drive-Streamable-Link-Generator).
