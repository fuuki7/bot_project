import random
import datetime
from mutagen.mp3 import MP3 as mp3
import pygame
import time
import win32com.client as wincl
voice = wincl.Dispatch("SAPI.SpVoice")

times = datetime.datetime.now()
ai = "アイ＞＞"

def tim():
    print(ai + "今の時間は" + str(times.hour) + "時" + str(times.minute) + "分だよ")
    voice.Speak("今の時間は" + str(times.hour) + "時" + str(times.minute) + "分だよ")

def year():
    print(ai + "今日は" + str(times.month) + "月" + str(times.day) + "日だよ")
    voice.Speak("今日は" + str(times.month) + "月" + str(times.day) + "日だよ")

ti = times.hour

hen = ["どうかした？" , "おーい" , "なんか話してよー"]
l = ["大吉","中吉","小吉","吉","末吉","凶","大凶"]
s = "きっといいことあるよ！！"
x = "運勢なんて気にせず頑張ろう！！"
z ={"大吉": s ,"中吉": s ,"小吉": s ,"吉": s ,"末吉":"いいことあるといいね！！","凶": x ,"大凶": x}

def omi():
    a = random.randint(0,6)
    v = l[a]
    print(ai + "今日のあなたの運勢は" + v + "だよ!\n" + ai + z[v])
    voice.Speak("今日のあなたの運勢は" + v + "だよ!\n" + z[v])

def jan():
    ff = "じゃんけん終了"
    print(ai + "じゃんけん大会スタート！")
    voice.Speak("じゃんけん大会スタート！")
    print(ai + "番号を入力してね")
    voice.Speak("番号を入力してね")
    print("[1.グー　2.チョキ　3.パー]")
    ja = input("番号:")
    jb = int(ja)
    jc = random.randint(1,3)
    if jb==1:
        if jc==1:
            print(ai + "グー　　\n" + ai + "あいこだよ")
            voice.Speak("あいこだよ")
            print(ff)
        elif jc==2:
            print(ai + "チョキ \n" + ai + name + "の勝ちだよ")
            voice.Speak( name + "の勝ちだよ")
            print(ff)
        else:
            print(ai + "パー \n" + ai + "私の勝ちだよ！")
            voice.Speak("私の勝ちだよ！")
            print(ff)
    elif jb==2:
        if jc==1:
            print(ai + "グー\n" + ai + "私の勝ちだよ！")
            voice.Speak("私の勝ちだよ！")
            print(ff)
        elif jc==2:
            print(ai + "チョキ \n" + ai + "あいこだよ")
            voice.Speak("あいこだよ")
            print(ff)
        else:
            print(ai + "パー \n" + ai + name + "の勝ちだよ")
            voice.Speak( name + "の勝ちだよ")
            print(ff)
    elif jb==3:
        if jc==1:
            print(ai + "グー \n" + ai + name + "の勝ちだよ")
            voice.Speak( name + "の勝ちだよ")
            print(ff)
        elif jc==2:
            print(ai + "チョキ \n" + ai + "私の勝ちだよ！")
            voice.Speak("私の勝ちだよ！")
            print(ff)
        else:
            print(ai + "パー \n" + ai + "あいこだよ")
            voice.Speak("あいこだよ")
            print(ff)
    else:
        print(ai + "1から3の整数を選んでね")
        voice.Speak("1から3の整数を選んでね")
        print(ff)


eotw = ["Dropout Boulevard.mp3" , "Bad Day.mp3" , "Fangs.mp3" , "Forever.mp3" , "Gone.mp3" , "My Sleeping Beauty.mp3" , "Hollow.mp3" , "Over.mp3" , "Rollerskates.mp3" , "Stargazer.mp3"]

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
    print(ai + "おはよう！")
    voice.Speak("おはよう")
elif ti >9 and ti < 19:
    print(ai + "こんにちわ！")
    voice.Speak("こんにちわ")
else:
    print(ai + "こんばんわ！")
    voice.Speak("こんばんわ")

print("アイ＞＞私はアイ\nアイ＞＞君のお名前は？")
voice.Speak("私はアイ、君のお名前は？")
name = input("名前＞ ")
print(ai + name + "っていうんだ、よろしくね！")
voice.Speak( name + "っていうんだ、よろしくね！")
pro = name + ">"


def h():
    cunt = 0
    while 1:
        an = input(pro)
        if an == "こんにちわ" or an == "おはよう" or an == "こんばんわ":
            print(ai + an + "!")
            voice.Speak(an)

        elif an == "ばいばい" or an == "さよなら":
            if ti >= 19:
                print(ai + "またお話ししようね！\n" + ai + "おやすみ！" )
                voice.Speak( "またお話ししようね！おやすみ！" )
                break
            else:
                print(ai + "ばいばい！\n" + ai + "またお話ししようね！")
                voice.Speak("ばいばい！またお話ししようね！")
                break

        elif not an:
            aw = random.randint(0,2)
            print(ai + hen[aw])
            voice.Speak(hen[aw])
            cunt += 1
            print("無視回数" + str(cunt))
            
            if cunt == 8:
                print(ai + "もう行くね")
                voice.Speak("もう行くね")
                break

        elif an == "おみくじ":
            omi()
        
        elif an == "今の時間は？":
            tim()

        elif an == "今日の日付は？":
            year()

        elif an == "じゃんけんしよ":
            jan()
            print(ai + "もう一回やる？")
            voice.Speak("もう一回やる？")
            dd = input("はい、いいえ＞")
            while dd == "はい":
                jan()
                print(ai + "もう一回やる？")
                voice.Speak("もう一回やる？")
                dd = input("はい、いいえ＞")
        
        elif an == "音楽かけて":
            m = random.randint(0,9)   
            print(eotw[m])
            music(eotw[m])

        else:
            print(ai + "{}なんだね！".format(an))
            voice.Speak("{}なんだね！".format(an))

h()

print("終了")