"""
Bu yazılımı paylaşmadan önce bu yazılımın MIT Lisansı ile lisanslandığını lütfen unutmayınız.
"""

#!/usr/bin/env python
import requests
import threading
from threading import Thread
from requests import get

def main():
	try:
		print("""\033[1;36m
           _  ________ _  _              _____  ______ 
     /\   | |/ /____  | || |       /\   |  __ \|  ____|
    /  \  | ' /    / /| || |_     /  \  | |__) | |__   
   / /\ \ |  <    / / |__   _|   / /\ \ |  ___/|  __|  
  / ____ \| . \  / /     | |    / ____ \| |    | |     
 /_/    \_\_|\_\/_/      |_|   /_/    \_\_|    |_|\033[1;31mv1.0
                                                       
\033[0m
""")
		print("\033[1;32m[ Author  : Vagus ]\033[0m")
		print("\033[1;32m[ Website : https://ak74security.org/ ]\033[0m")
		print("\033[1;32m[ Discord : https://discord.gg/4Ra3dgE ]\033[0m\n")
		while True:
			print("\033[1m[!] Linkleri girerken lütfen \033[1;31mhttp(s)://\033[0m\033[1m'yi eklemeyin. Yoksa yazılımda hata çıkacaktır.\n[?] Aşağıya linki yazınız. (örn: www.siteisim.com, siteisim.com).")
			a = input("\033[1;33mapf/> \033[1;0m")
			array = ["https://{}/admin.php".format(a),
			"http://admin.{}".format(a),
			"http://{}/admin/index.php".format(a),
			"http://{}/admin/adminhome.php".format(a),
			"http://{}/admin".format(a),
			"http://{}/adminhome.php".format(a),
			"http://{}/admin/school_info.php".format(a),
			"http://{}/school_info.php".format(a),
			"http://{}/admin/adminlogin.php".format(a),
			"http://{}/admin/admin_login.php".format(a),
			"http://{}/adminlogin.php".format(a),
			"http://{}/admin_login.php".format(a),
			"http://{}/admin/adminlogin.php".format(a),
			"http://{}/login.php".format(a),
			"http://{}/admin/login.php".format(a),
			"http://{}/news/admin/login.php".format(a)
			]
			for i in array:
				try:
					response = requests.get(i)
					if response.status_code == 200 or response.status_code == 302:
						print("\033[1;32m[+]\033[0m Admin Paneli Bulundu: {}".format(i))
					elif response.status_code == 401:
						print("\033[1;32m[+]\033[0m Admin Paneli Bulundu: {}".format(i))
					else:
						print("\033[1;31m[-]\033[0m Başarısız: {}".format(i))
				except:
					print("\033[1;31m[-]\033[0m Admin Paneli Bulunurken Bir Hatayla Karşılaşıldı: {}".format(i))
					continue
			print("\n\n\033[1mBu programı yapmamda yardımcı olan SonTürk'e teşekkürlerimi sunarım.")
			devam = input("Devam etmek istiyor musunuz(e/h):\033[0m ")
			if devam == "h":
				break

	except KeyboardInterrupt:
		print("\033[1;36mKlavye kısayolu ile çıkış talep edildi. Yazılımdan çıkış yapıldı.")
		sys.exit(0)
		
main()
