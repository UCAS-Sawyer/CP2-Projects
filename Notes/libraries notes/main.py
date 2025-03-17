#Sawyer Wood, libraries notes

#Requirements:
######pip install matplotlib######
######pip install numpy######
######pip install faker#####

import matplotlib.pyplot as plt
import numpy as np
from faker import Faker

fake = Faker(["it_IT", "ja_JP"])
for i in range(10):
    print("\n", fake.name(), "\n", fake.address(), "\n")

#fig, ax = plt.subplots()                                    # Create a figure containing a single Axes.
#ax.plot([1, 2, 3, 4, 5, 10, 100], [1, 4, 2, 3, 10, 1, 50])  # Plot some data on the Axes.
#plt.show()                                                  # Show the figure.