from mysql.connector import connect

con = connect(host="localhost", user="root", passwd="<PASSWORD>", database="DB")

cur = con.cursor(dictionary=True)
cur.execute("SELECT * FROM Touriste")

dico = cur.fetchone()

print(dico)