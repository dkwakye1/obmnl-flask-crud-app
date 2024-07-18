# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id':1, 'date':"2024-8-19", 'amount':10000 },
    {'id': 2, 'date': "2024-4-22", 'amount': 20000},
    {'id': 3, 'date': "2024-5-19", 'amount': -19000},
    {'id': 4, 'date': "2024-6-25", 'amount': 17900},
]

# Read operation
@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions=transactions)

# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        id = len(transactions)+1
        date = request.form['date']
        amount = float(request.form['amount'])
        data = {'id':id, 'date':date, 'amount':amount}
        transactions.append(data)
        return redirect(url_for('get_transactions'))

# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'GET':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template('edit.html', transaction=transaction)


    if request.method == 'POST':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                date = request.form['date']
                amount = float(request.form['amount'])
                transaction['date'] = date
                transaction['amount'] = amount
                break
        return redirect(url_for('get_transactions'))

# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    return redirect(url_for('get_transactions'))

# Run the Flask app
if __name__ == "__main__":
    app.run()
    