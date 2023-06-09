# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DkEuCJJ-vLdF47ThWA_VV08HwiLhqdZ9
"""

import matplotlib.pyplot as plt
import numpy as np
import math

# Calculation of the time step
# Lifetime of the shortest-living star is considered a unit time-step.
# Lifetime (t) = 10^(10) x (M^(-2.5))
time_step = pow(10, 10) * pow(25, (-2.5))
rounded = round(time_step, 3 - int(math.floor(math.log10(abs(time_step)))) - 1)

print("Timestep (i.e. lifetime of the shortest living star : ", ('{:.2e}'.format(rounded)))


# Star class holds attributes for each type of star
class StarType:
    def __init__(self, name, mass, lifetime, existing):
        self.name = name
        self.mass = mass
        self.lifetime = lifetime
        # Array to hold different batches of stars born at different steps
        # For example, element 1 - stars born at step 1, element 2 - starts born at step 2 etc.
        self.existing = existing


class Life:
    # For each batch of stars, this object holds the count and life remaining for that batch (number of steps)
    # For example Life(E, 4) means the batch contains 'E' stars which will be alive for 4 more steps.
    def __init__(self, count, life_remaining):
        self.count = count
        self.life_remaining = life_remaining


# List to hold values of luminosity at each step
luminosity = []
timeline = []

# Create star types and set masses, types by mass
star_25 = StarType("25M Stars", 25, 0, [])
star_14 = StarType("14M Stars", 14.35, 0, [])
star_5 = StarType("5M Stars", 5.03, 0, [])
star_2 = StarType("2M Stars", 2.005, 0, [])
star_1 = StarType("1M Stars", 1, 0, [])

# Temporary values
A = 1000
B = 400
C = 150
D = 60
E = 15

# Make a list of all star types
starTypes = [star_25, star_14, star_5, star_2, star_1]

# Calculate lifetime of each star type based on mass
for x in starTypes:
    lifetime = pow(10, 10) * pow(x.mass, (-2.5))
    rounded = round(lifetime, 3 - int(math.floor(math.log10(abs(lifetime)))) - 1)
    x.lifetime = ('{:.2e}'.format(rounded))

# print known parameters for each type of star (i.e. mass and lifetime)
for x in starTypes:
    print("Star mass : ", x.mass, "\t\t Lifetime :", x.lifetime)

# Take time steps (each of 3.2 x 10^6 years and calculate star population at each step)
for step in range(1, 3751,2):
    years = time_step * step
    print("Step - ", step, "\t\t Years passed : ", ('{:.2e}'.format(years)), " Years")


    for startype in starTypes:
      new_existing = []
      for star_batch in startype.existing:
        if star_batch.life_remaining > 0:
            new_life_remaining = star_batch.life_remaining - 1
            if new_life_remaining > 0:
                star_batch.life_remaining = new_life_remaining
                new_existing.append(star_batch)

      startype.existing = new_existing
    # FOR STAR_25
    # For pre-existing stars reduce life remaining by 1 step.
    # If life remaining reaches 0, consider those stars as dead.
    # new_existing = []
    # for star_batch in star_25.existing:

    #     if star_batch.life_remaining > 0:
    #         new_life_remaining = star_batch.life_remaining - 1
    #         if new_life_remaining > 0:
    #             star_batch.life_remaining = new_life_remaining
    #             new_existing.append(star_batch)

    # star_25.existing = new_existing

    # FOR STAR_14
    # For pre-existing stars reduce life remaining by 1 step.
    # If life remaining reaches 0, consider those stars as dead.
    # new_existing = []
    # for star_batch in star_14.existing:
    #     if star_batch.life_remaining > 0:
    #         new_life_remaining = star_batch.life_remaining - 1
    #         if new_life_remaining > 0:
    #             star_batch.life_remaining = new_life_remaining
    #             new_existing.append(star_batch)

    # star_14.existing = new_existing

    # # FOR STAR_5
    # # For pre-existing stars reduce life remaining by 1 step.
    # # If life remaining reaches 0, consider those stars as dead.
    # new_existing = []
    # for star_batch in star_5.existing:
    #     if star_batch.life_remaining > 0:
    #         new_life_remaining = star_batch.life_remaining - 1
    #         if new_life_remaining > 0:
    #             star_batch.life_remaining = new_life_remaining
    #             new_existing.append(star_batch)

    # star_5.existing = new_existing

    # # FOR STAR_2
    # # For pre-existing stars reduce life remaining by 1 step.
    # # If life remaining reaches 0, consider those stars as dead.
    # new_existing = []
    # for star_batch in star_2.existing:
    #     if star_batch.life_remaining > 0:
    #         new_life_remaining = star_batch.life_remaining - 1
    #         if new_life_remaining > 0:
    #             star_batch.life_remaining = new_life_remaining
    #             new_existing.append(star_batch)

    # star_2.existing = new_existing

    # # FOR STAR_1
    # # For pre-existing stars reduce life remaining by 1 step.
    # # If life remaining reaches 0, consider those stars as dead.
    # new_existing = []
    # for star_batch in star_1.existing:
    #     if star_batch.life_remaining > 0:
    #         new_life_remaining = star_batch.life_remaining - 1
    #         if new_life_remaining > 0:
    #             star_batch.life_remaining = new_life_remaining
    #             new_existing.append(star_batch)

    # star_1.existing = new_existing

    # STOP forming new stars if the current year value is more than 1 Billion
    if years <= 1000000000:
        # New star formation at this step

        # print("E stars of type ", star_25.name, " were born.")
        # print("D stars of type ", star_14.name, " were born.")
        # print("C stars of type ", star_5.name, " were born.")
        # print("B stars of type ", star_2.name, " were born.")
        # print("A stars of type ", star_1.name, " were born.")

        # Add new stars with corresponding life remaining (in terms of how many steps i.e. 3.2 x 10^6 years)
        new_25 = Life("E", 1)
        star_25.existing.append(new_25)

        new_14 = Life("D", 4)
        star_14.existing.append(new_14)

        new_5 = Life("C", 55)
        star_5.existing.append(new_5)

        new_2 = Life("B", 550)
        star_2.existing.append(new_2)

        new_1 = Life("A", 31250)
        star_1.existing.append(new_1)

    # Existing stars at this step :

    print(len(star_1.existing), "A (", star_1.name, ") +", len(star_2.existing), "B (", star_2.name, ") +",
          len(star_5.existing), "C (", star_5.name, ") +", len(star_14.existing), "D (", star_14.name, ") +",
          len(star_25.existing), "E (", star_25.name, ")")

    # Luminosity = L_solar x ( M  / M_solar)^(3.9)
    # Luminosity = 3.828 x 10^26 x M^(3.9)
    lum_star_1 = 3.828 * pow(10, 26) * pow(star_1.mass, 3.9) * (len(star_1.existing) * A)
    lum_star_2 = 3.828 * pow(10, 26) * pow(star_2.mass, 3.9) * (len(star_2.existing) * B)
    lum_star_5 = 3.828 * pow(10, 26) * pow(star_5.mass, 3.9) * (len(star_5.existing) * C)
    lum_star_14 = 3.828 * pow(10, 26) * pow(star_14.mass, 3.9) * (len(star_14.existing) * D)
    lum_star_25 = 3.828 * pow(10, 26) * pow(star_25.mass, 3.9) * (len(star_25.existing) * E)

    # Total luminosity is the addition of all luminosities calculated above for eact type of star
    total_luminosity = lum_star_1 + lum_star_2 + lum_star_5 + lum_star_14 + lum_star_25

    # Append total luminosity for the step to the Luminosity list
    luminosity.append(total_luminosity)
    timeline.append(years)

    print("---------------------------------")

# Potting Luminosity vs time
print("Luminosity Graph")

# scaled_luminosity = [v / 1e32 for v in luminosity]

# create a new plot and set the size
fig, ax = plt.subplots(figsize=(10, 6))  # width, height in inches

# plot your data
ax.plot(luminosity)

# add a title and axis labels
ax.set_title("Luminosity with Time (years)")
ax.set_xlabel("Timeline (Years)")
ax.set_ylabel("Luminosity")

# show the plot
plt.show()