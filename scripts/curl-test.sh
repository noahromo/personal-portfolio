#!/bin/bash

curl -X Post http://localhost:5000/api/timeline_post -d 'name=Test&email=test@test.com&content=Testing my endpoints.'
curl http://localhost:5000/api/timeline_post 
curl -X DELETE http://localhost:5000/api/timeline_post/0
curl http://localhost:5000/api/timeline_post 