"""WIMPY description language: language primitives."""

from __future__ import division
from __future__ import absolute_import


from ibvp.language.symbolic.primitives import (
    div,
    grad,
    Expression as ibvpExpression,
    Field
)

import pymbolic.primitives as p


class Expression(ibvpExpression):
    pass

class DualityPairing(Expression):
    def __init__(self, trialexpr, testexpr, domain=None):
        self.trialexpr = trialexpr
        self.testexpr = testexpr
        self.domain = domain
        #etc?
    
    mapper_method=intern("map_duality_pairing")

# vim: foldmethod=marker
