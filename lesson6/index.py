from  flask  import  Flask , render_template , request , redirect , url_for , session
import mysql.connector

dbset =  mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="adgjl147",
    database="website",
    charset='utf8',
    buffered=True
    )
mycursor = dbset.cursor()

app = Flask ( __name__ )
app.secret_key = b' \xcc \xdf U \xad # \xb2 \n \xa9 \xde \x1e \xe1 |'
  
@app.route ( "/" )
def  index ():                 
    return  render_template ( "signin.html" )
    
 #註冊 
@app.route ( "/signup" , methods = [ "POST" ])
def  signup (): 
    mycursor.execute ("SELECT username FROM user") #在表單找資料
    username = mycursor.fetchall() #找到的username
    print (type(username))
    # print (type(request.values[ "username" ]))
    # print (type(request.values[ "username" ]))
    # print (username)
    # print (request.values[ "username" ])
    if (str(request.values[ "username" ]),) not in username: 
        #把資料庫的username和用戶輸入的username比較，如果沒有就寫入，如果資料庫有就去錯誤頁
       sql = "INSERT INTO user (name, username, password) VALUES (%s, %s, %s)" #對資料庫寫入姓名、帳號、密碼的欄位
       val = (request.values[ "name" ],request.values[ "username" ],request.values[ "password" ])
       mycursor.execute(sql, val)
       dbset.commit()
       return render_template ( "signin.html" )
    else:
       return redirect ("/error/?message=帳號已經被註冊")
    
# 登入 
@app.route ( "/signin" , methods = [ "POST" ])
def  signin ():
    session[ "username" ]= request.values[ "username" ]#session就是把用戶輸入的資料放入空間
    session[ "password" ]= request.values[ "password" ] 
    mycursor.execute ("SELECT name, username, password FROM user")
    result = mycursor.fetchall() #找到所有資料，往下做比較
    # print(result)
    for i in range(len(result)):
        print(type(result[i][1]))
        if result[i][1] == request.values["username"] and result[i][2] == request.values["password"]:
            session["name"] = result[i][0]
            return redirect("/member")
    return redirect("/error/?message=帳號與密碼錯誤") 
    #到錯誤頁面的判斷條件在登入時就要做，此時訊息名稱message要與錯誤頁面的訊息指令相同，才抓得到資料

#登入成功
@app.route ( "/member" )
def  member ():
    if  session.get ( "user" ):
        return  render_template ( "member.html", nametitle=session[ "name" ] )
    else :
        return  redirect ( "/" )

#登入失敗    
@app.route ( "/error/" )
def  error ():
    msgtxt=request.args.get("message")
    return  render_template ( "error.html" )

#登出    
@app.route ( "/signout" )
def  signout ():
    session.pop ( "user" , None )
    return  redirect ( url_for ( "index" ))
    
if  __name__ == "__main__" :
    app.run ( port = '3000' , debug = True )
    