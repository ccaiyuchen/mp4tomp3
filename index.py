from tkinter.tix import DirList
import os

mp4path = "data/mp4/"
# mp3 文件路径
mp3path = "data/mp3/"

dirs = os.listdir(mp4path)
for file in dirs:
    mp4FilePath = mp4path + file
    # 修改格式名 str.replace(old, new[, max])
    mp3FilePath = mp3path + file.replace(".mp4",".mp3")
    sh = './ffmpeg -i "'+mp4FilePath+'" -b:a 256K '+'"'+mp3FilePath+'"'
    os.system(sh)
    
        
# 打开mp4文件夹遍历
# 执行sh转mp3
# 保存

