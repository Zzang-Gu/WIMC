import pyodbc

def connectDB():
    coxn = pyodbc.connect("DSN=WIMC")
    cur = coxn.cursor()

    return cur

def selectData():
    cur = connectDB()

    result = cur.execute("select * from WIMC_CODE_INFO")

    columns = [column[0] for column in cur.description]
    rows = result.fetchall()

    print(columns)
    print(rows)
