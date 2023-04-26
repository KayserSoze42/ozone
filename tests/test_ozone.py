import string
import random

from Ozone.Ozone import Ozone


# Generate invalid data for testing
randomInvalidStrings = []

# Generate 100 invalid sets of strings
for i in range(1, 101):

    # Generate random string using letters only, length of 25-34 characters
    randomInvalidStrings.append(
        ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(25,35)))
    )

    # Generate random string using lowercase letters only, length of 25-34 characters
    randomInvalidStrings.append(
        ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(25, 35)))
    )

    # Generate random string using uppercase letters only, length of 25-34 characters
    randomInvalidStrings.append(
        ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(25, 35)))
    )

    # Generate random string using digits only, length of 25-34 characters(digits?)
    randomInvalidStrings.append(
        ''.join(random.choice(string.digits) for _ in range(random.randint(25, 35)))
    )

def test_ozonize_returns_empty() -> None:

    # Iterate over the list of random invalid strings
    for invalidString in randomInvalidStrings:

        # Test for the Ozone.ozonize to return ('','') since nothing is found (nothing is written as well)
        assert Ozone.ozonize(invalidString) == ('', '')

