# Bullshitbingogpt

Bullshitbingogpt is the application for reviewing your original idea in a funny-form (like a game).
You can enter your text and our algorithm extract the theme and create a bullshit-bingo for it.
After it compare it with your text and give you the result: how much buzzwords you have.
It uses OpenAI for text processing and don't store your data.

Start app:
```
flask --app app run
```

Docker:
```
docker build -t bullshitbingogpt .
docker run -it bullshitbingogpt:latest
```