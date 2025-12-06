# 🎁 Epic Games Free Games → Discord Webhook Notifier

A simple Python CLI tool that **fetches the current free games from Epic Games** and sends them to a **Discord channel** using a webhook.  
Once a game is sent, it gets **saved locally**, so it will **never be sent twice** unless you remove it manually.

---

## 🚀 Features

- ✔ Fetches free games from the official Epic Games API  
- ✔ Sends game info + image directly to a Discord webhook  
- ✔ Saves previously sent games (`sent_games.txt`)  
- ✔ Saves the webhook so the user only enters it once  
- ✔ Prevents duplicate messages  
- ✔ Clean CLI output with color feedback  

## 📦 installation

Download the **.exe** file

---
## 🔧 **How It Works**

1️⃣: **Fetch Game Data**

The script calls Epic’s API and extracts:

Name

Image URL

2️⃣: **Check Duplicates**

The tool reads sent_games.txt.
If all free games are already listed → it sends nothing.

3️⃣: **Send to Discord**

For any new game:
A Discord embed message is created
Sent via webhook
Game saved to sent_games.txt

---

## 📝 Notes

Delete sent_games.txt to resend all games.

Delete webhook.txt to set a new Discord webhook.

to find the sent_games.txt / webhook.txt: Press **Windows + R** will show you the "RUN" box where you can type commands type in **appdata** then press enter a folder will pop up go to **Local** then **EpicFreeGamesBot** go inside the folder then you will find the .txt files

Example:  **"C:\Users\username\AppData\Local\EpicFreeGamesBot\EpicFreeGamesBot"** >> replace the "**username**" with your **pc username**

If you experience any problems run the script with **administrator**

if you want to make this script executes everytime you open your pc press **Windows + R** then type **shell:startup** a folder will open take the shortcut from the script then put it inside that folder 
---
**This project was mainly created for practice. If you notice anything you don’t like, feel free to reach out I might even make a small commission for you!**
