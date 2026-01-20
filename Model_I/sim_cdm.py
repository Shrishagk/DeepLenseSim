import matplotlib.pyplot as plt
import numpy as np
import random
import os

from deeplense.lens import DeepLens


# Number of sims
num_sim = int(5e3)

for i in range(num_sim):
    lens = DeepLens()
    lens.make_single_halo(1e12)
    lens.make_old_cdm()
    lens.make_source_light()
    lens.simple_sim()
    File = lens.image_real
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
