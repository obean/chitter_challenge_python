import os

from app import create_app

config_name = os.getenv('APP_SETTINGS')

app = create_app(config_name)
app.secret_key = os.getenv('SECRET')

if __name__ == '__main__':
  app.run()