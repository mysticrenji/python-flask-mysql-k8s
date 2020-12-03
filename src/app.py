
from flask import Flask, render_template, request, url_for, flash, redirect,jsonify
import MySQLdb , json
app = Flask(__name__)

conn = ""


def get_db_conn(host, user, passwd, db):
    """
    Get connection to MySQL database
    """
    global conn
    if not conn.open:
        conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    return conn


def db_init(host, user, passwd, db):
    """
    Initialize the database by creating employee table
    """

    global conn
    try:
        conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        cur=conn.cursor()
        cur.execute("show tables like 'products'")
        if not cur.rowcount:
            cur.execute("create table products(id INT(10) NOT NULL AUTO_INCREMENT, productname VARCHAR(30) NOT NULL, brand VARCHAR(30) NOT NULL,category VARCHAR(30) NOT NULL, stockstatus VARCHAR(30) NOT NULL, store VARCHAR(30) NOT NULL, quantity INT(10) NOT NULL, CONSTRAINT id_pk PRIMARY KEY (id),CONSTRAINT uk UNIQUE(productname,store))")
            conn.commit()
            conn.close()
        else:
            print ("Database table already present")
    except Exception as msg:
        print ("Exception while initializing database : %s"%msg)


@app.route('/')
def home():
    """
    Landing Page
    """
    return redirect('/store/Grover-de')

@app.route('/store/Grover-de')
def grover_de():
    """
    Grover DE Page
    """
    products= fetch_data('Grover-de')
    return render_template("homepage.html", products=products)

@app.route('/store/mm-Berlin')
def mm_berlin():
    """
    Grover Berlin Page
    """
    products= fetch_data('mm-Berlin')
    return render_template("homepage.html", products=products)


@app.route('/api/Grover-de')
def api_grover_de():
    """
    Grover DE Page
    """
    products= fetch_data('mm-Berlin')
    return (json.dumps(products,indent=4)) 

@app.route('/api/mm-Berlin')
def api_mm_berlin():
    """
    Grover Berlin Page
    """
    products= fetch_data('mm-Berlin')
    return (json.dumps(products,indent=4)) 

def fetch_data(store):
    data=""
    try:
        conn = get_db_conn(host="mysql-service.default", user="root", passwd="admin", db="admin")
        cur = conn.cursor()
        cur.execute("SELECT productname,brand,category,stockstatus,store,quantity FROM products where store=%s"%store)
        if cur.rowcount:
            data = cur.fetchall()
            return data
        conn.close()
    except Exception as msg:
        print ("Exception : %s"%(msg))
        msg = "Exception while fetching data %s"%(msg)
    return data

def insert_data():
    try:
        conn = get_db_conn(host="mysql-service.default", user="root", passwd="admin", db="admin")
        cur = conn.cursor()
        sql1 = ("INSERT INTO products (id,productname, brand,category,stockstatus,store,quantity) VALUES (1,\"Iphone\", \"Apple\",\"Phones\",\"In Stock\",\"Grover-de\", 10)")
        #val1 = (1,"Iphone", "Apple","Phones","In Stock","Grover-de", 10)
        cur.execute(sql1)
        # val2 = ("Galaxy A4", "Samsung","Phones","In Stock","mm-Berlin", 10)
        # cur.execute(sql, val2)
        conn.commit()
        print(cur.rowcount, "Record inserted successfully into products table")
        conn.close()
    except Exception as msg:
        print ("Exception : %s"%(msg))
        msg = "Exception while fetching data %s"%(msg)
    

# @app.route("/storedata", methods=["POST"])
# def store_data():
#     """
#     Store the employee data in database and return msg
#     """

#     try:
#         conn = get_db_conn(host="mysql-service.default", user="root", passwd="admin", db="admin")
#         cur = conn.cursor()
#         cur.execute("insert into employee values (%s, '%s')"%(request.form['id'], request.form['name']))
#         conn.commit()
#         msg = "Inserted Data for Employee : %s"%(request.form['name'])
#     except Exception as msg:
#         print "Exception : %s"%(msg)
#         msg = "Exception while inserting data %s"%(msg)
#     return msg


# @app.route("/getdata/<int:id>", methods=["GET"])
# def get_data(id):
#     """
#     Get Employee data using Employee ID
#     """

#     try:
#         conn = get_db_conn(host="mysql-service.default", user="root", passwd="admin", db="admin")
#         cur = conn.cursor()
#         cur.execute("select * from employee where id=%d"%id)
#         if cur.rowcount:
#             res = cur.fetchone()
#             msg = "Employee Details ID : %d  Name : %s"%(res[0], res[1])
#         else:
#             msg = "Data for Employee ID : %d not present"%(id)
#     except Exception as msg:
#         print "Exception : %s"%(msg)
#         msg = "Exception while fetching data %s"%(msg)
#     return msg


if __name__ == '__main__':
    db_init(host="mysql-service.default", user="root", passwd="admin", db="admin")
    insert_data()
    app.run(host="0.0.0.0", port=5000)
