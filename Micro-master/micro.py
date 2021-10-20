# Date: 02/03/2019
# Author: Mohamed
# Description: Main file

from os import urandom
import requests as urlrequest 
from urllib.parse import urlparse
from lib.database import Database
from flask import Flask, render_template, request, jsonify, redirect, abort


class Webserver:

    def __init__(self):
        self.database = Database()
        self.app = Flask(__name__)
        self.app.secret_key = urandom(0x200)
    
    @property
    def server_url(self):        
        parse = urlparse(request.url)
        return '{}://{}/'.format(parse.scheme, parse.netloc)
    
    def add_paths(self):
        self.app.add_url_rule('/', 'index', self.index, defaults={'link_id': ''})
        self.app.add_url_rule('/<path:link_id>', 'index', self.index)

        self.app.add_url_rule('/create', 'create', self.create, methods=['POST'])
    
    def index(self, link_id):
        if link_id:

            if self.database.link_id_exists(link_id):
                url = self.database.get_link_url(link_id)
                return redirect(url)
                
            return abort(404)
        return render_template('index.html')

    def parser_url(self, url):
        parse = urlparse(url)

        link1 = '{}://{}{}{}{}{}'.format(
            'https' if not parse.scheme else parse.scheme, 
            parse.netloc.lower(), parse.path, parse.params, '?' + parse.query if parse.query else '', parse.fragment
        )

        link2 = link1.replace('https', 'http') 

        try:
            urlrequest.get(link1)
            link = link1
        except:
            link = link2        

        return link if ((parse.netloc or parse.path) and urlparse(request.url).netloc != parse.netloc) else ''     

    def get_link_id(self, link_url):
        url = urlparse(request.url).netloc
        link_id = self.database.generate_link_id(url)
        
        self.database.add_link(link_url, link_id)
        return link_id
            
    def create(self):
        if not 'link' in request.form:
            return jsonify({ 'resp': '' })

        link_url = request.form['link']
        link_url = self.parser_url(link_url)

        if not link_url:
            return jsonify({ 'resp': '' })

        if self.database.link_url_exists(link_url):
            return jsonify({ 'resp': self.server_url + self.database.get_link_id(link_url) })
        
        link_id = self.get_link_id(link_url)
        return jsonify({ 'resp': self.server_url + link_id})       
        
    def start(self):        
        self.add_paths()
        self.database.start()
        self.app.run(debug=False)


if __name__ == '__main__':
    webserver = Webserver()
    webserver.start()