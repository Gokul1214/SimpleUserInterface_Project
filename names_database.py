import pyodbc

class Database:
    _connection = None

    @classmethod
    def connect(cls):
        if cls._connection == None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'NAMES'
            username = '275student'
            password = '275student'
            cls._connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database
                + ';UID=' + username + ';PWD=' + password)

    @classmethod
    def fetch_gender(cls):
        from names_show import ShowGender

        sql = '''
        SELECT DISTINCT Gender
        FROM year_gender_totals
        '''

        cls.connect()
        cursor = cls._connection.cursor()
        cursor.execute(sql)
        genders = []
        gender = cursor.fetchone()
        while gender:
            genders.append(ShowGender(gender[0]))
            gender = cursor.fetchone()
        return genders

    @classmethod
    def fetch_names(cls, gender, name):
        from names_show import Names

        sql = '''
        SELECT Name, Year, Gender, NameCount, Total
        FROM all_data
        WHERE Name = ?
        AND Gender = ?
        ORDER BY Year;
        '''
        cls.connect()
        cursor = cls._connection.cursor()

        if (gender == '-- All Genders --'):
            sql = '''
            SELECT Name, Year, Gender, NameCount, Total
            FROM all_data
            WHERE Name = ?
            ORDER BY Year;
            '''
            cursor.execute(sql, name)
        else:
            cursor.execute(sql, name, gender)
        names = []
        results = cursor.fetchall()
        for row in results:
            names.append(Names(row[0], row[1], row[2], row[3], row[4]))
        return names