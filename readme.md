# Audio Generator Flask API

## Instructions on how to Install and Run the FastAPI Server

✅ Install Requirements
pip install -r requirements.txt
✅ Run the Server
python app.py
✅ Open the Server in your browser
http://localhost:5000/
✅ View the API Documentation
http://localhost:5000/docs

## Requirements

📑 Python 3+
📑 FastAPI
📑 UUID
📑 pydub
📑 uvicorn[standard]
📑 jinja2

📞 If you encounter any issues, please reach out to me
"# audioGeneratorFastAPI"

## Deploying to Heroku

(I have already added the Procfile to the project, so no more configuration is needed)
🔥 Easier Method, Using Github
✅ Create a Github Repository and connect it to your Heroku account
✅ Add this FFMPEG buildpack to your heroku app settings:
https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
✅ Deploy your application to Heroku
