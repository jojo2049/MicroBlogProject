from app import app, db
from app.models import User, Post

#able to run flask shell without importing repeatedly
@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'User': User, 'Post': Post}
