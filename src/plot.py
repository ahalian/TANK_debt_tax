import matplotlib.pyplot as plt




def plot_irf(trj,vars):
    """ Plot the Impulse Response Functions.
    	Args:
		    trj: after shock trajectory
		    vars: variables for IRF
        Returns:
		    fig: Returns IRF graph
    """

fig, axs = plt.subplots(5, 5, figsize=(15, 12))  
for i, v in enumerate(vars):
    var_idx = base.var_names.index(v)  
    var_idx_debt = debt.var_names.index(v) 

    percentage_change_model1 = trj[:50, var_idx]
    percentage_change_model2 = trj_debt[:50, var_idx_debt]

    axs.flatten()[i].plot(percentage_change_model1, label='Base', color='blue')
    axs.flatten()[i].plot(percentage_change_model2, label='Debt', color='red', linestyle='dashed')
    axs.flatten()[i].set_xlabel('Time')
    axs.flatten()[i].set_title(v)
    axs.flatten()[i].legend()

fig.tight_layout()
plt.show()
    return fig