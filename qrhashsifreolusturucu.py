import streamlit as st
import random
import string
import pyqrcode
import png
import hashlib

buyuk=random.choice(string.ascii_uppercase)
kucuk=random.choice(string.ascii_lowercase)
rakam=random.choice(string.digits)
sembol=random.choice(string.punctuation)

sifre1=[buyuk,kucuk,rakam,sembol]
random.shuffle(sifre1)

sifre2=random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation, k=4)
random.shuffle(sifre2)

sifre3=sifre1+sifre2
random.shuffle(sifre3)

hash_sifre=hashlib.md5(''.join(sifre3).encode()).hexdigest()

qr=pyqrcode.create(hash_sifre)
qr.png('qrkod.png',scale=6)
st.image('qrkod.png')

st.button('Yenile')
st.write('Şifre: ',''.join(sifre3))
st.write('Hash Şifre: ',hash_sifre)

st.image('https://m.media-amazon.com/images/I/61h7XvsUBRL._AC_SL1500_.jpg')



