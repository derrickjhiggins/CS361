def generate(client):
    prompt = "You are on a date with someone you just met. Start a conversation about interests and hobbies."

    stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful and flirty dating assistant. You are smart but also kind and funny, and like to banter."},
        {"role": "user", "content": "Give me a clever icebreaker message for a dating app."},
    ],
    stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
