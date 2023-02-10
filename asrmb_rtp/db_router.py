from .models import *

ROUTED_MODELS_GASCALC = [
    TeclossesOne,
    TeclossesTwo,
    TeclossesTree,

]


class Rp_p_calc_gas_and_cond_losses_db_router(object):
    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS_GASCALC:
            return 'rp_p_calc_gas_and_cond_losses'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS_GASCALC:
            return 'rp_p_calc_gas_and_cond_losses'
        return None
