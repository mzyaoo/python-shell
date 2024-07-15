import os


def count_png_files(directory):
    png_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.jpg'):
                png_count += 1
    return png_count


# 输入文件夹路径
directory_path = '/Users/imzyao/Downloads/20240710确认510可印制二维码/'
png_count = count_png_files(directory_path)
print(f"Total number of PNG files: {png_count}")
