# Phoenix Prime Service API Examples Package 

This repository provides examples for the Phoenix Prime Service API endpoints. Relevant repositories 
on FIX-based trading are listed as follows.

  - [Phoenix Prime FIX Foundation Package](https://github.com/mtxpt/phx-fix-base)
  - [Phoenix Prime FIX Client Examples Package](https://github.com/mtxpt/phx-fix-examples)


## Service API vs FIX API

Detailed documentation on the Phoenix Prime Service API and the Phoenix Prime FIX endpoints can be found in the 
Phoenix Prime [official documentation](https://api-reference.qat.platform.matrixport.io/docs/en-us/phoenix.html#phoenix). 
In general, the FIX endpoints provide trade execution (e.g. NewOrderSingle, OrderStatusRequest, etc.) and market data,
whereas REST endpoints (labelled as "Service API" in the documentation) expose additional management services
which are not included in the FIX standard, such as account management, or risk and margin related functions. 
The following services are exposed as REST endpoints:
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

Most Phoenix Prime Service API endpoints are implemented in `phx.service_api.client.py`. 
The script `tests.sample_test.py` corresponds to simple queries for wallet balances and positions. 
Before running `tests.sample_test.py`, insert your Phoenix API and secret keys of the account into 
`tests.secret.json`. 