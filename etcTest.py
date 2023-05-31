import etcDb
import pyodbc

if __name__ == "__main__":
    # columns, rows = db.selectCloths("20231662", "TOP")

    # print(rows[0][2])
    # print(rows[0][3])
    # print(rows[0][4])

    # f = open(rows[0][2], "wb")
    # f.write(rows[0][3])
    # f.close()

    # print(columns)
    # print(rows)

    # for idx in range(3, 11, 1):
    #     f = open(".\\img\\test\\"+str(idx)+".png", "rb")
    #     bindata = f.read()

    #     db.insertCloths("20231662", "TEST"+str(idx)+"", pyodbc.Binary(bindata), "TOP", "0E0E0E", "20230531", "20230531")

    f = open(".\\img\\test\\0.png", "rb")
    bindata = f.read()

    etcDb.updateCloths(2, "20231662", "TEST0", pyodbc.Binary(bindata), "TOP", "0E0E0E", "20230531", "20230531")