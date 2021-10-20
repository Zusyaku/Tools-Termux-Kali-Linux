# Date: 02/03/2019
# Author: Mohamed
# Description: DBMS

import sqlite3
from . import const
from requests import get 
from string import ascii_letters
from random import choice, randint


class Database:
 
    def __init__(self):
        self.db_path = const.DatabaseConst.DATABASE_FILE.value
        self.printable = ascii_letters + ''.join([str(_) for _ in range(10)])

    def start(self):
        self.db_create('''
        CREATE TABLE IF NOT EXISTS
        Link(
            link_id TEXT PRIMARY KEY,
            link_url TEXT
        );
        ''')

    ### Database Wrappers ###

    def db_query(self, cmd, args, fetchone=True):
        database = sqlite3.connect(self.db_path)
        sql = database.cursor().execute(cmd, args)
        data = sql.fetchone()[0] if fetchone else sql.fetchall()
        database.close()
        return data

    def db_update(self, cmd, args):
        database = sqlite3.connect(self.db_path)
        database.cursor().execute(cmd, args)
        database.commit()
        database.close()

    def db_create(self, cmd):
        database = sqlite3.connect(self.db_path)
        database.cursor().execute(cmd)
        database.commit()
        database.close()

    ### Misc ###
    
    def add_link(self, link_url, link_id):
        self.db_update('''
        INSERT INTO Link(link_id, link_url)
        VALUES(?, ?);
        ''', [link_id, link_url])
    
    def link_url_exists(self, link_url):
        data = self.db_query('SELECT * FROM Link WHERE link_url=?;', [link_url], False)
        return True if len(data) else False
    
    def link_id_exists(self, link_id):
        data = self.db_query('SELECT * FROM Link WHERE link_id=?;', [link_id], False)
        return True if len(data) else False
    
    def generate_link_id(self, server_url):
        while True:
            link_id = ''.join([choice(self.printable) for _ in range(randint(4, 7))])

            if not self.link_id_exists(link_id):
                    return link_id
    
    def get_link_url(self, link_id):
        return self.db_query('SELECT link_url FROM Link WHERE link_id=?;', [link_id])
    
    def get_link_id(self, link_url):
        return self.db_query('SELECT link_id FROM Link WHERE link_url=?;', [link_url])
