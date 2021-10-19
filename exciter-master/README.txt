EXCITER
========
  is an open source penetration testing tool that automates testing accounts to the site's login page,
  based on Dictionary Attack. this tools will automatically search the url action and all inputs on the
  website which will be used to send login data to the server

INSTALLATION ON LINUX
=====================
  [package needed]
    1. git
    2. python3 or above

  [step]
    $  git clone https://github.com/zevtyardt/exciter
    $  cd exciter
    $  pip3 install -r requirements.txt
    $  python3 exciter.py -h

USAGE
=====
  $ python3 exciter.py -t https://eaxmple.com/login.php -p password list

CHANGELOG
=========
  1. add __init__.py in each folder because setuptools.find_pakages doesn't work in python3
     now you can install this tool just by typing  pip3 install . in the exciter folder

SUPPORT ME
==========
  1. publish and review in your blog ^^
