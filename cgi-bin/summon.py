#!/usr/bin/env python3
 
import random
import os
import sys

# HTMLヘッダ -------------------------------------
HTML_Head = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>summon</title>
    <link rel="stylesheet" href="../css/summon.css?v=2">
</head>
"""
 
# HTMLボディ -------------------------------------
HTML_Body = """


<body>
   
    <div class="headerbg">
        <p><img src="../img/headerbg2.png" alt=""></p>
    </div>
   
   
    <h1>
        <div class="logo">
            <ul>
                <li><a href="../index.html"><img src="../img/logo.svg"></a></li>
            </ul>
        </div>
    </h1>
    
"""


# ランダム設定 -------------------------------------
RandNum = random.randint(1,50)      # 1～50までのランダム値を取得（ファイル名の1～50になる）
RandStr = str(RandNum)              # 取得した数値を文字へ変換
FileName = RandStr + ".mp4"         # 1～50の文字と.mp4を結合してファイル名にする
# HTMLに組み込む
HTML_File = "<form action=\"\">\n <video autoplay muted>\n <source src=\"../vid/" + FileName + "\" type=\"video/mp4\">\n </video> </form>"
 
# 例）↑のHTML_File変数への代入、ややこしいですよね。
#     Pythonでは、以下の様な書き方も出来ます。こちらの方が楽かな。
#HTML_File = f"""
#<form action="">
#    <video autoplay muted>
#        <source src="../vid/{FileName}" type="video/mp4">
#     </video>
# </form>
# """

file = "summon_num.txt"
ret = os.path.isfile(file)
stream = open(file, "w")
stream.write(RandStr)
stream.close()




# HTMLその下 -------------------------------------
HTML_Foot = """

<div class="lineup">
    <ul>
        <li><a href="../lineup.html"><img src="../img/lineup.png"></a></li>
    </ul>
</div>


      <div class="button">
        <nav>
            <ul>
               
                <li><a href="../index.html"><img src="../img/modoru.png" alt=""></a></li>
                <li><a href="qr.py"><img src="../img/hozon.png" alt=""></a></li>
               
            </ul>
        </nav>
      </div>

   
    <footer><p><img src="../img/footerbg.png" alt=""></p></footer>
 
</body>
</html>
"""
 
# 画面出力 ------------------------------------------
print( HTML_Head )
print( HTML_Body )
print( HTML_File)
print( HTML_Foot )
 
