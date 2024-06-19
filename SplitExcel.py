import pandas as pd
import os
import re

# 拆分Excel文件到不同的目录中，根据多列进行拆分。
# 以下脚本为根据'区'和'街道'列进行拆分。
# 拆分后的目录为：父级目录 -> 多个区文件夹 -> 多个街道文件夹，区Excel数据 -> 街道Excel数据。
# 请根据您的需求修改脚本。


# 确保已经安装了必要的库
try:
    import xlrd
except ImportError:
    print("正在安装xlrd库...")
    os.system("pip install xlrd>=2.0.1")

try:
    import openpyxl
except ImportError:
    print("正在安装openpyxl库...")
    os.system("pip install openpyxl")

# 读取Excel文件
try:
    df = pd.read_excel('/Users/imzyao/Downloads/第二批制二维码0617(4).xls', sheet_name='Sheet1')
except Exception as e:
    print(f"读取Excel文件时出错: {e}")
    exit()

# 检查数据框的列名
print(f"数据框的列名: {df.columns.tolist()}")

# 检查是否包含'区'和'街道'列
if '区' not in df.columns or '街道' not in df.columns:
    print("数据框中缺少'区'或'街道'列")
    exit()

# 获取唯一的区和街道组合
unique_combinations = df[['区', '街道']].drop_duplicates()

# 定义非法字符替换函数
def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "_", filename)

# 定义基目录
base_directory = '/Users/imzyao/Downloads/第二批二维码'  # 修改此路径为您的目标目录

# 创建基目录（如果不存在）
if not os.path.exists(base_directory):
    try:
        os.makedirs(base_directory)
    except Exception as e:
        print(f"创建基目录时出错: {e}")
        exit()

# 获取唯一的区
unique_districts = df['区'].unique()

# 遍历每个唯一区并创建相应的文件夹和区级Excel文件
for district in unique_districts:
    district_folder = sanitize_filename(str(district))
    district_path = os.path.join(base_directory, district_folder)

    print(f"处理区文件夹: {district_path}")

    # 创建区文件夹（如果不存在）
    if not os.path.exists(district_path):
        try:
            os.makedirs(district_path)
        except Exception as e:
            print(f"创建区文件夹时出错: {e}")
            continue

    # 根据当前区过滤数据
    district_df = df[df['区'] == district]

    # 将区的数据保存到区级Excel文件中
    try:
        district_df.to_excel(os.path.join(district_path, f"{district_folder}.xlsx"), index=False)
    except Exception as e:
        print(f"保存区文件时出错: {e}")

# 遍历每个唯一组合并创建相应的街道文件夹和街道Excel文件
for _, row in unique_combinations.iterrows():
    district_folder = sanitize_filename(str(row['区']))
    street_folder = sanitize_filename(str(row['街道']))
    district_path = os.path.join(base_directory, district_folder)
    street_folder_path = os.path.join(district_path, street_folder)

    print(f"处理文件夹: {street_folder_path}")

    # 创建街道文件夹（如果不存在）
    if not os.path.exists(street_folder_path):
        try:
            os.makedirs(street_folder_path)
        except Exception as e:
            print(f"创建街道文件夹时出错: {e}")
            continue

    # 根据当前的文件夹和文件名过滤数据
    filtered_df = df[(df['区'] == row['区']) & (df['街道'] == row['街道'])]

    # 将数据保存到新的街道Excel文件中
    try:
        filtered_df.to_excel(os.path.join(street_folder_path, f"{street_folder}.xlsx"), index=False)
    except Exception as e:
        print(f"保存文件时出错: {e}")
