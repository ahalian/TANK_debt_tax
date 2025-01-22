import econpizza as ep

def run_model(mod):
    """ This function runs the model and saves it"""
    mod = ep.parse(mod)
    mod = ep.load(mod)
    _ = mod.solve_stst()
    return mod

def add_shock(shock_size):
    """ This function simulates the behaviour of the model after shock"""
    shock = ("e_g", shock_size)
    trj, flag = mod.find_path(shock=shock)
    return trj