#Random sale of NFT

This script is designed to create a smart contract for the random sale of NFT, which you can use in presales or other marketing activities.

When sending an NFT to a smart contract, an NFT can be bought by sending a specified amount in TON. The smart contract will send a random NFT to the buyer.

An example of work here https://playmuse.org/buynft

Fill in the OWNER_SID field in the file _secrets.py , this is the field for the keyword of your admin wallet. The administrator's wallet manages the smart contract and will be its administrator by accessing it using commands.

Run the script manage.py , copy the address of the smart contract that was received when running the script. Paste it into the CONTRACT_ADDRESS field (line 7) in manage.py

An NFT to an address cannot be minted directly to the address of a smart contract. Since an incoming transaction is needed so that the purchase of your NFTs from a smart contract is possible. Send NFT to the smart contract address from the administrator's or provider's wallet

The OWNER can send the NFT (which is specified in _secrets.py ) or PROVIDER
In order to change OWNER to PROVIDER, you need to enter the edit_provider command
and enter the wallet address that you want to set as PROVIDER.

NFT price change, edit_price command
Output TON withdraw_ton

To change the network operation mode in the main network or test network, use the file _utils.py line 5

If less than the set sale price is sent to the smart contract, the ton will be returned to the sender. 

If more than a TON is sent to the smart contract, the amount of NFT and the change in TON will be sent
