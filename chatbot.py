# chatbot.py
def get_chatbot_reply(user_message):
    msg = user_message.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! 👋 How can I assist you today?"
    elif "appointment" in msg:
        return "You can book an appointment on our homepage. Just fill out your name, email, and preferred time!"
    elif "cancel" in msg:
        return "To cancel, please email us at hospital.support@example.com with your Request ID."
    elif "time" in msg or "hours" in msg:
        return "Our hospital operates from 9 AM to 6 PM, Monday to Saturday."
    elif "doctor" in msg:
        return "We have specialists in every department — please tell me which department you want?"
    elif "emergency" in msg:
        return "In an emergency, please call our 24x7 helpline: +91-9876543210 🚑"
    elif "thank" in msg:
        return "You're most welcome! 😊"
    else:
        return "I'm not sure about that 🤔, but you can contact our helpdesk at reception."

