# MOVIE   
Dropboxのカメラアップロードから動画（mp４）を指定されたディレクトリへ名前を変えながらコピーする。  

## pythonのバージョン
3.10.12

## 前提条件
Ubuntu上でDropboxを使用  

## 準備
Dropbox カメラアップロードを使用してください  

## インストール
GitHubからクローン  
```
git clone git@github.com:ariichi88/movie.git
```
movie.pyをパスの等っている場所にコピー 
```
cp movie.py /hoge/fuga
```
FROM\_DIRとTO\_DIRの設定  
エディタでmovie.pyを開きFROM\_DIRとTO\_DIRを設定する  

実行権（パーミッション）の変更 
```
chmod +x movie.py
```

## FROM\_DIRとTO\_DIRの設定例
FROM\_DIR = '/home/*username*/Dropbox/カメラアップロード/'  
TO\_DIR = '/home/*username*/Videos/'  

## 使い方
movie.py [日付] 新しい名前  
※　日付はyyyy/mm/ddの形式で、名前は日本語でもOKです。  
※　日付を省略した場合は今日の日付になります。  

## 最後に
Ubuntuを使用していてDropboxを使用している人しか関係しませんが良ければ使ってみてください。  
