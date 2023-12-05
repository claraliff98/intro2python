import matplotlib.pyplot as plt

def myscatter3(X,color="blue"):
    fig = plt.gcf()
    if len(fig.axes) == 0:
        ax = fig.add_subplot(projection='3d')
    else:
        ax = fig.gca()

    ax.scatter(X[:,0],X[:,1],X[:,2],color=color)

def vecarrow3d(v):
    fig = plt.gcf()
    if len(fig.axes) == 0:
        ax = fig.add_subplot(projection='3d')
    else:
        ax = fig.gca()


    ax.quiver(0,0,0,v[0],v[1],v[2])
