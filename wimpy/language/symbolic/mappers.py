
from __future__ import division
from __future__ import absolute_import
from six.moves import range


from ibvp.language.symbolic.mappers import (
    IdentityMapper as IdentityMapperBase,
    CombineMapper as CombineMapperBase,
    Collector as CollectorBase,
    WalkMapper as WalkMapperBase,
    EvaluationMapper as EvaluationMapperBase,
    StringifyMapper as StringifyMapperBase,
    Dimensionalizer,
    DerivativeBinder as DerivativeBinderBase,
    
    DerivativeSourceAndNablaComponentCollector
    as DerivativeSourceAndNablaComponentCollectorBase,
    NablaComponentToUnitVector
    as NablaComponentToUnitVectorBase,
    DerivativeSourceFinder
    as DerivativeSourceFinderBase, DifferentiationMapper as DifferentiationMapperBase, PrettyStringifyMapper as PrettyStringifyMapperBase,DistributeMapper as DistributeMapperBase, Scalarizer as ScalarizerBase
)

from pymbolic.mapper.stringifier import (
    CSESplittingStringifyMapperMixin,
    PREC_NONE
)

import ibvp.language.symbolic.primitives as ibvpp
import pymbolic.primitives as pp
import numpy as np
import wimpy.language.symbolic.primitives as w



class IdentityMapper(IdentityMapperBase):
    def map_duality_pairing(self,expr):
        return expr
        
        
class CombineMapper(CombineMapperBase):
    pass
    
class Collector(CollectorBase, CombineMapper):
    pass

class WalkMapper(WalkMapperBase):
    pass

class StringifyMapper(StringifyMapperBase):
    #do I need operations and arguments here or just operations?
    def map_duality_pairing(self, expr, enclosing_prec):
        if expr.domain:
            dom = "_%s" % (self.rec(expr.domain),)
        else:
            dom = ""
            return "(%s, %s)%s" % (self.rec(expr.trialexpr, PREC_NONE),
                                   self.rec(expr.testexpr,PREC_NONE), 
                                   dom)
            print('StringifyMapper')
	#new file
	#if trialop == -div(grad)
	#	return "(%s, %s)_%s+" % (self.rec(expr.trialop, PREC_NONE),
	#							self.rec(expr.testop,PREC_NONE), 
	#							self.rec(expr.domain))		
	#def map_div_grad_duality_pairing(self,expr,enclosing_prec)
	#	return "
	#separate script for duality pairing? Where should the conversion
	#occur?

class PrettyStringifyMapper(
        CSESplittingStringifyMapperMixin,
        StringifyMapper):
    pass

#class PrettyStringifyMapper(PrettyStringifyMapperBase):
#    def map_duality_pairing(self, expr, enclosing_prec):
#        return "hi there"
        

class DistributeMapper(DistributeMapperBase):
    pass

class EvaluationMapper(EvaluationMapperBase):
    pass
        
class DerivativeSourceAndNablaComponentCollector(
        DerivativeSourceAndNablaComponentCollectorBase,
        Collector):
    pass

class NablaComponentToUnitVector(
        NablaComponentToUnitVectorBase,
        EvaluationMapper):
    pass

class DerivativeSourceFinder(
        DerivativeSourceFinderBase,
        EvaluationMapper):
    pass

class DerivativeBinder(DerivativeBinderBase):
    pass

class Scalarizer(ScalarizerBase):
    pass

class DifferentiationMapper(DifferentiationMapperBase):
    pass

class HasSomethingMapper(CombineMapper):
    def combine(self, values):
        import operator
        return reduce(operator.or_, values)

    def map_constant(self, expr):
        return False

    map_field = map_constant
    map_derivative = map_constant
    map_time_derivative = map_constant
    
class HasGradMapper(HasSomethingMapper):
	def map_grad(self, expr):
		return True

has_grad = HasGradMapper()

class DivGradIBP(IdentityMapper):
	#has_grad = HasGradMapper()
	def map_duality_pairing(self,expr):
		trialexpr = expr.trialexpr
		if isinstance(trialexpr.op, ibvpp._Div):
			divargument = trialexpr.argument
			if has_grad(divargument):
				return -1*w.DualityPairing(divargument, w.grad(expr.testexpr))						
		else:
			return expr	


class MyDistributeMapper(IdentityMapper):
	def map_duality_pairing(self, expr):
		if isinstance(expr.trialexpr, pp.Sum): #we had ibvpp.Sum? Having problems with this
			factors = tuple()
			for ch in expr.trialexpr.children:
				factors = factors + (self.rec(w.DualityPairing(ch,expr.testexpr)),)
			return pp.Sum(factors)
		elif isinstance(expr.trialexpr, pp.Product):
			const_factors = tuple()
			nonconst_factors = tuple()
			for ch in expr.trialexpr.children:
				if isinstance(ch, int) or isinstance(ch, float):
					const_factors = const_factors + (ch,)
				else:
					nonconst_factors = nonconst_factors + (ch,)
			cf = pp.Product(const_factors)
			if len(nonconst_factors) == 1:
				return cf * self.rec(w.DualityPairing(nonconst_factors[0], expr.testexpr))
			else:
				ncf = pp.Product(nonconst_factors)
				return cf * w.DualityPairing(ncf, expr.testexpr)
		else:
			return expr
				
