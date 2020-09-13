from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL Configuration
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = ""
app.config["MYSQL_DATABASE_DB"] = "flaskmysql"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config['MYSQL_DATABASE_SOCKET'] = None

mysql.init_app(app)