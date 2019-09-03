from pyanno import voting
from pyanno.voting import labels_frequency
from numpy.testing import assert_array_equal
import numpy as np

def test_returnvalue():
    return_value = labels_frequency([[1, 1, 2], [-1, 1, 2]], 4)
    expected = np.array([ 0. ,  0.6,  0.4,  0. ])
    assert_array_equal(return_value, expected)
