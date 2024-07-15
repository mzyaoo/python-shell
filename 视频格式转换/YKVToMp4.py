import subprocess

def convert_ykv_to_mp4(input_file, output_file):
    # 构建FFmpeg命令
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libx264',  # 使用H.264视频编码
        '-c:a', 'aac',  # 使用AAC音频编码
        '-strict', 'experimental',  # 允许使用实验性AAC编码器
        output_file
    ]

    # 运行命令并捕获输出
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 检查命令执行是否成功
    if result.returncode == 0:
        print(f'Successfully converted {input_file} to {output_file}')
    else:
        print(f'Error converting {input_file} to {output_file}')
        print(result.stderr.decode('utf-8'))


# 示例用法
input_file = 'input.ykv'
output_file = 'output.mp4'
convert_ykv_to_mp4(input_file, output_file)
