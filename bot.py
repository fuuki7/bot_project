import random
import datetime
from mutagen.mp3 import MP3 as mp3
import pygame
import time
import win32com.client as wincl
import urllib3
from bs4 import BeautifulSoup

voice = wincl.Dispatch("SAPI.SpVoice")
times = datetime.datetime.now()
ai = "ジャービス＞＞"
ti = times.hour
hen = ["どうかしましたか？" , "大丈夫ですか？" , "何か仕事はありますか？"]
l = ["大吉","中吉","小吉","吉","末吉","凶","大凶"]
s = "きっといいことがあるでしょう"
x = "運勢など気にせず頑張ってください"
z ={"大吉": s ,"中吉": s ,"小吉": s ,"吉": s ,"末吉": s ,"凶": x ,"大凶": x}
eotw = ["Dropout Boulevard.mp3" , "Bad Day.mp3" , "Fangs.mp3" , "Forever.mp3" , "Gone.mp3" , "My Sleeping Beauty.mp3" , "Hollow.mp3" , "Over.mp3" , "Rollerskates.mp3" , "Stargazer.mp3"]
url = 'https://weather.yahoo.co.jp/weather/jp/8/4010.html'
http = urllib3.PoolManager()
instance = http.request('GET', url)
soup = BeautifulSoup(instance.data, 'html.parser')

def tenki_today():
    tenki_today = soup.select_one('#main > div.forecastCity > table > tr > td > div > p.pict')
    print(ai + "今日の天気は"+tenki_today.text + "です")
    voice.Speak("今日の天気は"+tenki_today.text + "です")

def tenki_tomorrow():
    tenki_tomorrow = soup.select_one('#main > div.forecastCity > table > tr > td + td > div > p.pict')
    print(ai + "明日の天気は"+tenki_tomorrow.text + "です")
    voice.Speak("明日の天気は"+tenki_tomorrow.text + "です")

def tim():
    print(ai + "今の時間は" + str(times.hour) + "時" + str(times.minute) + "分です")
    voice.Speak("今の時間は" + str(times.hour) + "時" + str(times.minute) + "分です")

def year():
    print(ai + "今日は" + str(times.month) + "月" + str(times.day) + "日です")
    voice.Speak("今日は" + str(times.month) + "月" + str(times.day) + "日です")

def omi():
    a = random.randint(0,6)
    v = l[a]
    print(ai + "今日の" + names + "の運勢は" + v + "です\n" + ai + z[v])
    voice.Speak("今日の" + names + "の運勢は" + v + "です\n" + z[v])

def jan():
    ff = "じゃんけん終了"
    print(ai + "じゃんけん大会スタートです")
    voice.Speak("じゃんけん大会スタートです")
    print(ai + "番号を入力してください")
    voice.Speak("番号を入力してください")
    print("[1.グー　2.チョキ　3.パー]")
    ja = input("番号:")
    jb = int(ja)
    jc = random.randint(1,3)
    if jb==1:
        if jc==1:
            print(ai + "グー　　\n" + ai + "あいこです")
            voice.Speak("あいこです")
            print(ff)
        elif jc==2:
            print(ai + "チョキ \n" + ai + name + "の勝ちです")
            voice.Speak( name + "の勝ちです")
            print(ff)
        else:
            print(ai + "パー \n" + ai + "私の勝ちです")
            voice.Speak("私の勝ちです")
            print(ff)
    elif jb==2:
        if jc==1:
            print(ai + "グー\n" + ai + "私の勝ちです")
            voice.Speak("私の勝ちです")
            print(ff)
        elif jc==2:
            print(ai + "チョキ \n" + ai + "あいこです")
            voice.Speak("あいこです")
            print(ff)
        else:
            print(ai + "パー \n" + ai + name + "の勝ちです")
            voice.Speak( name + "の勝ちです")
            print(ff)
    elif jb==3:
        if jc==1:
            print(ai + "グー \n" + ai + name + "の勝ちです")
            voice.Speak( name + "の勝ちです")
            print(ff)
        elif jc==2:
            print(ai + "チョキ \n" + ai + "私の勝ちです")
            voice.Speak("私の勝ちです")
            print(ff)
        else:
            print(ai + "パー \n" + ai + "あいこです")
            voice.Speak("あいこです")
            print(ff)
    else:
        print(ai + "1から3の整数を選んでください")
        voice.Speak("1から3の整数を選んでください")
        print(ff)

def music(ongaku):
    filename = ongaku
    pygame.mixer.init()
    pygame.mixer.music.load(filename) 
    mp3_length = mp3(filename).info.length 
    pygame.mixer.music.play(1) 
    time.sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

print("会話開始")

if ti <= 9:
    print(ai + "おはようございます")
    voice.Speak("おはようございます")
elif ti >9 and ti < 19:
    print(ai + "こんにちわ")
    voice.Speak("こんにちわ")
else:
    print(ai + "こんばんわ")
    voice.Speak("こんばんわ")

print("ジャービス＞＞私はジャービス\nジャービス＞＞あなたの生活のサポートをさせていただきます")
voice.Speak("私はジャービス、あなたの生活のサポートをさせていただきます")
print(ai +  'あなたのお名前を教えてください')
voice.Speak("あなたのお名前を教えてください")
name = input("名前＞ ")
names = name + '様'
print(ai + names + "ですね。よろしくお願いします。")
voice.Speak( names + "ですね。よろしくお願いします。")
pro = name + ">"


def h():
    cunt = 0
    while 1:
        an = input(pro)
        if an == "こんにちわ" or an == "おはようございます" or an == "こんばんわ":
            print(ai + an + "!")
            voice.Speak(an)

        elif an == "ばいばい" or an == "さよなら":
            if ti >= 19:
                print(ai + "また何かあれば呼んでください\n" + ai + "おやすみなさい" )
                voice.Speak( "また何かあれば呼んでください、おやすみなさい" )
                break
            else:
                print(ai + "さようなら\n" + ai + "また何かあれば呼んでください")
                voice.Speak("さようなら、また何かあれば呼んでください")
                break

        elif not an:
            aw = random.randint(0,2)
            print(ai + hen[aw])
            voice.Speak(hen[aw])
            cunt += 1
            print("無視回数" + str(cunt))
            
            if cunt == 8:
                print(ai + "また用があるときに呼んでください")
                voice.Speak("また用があるときに呼んでください")
                break

        elif an == "おみくじ":
            omi()
        
        elif an == "今の時間は？":
            tim()

        elif an == "今日の日付は？":
            year()

        elif an == "じゃんけんしよ":
            jan()
            print(ai + "もう一度やりますか？？")
            voice.Speak("もう一度やりますか？？")
            dd = input("はい、いいえ＞")
            while dd == "はい":
                jan()
                print(ai + "もう一度やりますか？？")
                voice.Speak("もう一度やりますか？？")
                dd = input("はい、いいえ＞")
        
        elif an == "音楽かけて":
            m = random.randint(0,9)   
            print(eotw[m])
            music(eotw[m])

        elif an == "今日の天気教えて":
            tenki_today()

        elif an == "明日の天気教えて":
            tenki_tomorrow()

        else:
            print(ai + "{}なんですね".format(an))
            voice.Speak("{}なんですね".format(an))

h()

print("終了")