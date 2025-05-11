#!/usr/bin/env python3
 
import os
import sys

# HTMLヘッダ -------------------------------------
HTML_Head = """
<!DOCTYPE html>
<html lang="jp">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>シナモロール</title>
    <link rel="stylesheet" href="../css/qr.css">
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
                <li><a href="../home.html"><img src="../img/logo.svg"></a></li>
            </ul>
        </div>
    </h1>
"""
#  --------------------------------------------------------
file = "summon_num.txt"

ret = os.path.isfile(file)
stream = open(file, "r")
qr_number = stream.readline() + ".png"
stream.close()
HTML_File =  "<div class = \"qr\"><p>\n <img src=\"../qr/" + qr_number + "\">\n </p></div>"

# ---------------------------------------------------------
HTML_Foot = """


    <div class="button">
        <ul>
            <li><a href="../home.html"><img src="../img/home_modoru.png" alt=""></a></li>
        </ul>
    </div>

    <div class="lineup">
        <ul>
            <li><a href="../lineup.html"><img src="../img/lineup.png"></a></li>
        </ul>
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