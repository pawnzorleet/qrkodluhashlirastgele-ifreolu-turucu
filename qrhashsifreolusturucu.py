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

st.image('https://scontent.fsaw1-11.fna.fbcdn.net/v/t1.6435-9/118794700_3090240834435213_1281607157223323725_n.jpg?stp=dst-jpg_tt6&cstp=mx675x379&ctp=s675x379&_nc_cat=104&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=127cfc&_nc_ohc=ujGjM3y7n6AQ7kNvwHNecuU&_nc_oc=AdrZ_FdIIVX96hcdNLIfIpb-RRT30COsmBlwc0AasXfuFHljqwFLU77AMzJwvIaL3to&_nc_zt=23&_nc_ht=scontent.fsaw1-11.fna&_nc_gid=PNc7Stzhn_WoVaYWg95uvw&_nc_ss=7b289&oh=00_AQKhseQG9agmrGIH63JW-mQXtHH6Bzrx1-7KA2XzK-U2NA&oe=6AC752F4')



