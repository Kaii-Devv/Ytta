# main
from flask import Flask, send_file, request, jsonify, render_template, Response
import requests, re, io,os,asyncio,subprocess,speedtest
import random
#from proxy_checker import ProxyChecker

import threading
import numpy as np
from concurrent.futures import ThreadPoolExecutor,as_completed,wait,FIRST_COMPLETED

app = Flask(__name__)

def stream_chunks(x):
    for chunk in x.raw.stream(1048576, decode_content=True):
        yield chunk

def check(proxy,tok,hasil,pool,file):
  #print(hasil)
  if len(str(hasil))>5:return
  if os.path.exists(file):return
  proxy = {
    'http': 'socks5://'+proxy,
    'https': 'socks5://'+proxy
}
  try:
    ses=requests.Session()
    host= 'https://d0o0d.com'
    ses.proxies.update(proxy)
    log2=ses.get(host+"/e/"+tok,headers={'Host': 'd0o0d.com', 'referer': 'https://d0o0d.com/e/', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.9.0'},timeout=3)
    if not 'ddos' in log2.text.lower():
        link=host+"/pass_md5/"+re.search("/pass_md5/(.*?)', function",str(log2.text)).group(1)
        result = ses.get(link,headers={"Host": host.replace('https://',''),"referer": log2.url,"accept-encoding": "gzip","cookie": "lang=1","user-agent": "okhttp/4.9.0"},timeout=3).text+"".join([random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for _ in range(10)])+"?token="+link.split("/")[-1]+"&expiry=1"+"".join([str(random.randrange(1,9)) for _ in range(12)])
       # print(result,ses)
        ini = ses.get(result,headers={'Range': 'bytes=0-', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.144 Chrome/77.0.3865.144 Safari/537.36', 'Referer': 'https://dooood.com/', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'},stream=True,timeout=3)
        proxyt=proxy['http']
        if os.path.exists(file):return
        hasil.update({'response':ini,'headers':ini.headers})
        subprocess.Popen(['curl', '-x', proxyt, '-H', 'Range: bytes=0-', '-H', 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.144 Chrome/77.0.3865.144 Safari/537.36', '-H', 'Referer: https://dooood.com/', '-H', 'Connection: Keep-Alive', '-H', 'Accept-Encoding: gzip', result, '-o', file])

        print(file)
        
        pool.shutdown()
    else:pass
  except Exception as e :pass
@app.route('/d/')
def unduh():
  try:
      tok = request.args.get('token')
      if tok:
          pass
      else:
          return {'return': 'need params token'}

      proxy = requests.get(
          'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
      proxies = np.char.replace(proxy.split('\n')[:-1], '\r', '')
      myhasil = ''
      hasil={}
      file='dood/'+"".join([random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for _ in range(10)])+'.mp4'
      with ThreadPoolExecutor(max_workers=20) as pool:
          for proxy in proxies:
              pool.submit(check, proxy, tok,hasil,pool,file)

    #  print(hasil)
      
      #file='dood/'+"".join([random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for _ in range(10)])+'.mp4'
     # with ThreadPoolExecutor(max_workers=1) as pool:
      #threading.Thread(target=build,args=(hasil['response'],file)).start()
    #return hasil
      #open(file,'w').write('content is loading')
      #return send_file(hasil['response'].raw,as_attachment=True,download_name='video.mp4')
    #return Response(hasil['response'].iter_content(chunk_size=8000), content_type='video/mp4')

      return {'result':file,'headers':str(hasil['headers']),'warning':'wait for generate content'}
      
      
          

  except Exception as e:
      return {'result': str(e)}

def build(ini,file):
    achunk=b''
    try:
        
        for chunk in ini.raw.stream(10024, decode_content=False):
            achunk+=chunk
        open(file,'wb').write(achunk)
    except Exception as e:
        open(file,'wb').write(achunk)
        #print(e)

@app.route('/dood/<judul>')
def dood(judul):
    try:return send_file('dood/'+judul)
    except:return 'content is loading'


#app.run(port=81,host='0.0.0.0')
app.run()

