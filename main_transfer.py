import xrpl
from xrpl.account import get_balance, get_next_valid_seq_number
from xrpl.clients import JsonRpcClient
from xrpl.ledger import get_latest_validated_ledger_sequence
from xrpl.models.transactions import Payment
from xrpl.transaction import submit_and_wait, autofill_and_sign
from services.xrp_tools import get_minimum_xrp_wallet, xrp_generate_destination_tag, XRPConsts


def transfer(private_key, public_key, my_address, to_address, amount, memo, decimals):

    xrp_wallet = xrpl.wallet.Wallet(private_key=private_key, public_key=public_key)

    client_url = XRPConsts.XRP_MAINNET_URL

    client = JsonRpcClient(client_url)

    current_validated_ledger = get_latest_validated_ledger_sequence(client)

    sequence = int(get_next_valid_seq_number(my_address, client))

    destination_tag = int(memo) if memo else xrp_generate_destination_tag()

    account_balance = get_balance(my_address, client)

    if account_balance < get_minimum_xrp_wallet(decimals):
        return "Balance is insufficient!"

    payment_items = {
        "account": xrp_wallet.classic_address,
        "destination": to_address,
        'amount': str(amount),
        'sequence': sequence,
        'last_ledger_sequence': current_validated_ledger + 20,
        'fee': '10',
        "destination_tag": destination_tag
    }

    tx_payment = Payment(**payment_items)
    signed_tx = autofill_and_sign(tx_payment, client, xrp_wallet)
    tx_response = submit_and_wait(signed_tx, client)
    tx_hash = tx_response.result

    return tx_hash
