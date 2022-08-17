import requests

def link_checker(link):
    a =[]
    try:
        #GET request
        req = requests.get(link)

        #check status-
        
        if req.status_code in [400,404,403,408,409,501,502,503]:
            a.append(req)
            return a
            # return(f"{link} => Broken status-code:{req.status_code}")
        else:
            return(f"{link} => Good")
            
    #Exception
    except requests.exceptions.RequestException as e:
        # print link with Errs
        raise SystemExit(f"{link}: Somthing wrong \nErr: {e}")


urls = ['https://www.aiden-net.co.jp/,http://www.koshinmilk.co.jp,https://www.ushio.co.jp/jp/,https://www.sumitomocorp.com/ja/jp,https://www.mitsui.com/jp/ja/index.html,http://www.sms.co.jp,http://www.nihon-shuji.or.jp/,https://www.shigapatent.com/jp/aboutus/ourfirm/,https://www.nisitokyobus.co.jp/,https://www.lapis-semi.com/,https://www.asahiseiko.com/,http://www.itochu-metals.co.jp,https://www.enoteca.co.jp/,https://www.okamotoya.com/,https://www.komatsu.jp/ja,http://www.sakainet.co.jp,http://www.shikizai.com,https://www.polyplastics.com/,https://www.ana.co.jp/,https://www.hakuju.co.jp/,http://www.itc-ps.co.jp/index.html,https://www.conexio.co.jp,https://www.taito.co.jp/,https://www.gracecontinental.com/,https://www.u-tokai.ac.jp/,https://www.bdo.or.jp/en-gb/home-en,https://www.val.co.jp/,https://www.jskk.co.jp/,https://www.tein.co.jp/e/index.html,https://www.shukoh.co.jp/,https://www.sonyengineering.co.jp/redirect.html,https://www.umc.co.jp/?ml_lang=en,http://www.junseikai.org/,http://www.funabashikousan.com/redirect.html,https://www.aeoncom.co.jp/,https://greenbox722.co.jp/,https://coopkyosai.coop/,https://www.joyosuisan.com/,https://www.hirosawaseiki.co.jp/index.htm,https://www.ichihara-hospital.or.jp/,https://www.icc.ac.jp/,http://www.katsu-p.com/top.html,https://kito.com/,http://www.sj-nagano.jp/,https://www.takashima.co.jp/,https://www.tana-x.co.jp/,https://onozo.co.jp/en/,https://www.hanshin-dw.co.jp/,http://www.enyuukai.jp,https://www.gifu-shinoda.co.jp/en/,https://buhin.nissan.co.jp/hokuriku/,http://www.takamatsu-p.jp/,https://buhin.nissan.co.jp/sanyo/,http://matsumoto-jukogyo.co.jp/,https://www.tosoh-finechem.com/jp,https://www.og-wellness.jp/,http://yonago-show.sakura.ne.jp/okadahp/,http://www.nishiin.jp,http://www.njrf.co.jp/,http://www.karatsu.co.jp,https://yamagata-royal.com/']


a = link_checker(urls)
print(a)