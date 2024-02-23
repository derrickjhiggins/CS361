def generate(client, filepath, additionalDirections=None):
    # define initial prompt and messages
    prompt = "You are on a date with someone you just met. Start a conversation about interests and hobbies."
    messages =[
        {"role": "system", "content": "You are a helpful and flirty dating assistant. You are smart but also kind and funny, and like to banter."},
        {"role": "user", "content": "Give me a clever icebreaker message for a dating app. Tell me something you've never said before."},
    ]

    # check if filepath contains previous conversation text or additional directions provided
    if filepath:
        with open(filepath, 'r') as previousConversation:
            messages.append({"role": "user", "content": ''.join(previousConversation.readlines())})
    if additionalDirections:
        messages.append({"role": "user", "content": additionalDirections})
    
    # generate response
    stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    stream=True
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
