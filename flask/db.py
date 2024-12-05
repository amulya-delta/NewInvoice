from sqlalchemy import create_engine
import urllib.parse

# db_username = 'admin'
# db_password = 'deltapython2024'
# db_host = 'database-1.cfwei84gm8z1.ap-southeast-2.rds.amazonaws.com'
# db_port = '3306'
# db_name = 'mfg_tool'

db_username = 'admin'
db_password = 'Delta_2024'
db_host = 'deltainvoice.ct0g6qeuke9e.us-east-1.rds.amazonaws.com'
db_port = '3306'
db_name = 'details'
# db_username = 'root'
# db_password = 'new_password'
# db_host = 'localhost'
# db_port = '3306'
# db_name = 'invoicedetails'

url_passord=urllib.parse.quote(db_password)

db_url = f'mysql+mysqlconnector://{db_username}:{url_passord}@{db_host}:{db_port}/{db_name}'

engine = create_engine(db_url)


try:
    with engine.connect() as connection:
        print("Connection to MySQL database successful!")
except Exception as e:
    print(f"Error connecting to MySQL database: {e}")


