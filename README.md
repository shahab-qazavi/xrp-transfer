# xrp-transfer
Transfer XRP in Ripple mainnet with memo address using xrpl-py library


Dependency:

    xrpl-py version 2.1.0


First, install the requirements.txt file

    pip install -r requirements.txt


And then use xrp_transfer() function.


For using xrp_transfer() function you must have to:

    origin wallet private key ==> private_key
  
    origin wallet public key ==> public_key
  
    origin wallet address ==> my_address
  
    destination wallet addres ==> to_address
  
    amount value for transfering XRP ==> amount
  
    decimals for calculate correct XRP coin for checking account balance ==> decilams

    memo address (it's optional) ==> memo
