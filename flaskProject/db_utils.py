"""
Database utility functions and CLI commands for managing the database.

flask drop-tables
flask create-tables
flask reset-users
flask seed-users
"""

import os
from flaskProject.db_setup import init_db, Base, Session
from dotenv import load_dotenv
load_dotenv()
import click
from flaskProject.models.users_model import Users

DATABASE_URL = os.getenv("DB_URL")
init_db(DATABASE_URL)


# Make sure DB is initialized
def register_cli_commands(app, bcrypt, db_url):
    engine = init_db(db_url)  

    @app.cli.command("drop-tables")
    def drop_tables():
        Base.metadata.drop_all(bind=engine)
        click.echo("All tables dropped.")

    @app.cli.command("create-tables")
    def create_tables():
        Base.metadata.create_all(bind=engine)
        click.echo("All tables created.")

    @app.cli.command("reset-users")
    def reset_users_table():
        Users.__table__.drop(bind=engine)
        Users.__table__.create(bind=engine)
        click.echo("Users table reset.")

    @app.cli.command("seed-users")
    def seed_users():
        session = Session()
        try:
            user = Users(
                user_name="testuser",
                password=bcrypt.generate_password_hash("password123").decode("utf-8")
            )
            session.add(user)
            session.commit()
            click.echo(f"User {user.user_name} created")
        except Exception as e:
            session.rollback()
            click.echo(f"Error seeding user: {e}")
        finally:
            session.close()