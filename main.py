import pandas as pd

# 创建日期范围
start_date = '2023-06-01'
end_date = '2024-05-31'
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# 创建日历DataFrame
calendar = pd.DataFrame({'日期': dates})

# 提取年、月、日信息
calendar['年份'] = calendar['日期'].dt.year
calendar['月份'] = calendar['日期'].dt.month
calendar['日'] = calendar['日期'].dt.day

# 格式化日期字符串
calendar['日期'] = calendar['日期'].dt.strftime('%Y-%m-%d')

# 导出为Excel文件
calendar.to_excel('calendar.xlsx', index=False)
