from pyrogram import Client

app = Client('my_bot')


with app:
    print(app.get_me())


@app.on_message()
def my_function(client, message):
    print(message)
    app.forward_messages(422188879, message_ids=message.message_id, from_chat_id=message.from_user.id)


app.run()
