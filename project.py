from flask import Flask, render_template, request
import stripe

#web: PUBLISHABLE_KEY=pk_test_6pRNASCoBOKtIshFeQd4XMUh SECRET_KEY=MadNessSecretKeyed10!!!233!21OK python project.py
PUBLISHABLE_KEY="pk_test_6pRNASCoBOKtIshFeQd4XMUh"
SECRET_KEY="sk_test_BQokikJOvBiI2HlWgH4olfQ2"

# stripe_keys = {
#     'secret_key': os.environ['SECRET_KEY'],
#     'publishable_key': os.environ['PUBLISHABLE_KEY']
# }

stripe_keys = {
	'secret_key': SECRET_KEY,
	'publishable_key': PUBLISHABLE_KEY
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)
app.secret_key = 'MadNessSecretKeyed10!!!233!21OK'

@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    #Can use a get on the dropdown to choose the product to sell to the individual
    #We just need to get the one used in the form then change the logic below to reflect the other product
    amount = 2200

    customer = stripe.Customer.create(
        email='customer@example.com',
        #email =request.form['email'],
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Shampoo'
    )

    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
	app.run(debug=False)

