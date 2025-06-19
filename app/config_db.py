from app import db, create_app
from app.models import users, region, local

app = create_app()

with app.app_context():
    db.create_all()
    print("Banco de dados criado com sucesso.")
