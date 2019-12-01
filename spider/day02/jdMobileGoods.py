# coding=utf-8
# /user/bin/env python

"""
author:ranlay
date:2019/12/1 17:07
desc:爬取京东手机商品数据
"""
import requests
from lxml import etree
import time
import csv
import sys

class jdMobileGoodsSpider():
    def __init__(self):
        self.filename = 'JD_Phone.csv'
        self.header = {
            'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=4&s=84&scrolling=y&log_id=1529828108.22071&tpl=3_M&show_items=7651927,7367120,7056868,7419252,6001239,5934182,4554969,3893501,7421462,6577495,26480543553,7345757,4483120,6176077,6932795,7336429,5963066,5283387,25722468892,7425622,4768461',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=58&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
        }

    def crow_first(self, n):
        """
        作用：抓取每页前30条商品信息
        :param n: 页数
        :return:
        """
        # 构造每一页的url变化
        url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page='+str(2*n-1)
        r = requests.get(url, headers = self.header)
        # 指定编码方式，不然会出现乱码
        r.encoding = 'utf-8'
        html = etree.HTML(r.text)
        # 定位到每一个商品标签li
        datas = html.xpath('//li[contains(@class, "gl-item")]')
        # 将抓取的结果保存到本地CSV文件中
        with open(self.filename, 'a', newline='', encoding='utf-8') as f:
            write = csv.writer(f)
            for data in datas:
                p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em')
                p_link = data.xpath('div/div[@class="p-name p-name-type-2"]/a/@href')
                p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
                p_comment = data.xpath('div/div[5]/strong/a/text()')
                # 这个if判断用来处理那些价格可以动态切换的商品，他们的价格位置在属性中放了一个最低价
                if len(p_price) == 0:
                    p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
                write.writerow([p_name[0].xpath('string(.)'), p_link[0], p_price[0], p_comment[0]])
        f.close()

    def crow_last(self):
        pass

    def start_work(self):
        for i in range(1,3):
            print('***********')
            try:
                print('  First page:  ' + str(i))
                self.crow_first(i)
                sys.exit()
            except Exception as e:
                print(e)

        print('谢谢使用！')

if __name__ == '__main__':
    spider = jdMobileGoodsSpider()
    spider.start_work()
