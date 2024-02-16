import requests
from bs4 import BeautifulSoup

# 目标网页URL
url = 'http://www.baidu.com/'


# 发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.ok:
    # 让requests库自动猜测编码
    response.encoding = response.apparent_encoding
    
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 提取网页的标题
    title = soup.find('title').get_text()

    print('网页标题:', title)
else:
    print('请求失败，状态码:', response.status_code)