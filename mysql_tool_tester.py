# import mysql
# import mysql.connector
from mysql_tools import easy_sql

esql = easy_sql(db="arduino_stackexchange_com")
# dbc.database = "english_stackexchange_com"
print(esql.database)


query = """SELECT MAX(Score) FROM Posts;"""

df = esql.query_to_pandas(query)

print(df.head())
