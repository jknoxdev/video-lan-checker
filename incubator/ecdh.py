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
import hashlib
import base58
import binascii
import os
import codecs
import random
import sys
import time
import datetime
import json
import requests
import urllib.request
import urllib.parse
import urllib.error
import ssl
import socket
import http.client
import subprocess
import shutil
import getpass
import platform
import re
import uuid
import logging
import logging.handlers
import configparser
import csv


# generate a random private key

private_key = os.urandom(32).hex().upper()
print("Private Key: " + private_key)

# generate a public key from the private key
public_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1).verifying_key.to_string().hex().upper()

print("Public Key: " + public_key)
