urls = ['https://www.aiden-net.co.jp/,http://www.koshinmilk.co.jp,https://www.ushio.co.jp/jp/,https://www.sumitomocorp.com/ja/jp,https://www.mitsui.com/jp/ja/index.html,http://www.sms.co.jp,http://www.nihon-shuji.or.jp/,https://www.shigapatent.com/jp/aboutus/ourfirm/,https://www.nisitokyobus.co.jp/,https://www.lapis-semi.com/,https://www.asahiseiko.com/,http://www.itochu-metals.co.jp,https://www.enoteca.co.jp/,https://www.okamotoya.com/,https://www.komatsu.jp/ja,http://www.sakainet.co.jp,http://www.shikizai.com,https://www.polyplastics.com/,https://www.ana.co.jp/,https://www.hakuju.co.jp/,http://www.itc-ps.co.jp/index.html,https://www.conexio.co.jp,https://www.taito.co.jp/,https://www.gracecontinental.com/,https://www.u-tokai.ac.jp/,https://www.bdo.or.jp/en-gb/home-en,https://www.val.co.jp/,https://www.jskk.co.jp/,https://www.tein.co.jp/e/index.html,https://www.shukoh.co.jp/,https://www.sonyengineering.co.jp/redirect.html,https://www.umc.co.jp/?ml_lang=en,http://www.junseikai.org/,http://www.funabashikousan.com/redirect.html,https://www.aeoncom.co.jp/,https://greenbox722.co.jp/,https://coopkyosai.coop/,https://www.joyosuisan.com/,https://www.hirosawaseiki.co.jp/index.htm,https://www.ichihara-hospital.or.jp/,https://www.icc.ac.jp/,http://www.katsu-p.com/top.html,https://kito.com/,http://www.sj-nagano.jp/,https://www.takashima.co.jp/,https://www.tana-x.co.jp/,https://onozo.co.jp/en/,https://www.hanshin-dw.co.jp/,http://www.enyuukai.jp,https://www.gifu-shinoda.co.jp/en/,https://buhin.nissan.co.jp/hokuriku/,http://www.takamatsu-p.jp/,https://buhin.nissan.co.jp/sanyo/,http://matsumoto-jukogyo.co.jp/,https://www.tosoh-finechem.com/jp,https://www.og-wellness.jp/,http://yonago-show.sakura.ne.jp/okadahp/,http://www.nishiin.jp,http://www.njrf.co.jp/,http://www.karatsu.co.jp,https://yamagata-royal.com/']


# import requests
# broken_urls = []
# active_urls =[]
# for i in range(len(urls)):
#     try:
#         request_response = requests.head(urls[i])
    
#         if request_response.status_code >=200 and request_response.status_code < 300:
#             active_urls.append(urls[i])
#         elif request_response.status_code >=300 and request_response.status_code<600:
#             broken_urls.append(urls[i])
            
#     except ConnectionError as e:
#         broken_urls.append(urls[i])
    
# print("Active URLs:",active_urls)
# print("___________________________")
# print("Broken URLs:",broken_urls)
# from urllib.request import urlopen, HTTPError, URLError
# a = []
# b = []
# for i in range(len(urls)):
#     try:
#         myURL = urlopen(urls[i])
#     except HTTPError as e:
#         a.append(urls[i])
#         print('HTTP Error code: ', e.code)
#     else:
#         print('No Error.')
# print(a)
# import urllib3
# from requests.exceptions import ConnectionError
# import requests
# http = urllib3.PoolManager()
# ajaira_irls=[]
# active_urls=[]
# broken_urls=[]
# for i in range(len(urls)):
#     try:
#         # x = http.request('GET', urls[i])
#         # if x.status == 200:
#         #     b.append(urls[i])
#         # else:
#         #     c.append(urls[i])
#         r = requests.get(urls[i], timeout=0.001)
#         if r.status_code == 200:
#             active_urls.append(urls[i])
#         else:
#             broken_urls.append(urls[i])

#     except ConnectionError as e:
#         ajaira_irls.append(urls[i])
        
# print("________________ active _____________________________")

# print(active_urls)

# print("________________ Broken _____________________________")
# print(broken_urls)


# from requests.exceptions import ConnectionError
# for i in range(len(urls)):
#     try:
#         r = requests.get(urls[i], timeout=0.001)
#         print(r.status_code)
#     except ConnectionError as e:    # This is the correct syntax
#         print(e)
#         r = "No response"
        
        
        
        
