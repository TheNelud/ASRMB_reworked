from .models import *


ROUTED_MODELS_COMPONENT_COMPOSITION = [
    P1ComponentCompositionOfUnstableCondensate,
    P2ComponentCompositionOfGas,
    P3DeterminationOfTheComponentOfGas,
    P4GasCompositionToTheProtocol,
    P5DeterminationOfTheComponentComposition,
    P6CompositionOfGasOutput,
    P7CompositionOfGas10c,
    P8CompositionOfTheCondensate,
    P9ComponentOfTheSeparationGas,
    P10ProtokolKGN
]

ROUTED_MODELS_RESULT_CONSTANT = [
    NrProd
]


class Rp_p_component_composition_db_router(object):
    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS_COMPONENT_COMPOSITION:
            return 'rp_p_component_composition'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS_COMPONENT_COMPOSITION:
            return 'rp_p_component_composition'
        return None


class Rp_p_result_constant_db_router(object):
    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS_RESULT_CONSTANT:
            return 'rp_p_result_constant'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS_RESULT_CONSTANT:
            return 'rp_p_result_constant'
        return None
