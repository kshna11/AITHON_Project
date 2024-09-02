from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a database model for storing transactions
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_holder_name = db.Column(db.String(100), nullable=False)
    credit_card_no = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Transaction {self.id}>'

# Define a function to check if a message is legitimate
def check_message_legit(message):
    return message in legit_messages

# Define a function to check if a payment URL is legitimate
def check_url_legit(url):
    return url in legit_urls

@app.route("/chatbot")
def donation_page():
    return render_template('chatbot.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        # Get input from the form
        account_holder_name = request.form['account_holder_name']
        credit_card_no = request.form['credit_card_no']
        amount = float(request.form['amount'])
        payment_url = request.form['payment_url']

        # Check if the payment URL is legitimate
        if check_url_legit(payment_url):
            # Save the successful transaction to the database
            new_transaction = Transaction(
                account_holder_name=account_holder_name,
                credit_card_no=credit_card_no,
                amount=amount,
                payment_url=payment_url
            )
            db.session.add(new_transaction)
            db.session.commit()
            return render_template('success.html')
        else:
            return render_template('fraud.html')
    else:
        return render_template('payment.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        # Get input from the form
        input_message = request.form['message']

        # Check if the message is legitimate
        if check_message_legit(input_message):
            return render_template('fraud1.html')
        else:
            return render_template('legit.html')
    else:
        return render_template('message.html')

# Define a set of legitimate payment URLs
legit_urls = {
    "https://www.paypal.com/",
    "https://www.stripe.com/",
    "https://www.venmo.com/",
    "https://www.square.com/",
    "https://www.cashfree.com/",
    "https://www.billdesk.com/",
    "https://payu.in/",
    "https://www.ccavenue.com/",
    "https://www.instamojo.com/",
    "https://www.direcpay.com/",
    "https://juspay.in/",
    "https://www.epaisa.com/",
    "https://razorpay.com/",
    "https://www.paypal.com",
    "https://www.stripe.com",
    "https://www.venmo.com",
    "https://www.square.com",
    "https://www.cashfree.com",
    "https://www.billdesk.com",
    "https://payu.in",
    "https://www.ccavenue.com",
    "https://www.instamojo.com",
    "https://www.direcpay.com",
    "https://juspay.in",
    "https://www.epaisa.com",
    "https://razorpay.com",
}

# Define a set of legitimate messages
legit_messages = {
     "XXXMobileMovieClub: To use your credit, click the WAP link in the next txt message or click here>> http://wap. xxxmobilemovieclub.com?n=QJKGIGHJJGCBL",
    "URGENT! You have won a 1 week FREE membership in our å£100,000 Prize Jackpot! Txt the word: CLAIM to No: 81010 T&C www.dbuk.net LCCLTD POBOX 4403LDNW1A7RW1",
    "SIX chances to win CASH! From 100 to 20,000 pounds txt> CSH11 and send to 87575. Cost 150p/day, 6days, 16+ TsandCs apply Reply HL 4 info",
    "Urgent UR awarded a complimentary trip to EuroDisinc Trav, Aco&Entry41 Or å£1000. To claim txt DIS to 87121 18+6*å£1.50(moreFrmMob. ShrAcomOrSglSuplt)10, LS1 3AJ",
    "GENT! We are trying to contact you. Last weekends draw shows that you won a å£1000 prize GUARANTEED. Call 09064012160. Claim Code K52. Valid 12hrs only. 150ppm",
    "PRIVATE! Your 2004 Account Statement for 07742676969 shows 786 unredeemed Bonus Points. To claim call 08719180248 Identifier Code: 45239 Expires",
    "URGENT! Your Mobile No. was awarded å£2000 Bonus Caller Prize on 5/9/03 This is our final try to contact U! Call from Landline 09064019788 BOX42WR29C, 150PPM",
    "You are a winner U have been specially selected 2 receive å£1000 or a 4* holiday (flights inc) speak to a live operator 2 claim 0871277810910p/min (18+)",
    "Customer service annoncement. You have a New Years delivery waiting for you. Please call 07046744435 now to arrange delivery",
    "You are a winner U have been specially selected 2 receive å£1000 cash or a 4* holiday (flights inc) speak to a live operator 2 claim 0871277810810",
    "URGENT! We are trying to contact you. Last weekends draw shows that you have won a å£900 prize GUARANTEED. Call 09061701939. Claim code S89. Valid 12hrs only",
    "Please call our customer service representative on FREEPHONE 0808 145 4742 between 9am-11pm as you have WON a guaranteed å£1000 cash or å£5000 prize!",
    "500 New Mobiles from 2004, MUST GO! Txt: NOKIA to No: 89545 & collect yours today!From ONLY å£1 www.4-tc.biz 2optout 087187262701.50gbp/mtmsg18",
    "Congratulations ur awarded 500 of CD vouchers or 125gift guaranteed & Free entry 2 100 wkly draw txt MUSIC to 87066 TnCs www.Ldew.com1win150ppmx3age16",
    "Ur ringtone service has changed! 25 Free credits! Go to club4mobiles.com to choose content now! Stop? txt CLUB STOP to 87070. 150p/wk Club4 PO Box1146, MK45 2WT",
    "HMV BONUS SPECIAL 500 pounds of genuine HMV vouchers to be won. Just answer 4 easy questions. Play Now! Send HMV to 86688 More info:www.100percent-real.com",
    "T-Mobile customer you may now claim your FREE CAMERA PHONE upgrade & a pay & go sim card for your loyalty. Call on 0845 021 3680.Offer ends 28thFeb.T&C's apply",
    "SMS. ac Blind Date 4U!: Rodds1 is 21/m from Aberdeen, United Kingdom. Check Him out http://img. sms. ac/W/icmb3cktz8r7!-4 no Blind Dates send HIDE",
    "REMINDER FROM O2: To get 2.50 pounds free call credit and details of great offers pls reply 2 this text with your valid name, house no and postcode",
    "This is the 2nd time we have tried 2 contact u. U have won the å£750 Pound prize. 2 claim is easy, call 087187272008 NOW1! Only 10p per minute. BT-national-rate",
    # ... (your messages here)
}

if __name__ == '__main__':
    # Create the database and tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
