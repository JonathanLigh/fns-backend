from sqlalchemy import create_engine

db = create_engine("postgresql://localhost:5432/fns")


print(db)