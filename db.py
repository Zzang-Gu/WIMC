import pyodbc
from PIL import Image
import os

def connectDB():
    conn = pyodbc.connect("DSN=WIMC")
    cur = conn.cursor()

    return cur

def selectCloths(userId, tpCd):
    cur = connectDB()

    query = """
            SELECT
                CLOTH_ID,
                CLOTH_NM,
                CLOTH_IMG,
                (SELECT CD_VALUE FROM WIMC_CODE_INFO WHERE GRP_CD_ID = 'TP_CD' AND CD_ID = TP_CD) AS TP_CD,
                (SELECT CD_VALUE FROM WIMC_CODE_INFO WHERE GRP_CD_ID = 'COLOR_CD' AND CD_ID = COLOR_CD) AS COLOR_CD
            FROM
                WIMC_CLOTH_INFO
            WHERE USER_ID = ?
            AND TP_CD = ?
        """

    result = cur.execute(query, (userId, tpCd))

    columns = [column[0] for column in cur.description]
    rows = result.fetchall()

    return columns, rows

def updateCloths(clothId, userId, clothNm, clothImg, tpCd, colorCd, prchsDe, lastUseDe):
    cur = connectDB()

    # CLOTH_IMG.FILENAME
    # CLOTH_IMG.FILEDATA
    # TEST
    query = """
            UPDATE
                WIMC_CLOTH_INFO
            SET
                USER_ID = ?,
                CLOTH_NM = ?,
                CLOTH_IMG = ?,
                TP_CD = ?,
                COLOR_CD = ?,
                PRCHS_DE = ?,
                LAST_USE_DE = ?
            WHERE
                CLOTH_ID = ?
    """

    # print(query)

    record = (userId, clothNm, clothImg, tpCd, colorCd, prchsDe, lastUseDe, clothId)
    # print(type(record))
    # print(record)
    # '20231662', 'TEST2', 'TOP', '0E0E0E', '20230531', '20230531'

    cur.execute(query, record)
    cur.commit()

if __name__ == "__main__":
    # columns, rows = selectCloths("20231662", "TOP")

    # print(rows[0][2])
    # print(rows[0][3])
    # print(rows[0][4])

    # f = open(rows[0][2], "wb")
    # f.write(rows[0][3])
    # f.close()

    # print(columns)
    # print(rows)

    # f = Image.open(".\\img\\myCloset\\test174x178.png", "r")
    # f.show()

    f = open(".\\img\\myCloset\\test174x178.png", "rb")
    with open(".\\img\\myCloset\\test174x178.png", 'rb'):
        bindata = f.read()

    updateCloths(2, "20231662", "TEST2", pyodbc.Binary(bindata), "TOP", "0E0E0E", "20230531", "20230531")

