# Bullshitbingogpt

Bullshitbingogpt is the application for reviewing your original idea in a funny-form (like a game).
You can enter your text and our algorithm extract the theme and create a bullshit-bingo for it.
After it compare it with your text and give you the result: how much buzzwords you have.
It uses OpenAI for text processing and don't store your data.

Start app:
```
pip install -r requirements.txt
flask --app app run
```

Docker:
```
docker build -t bullshitbingogpt .
docker run -p80:80 -it bullshitbingogpt:latest
docker tag bullshitbingogpt:latest us-central1-docker.pkg.dev/bullshitbingogpt/bullshitbingogpt/bullshitbingogpt
docker push us-central1-docker.pkg.dev/bullshitbingogpt/bullshitbingogpt/bullshitbingogpt:latest
```