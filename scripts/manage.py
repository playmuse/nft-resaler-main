from tonsdk.boc import Cell, begin_cell, begin_dict
from tonsdk.contract.wallet import Wallets
from tonsdk.utils import Address, to_nano, from_nano
from _utils import send_boc, get_seqno, run_get_method, fetch_items_by_collection
from _secrets import OWNER_SEED, OWNER_WALLET_VERSION

CONTRACT_ADDRESS = 'Received smart contract address'


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

    print(f"Resaler address: {CONTRACT_ADDRESS}")
    command = input("Enter command: ")

    if command == 'edit_price':
        query = wallet.create_transfer_message(
            CONTRACT_ADDRESS, to_nano(0.05, 'ton'), wallet_seqno,
            payload=begin_cell()
                .store_uint(3, 32)
                .store_coins(int(float(input(f"Enter new price in TONs: ")) * 10 ** 9))
                .end_cell()
        )
        send_boc(query['message'].to_boc(False))
        return
    elif command == 'edit_provider':
        query = wallet.create_transfer_message(
            CONTRACT_ADDRESS, to_nano(0.05, 'ton'), wallet_seqno,
            payload=begin_cell()
            .store_uint(4, 32)
            .store_address(Address(input(f"Enter new provider address: ")))
            .end_cell()
        )
        send_boc(query['message'].to_boc(False))
        return
    elif command == 'edit_owner':
        query = wallet.create_transfer_message(
            CONTRACT_ADDRESS, to_nano(0.05, 'ton'), wallet_seqno,
            payload=begin_cell()
            .store_uint(10, 32)
            .store_address(Address(input(f"Enter new owner address: ")))
            .end_cell()
        )
        send_boc(query['message'].to_boc(False))
        return
    elif command == 'withdraw_ton':
        query = wallet.create_transfer_message(
            CONTRACT_ADDRESS, to_nano(0.05, 'ton'), wallet_seqno,
            payload=begin_cell()
            .store_uint(5, 32)
            .store_address(Address(input(f"Enter destination address: ")))
            .store_coins(to_nano(float(input(f"Enter amount in TON: ")), 'ton'))
            .end_cell()
        )
        send_boc(query['message'].to_boc(False))
        return

    return




if __name__ == '__main__':
    main()





