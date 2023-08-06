# here is an example script to show the output of what the elliptical curve looks like when generating a key pair of private and public keys

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
