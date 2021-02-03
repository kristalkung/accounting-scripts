"""Print out all the melons in our inventory."""


from melons import melon_names


def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, attributes in melon_names.items():
        print(melon_name.upper())

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

print_melon(melon_names)