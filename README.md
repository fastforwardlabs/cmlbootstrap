## CML Bootstrap

> [Unoffocial] Wrapper class for the interacting with the CML API.

The CML Bootstrap library provides a list of methods for interacting with the CML backend api for `jobs`, `models`, `applications` and `experiments`.

## Installation

```shell
pip install -e git+https:// github.com/fastforwardlabs/cmlbootstrap
```

## Usage

```python
import CMLBootstrap

cmlb = CMLBootsrap(host, username, api_key, project_name)

user_details = cmlb.get_user()

```

## Documentation

The library current supports methods that cover the `jobs`, `models`, `applications` and `experiments` abstractions on CML. For additional details, see the [documentation README](docs).





