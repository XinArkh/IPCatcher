import urllib.request
import urllib.parse
import json
def translate(content):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.google.com/'
    data = {}
    data['type']='AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url, data)
    html=response.read().decode('utf-8')
    target =json.loads(html)

    return target['translateResult'][0][0]['tgt']
    # print ("翻译结果是：%s" %(target['translateResult'][0][0]['tgt']))