"""Strong-form BVP/IVP description language."""

from __future__ import division  
from __future__ import absolute_import
from six.moves import range

__copyright__ = "Copyright (C) 2014 Andreas Kloeckner"

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


from pytools import Record  #not sure what Record is


# {{{ problems

class PDESystem(Record):
    """
    .. attribute :: ambient_dim

    .. attribute :: pde_system

        A :class:`numpy.ndarray` of :class:`pymbolic.primitives.Expression`.

    .. attribute:: unknowns

        A list of subclasses of :class:`pymbolic.primitives.Variable`
        that are being solved for.
    """

    def __init__(self, ambient_dim, pde_system, unknowns):
        super(PDESystem, self).__init__(
            ambient_dim=ambient_dim,
            pde_system=pde_system,
            unknowns=unknowns,
            )

    def map_expressions(self, expr_map):
        return self.copy(
                pde_system=expr_map(self.pde_system),
                )


class BVP(PDESystem):
    """Shares all the attributes of its superclass :class:`BVP`,
    and additionally, has:

    .. attribute :: initial_condition
    """


class IBVP(BVP):
    """Shares all the attributes of its superclass :class:`BVP`,
    and additionally, has:

    .. attribute :: initial_condition
    """

    def __init__(self, ambient_dim, pde_system, unknowns, initial_condition):
        super(BVP, self).__init__(
            ambient_dim=ambient_dim,
            pde_system=pde_system,
            unknowns=unknowns,
            initial_condition=initial_condition,
                                  ) #redeclare?

    def map_expressions(self, expr_map):
        return super(IBVP, self).map_expressions(expr_map).copy(
                initial_condition=expr_map(self.initial_condition),
                )

# }}}


def scalarize(bvp):
    """
    :arg bvp: an instance of :class:`BVP` or a subclass thereof
    """
    from ibvp.language.symbolic.mappers import Scalarizer

    scalarizer = Scalarizer(bvp.ambient_dim)

    from ibvp.language.symbolic.util import join_fields

    def expr_map(expr):
        return join_fields(*scalarizer(expr))

    bvp = bvp.map_expressions(expr_map)

    import ibvp.language.symbolic.primitives as p

    scalar_unknowns = []
    for unk in bvp.unknowns:
        if isinstance(unk, (p.VectorField, p.MultiVectorField)):
            scalar_unknowns.extend(
                    "%s_%d" % (unk.name, i)
                    for i in range(bvp.ambient_dim))
        else:
            scalar_unknowns.append(unk.name)

    return bvp.copy(unknowns=[p.Field(name) for name in scalar_unknowns])


# vim: foldmethod=marker
