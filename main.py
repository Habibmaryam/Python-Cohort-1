from crypto_utils import deposit

# Create an instance
my_deposit = deposit('Maryam')
# Deposit some tokens
my_deposit.deposit('ETH', 5)   
# View balance
print(my_deposit.view_balance())  # Output: {'ETH': 5}