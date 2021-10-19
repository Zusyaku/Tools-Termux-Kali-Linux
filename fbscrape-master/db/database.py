import pymysql
import json

class Database:
    # Table name to create in database
    tableName = "scrape"

    # Load target from [targets.json] configuration file
    def loadCredentials(self):
        file = open('config/database.json')
        data = json.load(file)
        return data

    def initDB(self):
        credentials = self.loadCredentials()
        return pymysql.connect(
            host=credentials['host'],
            user=credentials['user'],
            passwd=credentials['password'],
            db=credentials['database'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def __init__(self):
        self.connection = self.initDB()
        # Check if Table Exist or not.
        # If not exists then we create table
        if self.tableExists() == False:
            print("Creating table {}".format(self.tableName))
            self.createTable()

    def createTable(self):
        try:
            cursor = self.connection.cursor()
            sql = "CREATE TABLE {} (ID INT AUTO_INCREMENT PRIMARY KEY, post_id VARCHAR(255), post_text TEXT, username VARCHAR(255), name VARCHAR(255), datetime VARCHAR(255), total_likes INT, total_comments INT, total_share INT)".format(self.tableName)
            cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print("        [x] {}".format(e))

    def tableExists(self):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT COUNT(*) as total FROM information_schema.tables WHERE table_name = '{}'".format(self.tableName)
            cursor.execute(sql)
            self.connection.commit()
            if cursor.fetchone()['total'] > 0:
                return True
            return False
        except Exception as e:
            print("        [x] {}".format(e))

    def postExists(self, postId):
        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM {} WHERE post_id = '{}'".format(self.tableName, postId)
            cursor.execute(sql)
            if cursor.rowcount == 0:
                return False
            return True
        except Exception as e:
            print("        [x] {}".format(e))
        
    def insert(self, scrape):
        try:
            cursor = self.connection.cursor()
            sql = "INSERT INTO {} (post_id, post_text, username, name, datetime, total_likes, total_comments, total_share) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)".format(self.tableName)
            cursor.execute(sql, (scrape.postId, scrape.postText, scrape.username, scrape.name, scrape.dateTime.strftime("%Y-%m-%d %H:%M:%S"), scrape.totalLikes, scrape.totalComments, scrape.totalShare))
            self.connection.commit()
        except Exception as e:
            print("        [x] {}".format(e))
