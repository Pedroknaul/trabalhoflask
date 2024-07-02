# models.py

from pony.orm import Database, Required, set_sql_debug

db = Database()

class Roupa(db.Entity):
    nome = Required(str)
    categoria = Required(str)
    tamanho = Required(str)

# Conecte-se ao banco de dados SQLite
db.bind(provider='sqlite', filename='bdroupa.sqlite', create_db=True)

# Crie as tabelas
db.generate_mapping(create_tables=True)
set_sql_debug(True)
