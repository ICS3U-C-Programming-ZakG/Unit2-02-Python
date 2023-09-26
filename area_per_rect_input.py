#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Sep. 25, 2023
# This program calculates the area and perimeter of a rectangle (cm)
# Using user given inputs.

import math


def main():
    # ask user for input of length and width
    print("This program calculates the area and perimeter")
    print("of a rectangle with user given inputs in cm.")
    length = float(input("Insert length (cm): "))
    width = float(input("Insert width (cm): "))

    # calculate area and perimeter
    area = length * width
    perimeter = 2 * (length + width)

    # display calculated area and perimeter
    print("The area of the rectangle is {:.2f}cm^2.".format(area))
    print("The perimeter of the rectangle is {:.2f}cm.".format(perimeter))


if __name__ == "__main__":
    main()
