## CML Bootstrap

> [Unoffocial] Wrapper class for the interacting with the CML API.

The CML Bootstrap library provides a list of methods for interacting with the CML backend api for `jobs`, `models`, `applications` and `experiments`.

## Installation

```shell
pip3 install git+https://github.com/fastforwardlabs/cmlbootstrap#egg=cmlbootstrap
```

## Usage

```python
from cmlbootstrap import CMLBootstrap

cml = CMLBootstrap(host, username, api_key, project_name)

user_details = cml.get_user({})

```

## Documentation

The library current supports methods that cover the `jobs`, `models`, `applications` and `experiments` abstractions on CML. For additional details, see the library [documentation](docs).





