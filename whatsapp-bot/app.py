from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body", "").lower()

    response = MessagingResponse()
    msg = response.message()

    if incoming_msg == "hi":
        msg.body("hi")
    elif incoming_msg == "help":
        msg.body("Commands:\nhi\nhelp\ninfo")
    elif incoming_msg == "info":
        msg.body("This is a Python WhatsApp Automation Bot 🚀")
    elif:
        msg.body("please Sorry 😔 I didn’t understand.\nType *help*")
    else:
        msg.body("sorry")

    return str(response)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
