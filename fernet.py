# generate_encrypted.py
from cryptography.fernet import Fernet
import json

KEY = b'K7WAbQQR6_1vQ7EXn7ImKk9xq7W7k8uYHnWbQeH0z3Q='  # Должен совпадать с клиентом

with open('iptv.json', 'r') as f:
    data = json.load(f)

encrypted = Fernet(KEY).encrypt(json.dumps(data).encode('utf-8'))

with open('iptv.bin', 'wb') as f:
    f.write(encrypted)