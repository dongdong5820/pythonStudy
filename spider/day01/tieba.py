# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2019/7/5 12:04
desc: 根据用户输入的关键字爬取贴吧页面
"""
import urllib,urllib2

def loadPage(url, filename):
    """
    作用：根据url发送请求，获取服务器响应文件
    :param url: 需要爬取的url
    :param filename: 处理的文件名
    :return: string(网页html内容)
    """
    print('正在下载' + filename)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    #创建request对象
    request = urllib2.Request(url, headers = headers)
    #发送请求，并读取响应文件
    return urllib2.urlopen(request).read()

def wirtePage(html,filename):
    """
    作用：将html写入到本地文件
    :param html: 网页内容
    :param filename: 本地文件
    :return: None
    """
    print('正在保存' + filename)
    # 写入文件
    with open(filename, 'w') as f:
        f.write(html)
    print('-' * 30)

def tiebaSpider(url,beginPage,endPage):
    """
    作用：贴吧爬虫调度器，负责处理每个页面的url
    :param url: 贴吧url的前部分(不包括页码参数pn)
    :param beginPage: 起始页
    :param endPage: 终止页
    :return: None
    """
    for page in range(beginPage,endPage+1):
        pn = (page - 1) * 50
        filename = '第' + str(page) + '页.html'
        fullurl = url + '&pn=' + str(pn)
        html = loadPage(url,filename)
        wirtePage(html,filename)
    print('谢谢使用')

if __name__ == '__main__':
    kw = raw_input('请输入需要爬取的贴吧名：')
    beginPage = int(raw_input('请输入起始页：'))
    endPage = int(raw_input('请输入终止页：'))

    url = 'http://tieba.baidu.com/f?'
    # urlencode对url参数进行编码
    key = urllib.urlencode({'kw':kw})
    fullurl = url + key
    tiebaSpider(fullurl,beginPage,endPage)
