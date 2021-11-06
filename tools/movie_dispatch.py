import os
import shutil
import settings
from rmt.media import get_media_info

movie_path = settings.get('rmt.rmt_moviepath')
movie_types = settings.get("rmt.rmt_movietype").split(",")


# 存量电影分类
def dispatch_directory(in_name):
    # 遍历文件
    print("【RMT】开始处理：", in_name)
    movie_name = in_name.split("(")[0].strip()
    movie_year = in_name.split("(")[1].replace("）", "").strip()
    # API检索出媒体信息
    org_path = os.path.join(movie_path, in_name)
    media = get_media_info(movie_name, movie_name, "电影", movie_year)
    Media_Type = media["type"]

    # 新路径
    media_path = os.path.join(movie_path, Media_Type, in_name)
    # 转移目录
    print("转移目录：" + org_path + " --> " + media_path)
    shutil.move(org_path, media_path)
    print(in_name + " 转移完成！")


print("开始处理：" + movie_path)
for movie_dir in os.listdir(movie_path):
    print("> " + movie_dir)
    if movie_dir not in movie_types and movie_dir != ".DS_Store":
        dispatch_directory(movie_dir)

