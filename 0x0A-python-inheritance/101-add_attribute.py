#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible:"""


def add_attribute(PO, PN, PV):
    if not hasattr(PO, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(PO, PN)):
        PO.__setattr__(PN, PV)
