#!/bin/bash

# 创建与Excel文件同名的文件夹并且将对应Excel移动至该文件夹，
# 目录结构为: 父文件夹 -> 多个子Excel文件

# 指定包含Excel文件的目录路径
source_dir="/Users/imzyao/Downloads/军残"  # 修改为你的实际路径

# 检查目录是否存在
if [ ! -d "$source_dir" ]; then
  echo "目录不存在: $source_dir"
  exit 1
fi

# 遍历目录中的所有文件
for file in "$source_dir"/*; do
  if [[ "$file" == *.xlsx || "$file" == *.xls ]]; then
    # 获取文件名（不包含扩展名）
    file_base_name=$(basename "$file")
    file_base_name="${file_base_name%.*}"

    # 创建与文件名对应的文件夹
    new_folder_path="$source_dir/$file_base_name"
    if [ ! -d "$new_folder_path" ]; then
      mkdir "$new_folder_path"
    fi

    # 移动Excel文件到对应的文件夹中
    mv "$file" "$new_folder_path"
    echo "已将文件 $file 移动到 $new_folder_path"
  fi
done

echo "操作完成"


