import pyodbc
#server
server = 'tcp:tloy1966.database.windows.net,1433'
database = 'RealPrice'
username = 'tloy1966'
password = '!123451966ccC'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
class sqlTest:
    def __init__(self):
        print ('init')        
def testSql():
    cursor = cnxn.cursor()
    cursor.execute("select top 1 * from dbo.maindata")
    row = cursor.fetchone()
    while row:
        print (row[2])
        row = cursor.fetchone()
    
def getDate():
    cursor = cnxn.cursor()
    cursor.execute("select top 17 * from dbo.maindata where city = 'A' and selltype = 'A'")
    data = cursor.fetchall()
    return data;
