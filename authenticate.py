#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pymongo
from flask import Flask, redirect,jsonify, url_for, request


# In[3]:


client = pymongo.MongoClient("mongodb+srv://Codack:mehulmj10@cluster0.wckve.mongodb.net/User?retryWrites=true&w=majority&connect=false")


# In[4]:


db = client.User
col=db.Login


# In[5]:


login={'emailId':"tom@gmail.com"}
col.find_one({'emailId':login['emailId']})['username']


# In[6]:


app=Flask(__name__)


# In[7]:


@app.route('/login')
def login():
    login={'emailId':request.args.get("emailId"),'password':request.args.get("password")}
    if(col.find_one(login)):
        username=col.find_one(login)['username']
        return jsonify({'login':True, 'message':"success" , 'username' : username })
    elif(col.find_one({'emailId' : login['emailId']})):
        return jsonify({'login':False, 'message':"password incorrect" })
    return jsonify({'login':False, 'message':"Email id doesnt exist" })


# In[8]:


@app.route('/signup')
def signup():
    login={'emailId':request.args.get("emailId"),'username':request.args.get("username"),'password':request.args.get("password")}
    if(col.find_one({'emailId':login['emailId']})):
        return jsonify({'signup':False, 'message':"email id already exists" })
    elif(col.find_one({'username':login['username']})):
        return jsonify({'signup':False, 'message':"username already exists" })
    col.insert_one(login)
    return jsonify({'signup':True, 'message':"success" })
#app.run(host='192.168.43.87')


# In[ ]:


app.run(host='192.168.43.87')


# In[ ]:





# In[ ]:




