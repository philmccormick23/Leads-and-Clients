from flask import Flask, render_template, request, redirect, request, session, flash
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('leadsclients')
# now, we may invoke the query_db method

@app.route('/')
def html():
    mysql = connectToMySQL("leadsclients")
    all_leads = mysql.query_db("SELECT * FROM leads")
    print("Fetched all friends", all_leads)
    return render_template('leads.html', leads=all_leads)







print("all the customers and leads", mysql.query_db("SELECT * FROM leads;"))
if __name__ == "__main__":
    app.run(debug=True)