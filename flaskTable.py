from flask import Flask
import mysql.connector

app = Flask(__name__)

def showCustomerTable():
    myTable = "<table style=\"width:100\">\n<tr>\n<th>id</th>\n<th>Name</th>\n<th>Address</th>\n</tr>\n"
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
        myTable = myTable + "<tr>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n</tr>".format(row[0],row[1],row[2])
        print(row)
    
    return myTable

print(showCustomerTable())
    
@app.route("/")
def home():
    
    myhtml = '''
<!DOCTYPE html>
<html>
<head>
<scipt src="http://code.jquery.com/jquery-latest.min.js"></script>
<script>
function()
{
    $.ajax({
        type:"get",
        url:"/showCustomerTable",
        datatype:"html",
        success:function(data)
        {
            $( ".showCustomerTable" ).hmtl(data);
        }
    });
};
</script>
</head>
<body>
<h1>Customers</h1>
<div class="showCustomerTable">
This will be replaced
</div>
</body>
</html>
'''
    return myhtml

if(__name__) == "__main__":
    app.run()