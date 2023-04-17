"""20: Generate Imports While Typing

Avoid interruption by letting PyCharm generate your imports as you type.

- We want a random customer using ``random.choice``

- Delete 'Larry'

- Wrong:

    - Go to top of file, type ``from random import choice``, go back

- Type ``cho`` and ``Ctrl-Space-Space``

- Or, type ``choice`` and ``Alt-Enter``

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/
"""
from random import choice

from fortytwo import App, Greeter

customers = ('Larry', 'Alice', 'Sam')


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        customer = choice(customers)  # Change to random customer
        customer_B = choice(customers)
        greeting = greeter(customer)
        return greeting


if __name__ == '__main__':
    print(main())
