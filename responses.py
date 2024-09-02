def get_chatbot_response(user_message):
    user_message = user_message.lower()

    # Tutorial for First-Time Users
    if "how do i use the payment system" in user_message or "guide me through the payment process" in user_message:
        return (
            "Hello! Welcome to our payment gateway. I'm here to help you navigate the payment process. "
            "First, enter your payment details like card number, expiry date, and CVV. "
            "Then, choose the amount and submit your payment. You will receive a confirmation once the payment is successful. "
            "Would you like to try a demo transaction now?"
        )

    # Fraud Detection Complaints
    elif "fraudulent charge" in user_message or "report fraud" in user_message:
        return (
            "I'm sorry to hear that you suspect fraudulent activity. Please provide the transaction ID or date and amount of the suspicious charge. "
            "Additionally, provide a brief description of the issue and your email address so our fraud team can follow up with you. "
            "An email will be prepared for you, or you can directly contact us at fraudsupport@paymentgateway.com."
        )

    # Payment Confirmation Inquiries
    elif "did my payment go through" in user_message or "confirm my payment" in user_message:
        return (
            "Can you please provide your transaction ID or the email address used for the payment? "
            "If successful, your payment confirmation will be shared shortly. "
            "If there was an issue, you may need to try again or use a different payment method."
        )

    # FAQs about Payment Methods and Security
    elif "what payment methods do you accept" in user_message or "how secure is my payment information" in user_message:
        return (
            "We accept all major credit and debit cards, including Visa, MasterCard, and American Express. "
            "You can also use PayPal for transactions. "
            "Regarding security, all transactions are encrypted using SSL technology and comply with PCI DSS standards. "
            "Would you like more details on our security measures?"
        )

    # Default Response for Unrecognized Queries
    else:
        return (
            "I'm not sure how to respond to that. Could you please rephrase your question, or let me know if you need help with payment, fraud reporting, or something else?"
        )