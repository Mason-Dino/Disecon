
# Disecon

![PyPI](https://img.shields.io/pypi/v/Disecon?color=gree) ![PyPI - License](https://img.shields.io/pypi/l/Disecon?color=gree)

#

Disecon is a python economy library where you could make a full economy system really easy.

## Installing

```
# Windows

pip install Disecon

# Lunix / Mac

python3 -m pip install Disecon
```
## Usage

### Starting Disecon

To start Disecon you need to do the following command bellow so that the database gets made. After you do the command you can delete the line that the command is on.

```python
from Disecon import *

start()
```

### Adding money

If you want to add some money into someones wallet you can follow the example bellow to add some money.

```python
from Disecon import *

wallet = money.wallet(amount=100, user_ID=Discord User ID)

wallet.add()
```

If you want to add some money into someones bank you can follow the example bellow to add some money. 

```python
from Disecon import *

bank = money.bank(amount=100, user_ID=Discord User ID)

bank.add()
```

### Subtracting money

If you want to subtract money from someones wallet do the following example below.

```python
from Disecon import *

wallet = money.wallet(amount=100, user_ID=Disecon User ID)

wallet.sub()
```

If you want to subtract money from someones bank you could follow the example below.

```python
from Disecon import *

bank = money.bank(amount=100, user_ID=Discord User ID)

bank.sub()
```

### Viewing User Info

If you want to view someones wallet, bank or net follow the example below.

```python
from Disecon import *

view = results.view(user_ID=Discord User ID)

view.wallet()
view.bank()
view.net()
```

### Leaderboard Info

If you want to see who's in a certain place and git user id, net, wallet and bank you can follow the example below.

```python
from Disecon import *

top = results.top(place=1)

top.user_ID()
top.net()
top.wallet()
top.bank()
```