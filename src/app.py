
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
    
    try:
        conn = get_db_conn(host="mysql-service.default", user="root", passwd="admin", db="admin")
        cur = conn.cursor()
       # sql"SELECT productname,brand,category,stockstatus,store,quantity FROM products where store=%s"
        cur.execute("SELECT productname,brand,category,stockstatus,store,quantity FROM products where store=%s",store)
        if cur.rowcount:
            data = cur.fetchall()
            return data
        conn.close()
    except Exception as msg:
        print ("Exception : %s"%(msg))
        msg = "Exception while fetching data %s"%(msg)
    

def insert_data():
    try:
        conn = get_db_conn(host="mysql-service.default", user="root", passwd="admin", db="admin")
        cur = conn.cursor()
        sql1 = ("INSERT INTO products (id,productname, brand,category,stockstatus,store,quantity) VALUES (1,\"Iphone\", \"Apple\",\"Phones\",\"In Stock\",\"Grover-de\", 10)")
        cur.execute(sql1)
        sql2 = ("INSERT INTO products (id,productname, brand,category,stockstatus,store,quantity) VALUES (2,\"GalaxyA4\", \"Samsung\",\"Phones\",\"Out Of Stock\",\"Grover-de\", 0)")
        cur.execute(sql2)
        sql3 = ("INSERT INTO products (id,productname, brand,category,stockstatus,store,quantity) VALUES (3,\"Huawei\", \"Apple\",\"Phones\",\"In Stock\",\"mm-Berlin\", 10)")
        cur.execute(sql3)
        sql4 = ("INSERT INTO products (id,productname, brand,category,stockstatus,store,quantity) VALUES (4,\"Iphone\", \"Apple\",\"Phones\",\"Out Of Stock\",\"mm-Berlin\", 0)")
        cur.execute(sql4)
        conn.commit()
        print(cur.rowcount, "Record inserted successfully into products table")
        conn.close()
    except Exception as msg:
        print ("Exception : %s"%(msg))
        msg = "Exception while fetching data %s"%(msg)
    

if __name__ == '__main__':
    db_init(host="mysql-service.default", user="root", passwd="admin", db="admin")
    insert_data()
    app.run(host="0.0.0.0", port=5000)
