#!/bin/bash

# 创建与Excel文件同名的文件夹并且将对应Excel移动至该文件夹，
# 目录结构为: 父文件夹 -> 多个子文件夹 -> 多个子Excel文件

 # 指定包含区文件夹的北京文件夹路径
 root_dir="/Users/imzyao/Downloads/第二批二维码/"  # 修改为你的实际路径

 # 检查根目录是否存在
 if [ ! -d "$root_dir" ]; then
   echo "根目录不存在: $root_dir"
   exit 1
 fi

 # 遍历北京文件夹中的所有区文件夹
 for district_dir in "$root_dir"/*; do
   if [ -d "$district_dir" ]; then
     # 遍历区文件夹中的所有Excel文件
     for file in "$district_dir"/*; do
       if [[ "$file" == *.xlsx || "$file" == *.xls ]]; then
         # 获取文件名（不包含扩展名）
         file_base_name=$(basename "$file")
         file_base_name="${file_base_name%.*}"

         # 创建与文件名对应的文件夹
         new_folder_path="$district_dir/$file_base_name"
         if [ ! -d "$new_folder_path" ]; then
           mkdir "$new_folder_path"
         fi

         # 移动Excel文件到对应的文件夹中
         mv "$file" "$new_folder_path"
         echo "已将文件 $file 移动到 $new_folder_path"
       fi
     done
   fi
 done

 echo "操作完成"
