import mariadb
from flask import Flask, request, Response
import json
import dbcreds
from flask_cors import CORS

   
app = Flask(__name__)
CORS(app)
@app.route("/signup",methods=['POST'])
def signup():
    if request.method == 'POST':
    
    
        conn = None
        cursor = None
        blogger_username = request.json.get("username")
        blogger_password = request.json.get("password")
        print(blogger_username)
        rows = None
        try:
            conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password,host=dbcreds.host,database=dbcreds.database,port=dbcreds.port)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO blogger(username,password) VALUES(?,?)",[blogger_username,blogger_password])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error:
            print("something went wrong: ")
            print(error)  
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("you made an account",mimetype="text/html", status=201) 
            else:
                return Response("something went wrong",mimetype="text/html", status=501)

@app.route("/login",methods=['POST'])
def login():
    if request.method == 'POST':
    
    
        conn = None
        cursor = None
        blogger_username = request.json.get("username")
        blogger_password = request.json.get("password")
        
        
        
    

    
        try:
            conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password,host=dbcreds.host,database=dbcreds.database,port=dbcreds.port)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM blogger WHERE username=? AND password=?",[blogger_username,blogger_password])
            user = cursor.fetchone()
            print(user)
        
        except Exception as error:
            print("something went wrong: ")
            print(error)  
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(user != None):
    
                return Response(json.dumps(user, default=str),mimetype="text/html", status=201) 
            else:
                return Response("something went wrong",mimetype="text/html", status=501)           

@app.route("/blog",methods=['GET','POST','PATCH','DELETE'])
def blog():
    if request.method == 'GET':
        conn = None
        cursor = None
        blog = None
        try:
            conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password,host=dbcreds.host,database=dbcreds.database,port=dbcreds.port)
            cursor = conn.cursor()
            cursor.execute("SELECT *FROM blog_post")
            blog = cursor.fetchall()
        except Exception as error:
            print("something went wrong: ")
            print(error)  
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(blog != None):
                return Response(json.dumps(blog, default=str),mimetype="application/json", status=200) 
            else:
                return Response("something went wrong!",mimetype="application/json", status=500)
    elif request.method == 'POST':
        conn = None
        cursor = None
        blog_post_content = request.json.get("content")
        blog_post_id = request.json.get("id")
        blog_post_blogger_id = request.json.get("blogger_id")
        
        
        
        rows = None
        try:
            conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password,host=dbcreds.host,database=dbcreds.database,port=dbcreds.port)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO blog_post(blogger_id,content) VALUES(?,?)",[blog_post_blogger_id,blog_post_content])
            conn.commit()
            rows = cursor.rowcount
        except Exception as error:
            print("something went wrong: ")
            print(error)  
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("you made a post",mimetype="text/html", status=201) 
            else:
                return Response("you have no permission to change this post",mimetype="text/html", status=501) 

    elif request.method == 'PATCH':
        conn = None
        cursor = None
        blog_post_content = request.json.get("content")
        blog_post_id = request.json.get("id")
        blog_post_blogger_id = request.json.get("blogger_id")
        
        rows = None
        try:
            conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password,host=dbcreds.host,database=dbcreds.database,port=dbcreds.port)
            cursor = conn.cursor()
            if blog_post_content !="" and blog_post_content != None:
                cursor.execute("UPDATE blog_post SET content=? WHERE id=? AND blogger_id=?",[blog_post_content,blog_post_id,blog_post_blogger_id])
            conn.commit()    

            rows = cursor.rowcount
        except Exception as error:
            print("something went wrong: ")
            print(error)  
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("post has been updated",mimetype="text/html", status=204) 
            else:
                return Response("you have no permission to update this post",mimetype="text/html", status=500) 

    elif request.method == 'DELETE':
        conn = None
        cursor = None
        
        blog_post_id = request.json.get("blog_id")
        blog_post_blogger_id = request.json.get("blogger_id")
        print(blog_post_id)
        rows = None
        try:
            conn = mariadb.connect(user=dbcreds.user,password=dbcreds.password,host=dbcreds.host,database=dbcreds.database,port=dbcreds.port)
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM blog_post WHERE id=? AND blogger_id=?",[blog_post_id])
            conn.commit()    

            rows = cursor.rowcount
        except Exception as error:
            print("something went wrong: ")
            print(error)  
        finally:
            if(cursor != None):
                cursor.close()
            if(conn != None):
                conn.rollback()
                conn.close()
            if(rows == 1):
                return Response("post DELETED",mimetype="text/html", status=204) 
            else:
                return Response("something went wrong",mimetype="text/html", status=500)  