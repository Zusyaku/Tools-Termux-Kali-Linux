# coding=utf-8


import requests, os, shutil
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor

try: shutil.rmtree(
    'get_proxy/__pycache__'
  )
except: pass

proxy_list = []
valid_proxy = []

def prox():
  print('''\033[00m
\033[96m1).\033[00mSearch Proxy From (free-proxy-list.com)
\033[96m2).\033[00mSearch Proxy From (free-proxy-list.net)
\033[96m3).\033[00mSearch Proxy From File
  ''')
  ask = int(
    input(
      '\033[00m>> \033[96m'
    )
  )
  if ask == 1:
    return proxy_com(
    )
  elif ask == 2:
    return proxy_net(
    )
  elif ask == 3:
    return from_file(
    )
  else:
    exit(
      '\n\033[00m[\033[91m!\033[00m] Wrong Input'
    )

def proxy_checker(prox):
  try:
    global valid_proxy
    if requests.get(
       'http://ip.ml.youngjoygame.com:30220/myip',
          verify=False,
          proxies=prox,
          timeout=10
        ).status_code == 200:
      valid_proxy.append(
        prox
      )
    print(
      end='\r\033[00m[\033[92m+\033[00m] Proxy Valid(\033[96m%s\033[00m) '%(
        len(
          valid_proxy
        )
      ),
      flush=True
    )
  except: pass

def proxy_com():
  limit = int(
    input(
      'Limit (ex: 100): '
    )
  )
  count = 1
  stop = False
  url = 'https://free-proxy-list.com?page=%s' %(
    str(
      count
    )
  )
  while 1:
    try:
      found = False
      r = requests.get(
        url,
        headers={'user-agent':'chrome'}
      ).text
      soup = bs(
        r,
        'html.parser'
      )
      for x in soup.find_all('a'):
        if x.has_attr(
          'alt'
        ) == True:
          proxy = (
            x['alt']
          )
          found = True
          proxy_list.append({
            'http':proxy.strip(),
            'https':proxy.strip()
          }) if len(
            proxy.strip().split(':')
          ) == 2 else None
          print(
            end='\r\033[00m[\033[92m+\033[00m] Search (%s) proxy.'%(
              len(proxy_list)
            ),
            flush=True
          )
          if len(
            proxy_list
          ) == limit or len(
            proxy_list
          ) > limit:
            stop = True
            break
      if found == False:
        print(
          '\n\033[00m[\033[91m!\033[00m](%s) proxy' %(
            str(
              len(
                proxy_list
              )
            )
          )
        )
        break
      elif stop == False:
        count+=1
        url = 'https://free-proxy-list.com?page=%s' %(
          str(
            count
          )
        )
      else:
        break
    except: pass
  if len(
    proxy_list
  ) != 0:
    print(
      '\n\033[00m[\033[96m*\033[00m] Search proxy valid'
    )
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[91mProxy Not Valid\033[00m'
    )
  else: exit(
    '\033[91mProxy Not Found\033[00m'
  )

def proxy_net():
  print(
    '\033[00m[\033[96m*\033[00m] Search proxy valid'
  )
  r = requests.get(
    'https://free-proxy-list.net/',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':e.strip(),
      'https':e.strip()
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[91mProxy Not Valid\033[00m'
    )
  else: exit(
    '\033[91mProxy Not Found\033[00m'
  )

def from_file():
  list = input(
    '\033[00mList proxy (\033[93mproxy.txt\033[00m): \033[93m'
  )
  if os.path.exists(
    list
  ):
    for data in open(
      list,
      'r',
      encoding='utf-8'
    ).readlines(
      ):
      prox = data.strip(
      ).split(
        ':'
      )
      try:
        if prox[0] and prox[1]:
          proxy_list.append({
            'http': data.strip(),
            'https': data.strip(),
          })
      except: pass
    if len(
      proxy_list
    ) != 0:
      print(
        '\033[00m[\033[96m*\033[00m] Total (%s) proxy' %(
          str(
            len(
              proxy_list
            )
          )
        )
      )
      print(
        '\033[00m[\033[96m*\033[00m] Search proxy valid'
      )
      with ThreadPoolExecutor(
        max_workers=50
      ) as thread:
        [
          thread.submit(
            proxy_checker,(
              prox
            )
          ) for prox in proxy_list
        ]
      if len(
        valid_proxy
      ) != 0:
        print(
          '\n'
        )
        return valid_proxy
      else: exit(
        '\033[91mProxy Not Valid\033[00m'
      )
    else: exit(
      '\033[91mProxy Not Found\033[00m'
    )
  else: exit(
    '\033[91mFile Not Found\033[00m "{0}"'.format(
      list
    )
  )
