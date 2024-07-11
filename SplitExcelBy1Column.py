import pandas as pd
import os

# 读取 Excel 文件并指定工作表
file_path = '/Users/imzyao/Downloads/20240710确认510可印制二维码.xls'  # 或者 'your_excel_file.xls'
# 替换为你要拆分的工作表名称
sheet_name = '无需核实-可印刷（510）'
# 指定生成的文件夹目录
target_directory = '/Users/imzyao/Downloads/20240710确认510可印制二维码'

# 根据文件扩展名选择引擎
if file_path.endswith('.xls'):
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='xlrd', dtype=str)
elif file_path.endswith('.xlsx'):
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl', dtype=str)
else:
    raise ValueError("Unsupported file format. Please use .xls or .xlsx files.")

# 获取唯一的区名称
districts = df['区'].unique()

# 创建对应的区文件夹并保存拆分的 Excel 文件
for district in districts:
    # 筛选出当前区的数据
    df_district = df[df['区'] == district]

    # 创建区的文件夹路径
    district_folder_path = os.path.join(target_directory, district)

    # 创建文件夹
    if not os.path.exists(district_folder_path):
        os.makedirs(district_folder_path)

    # 保存 Excel 文件
    district_file_path = os.path.join(district_folder_path, f'{district}.xlsx')
    df_district.to_excel(district_file_path, index=False)

print("拆分完成")