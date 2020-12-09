import math


#creating a cobb douglas function

"""
Y (rebate a Indexer receives) = 


wij = amount that indexer i has staked on subgraph j

omega = total amount staked in the network  (512606566617953495116552180)
theta_ij = amount of protocol fees indexer i has generated for the protocol on subgraph j  (queryfeescollected`?)
groß_thehta = total amount of protocol fees collected by the protocol (queryfeesAmount?)


(wij/omega)^alpha * ( Theta_ij / groß_theta) ^ 1- alpha


Example:

(wij/omega) = 50000000000000000000000 / 512606566617953495116552180 =  (0.00009754069) ^alpha
(Theta_ij / groß_thetha) =  queryfeesCollected/44995500000000000

zu hoher stake wird stärker bestraft als zu hohe arbeit!!!

_______________________________________


0x14c7db0bf796060da7212c0f851ce62a47805502 staked 49999 tokens on subgraph 0x6b7de4f906e3afd6d8e16c87beb9506ee2ad89182a22590f52bf79f09e76b3d6 (curve)

50000000000000000000000 -> staked

QueryFeesAmount_Total on this Subgraph = 44995500000000000

"""

"""
important cobb douglas function is:

stake^alpha * work^1-alpha

"""

#%%

# K = Stake
# L = WORK basically
#  z = irrelevant
# alpha output elasticity of capital [0,1]
def cobb_douglas(K,L ):

    # Create alpha and z
    z = 1
    alpha = 0.5

    return z * K**alpha * L**(1 - alpha)

# %%
cobb_douglas(0.3,0.4)
# %%
y1 = cobb_douglas(1.0, 0.5)
print(y1)
# %%
y2 = cobb_douglas(2*1.0, 2*0.5)
print(y2)
# %%
 50000000000000000000000 / 512606566617953495116552180
# %%
def marginal_products(K, L, epsilon):

    mpl = (cobb_douglas(K, L + epsilon) - cobb_douglas(K, L)) / epsilon
    mpk = (cobb_douglas(K + epsilon, L) - cobb_douglas(K, L)) / epsilon

    return mpl, mpk
# %%
tup = marginal_products(1.0, 0.5,  1e-4)

# %%
print(tup)

# %%
