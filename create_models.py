import os
from database.database import DATABASE_URL

# --notables after {} can convert the association table for many-to-many relations into
# a class. (No difference between them here as both Table or Class as associative intermediary
# works as the metadata holder and we do not need to insert anything into association
result = os.popen('flask-sqlacodegen {}'.format(DATABASE_URL)).read()

f = open('models/models.py', 'w')
f.write(str(result))
f.close()
