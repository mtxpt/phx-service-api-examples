# Phoenix Prime REST API Package 

This repository provides a demo of exchange connection through Phoenix REST API endpoints. Relevant repositories 
on FIX-based trading are listed as follows.

  - [Phoenix Prime FIX Foundation Package](https://github.com/mtxpt/phx-fix-base)
  - [Phoenix Prime FIX Client Examples Package](https://github.com/mtxpt/phx-fix-examples)


## REST API vs FIX API

Phoenix Prime REST and FIX endpoints details can be found in the Phoenix Prime [official documentation](https://api-reference.qat.platform.matrixport.io/docs/en-us/phoenix.html#phoenix). 
In general, the FIX endpoints provide trade execution (e.g. NewOrderSingle, OrderStatusRequest, etc.) and market data,
whereas REST endpoints (labelled as "Service API" in the documentation) expose additional management services
which are not included in the FIX standard, such as account management, or risk and margin related functions. 
The following requests have to be queried through REST endpoints:
  - Get assets
  - Fund transfer
  - Get margin type
  - Set margin type
  - Set isolated margin
  - Get leverage
  - Set leverage
  - Get history of open orders (through start and end timestamps)
  - Get history of trades (through start and end timestamps)

## Requirements 

The project requires
  - requests >= 2.31.0


## Usage and Configuration 

Most Phoenix REST endpoints are implemented in `entrexapi/client.py`. 
The script `sample_test.py` corresponds to simple queries for wallet balances and positions. 
Before running `sample_test.py`, insert your Phoenix API and secret keys of the account into `secret.json`. 