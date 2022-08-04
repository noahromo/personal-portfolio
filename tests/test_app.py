import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Portfolio</title>" in html
        # Team name
        assert "Welcome!" in html
        # Member names
        assert "Juan" in html
        assert "Malik" in html
        assert "Noah" in html
    
    def test_timeline(self):
        # GET
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # POST
        response = self.client.post("/api/timeline_post", data={
            "name": "Noah Romo",
            "email": "noahromo@test.com",
            "content": "This is a test."
        })
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json.get("name") == "Noah Romo"  
        assert json.get("email") == "noahromo@test.com"
        assert json.get("content") == "This is a test."
        # GET
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert len(json["timeline_posts"]) == 1
        # Timeline Page
        response = self.client.get("/timeline")
        html = response.get_data(as_text = True)
        assert 'name="name"' in html
        assert 'name="email"' in html
        assert 'name="content"' in html
        assert 'type="submit"' in html
    
    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post('/api/timeline_post', data={
            'email': 'john@example.com',
            'content': "Hello World, I'm John!",
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "john@example.com",
            "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
            "name": "John Doe",
            "email": "not-an-email",
            "content": "Hello World, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
