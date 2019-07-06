# coding=utf-8
# /usr/bin/env python

"""
Author: ranlaysu
date: 2019/7/5 15:34
desc: 通过手动添加cookie，访问需要登录后的页面
"""
import urllib2

url = 'https://user.gearbest.com/index#/favor/goods'
headers = {
	"Accept":"application/json, text/javascript, */*; q=0.01",
	"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
	"X-Requested-With":"XMLHttpRequest",
	"cookie":"AKAM_CLIENTID=5ec830797d8c75a5d4380f35c66ba962; gb_lang=en; gb_pipeline=GB; cdnname=https://css.gbtcdn.com/imagecache/gbw; cdn_countryCode=HK; gb_countryCode=HK; _gcl_au=1.1.575805458.1562311943; ORIGINDC=1; _ga=GA1.2.115428476.1562311944; _gid=GA1.2.973706503.1562311944; gb_currencyCode=USD; _dc_gtm_UA-48073707-1=1; _fbp=fb.1.1562311944618.2082063589; WEBF_guid=5ec830797d8c75a5d4380f35c66ba962_1562311944;od=nsoqwmcawydg1562311945001; osr_referrer=originalurl; osr_landing=https%3A%2F%2Fwww.gearbest.com%2F; gb_vid=aafcee98-2c03-a964-b749-d6bc6e250cfa; gb2019_gb_sid=605b715e-1d60-a02a-9c33-1c8a815e63bc; gb_fcm=1; gb_fcmPipeLine=GB; gb_vsign=786c2cefec84e7287b1729fe0a7c18983b13cc20; gb_guid=721511363; WEBF-email=suchangdong%40globalegrow.com; WEBF-email-sign=de571b96e68487ab1b16c26f779cc8d1; WEBF-email-sign-expire=1562322770; guid=14931190; gb_userinfo=eyJ1c2VyIjp7InVzZXJOYW1lIjoicmFubGF5c3UiLCJlbWFpbCI6InN1Y2hhbmdkb25nQGdsb2JhbGVncm93LmNvbSIsImF2YXRhciI6InVwbG9hZFwvZ2VhcmJlc3RcL2F2YXRhclwvMjAxODA4MTRcLzYwRjM3MUFDQjZCMUQ4N0NGQ0U1MTNGN0I2NDUxN0Y0LnBuZyIsImlzTmV3VXNlciI6MH0sImNvbGxlY3QiOjMsImNhcnRDb3VudCI6MTAsImlzTG9naW4iOnRydWUsInRpY2tldENvdW50IjowLCJzaXRlTWVzc2FnZVRpbWVJbnRlcnZhbCI6MH0%3D; gb_fcmtoken=c2o1h1FrUl0:APA91bE7JM008V_UvosjxDU4-93QLlKAxP_LktiAhozzzyztZEzNqYlKO8jEmrNVcAXkE45qaBzIgV9F2pFJs0KkyKxbH4_IfRZkEi9h2M7SQgmZrdKGhX9wqsKdEe7fwzRUN7sRE940; WEBF_predate=1562311972; landingUrl=https://www.gearbest.com/; gb_pf=%7B%22rp%22%3A%22originalurl%22%2C%22lp%22%3A%22https%3A%2F%2Fwww.gearbest.com%2F%22%2C%22wt%22%3A1562311972830%7D; gb_soa_www_session=eyJpdiI6IkJZT0lsaUpTcEdmWTM4dWhSdVR1blE9PSIsInZhbHVlIjoiZjNhbmpORElSYUZoeHB6bmZKM3NzN3R3NGZjMnVCa29cL1wvVzVuNW9ENTdJaHlUZTJsR3orYVVwWm05R0lPam5tenJiMG52eEVZSmhjZWhQUzZ6SDJzZz09IiwibWFjIjoiZGU5YjNhNjQ0MDM0M2JhMGFmNDI3ZDBhOGNiNzJhZDI1OWUzY2E1MzU2MTAzNGU4NDgwMGJmZGUxOThlNDI2ZCJ9; gb2019_gb_sid_605b715e-1d60-a02a-9c33-1c8a815e63bc=false"
}
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request).read()
# 没有cookie时，返回 {"status":1,"msg":"fail","data":{"redirectUrl":"https:\/\/login.gearbest.com\/m-users-a-sign.htm?ref=&type=1"}}
print(response)
