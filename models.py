from pony.orm import Database, Required, set_sql_debug

db = Database()

class Roupa(db.Entity):
    nome = Required(str)
    categoria = Required(str)
    tamanho = Required(str)

db.bind(provider='sqlite', filename='bdroupa.sqlite', create_db=True)

db.generate_mapping(create_tables=True)
set_sql_debug(True)
