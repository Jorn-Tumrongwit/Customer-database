from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def showCustomerTable():
    myTable = '''
    <!DOCTYPE html>
    <html>
    <head>
    <scipt src="http://code.jquery.com/jquery-latest.min.js"></script>

    </head>
    <body>
    <center>
    <h1>Customers</h1>
    <table border="1">
        <tr>
            <b><th>id</th>
            <th>Name</th>
            <th>Address</th></b>
        </tr>
    '''
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="gamz"
    )

    print(mydb)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    
    mycursor.execute("SELECT * FROM CUSTOMERS ORDER BY id;")
    myresultShow = mycursor.fetchall()
    for row in myresultShow:
        myTable = myTable + '''
        <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
        '''.format(row[0],row[1],row[2])
        print(row)
        
    myTable = myTable + '''
    </center>
    </body>
    </html>
    '''
    
    return myTable


if __name__ == "__main__":
    app.run()