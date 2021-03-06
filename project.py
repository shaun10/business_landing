import os
from flask import Flask, render_template, request
import stripe


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

itemsAvail = {'shampoo':2400, 'conditioner':2600,'leaveInConditioner':2900}

@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/chargeSha', methods=['POST'])
def chargeSha():
    # Amount in cents
    #Can use a get on the dropdown to choose the product to sell to the individual
    #We just need to get the one used in the form then change the logic below to reflect the other product
    amount = 2400

    customer = stripe.Customer.create(
        email='order@.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description="Shampoo Purchase"
        
    )

    return render_template('charge.html', amount=int(amount/100))

@app.route('/chargeCon', methods=['POST'])
def chargeCon():
    # Amount in cents
    #Can use a get on the dropdown to choose the product to sell to the individual
    #We just need to get the one used in the form then change the logic below to reflect the other product
    amount = 2600
    customer = stripe.Customer.create(
        email='order@.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description="Conditioner Purchase"
    )

    return render_template('charge.html', amount=int(amount/100))

@app.route('/chargeLeave', methods=['POST'])
def chargeLeave():
    # Amount in cents
    #Can use a get on the dropdown to choose the product to sell to the individual
    #We just need to get the one used in the form then change the logic below to reflect the other product
    amount = 2900

    customer = stripe.Customer.create(
        email='order@.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description="Leave in Conditioner Purchase"
        
    )

    return render_template('charge.html', amount=int(amount/100))

if __name__ == '__main__':
	#app.run(debug=True)
	app.run(host='0.0.0.0', port=int(os.environ.get("PORT")))

