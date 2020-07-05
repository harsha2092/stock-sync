import psycopg2

def writeToPostgresFromCsvFile(fileName, tableName):
    #TODO: need to write to config and keep it as env/secret before uploading to git or going live
    conn = psycopg2.connect("host=localhost dbname=stock_analysis user=postgres password=admin")
    cur = conn.cursor()

    print("uploading file " + fileName + " to table " + tableName + " in stock_analysis db")
    with open(fileName, 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, tableName, sep=',')
        conn.commit()