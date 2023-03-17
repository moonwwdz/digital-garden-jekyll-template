import os
from datetime import datetime

# 定义目录路径
dir_path = '/root/obsidian-web/_notes/2 闪念笔记/日记'

files = os.listdir(dir_path)

# 获取所有有数据的月份
months_dict = {}
for file in files:
    if not file.endswith('.md'):  # 排除非markdown格式的文件
        continue
    date_str = file.split('.')[0][:7]  # 提取年月部分字符串
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m')  # 转换为datetime对象
        month_str = date_obj.strftime('%Y-%m')
        if month_str not in months_dict:
            months_dict[month_str] = []
        months_dict[month_str].append(file)
    except ValueError:
        pass

# 按月份分组生成表格内容
table_str = ''
for month_str, file_list in sorted(months_dict.items(), reverse=True):
    table_str += f'\n## {month_str}\n\n'
    table_str += '|周一|周二|周三|周四|周五|周六|周日|\n'
    table_str += '|---|---|---|---|---|---|---|\n'

    first_day = datetime.strptime(f'{month_str}-01', '%Y-%m-%d')
    weekday_offset = first_day.weekday()

    days_in_month = 1
    for i in range(6):  # 最多只会有6行
        row_str = '|'
        for j in range(7):
            if i == 0 and j < weekday_offset:
                row_str += '   |'
            elif days_in_month > 31:  # 最多31天
                row_str += '   |'
            else:
                day_str = f'{days_in_month:02d}'
                if any(day_str in x[-5:] for x in file_list):
                    link_str = f'[{day_str}]({month_str}-{day_str})'
                    row_str += f'**{link_str}**|'
                else:
                    row_str += f'{day_str} |'
                days_in_month += 1
        table_str += row_str + '\n'

# 写入markdown文件
with open('/root/obsidian-web/_notes/2 闪念笔记/日记/日记日历.md', 'w+') as f:
    f.write(table_str)
