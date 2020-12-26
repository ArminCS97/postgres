import os
from database.database import DATABASE_URL


result = os.popen('flask-sqlacodegen {}'.format(DATABASE_URL)).read()

f = open('models.py', 'w')
f.write(str(result))
f.close()
