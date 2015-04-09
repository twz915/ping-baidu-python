#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-04-09 13:24:50
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
# @Version : 0.0.1
from __future__ import unicode_literals

import requests

def main():
    site_title = '自强学堂'# 网站名称
    host_url = 'http://www.ziqiangxuetang.com'# 网站网址
    # 更新的文章链接
    update_url = 'http://www.ziqiangxuetang.com/django/django-queryset-api.html'
    # 网站rss地址
    rss_url = 'http://www.ziqiangxuetang.com/latest_feed/'
    
    xml = '''
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
    <methodName>weblogUpdates.extendedPing</methodName>
    <params>
        <param>
            <value><string>%s</string></value>
        </param>
        <param>
            <value><string>%s</string></value>
        </param>
        <param>
            <value><string>%s</string></value>
        </param>
        <param>
            <value><string>%s</string></value>
        </param>
    </params>
</methodCall>''' % (site_title, host_url, update_url, rss_url)
    
    xml = xml.encode('utf-8')
    headers={
      'Content-Type': 'text/xml',
      'User-Agent': 'request',
      'Content-Length': len(xml)
    }
    return requests.post('http://ping.baidu.com/ping/RPC2', data=xml, headers=headers)

if __name__ == '__main__':
    print main().content
