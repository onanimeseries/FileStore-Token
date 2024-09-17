# 📁 Advance File Sharing Token Bot

<div align="center">
  <img src="https://files.catbox.moe/c5ngwn.jpg" alt="Bot" width="300" style="border: 5px solid #e94560; border-radius:30px;">
</div>

<p align="center">
  <a href="https://t.me/ultroid_official">
    <img src="https://img.shields.io/badge/%E1%B4%8F%C9%B4%C9%A2%E1%B4%8F%C9%AA%C9%B4%C9%A2%20%E1%B4%80%C9%B4%C9%AA%E1%B4%8D%E1%B4%87%20%EA%9C%B1%E1%B4%87%CA%80%C9%AA%E1%B4%87%EA%9C%B1-CHANNEL-blue?style=for-the-badge&logo=telegram" alt="ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ ꜱᴇʀɪᴇꜱ Channel">
  </a>
  <a href="https://t.me/ultroidofficial_chat">
    <img src="https://img.shields.io/badge/Ultroid%20%F0%9D%95%8F%20Official-Group-blue?style=for-the-badge&logo=telegram" alt="ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ ꜱᴇʀɪᴇꜱ Group">
  </a>
</p>


<h1 style="display: flex; align-items: center;">
  <img src="https://files.catbox.moe/umzdcz.webp" alt="Saturo" width="60" style="margin-right: 10px;">
  <span style="position: relative; top: -3px; left: -5px; font-size: 45px;">Ｓａｔｕｒｏ：</span>
</h1>




Telegram Bot to store posts and documents accessible via special links.<br>

## 🚀 Overview

File Sharing Token Bot is a Telegram bot designed to store posts and documents, accessible through special links. This bot provides a convenient way to manage and share content within Telegram.

### ✨ Features

- Store posts and documents.
- Access content via special links.
- Easy to deploy and customize.
- Token Verifiction
- Auto Deletion
- #New Added 2'F-sub
## 🛠️ Setup

To deploy the bot, follow these steps:

1. Add the bot to a database channel with all permissions.
2. Add the bot to the ForceSub channel as an admin with "Invite Users via Link" permission if ForceSub is enabled.

## 📦 Installation

### Deploy on Heroku

Click the button below to deploy the bot on Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

For a detailed deployment guide, watch [this tutorial video](https://youtu.be/7jBbBL9t9jI?si=j52MwTn41TXsc76l).

### Deploy on Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/1jKLr4)

### Deploy on Koyeb

Click the button below to deploy the bot on Koyeb:

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/ibrahimkhan008/FileStore-Token&branch=main&name=FileStore-Token)

### Deploy on Your VPS

```bash
git clone https://github.com/ibrahimkhan008/FileStore-Token
cd FileStore-Token
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````
---
## Deploy on VPS
---
## Prerequisites

### 1. Installing requirements

- Clone this repo:

```
git clone https://github.com/ibrahimkhan008/FileStore-Token/ && cd FileStore-Token
```

- For Debian based distros

```
sudo apt install python3 python3-pip
```

Install Docker by following the [Official docker docs](https://docs.docker.com/engine/install/#server).
Or you can use the convenience script: `curl -fsSL https://get.docker.com |  bash`


- For Arch and it's derivatives:

```
sudo pacman -S docker python
```

------

### 2. Build And Run the Docker Image

Make sure you still mount the app folder and installed the docker from official documentation.

- There are two methods to build and run the docker:
  1. Using official docker commands.
  2. Using docker-compose.

------

#### Build And Run The Docker Image Using Official Docker Commands

- Start Docker daemon (SKIP if already running, mostly you don't need to do this):

```
sudo dockerd
```

- Build Docker image:

```
sudo docker build . -t uxbbot
```

- Run the image:

```
sudo docker run -p 80:80 -p 8080:8080 uxbbot
```

- To stop the running image:

```
sudo docker ps
```

```
sudo docker stop id
```

----

#### Build And Run The Docker Image Using docker-compose

**NOTE**: If you want to use ports other than 80 and 8080 change it in [docker-compose.yml](docker-compose.yml).

- Install docker compose

```
sudo apt install docker-compose
```

- Build and run Docker image:

```
sudo docker-compose up --build
```

- To stop the running image:

```
sudo docker-compose stop
```

- To run the image:

```
sudo docker-compose start
```

- To get latest log from already running image (after mounting the folder):

```
sudo docker-compose up
```

---

Cmd to start the Bot: bash start.sh
🔧 Admin Commands

```
start - start the bot or get posts

batch - create link for more than one posts

genlink - create link for one post

users - view bot statistics

broadcast - broadcast any messages to bot users

stats - checking your bot uptime
```

🛠️ Variables

* `API_HASH` Your API Hash from my.telegram.org
* `APP_ID ` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `DB_URI ` Your mongo db url [tutorial video](https://youtu.be/qFB0cFqiyOM).
* `DB_name ` Your mongo db session name ( random )
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/codexbotz/File-Sharing-Bot/blob/main/README.md#start_message'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `FORCE_SUB_CHANNEL2` Optional: ForceSub Channel ID, leave 0 if you want disable force sub
* `PROTECT_CONTENT` Optional: True if you need to prevent files from forwarding

### Extra Variables

* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML and <a href='https://github.com/7thofficial/File-Sharing-Bot/blob/main/README.md#custom_caption'>fillings</a> for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False
* `BOT_STATS_TEXT` put your custom text for stats command, use HTML and <a href='https://github.com/7thofficial/File-Sharing-Bot/blob/main/README.md#custom_stats'>fillings</a>
* `USER_REPLY_TEXT` put your text to show when user sends any message, use HTML

### Token Variables

* `IS_VERIFY` = Default : "True" (if you want off : False )
* `SHORTLINK_URL` = Your shortner Url ( ex. "publicearn.com")
* `SHORTLINK_API` = Your shortner API (ex. "971f149c5c6978f6638759fe769a54bd695cf704")
* `VERIFY_EXPIRE` = ( ex. 86400)) # Add time in seconds


### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

#### CUSTOM_STATS

* `{uptime}` - Bot Uptime


💬 Support
Join Our [Telegram Group](https://t.me/ultroidofficial_chats)<br> For Support/Assistance And Our [Channel](https://www.telegram.dog/OnAnimeSeries) For Updates.   
   
Report Bugs, Give Feature Requests There..   

🎉 Credits

Thanks to Dan for his awesome library. [Libary](https://github.com/pyrogram/pyrogram)
Our support group members.

📝 License
GNU GPLv3 [![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html) 

[FILE-SHARING-BOT](https://github.com/ibrahimkhan008/FileStore-Token/) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 


   **Star this Repo if you Liked it ⭐⭐⭐**

