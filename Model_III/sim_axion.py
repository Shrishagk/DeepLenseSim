import matplotlib.pyplot as plt
import numpy as np
import random
import os
from deeplense.lens import DeepLens


# Number of sims
num_sim = int(3e5)


axion_masses = 10**np.random.uniform(-24,-22,num_sim)

for i in range(num_sim):
    lens = DeepLens(axion_mass=axion_masses[i])
    lens.make_single_halo(1e12)
    lens.make_vortex(3e10)
    lens.set_instrument('hst')
    lens.make_source_light_mag()
    lens.simple_sim_2()
    File = np.array([lens.image_real,axion_masses[i]])

    # This tells the computer: "Start where this script is, then find the data folder."
    base_path = os.path.join(os.getcwd(), 'data', 'Model_I', 'axion')

    # This creates the folder if it doesn't exist yet
    os.makedirs(base_path, exist_ok=True)


if False:
    plt.figure(figsize=(10,5))
    plt.subplot(2,2,1)
    plt.imshow(lens.image_real)
    plt.colorbar()
    plt.subplot(2,2,2)
    plt.imshow(np.sqrt(lens.image_real))
    plt.colorbar()
    plt.subplot(2,2,3)
    plt.imshow(lens.poisson)
    plt.colorbar()
    plt.subplot(2,2,4)
    plt.imshow(lens.bkg)
    plt.colorbar()
    plt.show()
