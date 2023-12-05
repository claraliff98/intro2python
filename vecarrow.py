import matplotlib.pyplot as plt
def vecarrow(X):
    plt.quiver(0,0,X[0],X[1],angles='xy',scale_units='xy',scale=1)
