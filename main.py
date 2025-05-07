import psycopg2
conn = psycopg2.connect(dbname='mydb', user='postgres', host='localhost', password='723723', port=5432)
if conn:
    print("Connected to PostgreSQL")

cur = conn.cursor()
m_name = input("Введите название станка: ")
machine_type =  input("Введите тип станка: ")
status = input("Введите статус станка: ")
sql = f"INSERT INTO machines(m_name, machine_type, status) VALUES (%s, %s, %s)"
cur.execute(sql, (m_name, machine_type, status))
#conn.commit()

cur = conn.cursor()
cur.execute('SELECT * FROM machines')
results = cur.fetchall()
print(results)

cur.close()
conn.close()