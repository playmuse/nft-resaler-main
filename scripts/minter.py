

from tonsdk.boc import Cell, begin_cell
from tonsdk.contract.wallet import Wallets
from tonsdk.utils import Address, to_nano, from_nano
from _utils import send_boc, get_seqno, run_get_method
from _resaler import NFTResaler
from _secrets import OWNER_SEED, OWNER_WALLET_VERSION


def main():
    _, pk, sk, wallet = Wallets.from_mnemonics(OWNER_SEED.split(' '), OWNER_WALLET_VERSION)
    wallet_address = wallet.address.to_string(1, 1, 1)
    wallet_seqno = get_seqno(wallet_address)
    print(f"Wallet address: {wallet_address} | Seqno: {wallet_seqno}")
    if wallet_seqno == 0:
        print("Wallet is not deployed. Deploying...")
        send_boc(
            wallet.create_init_external_message()['message'].to_boc(False)
        )
        main()
        return

    collection = NFTResaler(
        owner_address=wallet.address
    )
    print(f"Resaler address: {collection.address.to_string(1, 1, 1)}")

    query = wallet.create_transfer_message(
        collection.address.to_string(True, True, True), to_nano(0.05, 'ton'), wallet_seqno,
        state_init=collection.create_state_init()['state_init'],
        payload=begin_cell().store_uint(7, 32).end_cell()
    )
    send_boc(query['message'].to_boc(False))
    return






if __name__ == '__main__':
    main()




