from sqlalchemy import create_engine, MetaData

SQLALCHEMY_DATABASE_URI:str = 'mysql+pymysql://root@localhost:3306/master'

engine = create_engine(SQLALCHEMY_DATABASE_URI)
meta = MetaData()
conn = engine.connect()