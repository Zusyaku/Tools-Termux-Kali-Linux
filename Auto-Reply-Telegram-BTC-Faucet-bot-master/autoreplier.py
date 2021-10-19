import time
from telethon import TelegramClient, events

# sample API_ID from https://github.com/telegramdesktop/tdesktop/blob/f98fdeab3fb2ba6f55daf8481595f879729d1b84/Telegram/SourceFiles/config.h#L220
# or use your own
api_id = 17349
api_hash = '344583e45741c457fe1862106095a5eb'

# fill in your own details here
phone = 'PHONE_NUMBER_WITH_PREFIX'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'  # if you have two-step verification enabled

# content of the automatic reply
message = "/faucet"

def main():

    # Create the client and connect
    client = TelegramClient(username, api_id, api_hash, update_workers=1, spawn_read_thread=False)
    client.start(phone, password)

    @client.on(events.NewMessage(incoming=True))
    def _(event):
        if event.is_private:

            # from_id is the id of the bot
            # to check the id you can print(event.message.from_id) and get a message in the chat
            # so you will have the id of that conversation
            # CHANGE 123456789 WITH THE BOT BTC FAUCET FROM_ID
            if event.message.from_id == 123456789:
                if "balance" in event.message.message:
                    # it prints the balance in console
                    print(event.message.message[event.message.message.index("balance"):])
                time.sleep(29)  # pause for 29 second to rate-limit automatic replies
                # it sends the message after time.sleep()
                client.send_message(event.message.from_id, message)
                # it prints the sending time
                print('Sent...',time.asctime())
            # your from_id, the id of the conversation with yourself
            # used to turn off the script from a telegram client
            # CHANGE 123456789 WITH YOUR FROM_ID
            elif event.message.from_id == 123456789:
                # check if the message sent is equals to "TURNOFFTHESCRIPT"
                if (event.is_private and event.message.message == "TURNOFFTHESCRIPT"):
                    newmessage = "Ok Boss, turning off!"
                    # it sends the message
                    client.send_message(event.message.from_id, newmessage)
                    # disconnect the client
                    client.disconnect()

    print(time.asctime(), '-', 'Auto-replying...')
    client.idle()
    client.disconnect()
    print(time.asctime(), '-', 'Stopped!')


if __name__ == '__main__':
    main()
