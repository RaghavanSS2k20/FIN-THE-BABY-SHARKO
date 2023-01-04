from flask import *
import requests
import sys
#//from urllib import *
take=0
#import models as dbhandler
app=Flask(__name__)
import sqlite3 as sql
message=""
def api(strng):
            querystring = {"url":strng,"showAllResults":"false"}
            url = "https://reverse-google-image-search.p.rapidapi.com/reverseImageSearch"
            headers = {
	        "X-RapidAPI-Host": "reverse-google-image-search.p.rapidapi.com",
	        "X-RapidAPI-Key": "d1869f472amsh706c8dbcf4cf939p147e3bjsn048c5e14b83e"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            resp = response.text

            return resp

def search_by_keyword(strng):
    # querystring = {"q":strng,"hl":"en"}
    # url = "https://google-image-search1.p.rapidapi.com/v2/"
    # headers = {
	# "X-RapidAPI-Host": "google-image-search1.p.rapidapi.com",
	# "X-RapidAPI-Key": "d1869f472amsh706c8dbcf4cf939p147e3bjsn048c5e14b83e"
    # }
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # resp = response.text
    # return resp
    url = "https://bing-image-search1.p.rapidapi.com/images/search"

    querystring = {"q":strng}

    headers = {
	"X-RapidAPI-Key": "d1869f472amsh706c8dbcf4cf939p147e3bjsn048c5e14b83e",
	"X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text



app.config['SECRET_KEY'] = 'RAGHAVANRELIVINGTHELIFE'
conn = sql.connect("database.db")
c = conn.cursor()
lmsg = "good"
#c.execute("drop table if exists users")
#createTable = "create table users (emailId text PRIMARY key,password text not null,noOfsearches integer DEFAULT 0)"
#alert = "fool"
# def insertUser(emailid,password):
#     con = sql.connect("database.db")
#     cur = con.cursor()
#     cur.execute("INSERT INTO users (emailId,password) VALUES (?,?)", (username,password))
#     con.commit()
#     con.close()

# def retrieveUsers():
# 	con = sql.connect("database.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT emailIdx, password FROM users")
# 	users = cur.fetchall()
# 	con.close()
# 	return users

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/login')
# def login():
#     return render_template("login.html")

@app.route('/mainpage')
def mainpage():
    return render_template("mainpage.html")
    # import requests

    # url = "https://reverse-google-image-search.p.rapidapi.com/reverseImageSearch"

    # querystring = {"showAllResults":"false"}

    # payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
    # headers = {
    #     "content-type": "multipart/form-data; boundary=---011000010111000001101001",
    #     "X-RapidAPI-Host": "reverse-google-image-search.p.rapidapi.com",
    #     "X-RapidAPI-Key": "d1869f472amsh706c8dbcf4cf939p147e3bjsn048c5e14b83e"
    # }

    # response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    
    # # print(response.text)
    


# @app.route('/searchbyfileupload')
# def searchbyfileupload():
#     return render_template("searchbyfileupload.html")

@app.route('/mainpage/uploadfile')
def uploadFile():
    return render_template("searchbyfileupload.html")

@app.route('/mainpage/searchbytext',methods=['POST','GET'])
def searchbykeyword():
    if request.method == 'POST':
        url = "https://google-image-search1.p.rapidapi.com/v2/"
        query = request.form['keyword']
        resp = search_by_keyword(query)
        data = json.loads(resp)
        value=[]
        value = data["value"]
        
        return render_template("searchbykeyword.html",value=value)


    return render_template("searchbykeyword.html")

# @app.route('/mainpage/searchbylink/results')
# def result():
    

@app.route('/mainpage/searchbylink',methods=['POST','GET'])
def searchbylink():
        message=""
        if request.method == 'POST':
            url = "https://reverse-google-image-search.p.rapidapi.com/reverseImageSearch"
            link = request.form['inpt']
            # querystring = {"url":request.form["inpt"],"showAllResults":"false"}

            # headers = {
	        # "X-RapidAPI-Host": "reverse-google-image-search.p.rapidapi.com",
	        # "X-RapidAPI-Key": "d1869f472amsh706c8dbcf4cf939p147e3bjsn048c5e14b83e"
            # }

            # response = requests.request("GET", url, headers=headers, params=querystring)
            # msg = response.text
        #print(response.text)
    
        #link = request.form["link"]
            resp = api(link)
            # session["response"] = resp
            data = json.loads(resp)
            links = data["links"]
            res = data['result']
            resp = search_by_keyword(res)
            data = json.loads(resp)
            links=data["value"]
            # return redirect(url_for('results'))
            context = {}
            context['links']=links
            context['link']=links
            domain={}
            # for link in links:
            #     domain[link] =  urlparse(link).netloc
            return render_template("searchbylink.html",link=link,links=links)
       
        
            
        return render_template("searchbylink.html")
@app.route('/mainpage/searchbylink/result')
def results():
    return render_template("results.html")

@app.route('/login',methods=['POST','GET'])

def login():
    lmsg = "good"
    
    
    userData=""
    if request.method == "POST":

        email = request.form["emailId"]
        password = request.form["password"]
        conn = sql.connect("database.db")
        c=conn.cursor()
        c.execute("select * from users where emailId = '"+email+"' and password='"+password+"'")
        userData = c.fetchall()
        if userData == None:
            lmsg = "AUTHFAILED"
            # take = 0
            return render_template('login.html',message="AUTHFAILED")

        for i in userData:
            if(email==i[0] and password==i[1]):
                session["logedin"] = True
                session["username"] = email
                lmsg='success'
                
                return redirect(url_for("mainpage"))
            # else:
            #     lmsg = "username or password doesnt exist"
            #     return render_template("login.html",message=lmsg)

        
        

    # if take:
    #     return render_template('login.html',message='AUTHFAILED')
    return render_template('login.html',message=lmsg)

@app.route('/anonymous')
def anonymous():
    return render_template("anonymousmainpage.html")
@app.route('/login/signup',methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        if request.form["emailId"] != '' and request.form["password"]!= '':
            email=request.form["emailId"]
            datatp = ''
            password=request.form["password"]
            conn = sql.connect("database.db")
            cur = conn.cursor()
            
            # checkCondition = "select * from users where emailId = (?)"
            cur.execute("select * from users where emailId = (?)",(email,))
           
            data=cur.fetchall()
            if data:
                print(data, file=sys.stdout)
                #app.logger.info('testing info log')
                message = "already exist"
                return render_template("signup.html", message=message)
                
                

            else:
                cur.execute("INSERT INTO users VALUES('"+email+"','"+password+"',0)")
                message = "usercreated"
                conn.commit()
                conn.close()
                return redirect(url_for('login')) 

            

            
            
            
            

        else:
            msg="SW-001"
            return redirect(url_for('mainpage'))
    message = "somethins"
    return render_template("signup.html",message=message)

@app.route('/mainpage/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for("anonymous"))



@app.route('/mainpage/searchbylink/<link>')
def imagelink():
    return redirect(link,code=302)

if __name__ == "__main__":
    app.run(debug=True)


