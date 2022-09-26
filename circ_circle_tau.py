#!/usr/bin/env python3
# Created by: Spencer.S
# Created on: Sept 26,2022
# Program that calculates circumference of a circle
import constants


def main():
    # Request radius from user
    radius = float(input("What is radius of the circle? (cm): "))

    # Calculate the circumference
    circumference = constants.Tau5 * radius

    # Display end result to user
    print("Circumference = {} cm".format(circumference))


if __name__ == "__main__":
    main()
