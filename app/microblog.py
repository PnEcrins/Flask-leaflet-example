from app import app, DB
from app.models import User

@app.shell_context_processor
def make_shell_context():
    return {'DB': DB, 'User': User}