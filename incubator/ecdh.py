# here is an example script to show the output of what the elliptical curve looks like when generating a key pair of private and public keys
# generate a random private key
# generate a public key from the private key
# display the private key in a graphical window on the top left corner in a two-dimensional cartesian plane
# display the public key in a graphical window slightly below the private key in a two-dimensional cartesian plane
# display the elliptical curve in a graphical window in a two-dimensional cartesian plane with the private key and public key on the curve in the same column to show the relationship between the two keys
# in the center of the screen show a column of the numerical values of the private key, public key, and elliptical curve with a dot on the curve which moves with the mouse to show the value at x and y coordinates, 
# and the value of the private key and public key at the same x coordinate
# the elliptical curve is defined by the equation y^2 = x^3 + ax + b, this will also be shown in the second column of the screen
# in the third column of the screen, show a qr code of the private key, public key, and elliptical curve, each in their own qr code and row within the column
# in the fourth column of the screen, show the private key, public key, and elliptical curve in a text format
# on the bottom of the screen show social icon buttons for justin knox, github, twitter, facebook, linkedin, youtube, and instagram

# import the necessary libraries
import ecdsa
import os
import qrcode
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont

import math
import random
import time
import sys
import os
import qrcode

import sha3, random binascii

# generate a random private key

private_key = os.urandom(32).hex().upper()
print("Private Key: " + private_key)

# generate a public key from the private key
public_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1).verifying_key

print("Public Key: " + public_key)

# draw the graphical window, first grab the resolution of the screen
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print("Screen Width: " + str(screen_width))
print("Screen Height: " + str(screen_height))

# create the window
window = tk.Tk()
window.title("Elliptical Curve Digital Signature Algorithm")
window.geometry(str(screen_width) + "x" + str(screen_height))
window.configure(background='black')

# create the canvas
canvas = tk.Canvas(window, width=screen_width, height=screen_height, bg="black")
canvas.pack()

# create the private key label
private_key_label = tk.Label(window, text="Private Key: " + private_key, bg="black", fg="white")
private_key_label.place(x=0, y=0)

# create the public key label
public_key_label = tk.Label(window, text="Public Key: " + public_key, bg="black", fg="white")
public_key_label.place(x=0, y=50)

# create the elliptical curve label
elliptical_curve_label = tk.Label(window, text="Elliptical Curve: y^2 = x^3 + ax + b", bg="black", fg="white")
elliptical_curve_label.place(x=0, y=100)

# create the private key qr code
private_key_qr_code = qrcode.make(private_key)

# create the public key qr code
public_key_qr_code = qrcode.make(public_key)

# create the elliptical curve qr code
elliptical_curve_qr_code = qrcode.make("y^2 = x^3 + ax + b")

# draw the canvas to the screen in fullscreen mode
canvas.pack(fill=tk.BOTH, expand=1)
