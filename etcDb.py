import pyodbc

def connectDB():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=.\WIMC.accdb;')
    cur = conn.cursor()

    return cur

def selectCloths(userId, tpCd):
    cur = connectDB()

    query = """
            SELECT
                CLOTH_ID,
                CLOTH_NM,
                CLOTH_IMG,
                TP_CD,
                (SELECT CD_VALUE FROM WIMC_CODE_INFO WHERE GRP_CD_ID = 'TP_CD' AND CD_ID = TP_CD) AS TP,
                COLOR_CD,
                (SELECT CD_VALUE FROM WIMC_CODE_INFO WHERE GRP_CD_ID = 'COLOR_CD' AND CD_ID = COLOR_CD) AS COLOR,
                PRCHS_DE,
                LAST_USE_DE
            FROM
                WIMC_CLOTH_INFO
            WHERE USER_ID = ?
            AND (TP_CD = ? OR 'ALL' = ?)
            ORDER BY CLOTH_ID
        """

    result = cur.execute(query, (userId, tpCd, tpCd))

    columns = [column[0] for column in cur.description]
    rows = result.fetchall()

    return columns, rows

def updateCloth(clothId, clothNm, clothImg, tpCd, colorCd, prchsDe, lastUseDe):
    cur = connectDB()

    query = """
            UPDATE
                WIMC_CLOTH_INFO
            SET
                CLOTH_NM = ?,
                CLOTH_IMG = ?,
                TP_CD = ?,
                COLOR_CD = ?,
                PRCHS_DE = ?,
                LAST_USE_DE = ?
            WHERE
                CLOTH_ID = ?
    """

    record = (clothNm, clothImg, tpCd, colorCd, prchsDe, lastUseDe, clothId)

    cur.execute(query, record)
    cur.commit()

def insertCloth(userId, clothNm, clothImg, tpCd, colorCd, prchsDe):
    cur = connectDB()

    query = """
            INSERT INTO WIMC_CLOTH_INFO (USER_ID, CLOTH_NM, CLOTH_IMG, TP_CD, COLOR_CD, PRCHS_DE, LAST_USE_DE)
            VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    record = (userId, clothNm, clothImg, tpCd, colorCd, prchsDe, prchsDe)

    print(query, record)

    cur.execute(query, record)
    cur.commit()

def deleteCloths(clothIdList):
    cur = connectDB()

    query = "DELETE FROM WIMC_CLOTH_INFO WHERE CLOTH_ID IN ("

    for _ in range(len(clothIdList)):
        query = query + "?,"

    query = query[:-1] + ")"

    record = tuple(clothIdList)

    print(query, record)

    cur.execute(query, record)
    cur.commit()

def selectUser(userId):
    cur = connectDB()

    query = """
        SELECT 
            * 
        FROM
            WIMC_USER_INFO
        WHERE
            USER_ID = ?
    """

    record = (userId)
    result = cur.execute(query, record)

    columns = [column[0] for column in cur.description]
    rows = result.fetchall()

    return rows

def updateProfile(userId, userName, userGender, userBirthDate):
    cur = connectDB()

    query = """
        UPDATE
            WIMC_USER_INFO
        SET
            USER_NM = ?,
            SEX_CD = ?,
            BRTHD_DE = ?
        WHERE
            USER_ID = ?
    """

    record = (userName, userGender, userBirthDate, userId)

    cur.execute(query, record)
    cur.commit()

def selectColorCd():
    cur = connectDB()

    query = """
        SELECT CD_ID, CD_VALUE
        FROM WIMC_CODE_INFO
        WHERE GRP_CD_ID = 'COLOR_CD'
        ORDER BY SORT_NO
    """

    result = cur.execute(query)

    columns = [column[0] for column in cur.description]
    rows = result.fetchall()

    return rows
