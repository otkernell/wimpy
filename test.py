"""Proteus target for IBVP translation."""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

__copyright__ = "Copyright (C) 2014 Rob Kirby, Andreas Kloeckner"

__license__ = """
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import numpy as np
import wimpy.sym as sym
import ibvp as ibvp
import pymbolic as p





def is_constant(value):
    return isinstance(value, p.VALID_CONSTANT_CLASSES)


def test_duality_pairing():
	u = sym.Field("u")
	v = sym.Field("v")
	w = sym.Field("w")
	
	divgradIBP = sym.DivGradIBP()
	eqns = sym.DualityPairing(sym.div(2*sym.grad(u)),v)
	a = divgradIBP(eqns)
	print(sym.pretty(a))
    
	distributetest = sym.MyDistributeMapper()
    
	eqns2 = sym.DualityPairing(u+w+v,v)
	b = distributetest(eqns2)
	print(sym.pretty(b))
    
	eqns3 = sym.DualityPairing(3*u*4*w,v)
	c = distributetest(eqns3)
	print(sym.pretty(c))
	
	eqns4 = sym.DualityPairing(u*(u+v),v)
	d = distributetest(eqns4)
	print(sym.pretty(d))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        exec(sys.argv[1])
    else:
        from py.test.cmdline import main
        main([__file__])
