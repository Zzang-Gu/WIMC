import pyodbc

def connectDB():
    conn = pyodbc.connect("DSN=WIMC")
    cur = conn.cursor()

    return cur

def selectCloths(userId, tpCd):
    cur = connectDB()

    # CLOTH_IMG.FILENAME
    # CLOTH_IMG.FILEDATA
    # TEST
    query = f"""
            SELECT
                CLOTH_ID,
                CLOTH_NM,
                TEST,
                (SELECT CD_VALUE FROM WIMC_CODE_INFO WHERE GRP_CD_ID = 'TP_CD' AND CD_ID = TP_CD) AS TP_CD,
                (SELECT CD_VALUE FROM WIMC_CODE_INFO WHERE GRP_CD_ID = 'COLOR_CD' AND CD_ID = COLOR_CD) AS COLOR_CD
            FROM
                WIMC_CLOTH_INFO
            WHERE USER_ID = '{userId}'
            AND TP_CD = '{tpCd}'
    """

    result = cur.execute(query)

    columns = [column[0] for column in cur.description]
    rows = result.fetchall()

    return columns, rows

if __name__ == "__main__":
    columns, rows = selectCloths("20231662", "TOP")

    print(rows[0][2])
    print(rows[0][3])
    print(rows[0][4])

    f = open(rows[0][2], "wb")
    f.write(rows[0][3])
    f.close()

    # print(columns)
    # print(rows)