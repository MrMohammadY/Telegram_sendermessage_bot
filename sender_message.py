from pyrogram import Client

app = Client('my_bot')


with app:
    print(app.get_me())


@app.on_message()
def my_function(client, message):
    if message.from_user.id != 422188879:  # Edit this for Your id
        print(message)
        app.forward_messages(422188879, message_ids=message.message_id, from_chat_id=message.from_user.id)  # Edit this for Your id

    if message.from_user.id == 422188879:  # Edit this for Your id
        if message.text:
            app.send_message(message.reply_to_message.forward_from.id, message.text)
        elif message.photo:
            app.send_photo(message.reply_to_message.forward_from.id, message.photo.file_id, caption=message.caption if message.caption else '')
        elif message.video:
            app.send_video(message.reply_to_message.forward_from.id, message.video.file_id, caption=message.caption if message.caption else '')
        elif message.voice:
            app.send_voice(message.reply_to_message.forward_from.id, message.voice.file_id, caption=message.caption if message.caption else '')
        elif message.sticker:
            app.send_sticker(message.reply_to_message.forward_from.id, message.sticker.file_id,)
        elif message.location:
            app.send_location(message.reply_to_message.forward_from.id, longitude=message.location.longitude, latitude=message.location.latitude)
        elif message.animation:
            app.send_animation(message.reply_to_message.forward_from.id, message.animation.file_id)


app.run()
