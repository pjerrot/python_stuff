
from urllib import request
import time
import pymssql

def download_stock_date(csv_url):
    response = request.urlopen(csv_url) # denne skaber forbindelsen til nettet
    csv = response.read()  # læser den angivne fil
    csv_str = str(csv)  # gemmer indhold som string
    linier = csv_str.split("\\n") # splitter csv filen i linier ved csv filens egne linieskift
    dest_url = r'stock.csv'  # her angives filnavn hvor indhold skal gemmes. Dette kan være 'C:\...'
    fx = open(dest_url ,"w") # laver filen, så den kan skrive til
    for linie in linier:  # her løbes igennem samtlige linier...
        fx.write(linie + '\n') # her skrives hver linie
    fx.close()

today_day = time.strftime("%d")
today_month = time.strftime("%m")
today_year = time.strftime("%Y")


conn = pymssql.connect(server='IVABCRM01\SQLEXPRESS', database='stocksim')
cursor = conn.cursor()

i = 0
symbols = open('symbols.txt' ,'r')
for line in symbols:
    i += 1
    ticker = line[0:line.find("\t")]
    if ticker != "Ticker":
        print(ticker)
        try:
            henturl = "http://real-chart.finance.yahoo.com/table.csv?s=" + ticker + "&d=" + today_day + "&e=" + today_month + "&f=" + today_year + "&g=d&a=2&b=13&c=1986&ignore=.csv"
            download_stock_date(henturl)

            prices = open('stock.csv' ,'r')
            j = 0
            for line in prices:
                j += 1
                if j>1 and len(line)>5 is not None:
                    sql = "insert into stock(ticker, Dato, [Open], High, Low, [Close], Volume,Adj_Close) values('" + ticker + "'," + line + ")"
                    cursor.execute(sql.replace("-", ""))
                    conn.commit()
        except:
            print("Failed")

cursor.close()
conn.close()

#############################
print(sql)
print(henturl)

# GOOGLE VERSION: henturl = "http://www.google.com/finance/historical?cid=304466804484872&startdate=Jul+6%2C+2015&enddate=Jul+18%2C+2016&num=30&output=csv"

cursor.execute('SELECT * FROM stock')

cursor.execute(sql.replace("-", "").replace("\n",""))

rows = cursor.fetchall()

columns = [column[0] for column in cursor.description]

for col in columns:
    print(col)

for row in rows:
    print(row)

conn.commit()



print(sql.replace("-",""))

cursor.execute(sql.replace("-",""))

len(line)
#    ticker = line[0:line.find("\t")]

cursor.execute("insert into stock(ticker, Dato, [Open], High, Low, [Close], Volume,Adj_Close) values('MSFT','20160102',100,120,90,110, 2000,2130)")

cursor.execute("insert into stock(ticker, Dato, [Open], High, Low, [Close], Volume,Adj_Close) values('MSFT','20160102',100,120,90,110, 2000,2100)")
conn.commit()

