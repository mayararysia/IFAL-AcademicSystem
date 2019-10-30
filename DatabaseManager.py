# -*- coding:utf-8 -*

import sqlite3
from sqlite3 import Error

class DatabaseManager:

        def __init__(self, nameDb):
                self._nameDb = nameDb
                self.createTables()

        def getNameDb(self):
                return self._nameDb
        
        def setNameDb(self, newName):
                self._nameDb = newName
        
        def query(self,  sql, parameters=()):
                try:
                        connection = sqlite3.connect(self._nameDb)
                except sqlite3.Error as error:
                        print("An error has occurred: " + error)
                else:
                        cursor = connection.cursor()
                        data = cursor.execute(sql, parameters)
                        connection.commit()
                        array = []
                        for item in data:
                                array.append(item)
                        connection.close()
                        return array

        def createTables(self):
                self.query(
                        "CREATE TABLE IF NOT EXISTS students ("
			"id INTEGER PRIMARY KEY NOT NULL, "
			"name TEXT NOT NULL, "
			"gender TEXT NOT NULL, "
			"date_of_birth TEXT NOT NULL, "
			"rg TEXT NOT NULL);")
                
                self.query(
                        "CREATE TABLE IF NOT EXISTS teachers ("
			"id INTEGER PRIMARY KEY NOT NULL, "
			"name TEXT NOT NULL, "
			"gender TEXT NOT NULL, "
			"academic_degree TEXT NOT NULL, "
			"date_of_birth TEXT NOT NULL, "
			"rg TEXT NOT NULL);")

                self.query(
                        "CREATE TABLE IF NOT EXISTS college_subjects ("
			"id INTEGER PRIMARY KEY NOT NULL, "
			"name TEXT NOT NULL,"
			"course TEXT NOT NULL);")
                
                self.query(
                        "CREATE TABLE IF NOT EXISTS notes ("
			"id INTEGER PRIMARY KEY NOT NULL, "
		"id_student INTEGER NOT NULL, "
			"id_teacher INTEGER NOT NULL, "
			"id_college_subject INTEGER NOT NULL, "
			"note1 REAL NOT NULL, "
			"note2 REAL NOT NULL);")

                print("Created database tables!")


        def listData(self, tableName):
                return self.query("select * from "+tableName)

        def listAData(self, tableName, identifier):
                array = []
                data = self.query("select * from "+ tableName + " where id="+identifier)
                for item in data:
                        array.append(item)
                return array
	

        def insert(self, tableName, data):
                      sql = "insert into " + tableName + " values ("
                      i=1
                      while i<=len(data):
                              if i==len(data):
                                      sql += "?)"
                              else:
                                      sql += "?, "
                              i+=1
                      data = tuple(data)
                      self.query(sql, data)
                      print("Data entered!")

        def deleteData(self, tableName, identifier):
                sql = "delete from " + tableName + " where id=" + identifier
                self.query(sql)
                print("Deleted data!")

        def updateData(self, tableName, attributes,  data):
                sql = "update " + tableName + " set ";
                
                i=0
                while i<len(attributes):
                        if i==(len(attributes)-2):
                                sql += str(attributes[i])+"=? where " 
                                i+=1
                                sql += str(attributes[i])+"=?" 
                        else:
                                sql += str(attributes[i])+"=?, "
                        i+=1
                
                data = tuple(data)
                self.query(sql, data)
                print("Updated data!")   
