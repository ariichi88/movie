# MOVIE   
Dropboxのカメラアップロードから動画（mp４）を指定されたディレクトリへ名前を変えながらコピー  

## pythonのバージョン
3.10.12

## 準備
Dropboxでカメラアップロードを使用しスマホで動画を自動でアップロードするように設定しておく。  

## 設定
FROM\_DIR = '/home/*username*/Dropbox/カメラアップロード/'  
TO\_DIR = '/home/*username*/Videos/'  

## 使い方
movie.py [日付] 新しい名前  
※　日付はyyyy/mm/ddの形式で、名前は日本語でもOK  
※　日付を省略した場合は今日の日付  
