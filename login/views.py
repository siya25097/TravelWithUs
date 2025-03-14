from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''

# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Khushi@1298",database='sample')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from user where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        user_data=tuple(cursor.fetchall())
        if not user_data:
            return render(request, 'travel/error.html')
        else:
            first_name = user_data[0][0]  # Assuming first_name is the first column
            last_name = user_data[0][1]    # Assuming last_name is the second column
            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            logged_in_user = {'username': em, 'first_name': first_name, 'last_name': last_name}
            return render(request, 'travel/home.html', {'user': logged_in_user})
    
    return render(request,'travel/login_page.html')