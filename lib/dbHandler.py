#!/usr/bin/python
# -*- coding: utf-8 -*-

# lib/dbHandler.py
# -----------------------
# This represents the database where the data will be logged.
# Its a collection of SQLite3 objects wrapped together for ease.


import sqlite3
import os
import sys

class dbObject():
    '''
    Database Object:
        This represents the database where the data will be logged. 
        Its a collection of SQLite3 objects wrapped together for ease.
        
        if dbPath is left blank on initialisation it will use an in
        :memory: database
    '''
    connection = None
    assert isinstance(connection, sqlite3.Connection)
    cursor = None
    assert isinstance(cursor, sqlite3.Cursor)
    dbPath = ''
    sensorTableName = ''
    
    def __init__(self, dbPath, sensorTableName='sensorData'):
        if dbPath == None:
            self.dbPath = ':memory:'
        else:
            self.dbPath = dbPath
        try:
            self.sensorTableName = sensorTableName
            self.connection = sqlite3.connect(self.dbPath)
            self.cursor = self.connection.cursor()
            self.checkDB()
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(e)
        
    def checkDB(self):      
        try:
            sSQL = 'SELECT count(*) FROM sqlite_master WHERE type="table" AND name=?;'
            self.cursor.execute(sSQL, self.sensorTableName)
            ret = self.cursor.fetchone()
            if ret == 0:
                self.createDB()
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(e)
            
    def createDB(self):
        try:
            sSQL = 'CREATE TABLE ?(id INTEGER PRIMARY KEY, date REAL, type TEXT, value REAL);'
            self.cursor.execute(sSQL, (self.sensorTableName,))
        except sqlite3.error, e:
            print "Error %s:" % e.args[0]
            sys.exit(e)
    
    def insertData(self, dataSet):
        '''Inserts a tuple of 3 values into the database'''
        try:
            dsInsert = self._prepareData(dataSet)
            assert isinstance(dsInsert, tuple)
            dsInsert
            sSQL = 'INSERT INTO sensorData VALUES(?, ?, ?, ?)'
            self.cursor.execute(sSQL, dataSet)
        except sqlite3.error, e:
            print "Error %s:" % e.args[0]
            