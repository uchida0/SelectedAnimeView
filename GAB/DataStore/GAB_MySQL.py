#import mysql.connector
import pymysql

class GAB_MySQL:
    
    def __init__(self, **dns):
        self.dns = dns
        self.connection = None

    
    def _open(self):
        self.connection = pymysql.connect(**self.dns)

    
    def _close(self):
        self.connection.close()
    
    
    #anime_dictを返す
    def anime_dict_query(self, cool):
        self._open()
        with self.connection.cursor() as cursor:
            query = (
                "SELECT * FROM " + cool
            )
            cursor.execute(query)
        
        anime_dict = cursor.fetchall()
        self._close()

        return anime_dict
    
    
    #db内にあるcoolのtable名を返す
    def all_cool(self):
        self._open()
        with self.connection.cursor() as cursor:
            query = (
                "SELECT cool, cool_view FROM cool_list;"
            )
            cursor.execute(query)
        
        cool_list = cursor.fetchall()
        self._close()
        #print(cool_list)

        return cool_list
    

    def select_cool(self, cool):
        self._open()
        with self.connection.cursor() as cursor:
            query = (
                "SELECT cool, cool_view FROM cool_list WHERE cool = %s;"
            )
            cursor.execute(query, cool)
        
        result = cursor.fetchall()
        self._close()
        #print(result[0])

        return result[0]

    
    def count_cool_anime(self, cool):
        self._open()
        with self.connection.cursor() as cursor:
            query = (
                "SELECT COUNT(*) FROM "+cool+";"
            )
            cursor.execute(query)
        
        result = cursor.fetchall()
        self._close()
        #print(result[0][0])

        return result[0][0]


"""
if __name__ == "__main__":
    dns ={
        "host": "localhost",
        "user": "sora",
        "password": "monster",
        "db": "good_anime_bu"
    }

    a = GAB_MySQL(**dns)
#    cl = a.all_cool()
#    print(cl)
    a.select_cool("spring_2021")
"""
        
