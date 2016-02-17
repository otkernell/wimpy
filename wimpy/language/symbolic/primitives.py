"""WIMPY description language: language primitives."""

from __future__ import division
from __future__ import absolute_import



import ibvp.language.symbolic.primitives as ibvp
import pymbolic.primitives as p

class Expression(ibvp.Expression):
    pass

class DualityPairing(ibvp.Expression):
    def __init__(self, trialexpr, testexpr, domain=None):
        self.trialexpr = trialexpr
        self.testexpr = testexpr
        self.domain = domain
        #etc?
    
    mapper_method=intern("map_duality_pairing")
    
    
class Field(ibvp.Field):
	pass
	

	
	
class _Div(ibvp.LinearOperator):
    def __getinitargs__(self):
        return ()

    mapper_method = "map_div"
div = _Div()

class _Grad(ibvp.LinearOperator):
    def __getinitargs__(self):
        return ()

    mapper_method = "map_grad"

grad = _Grad()

# vim: foldmethod=marker
