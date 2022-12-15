"""An implementation adding a symetric group class."""

from example_code.groups import Group
import numpy as np


class SymmetricGroup(Group):
    """Implementing Symetric Group class."""

    symbol = "S"

    def _validate(self, value):
        """Ensure that the value is allowed to be in a Symmetric Group."""
        asc_value = sorted(value)
        if not (asc_value[0] == 0 and asc_value[-1] == (self.n - 1)):
            raise ValueError("Element must contain all integers"
                             f"in the range [0, {self.n})")

    def operation(self, a, b):
        """Operation implementation for symetric groups."""
        return np.array([a[b[i]] for i in range(0, self.n)])
