import httpx
from time import sleep
import configparser
import os
from random import random
import colorama

os.system("clear")

colorama.init(autoreset=True)
colorama.init(wrap=True)

cf = configparser.ConfigParser()

cookie = ""
path = ""

try:
    cf.read("settings.ini", encoding='utf-8')
    path = cf.get("default", "path")
    cookie = cf.get("default", "cookie")
except:
    print(colorama.Style.BRIGHT + colorama.Fore.RED + "settings.ini不存在或已损坏！\n")
    print(colorama.Style.BRIGHT + colorama.Fore.YELLOW + "配置文件格式如下：\n\n" \
                                                         "[default]\n" \
                                                         "#下载文件夹,路径结尾为\\\n" \
                                                         "path=.\Py\\\n" \
                                                         "#cookie,开头为jiagong=***,不含ruot=***\n" \
                                                         "cookie=")
    os.system("pause")
    os.system("exit")

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': cookie,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Referer': '▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇'
}

greetings = "\n欢迎使用「数据删除」开发的「▇▇▇▇▇▇▇▇▇▇▇」。" \
            "\n本软件仅供学习使用，下载后请于24h之内删除。\n"

warnings = "注：大量请求会使得ip暂时性遭到▇▇▇▇▇▇▇▇▇▇▇▇▇▇封禁，重新拨号获取ip即可。\n"

rush = "行くぞ！\n"

print(colorama.Style.BRIGHT + colorama.Fore.YELLOW + greetings)
print(colorama.Style.BRIGHT + colorama.Fore.RED + warnings)
print(colorama.Style.BRIGHT + colorama.Fore.CYAN + rush)

print(colorama.Style.BRIGHT + colorama.Fore.GREEN + f"path设置为：{path}")
if not cookie:
    print(colorama.Style.BRIGHT + colorama.Fore.YELLOW + "配置文件内未检测到cookie，请稍后手动输入！\n")
else:
    print(colorama.Style.BRIGHT + colorama.Fore.GREEN + f"cookie设置为：{cookie}\n")

url_front = input(colorama.Style.BRIGHT + colorama.Fore.CYAN + "请输入要下载的▇▇▇▇▇▇源地址，\n"
                                                               "开头为▇▇▇▇▇▇▇▇▇，结尾为/ ：\n")

if not cookie:
    cookie = input(colorama.Style.BRIGHT + colorama.Fore.CYAN + "请输入cookie，开头为▇▇▇▇▇▇▇：\n")
else:
    cookie_new = input(
        colorama.Style.BRIGHT + colorama.Fore.CYAN + f"是否更新cookie？若不更新则按回车，默认使用文件内配置：cookie={cookie}\n")
    if cookie_new:
        cookie = cookie_new
        print(colorama.Style.BRIGHT + colorama.Fore.GREEN + f"cookie设置为：{cookie}\n")

start_page = int(input(colorama.Style.BRIGHT + colorama.Fore.CYAN + "请输入开始页码："))
final_page = int(input(colorama.Style.BRIGHT + colorama.Fore.CYAN + "请输入结束页码："))

'''
try:
    print(url_front + str(start_page).zfill(6) + '.jpg?zoom=0')
    for i in range(start_page, final_page + 1):
        page = str(i).zfill(6)

        url = url_front + page + '.jpg?zoom=0'
        res = httpx.get(url, headers=headers, follow_redirects=True)

        with open(path + 'p' + str(i) + '.jpg', 'wb') as outfile:
            outfile.write(res.content)
            print(colorama.Style.BRIGHT + colorama.Fore.GREEN + str(i) + "\t...... 完成！")

        if os.stat(path + 'p' + str(i) + '.jpg').st_size == 0:
            print(colorama.Style.BRIGHT + colorama.Fore.RED + "已到达IP访问阈值。IP可能被限制。")
            break

        s = random()
        if s == 1:
            s = 0.5
        s = 1 / (1 - s)
        if s > 3:
            s = 3.2
        s = s + random() - 0.7
        if i != final_page:
            sleep(s)

except Exception as e:
    print("错误啦！\n" + str(e))

os.system("pause")
'''

try:
    # print(url_front + str(start_page).zfill(6) + '.jpg?zoom=0')
    with httpx.Client() as c:

        c.headers.update(headers=headers)

        for i in range(start_page, final_page + 1):
            page = str(i).zfill(6)

            url = url_front + page + '.jpg?zoom=0'
            res = c.get(url, follow_redirects=True)

            with open(path + 'p' + str(i) + '.jpg', 'wb') as outfile:
                outfile.write(res.content)
                print(colorama.Style.BRIGHT + colorama.Fore.GREEN + str(i) + "\t...... 完成！")

            if os.stat(path + 'p' + str(i) + '.jpg').st_size == 0:
                print(colorama.Style.BRIGHT + colorama.Fore.RED + "已到达IP访问阈值。IP可能被限制。")
                os.remove(path + 'p' + str(i) + '.jpg')
                break

            s = random()
            if s == 1:
                s = 0.5
            s = 1 / (1 - s)
            if s > 3:
                s = 3.2
            s = s + random() - 0.7
            if i != final_page:
                sleep(s)

except Exception as e:
    print("错误啦！\n" + str(e))

os.system("pause")
