import requests,time,os,json
from requests import Session

os.system('clear')

def home():
    print('''
\x1b[92m   _____ __  ________\x1b[00m                  \x1b[96m[ OK.RU CALL - MONIFIRE ]\x1b[00m
\x1b[92m  / ___//  |/  / ___/\x1b[00m  |
\x1b[92m  \__ \/ /|_/ /\__ \ \x1b[00m  | › \x1b[92mFacebook\x1b[00m : \x1b[94mhttps://www.facebook.com/toey.monifty\x1b[00m
\x1b[92m ___/ / /  / /___/ / \x1b[00m  | › \x1b[92mGithub\x1b[00m : \x1b[94mhttps://github.com/MONIFIRE\x1b[00m
\x1b[92m/____/_/  /_//____/  \x1b[00m  | › \x1b[92mYoutube\x1b[00m : \x1b[94mhttps://youtube.com/channel/UCFa3KUU35a6IGAkhp3OWoTQ\x1b[00m
''')
    phone = input('\x1b[96mPHONE-NUMBER\x1b[00m :\x1b[92m ')
    print ('')

    if int(phone) <= 99999999 or int(phone) >= 999999999:
         print('\x1b[92m[ MONIFIRE ]\x1b[00m : \x1b[91m電話番号が間違って入力されました ! \x1b[00m')
         time.sleep(2)
         os.system('clear')
         home()
    else:
         for i in range(1):
             send = Session()
             send.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
             snd = send.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phone[1:]}")
             sed = send.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")
             if 'error' in snd.text or sed.text:
                  time.sleep(1)
                  print('\x1b[92m[ MONIFIRE ]\x1b[00m : \x1b[96m確認番号の送信に成功しました ✓ \x1b[00m')
                  time.sleep(2)

             else:
                  time.sleep(1)
                  print('\x1b[92m[ MONIFIRE ]\x1b[00m : \x1b[91m確認番号を送信できませんでした !\x1b[00m')
         time.sleep(1)
         print ('')
         hme = input('\x1b[92m[ MONIFIRE ] : 最初からやり直したいですか Y/N ?\x1b[00m \x1b[91m »\x1b[00m  \x1b[92m')
         print ('')
         if str(hme) == 'y' or str(hme) == 'Y':
              print('\x1b[92m[ MONIFIRE ]\x1b[00m : \x1b[96m家に入るのを終えた ~ \x1b[00m')
              time.sleep(2)
              os.system('clear')
              home()
         elif str(hme) == 'n' or str(hme) == 'N':
              print('\x1b[92m[ MONIFIRE ]\x1b[00m : \x1b[96m正常にキャンセルされました √ \x1b[00m')
         else: print('\x1b[92m[ MONIFIRE ]\x1b[00m : \x1b[91m不合格 X \x1b[00m')

home()
