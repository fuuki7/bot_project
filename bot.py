import random
import datetime

time = datetime.datetime.now()
ai = "アイ＞＞"

def tim():
    print(ai + "今の時間は" + str(time.hour) + "時" + str(time.minute) + "分だよ")

def year():
    print(ai + "今日は" + str(time.month) + "月" + str(time.day) + "日だよ")

ti = time.hour

hen = ["どうかした？" , "おーい" , "なんか話してよー"]
l = ["大吉","中吉","小吉","吉","末吉","凶","大凶"]
s = "きっといいことあるよ！！"
x = "運勢なんて気にせず頑張ろう！！"
z ={"大吉": s ,"中吉": s ,"小吉": s ,"吉": s ,"末吉":"いいことあるといいね！！","凶": x ,"大凶": x}

def omi():
    a = random.randint(0,6)
    v = l[a]
    print(ai + "今日のあなたの運勢は" + v + "だよ!\n" + ai + z[v])

print("会話開始")

if ti <= 9:
    print(ai + "おはよう！")
elif ti >9 and ti < 19:
    print(ai + "こんにちわ！")
else:
    print(ai + "こんばんわ！")

print("アイ＞＞私はアイ\nアイ＞＞君のお名前は？")
name = input("名前＞ ")
print(name + "っていうんだ、よろしくね！")
pro = name + ">"

def h():
    while 1:
        an = input(pro)
        if an == "こんにちわ" or an == "おはよう" or an == "こんばんわ":
            print(ai + an + "!")

        elif an == "ばいばい" or an == "さよなら":
            if ti >= 19:
                print(ai + "またお話ししようね！\n" + ai + "おやすみ！" )
                break
            else:
                print(ai + "ばいばい！\n" + ai + "またお話ししようね！")
                break

        elif not an:
            aw = random.randint(0,2)
            print(ai + hen[aw])

        elif an == "おみくじ":
            omi()
        
        elif an == "今の時間は？":
            tim()

        elif an == "今日の日付は？":
            year()

        else:
            print(ai + "{}、なんだね！".format(an))

h()

print("終了")