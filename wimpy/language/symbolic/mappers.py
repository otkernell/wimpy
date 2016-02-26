
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

import ibvp.language.symbolic.primitives as ibvp
import pymbolic.primitives as pp
import numpy as np



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

#class DivGradIBP(IdentityMapper):
#	def map_duality_pairing(self,expr):
#		def is_div_grad(expr):
#			
#		if is_div_grad(expr):
#			return "
#		else
#			return expr	





