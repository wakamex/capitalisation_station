# Capitalisation Station

Agent components specifically built for financial trading using agents.

Built with the [Olas](https://olas.network) stack.

## Getting Started

This repository contains a number of components that can be used to build trading agents. The components are built with the [Olas](https://olas.network) stack.

The main components of interest are

### Connections

- [eightballer/ccxt](packages/eightballer/connections/ccxt)
    This connection enables the agents to send messages to the ccxt connection allowing generic trading on more than 300 centralised exchanges.
- [eightballer/dcxt](packages/eightballer/connections/dcxt)
    This connection enables the agents to send messages to the dcxt connection allowing generic trading on a number of decentralised exchanges.
    The included exchanges are:
    - [Balancer](https://balancer.finance/)
    - [Uniswap](https://uniswap.org/)
    - [100x](https://100x.finance/)
    - [lyra](https://lyra.finance/)


In order to add a new exchange to the dcxt connection, you need to create a new connection in the [dcxt](packages/eightballer/connections/dcxt/dcxt/) directory.



### Setup for Development

If you're looking to contribute or develop with `capitalisation_station`, get the source code and set up the environment:

```shell
git clone https://github.com/StationsStation/capitalisation_station
cd capitalisation_station
poetry install && poetry shell
```

## Commands

Here are common commands you might need while working with the project:

### Formatting

```shell
make fmt
```

### Linting

```shell
make lint
```

### Testing

```shell
make test
```

### Locking

```shell
make hashes
```

### all

```shell
make all
```

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
