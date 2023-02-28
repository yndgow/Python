#skey 2
#opnsfteamcode 3250000
#mgtno CDFI3261032007000001
#opnsvcid 07_24_03_P
#updategbn I
#updatedt 2018-08-31 23:59:59.0
# opnsvcnm 하바나라이브하우스
# bplcnm 600042
# sitepostno 부산광역시 중구 남포동2가 25-10번지 쏠레마빌딩 901호
# sitewhladdr   
# rdnpostno 
# rdnwhladdr
# apvpermymd 
# dcbymd 
# clgstdt 
# clgenddt 
# ropnymd
# trdstatenm
# dtlstatenm
# x
# y
# lastmodts
# uptaenm
# sitetel
# stroomcnt
# bdng


import csv
import pymysql

# Connect to the database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="p3data"
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''CREATE TABLE IF NOT EXISTS csv_data
                 (
                    skey INTEGER, opnsfteamcode INTEGER, mgtno VARCHAR(255), opnsvcid VARCHAR(255), updategbn VARCHAR(255),
                    updatedt VARCHAR(255), opnsvcnm VARCHAR(255), bplcnm VARCHAR(255), sitepostno VARCHAR(255), sitewhladdr VARCHAR(255), 
                    rdnpostno VARCHAR(255), rdnwhladdr VARCHAR(255), apvpermymd VARCHAR(255), dcbymd VARCHAR(255), 
                    clgstdt VARCHAR(255), clgenddt VARCHAR(255), ropnymd VARCHAR(255), trdstatenm VARCHAR(255), dtlstatenm VARCHAR(255), 
                    x VARCHAR(255), y VARCHAR(255), lastmodts VARCHAR(255), uptaenm VARCHAR(255), sitetel VARCHAR(255), 
                    stroomcnt VARCHAR(255), bdng VARCHAR(255)
                 )''')

# Open the CSV file and read its contents
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter='|')
    # Skip the header row if it exists
    next(csv_reader, None)
    # Loop over each row in the file and insert it into the database
    for row in csv_reader:
        cursor.execute('INSERT INTO csv_data VALUES (%s,%s,%s)', row)

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()