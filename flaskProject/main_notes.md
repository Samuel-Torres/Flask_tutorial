other ways of importing and initializing Alchemy:

# SQLite initialization:
# connection = sqlite3.connect("database")
# cursor = connection.cursor()
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS Users (user_id INT, user_name TEXT, password TEXT)
# """
# )
# connection.commit()
# connection.close()

# _______________________________________________

# Alchemy ORM initialization:

# From main.py approach
# engine = create_engine("sqlite:///database")
# Base = declarative_base()

# modular models directory approach: