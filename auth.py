from flask import Flask, url_for, request, redirect, render_template
from pymongo import MongoClient
import utils

def init():
    client = MongoClient()
    db = client["users"]
    return db

def register(username, password):
    db = init()
    check = db.users.find_one({'username':username})
    if (check == None):
        db.users.insert({'username':username, 'password':password, 'cash':100000, 'stocks':{}})
        return True
    else:
        return False

def login(username, password):
    db = init()
    user = [x for x in db.users.find({'username':username, 'password':password}, fields = {'_id':False})]
    if (len(user) == 0):
        user = user[0]
        if username == user['username'] and password == user['password']:
            return True
        else:
            return False

def checkUser(username):
    db = init()
0    user = [x for x in db.users.find({'username':username}, fields = {'_id':False})]
    if (len(user) == 0):
        return False
    return True

def getStocks(username):
    db = init()
    stuff = [x for x in db.users.find({'username':username}, fields = {'_id':False})]
    return stuff['stocks']

def getCash(username):
    db = init()
    stuff = [x for x in db.users.find({'username':username}, fields = {'_id':False})]
    return stuff['cash']

def updateStocks(username, stocks):
    db = init()
    db.users.update({'username':username}, {'stocks':stocks})
    return True

def updateCash(username, cash):
    db = init()
    db.users.update({'username':username}, {'cash':cash})
    return True

def buy(username, symb, num):
    db = init()
    amount = utils.getAsk(symb) * num
    stocks = getStocks(username)
    cash = getCash(username)
    if (cash >= amount)):
        if (stocks[symb] > 0):
            stocks[symb] = stocks[symb] + num
            cash = cash - amount
            updateStocks(username, stocks)
            updateCash(username, cash)
            return True
        else:
            stocks[symb] = num
            cash = cash - amount
            updateStocks(username, stocks)
            updateCash(username, cash)
            return True
    else:
        return False

def sell(username, symb, num):
    db = init()
    amount = utils.getAsk(symb) * num
    stocks = getStocks(username)
    cash = getCash(username)
    if (stocks[symb] >= num):
        stocks[symb] = 0
        cash = cash + amount
        updateStocks(username, stocks)
        updateCash(username, cash)
        return True
    else:
        return False