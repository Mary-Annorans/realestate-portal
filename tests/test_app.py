import sys
import os

# Add the parent directory to Python path so "src" can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    
    assert response.status_code == 200
    assert b"Welcome to Real Estate Portal!" in response.data


