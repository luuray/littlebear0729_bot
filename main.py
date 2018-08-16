#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import random
sys.path.append("/usr/local/python3.6/lib/python3.6/site-packages")
sys.path.append("/usr/local/lib/python3.5/dist-packages")
import telebot
import time
from datetime import datetime,date
import datetime
random.seed(int(time.time()))

bot = telebot.TeleBot("REPLACE YOUR TOKEN HERE")


# welcome
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "这是一个 @LittleBear0729 写的私人bot.（尚未完成）")


#prpr
emotions = ['( >  < )', '⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄', '(≧ ﹏ ≦)', '(*/ω＼*)', 'ヽ(*。>Д<)o゜', '(つ ﹏ ⊂)', '| ω・`)']

@bot.message_handler(commands=['prpr'])
def prpr(message):
	randNum = random.randint(0, len(emotions)-1)
	bot.reply_to(message, emotions[randNum])
	print(message)


#class_schedule
schedule = ["英语\n化学\n语文\n数学\n物理\n----------\n历史\n自习\n班会",
"英语\n政治\n数学\n语文\n语文\n----------\n地理\n体育\n物理",
"英语\n物理\n信息\n数学\n化学\n----------\n历史\n国学\n生物",
"语文\n物理\n化学\n生物\n信息\n----------\n英语\n数学\n选修课\n选修课",
"英语\n语文\n数学\n体育\n政治\n----------\n地理\n音乐\n化学",
"今天上午有两节项目制课程！",
"太棒了，你今天没有课！去写作业或者去上课外班吧"]

day_of_week = datetime.date.today().weekday()
@bot.message_handler(commands=['class_schedule'])
def class_schedule(message):
	bot.reply_to(message, schedule[day_of_week])


#have_lunch
lunch_menu = ["不吃午饭", "地下自助餐",
"一楼清真面", "一楼套餐", "一楼卤肉饭", "一楼炒面",
"二楼拉面", "二楼炸酱面", "二楼鸡蛋西红柿面", "二楼刀削面", "二楼包子", "二楼粥", "二楼冒菜", "二楼鸡排饭", "二楼披萨"]

@bot.message_handler(commands=['have_lunch'])
def have_lunch(message):
	randNum = random.randint(0, len(lunch_menu)-1)
	if	randNum == 0:
		bot.reply_to(message, "今天中午宜" + lunch_menu[0])
	else:
		bot.reply_to(message, "今天中午宜吃" + lunch_menu[randNum])


#have_dessert
dessert_menu = ["不吃点心", "酸奶", "牛奶", "面包", "鸡肉串", "蛋挞"]

@bot.message_handler(commands=['have_dessert'])
def have_dessert(message):
	randNum = random.randint(0, len(dessert_menu)-1)
	if	randNum == 0:
		bot.reply_to(message, "今天中午宜" + dessert_menu[0])
	else:
		bot.reply_to(message, "今天中午来一个" + dessert_menu[randNum] + "吧~")


#todays_fortune
fortune_list = ["宜认真听课，会被表扬！", "宜认真听课，老师会鼓励你！", "宜认真听课，老师会看在眼里！", "宜认真听课，为自己负责！",
"宜上课睡觉，没人会发现~", "宜上课走神", "宜上课玩手机，没人会发现~", "宜上课聊天，老师视而不见", "宜上课捣乱，老师拿你没办法！嘻嘻",
"不宜上课睡觉，会被老师骂QAQ", "不宜上课玩手机，会被老师发现QAQ", "不宜上课说话，你的好友会被老师惩罚= =", "不宜上课捣乱，老师会惩罚你"]

@bot.message_handler(commands=['todays_fortune'])
def todays_fortune(message):
	randNum = random.randint(0, len(fortune_list)-1)
	bot.reply_to(message, "今天" + fortune_list[randNum])


#gaokao_countdown
@bot.message_handler(commands=['gaokao_countdown'])
def gaokao_countdown(message):
	gaokao_time = datetime.datetime(2020,6,7,0,0,0)
	current_time = datetime.datetime.now()
	dif_seconds = (gaokao_time - current_time).total_seconds()
	dif_days = int(dif_seconds//86400)
	bot.reply_to(message, "距离小熊2020年高考还有" + str(dif_days) + "天！")


#random_choose
@bot.message_handler(commands=['random'])
def random_choose(message):
	element = message.text.split()
	if len(element) == 1:
		bot.reply_to(message, "请在/random_choose后输入你想要随机获得的元素，用空格分开。例如：/random_choose 1 2")
	else:
		randNum = random.randint(1, len(element)-1)
		bot.reply_to(message, element[randNum])

bot.polling()
