# MOVIE   
Dropboxのカメラアップロードから動画（mp４）を指定されたディレクトリへ名前を変えながらコピーする。  

## pythonのバージョン
3.10.12

## 前提条件
Ubuntu上でDropboxを使用  

## 準備
Dropbox カメラアップロードを使用  

## 設定
FROM\_DIR = '/home/*username*/Dropbox/カメラアップロード/'  
TO\_DIR = '/home/*username*/Videos/'  

## 実行権（パーミッション）の変更 
```
chmod +x movie.py
```

## 使い方
movie.py [日付] 新しい名前  
※　日付はyyyy/mm/ddの形式で、名前は日本語でもOK  
※　日付を省略した場合は今日の日付  
