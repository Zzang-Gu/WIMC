import pyodbc

def connectDB():
    # conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=.\WIMC.accdb;')
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
            AND (TP_CD = ? OR 'ALL' = ?)
        """

    result = cur.execute(query, (userId, tpCd, tpCd))

    columns = [column[0] for column in cur.description]
    rows = result.fetchall()

    return columns, rows

def updateCloths(clothId, userId, clothNm, clothImg, tpCd, colorCd, prchsDe, lastUseDe):
    cur = connectDB()

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

    record = (userId, clothNm, clothImg, tpCd, colorCd, prchsDe, lastUseDe, clothId)

    cur.execute(query, record)
    cur.commit()

def insertCloths(userId, clothNm, clothImg, tpCd, colorCd, prchsDe, lastUseDe):
    cur = connectDB()

    query = """
            INSERT INTO WIMC_CLOTH_INFO (USER_ID, CLOTH_NM, CLOTH_IMG, TP_CD, COLOR_CD, PRCHS_DE, LAST_USE_DE)
            VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    record = (userId, clothNm, clothImg, tpCd, colorCd, prchsDe, lastUseDe)

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

    print(query, record)

    cur.execute(query, record)
    cur.commit()