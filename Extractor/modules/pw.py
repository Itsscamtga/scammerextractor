import requests, os, sys, re
import math
import json, asyncio
import subprocess
import datetime
from Extractor import app
from pyrogram import filters
from subprocess import getstatusoutput


async def get_otp(message, phone_no):
    url = "https://api.penpencil.co/v1/users/get-otp"
    query_params = {"smsType": "0"}

    headers = {
        "Content-Type": "application/json",
        "Client-Id": "5eb393ee95fab7468a79d189",
        "Client-Type": "WEB",
        "Client-Version": "2.6.12",
        "Integration-With": "Origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    }

    payload = {
        "username": phone_no,
        "countryCode": "+91",
        "organizationId": "5eb393ee95fab7468a79d189",
    }

    try:
        response = requests.post(url, params=query_params, headers=headers, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        await message.reply_text("**Failed to Generate OTP**")



async def get_token(message, phone_no, otp):
    url = "https://api.penpencil.co/v3/oauth/token"
    payload = {
        "username": phone_no,
        "otp": otp,
        "client_id": "system-admin",
        "client_secret": "KjPXuAVfC5xbmgreETNMaL7z",
        "grant_type": "password",
        "organizationId": "5eb393ee95fab7468a79d189",
        "latitude": 0,
        "longitude": 0
    }

    headers = {
        "Content-Type": "application/json",
        "Client-Id": "5eb393ee95fab7468a79d189",
        "Client-Type": "WEB",
        "Client-Version": "2.6.12",
        "Integration-With": "",
        "Randomid": "990963b2-aa95-4eba-9d64-56bb55fca9a9",
        "Referer": "https://www.pw.live/",
        "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }

    try:
        r = requests.post(url, json=payload, headers=headers)
        r.raise_for_status()
        resp = r.json()
        token = resp['data']['access_token']
        return token
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        await message.reply_text("**Failed to Generate Token**")
        
async def pw_login(app, Message, token):
    headers = {
        'Host': 'api.penpencil.xyz',
        'authorization': f"Bearer {token}",
        'client-id': '5eb393ee95fab7468a79d189',
        'client-version': '12.84',
        'user-agent': 'Android',
        'randomid': 'e4307177362e86f1',
        'client-type': 'MOBILE',
        'device-meta': '{APP_VERSION:12.84,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.physicswalb}',
        'content-type': 'application/json; charset=UTF-8',
    }

    params = {
       'mode': '1',
       'filter': 'false',
       'exam': '',
       'amount': '',
       'organisationId': '5eb393ee95fab7468a79d189',
       'classes': '',
       'limit': '20',
       'page': '1',
       'programId': '',
       'ut': '1652675230446', 
    }
    r = requests.get('https://api.penpencil.xyz/v3/batches/my-batches', params=params, headers=headers).json()["data"]
    details=""
    id_to_name_dict = {}
    for data in r:
        id_to_name_dict[data["_id"]] = data["name"]
        aa = f"BATCH: {data['name']}\nID: `{data['_id']}`\n\n"
        details += aa
    await app.reply_text(details)
    
    # await app.reply_text("Enter Batch ID")
    lolqq = await app.ask(Message.chat.id, text="**Enter Batch ID**")
    raw_text3 = lolqq.text
    batch = id_to_name_dict[raw_text3]
    response2 = requests.get(f'https://api.penpencil.xyz/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]
    
    await app.reply_text("**EXTRACTING DATA...** \n\n💡 Don't miss out! Join my<a href='https://t.me/scammer_botxz1'>Telegram channel</a> for updates. 📲🤩\n🔋 Powered by <a href='https://t.me/Scammer_botxz'>😎𝖘cᾰ𝗺𝗺ⲉ𝗿:)™~ </a> 🔥")
    for data in response2:
        tids = data['_id']
        params1 = {'page': '1', 'tag': '', 'contentType': 'exercises-notes-videos', 'ut': ''}
        response3 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{tids}/contents', params=params1, headers=headers).json()["data"]
        
        params2 = {'page': '2', 'tag': '', 'contentType': 'exercises-notes-videos', 'ut': ''}
        response4 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{tids}/contents', params=params2, headers=headers).json()["data"]
            
        params3 = {'page': '3', 'tag': '', 'contentType': 'exercises-notes-videos', 'ut': ''}
        response5 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{tids}/contents', params=params3, headers=headers).json()["data"]
            
        params4 = {'page': '4', 'tag': '', 'contentType': 'exercises-notes-videos', 'ut': ''}
        response6 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{tids}/contents', params=params4, headers=headers).json()["data"]
        
            
        try:
            for data in response3:
                class_title = data["topic"]
                class_url = data["url"].replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
                with open(f"{batch}.txt", 'a') as f:
                    f.write(f"{class_title}:{class_url}\n")
            for data in response3:
                    if 'homeworkIds' in data:
                        for homework in data['homeworkIds']:
                            pdf_topic = homework['topic']
                            for attachment in homework['attachmentIds']:
                                base_url = attachment['baseUrl']
                                key = attachment['key']
                                with open(f"{batch}.txt", 'a') as f:
                                    f.write(f"{pdf_topic} : {base_url+key}\n")
        except:
            pass
        try:
            for data in response4:
                class_title = data["topic"]
                class_url = data["url"].replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
                with open(f"{batch}.txt", 'a') as f:
                    f.write(f"{class_title}:{class_url}\n")
            for data in response4:
                    if 'homeworkIds' in data:
                        for homework in data['homeworkIds']:
                            pdf_topic = homework['topic']
                            for attachment in homework['attachmentIds']:
                                base_url = attachment['baseUrl']
                                key = attachment['key']
                                with open(f"{batch}.txt", 'a') as f:
                                    f.write(f"{pdf_topic} : {base_url+key}\n")
        except:
            pass
        try:
            for data in response5:
                class_title = data["topic"]
                class_url = data["url"].replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
                with open(f"{batch}.txt", 'a') as f:
                    f.write(f"{class_title}:{class_url}\n")
            for data in response5:
                    if 'homeworkIds' in data:
                        for homework in data['homeworkIds']:
                            pdf_topic = homework['topic']
                            for attachment in homework['attachmentIds']:
                                base_url = attachment['baseUrl']
                                key = attachment['key']
                                with open(f"{batch}.txt", 'a') as f:
                                    f.write(f"{pdf_topic} : {base_url+key}\n")
        except:
            pass
        try:
            for data in response6:
                class_title = data["topic"]
                class_url = data["url"].replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
                with open(f"{batch}.txt", 'a') as f:
                    enc_class_url = (f'{class_url}')
                    # enc_class_url = enc_url(f'{class_url}')
                    f.write(f"{class_title}:{enc_class_url}\n")
            for data in response3:
                    if 'homeworkIds' in data:
                        for homework in data['homeworkIds']:
                            pdf_topic = homework['topic']
                            for attachment in homework['attachmentIds']:
                                base_url = attachment['baseUrl']
                                key = attachment['key']
                                with open(f"{batch}.txt", 'a') as f:
                                    # pdf_url = enc_url(f'{base_url+key}')
                                    pdf_url = (f'{base_url+key}')
                                    f.write(f"{pdf_topic} : {pdf_url}\n")
        except:
            pass
        
    await app.reply_document(f"{batch}.txt", caption=f"🌟 Batch Name: `{batch}`\n\n**🤖 Extracted By: {Message.from_user.mention}**\n➖➖➖➖➖➖➖\n✨ Join our channel: [@scammer_botxz1](https://t.me/scammer_botxz1) 📢")
    # await bot.send_document(chat_id=ownerID, document=f"{batch}.txt", caption=f"🌟 Batch Name: `{batch}`\n\n**🤖 Extracted By: {m.from_user.mention}**\n➖➖➖➖➖➖➖\n✨ Join our channel: [@scammer_botxz1](https://t.me/scammer_botxz1) 📢", thumb=thumbnail)
    os.remove(f"{batch}.txt")
    await app.reply_text("Done")


async def pw_mobile(app, message):
    lol = await app.ask(message.chat.id, text="**ENTER YOUR PW MOBILE NO. WITHOUT COUNTRY CODE.**")
    phone_no = lol.text
    await lol.delete()
    await get_otp(message, phone_no)
    lol2 = await app.ask(message.chat.id, text="**ENTER YOUR OTP SENT ON YOUR MOBILE NO.**")
    otp = lol2.text
    await lol2.delete()
    token = await get_token(message, phone_no, otp)
    await message.reply_text(F"**YOUR TOKEN** => `{token}`")
    await pw_login(app, message, token)


async def pw_token(app, message):
    lol3 = await app.ask(message.chat.id, text="**ENTER YOUR PW ACCESS TOKEN**")
    token = lol3.text
    await lol3.delete()
    await pw_login(app, message, token)




    
