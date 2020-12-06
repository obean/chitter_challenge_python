# import os
# from app import create_app
# import pytest
# pytest_plugins = ['capybara.pytest_plugin']

# @pytest.fixture
# def app():
  
#   app = create_app(config_name="testing")
#   app.secret_key = os.getenv('SECRET')
#   client = app.test_client()
#   return app