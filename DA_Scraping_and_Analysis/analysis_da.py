import pandas as pd
import os
import pickle

df11 = pd.read_pickle(r'first_dict_da1.pickle')
print(len(df11))
df12 = pd.read_pickle(r'first_dict_da2.pickle')
print(len(df12))
df13 = pd.read_pickle(r'first_dict_da3.pickle')
print(len(df13))
df14 = pd.read_pickle(r'first_dict_da4.pickle')
print(len(df14))
df15 = pd.read_pickle(r'first_dict_da5.pickle')
print(len(df15))
df16 = pd.read_pickle(r'first_dict_da6.pickle')
print(len(df16))
df17 = pd.read_pickle(r'first_dict_da7.pickle')
print(len(df17))
df18 = pd.read_pickle(r'first_dict_da8.pickle')
print(len(df18))
df19 = pd.read_pickle(r'first_dict_da9.pickle')
print(len(df19))
df110 = pd.read_pickle(r'first_dict_da10.pickle')
print(len(df110))
df111 = pd.read_pickle(r'first_dict_da11.pickle')
print(len(df111))
df112 = pd.read_pickle(r'first_dict_da12.pickle')
print(len(df112))
df113 = pd.read_pickle(r'first_dict_da13.pickle')
print(len(df113))
df114 = pd.read_pickle(r'first_dict_da14.pickle')
print(len(df114))
df115 = pd.read_pickle(r'first_dict_da15.pickle')
print(len(df115))


df1 = {}
for i in df11:
    if(i in df1):
        df1[i] += df11[i]
    else:
        df1[i] = df11[i]
for i in df12:
    if(i in df1):
        df1[i] += df12[i]
    else:
        df1[i] = df12[i]
for i in df13:
    if(i in df1):
        df1[i] += df13[i]
    else:
        df1[i] = df13[i]
for i in df14:
    if(i in df1):
        df1[i] += df14[i]
    else:
        df1[i] = df14[i]
for i in df15:
    if(i in df1):
        df1[i] += df15[i]
    else:
        df1[i] = df15[i]
for i in df16:
    if(i in df1):
        df1[i] += df16[i]
    else:
        df1[i] = df16[i]
for i in df17:
    if(i in df1):
        df1[i] += df17[i]
    else:
        df1[i] = df17[i]
for i in df18:
    if(i in df1):
        df1[i] += df18[i]
    else:
        df1[i] = df18[i]
for i in df19:
    if(i in df1):
        df1[i] += df19[i]
    else:
        df1[i] = df19[i]
for i in df110:
    if(i in df1):
        df1[i] += df110[i]
    else:
        df1[i] = df110[i]
for i in df111:
    if(i in df1):
        df1[i] += df111[i]
    else:
        df1[i] = df111[i]
for i in df112:
    if(i in df1):
        df1[i] += df112[i]
    else:
        df1[i] = df112[i]
for i in df113:
    if(i in df1):
        df1[i] += df113[i]
    else:
        df1[i] = df113[i]
for i in df114:
    if(i in df1):
        df1[i] += df114[i]
    else:
        df1[i] = df114[i]
for i in df115:
    if(i in df1):
        df1[i] += df115[i]
    else:
        df1[i] = df115[i]


for i in df1:
    print(i, df1[i])

print("**-*-**-*-*-**-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**--*-*-*-*")

df21 = pd.read_pickle(r'second_dict_da1.pickle')
print(len(df21))
df22 = pd.read_pickle(r'second_dict_da2.pickle')
print(len(df22))
df23 = pd.read_pickle(r'second_dict_da3.pickle')
print(len(df23))
df24 = pd.read_pickle(r'second_dict_da4.pickle')
print(len(df24))
df25 = pd.read_pickle(r'second_dict_da5.pickle')
print(len(df25))
df26 = pd.read_pickle(r'second_dict_da6.pickle')
print(len(df26))
df27 = pd.read_pickle(r'second_dict_da7.pickle')
print(len(df27))
df28 = pd.read_pickle(r'second_dict_da8.pickle')
print(len(df28))
df29 = pd.read_pickle(r'second_dict_da9.pickle')
print(len(df29))
df210 = pd.read_pickle(r'second_dict_da10.pickle')
print(len(df210))
df211 = pd.read_pickle(r'second_dict_da11.pickle')
print(len(df211))
df212 = pd.read_pickle(r'second_dict_da12.pickle')
print(len(df212))
df213 = pd.read_pickle(r'second_dict_da13.pickle')
print(len(df213))
df214 = pd.read_pickle(r'second_dict_da14.pickle')
print(len(df214))
df215 = pd.read_pickle(r'second_dict_da15.pickle')
print(len(df215))


df2 = {}
for i in df21:
    if(i in df2):
        df2[i] += df21[i]
    else:
        df2[i] = df21[i]
for i in df22:
    if(i in df2):
        df2[i] += df22[i]
    else:
        df2[i] = df22[i]
for i in df23:
    if(i in df2):
        df2[i] += df23[i]
    else:
        df2[i] = df23[i]
for i in df24:
    if(i in df2):
        df2[i] += df24[i]
    else:
        df2[i] = df24[i]
for i in df25:
    if(i in df2):
        df2[i] += df25[i]
    else:
        df2[i] = df25[i]
for i in df26:
    if(i in df2):
        df2[i] += df26[i]
    else:
        df2[i] = df26[i]
for i in df27:
    if(i in df2):
        df2[i] += df27[i]
    else:
        df2[i] = df27[i]
for i in df28:
    if(i in df2):
        df2[i] += df28[i]
    else:
        df2[i] = df28[i]
for i in df29:
    if(i in df2):
        df2[i] += df29[i]
    else:
        df2[i] = df29[i]
for i in df210:
    if(i in df2):
        df2[i] += df210[i]
    else:
        df2[i] = df210[i]
for i in df211:
    if(i in df2):
        df2[i] += df211[i]
    else:
        df2[i] = df211[i]
for i in df212:
    if(i in df2):
        df2[i] += df212[i]
    else:
        df2[i] = df212[i]
for i in df213:
    if(i in df2):
        df2[i] += df213[i]
    else:
        df2[i] = df213[i]
for i in df214:
    if(i in df2):
        df2[i] += df214[i]
    else:
        df2[i] = df214[i]
for i in df215:
    if(i in df2):
        df2[i] += df215[i]
    else:
        df2[i] = df215[i]


for i in df2:
    print(i, df2[i])

print("**-*-**-*-*-**-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**--*-*-*-*")


df31 = pd.read_pickle(r'third_dict_da1.pickle')
print(len(df31))
df32 = pd.read_pickle(r'third_dict_da2.pickle')
print(len(df32))
df33 = pd.read_pickle(r'third_dict_da3.pickle')
print(len(df33))
df34 = pd.read_pickle(r'third_dict_da4.pickle')
print(len(df34))
df35 = pd.read_pickle(r'third_dict_da5.pickle')
print(len(df35))
df36 = pd.read_pickle(r'third_dict_da6.pickle')
print(len(df36))
df37 = pd.read_pickle(r'third_dict_da7.pickle')
print(len(df37))
df38 = pd.read_pickle(r'third_dict_da8.pickle')
print(len(df38))
df39 = pd.read_pickle(r'third_dict_da9.pickle')
print(len(df39))
df310 = pd.read_pickle(r'third_dict_da10.pickle')
print(len(df310))
df311 = pd.read_pickle(r'third_dict_da11.pickle')
print(len(df311))
df312 = pd.read_pickle(r'third_dict_da12.pickle')
print(len(df312))
df313 = pd.read_pickle(r'third_dict_da13.pickle')
print(len(df313))
df314 = pd.read_pickle(r'third_dict_da14.pickle')
print(len(df314))
df315 = pd.read_pickle(r'third_dict_da15.pickle')
print(len(df315))


df3 = {}
for i in df31:
    if(i in df3):
        df3[i] += df31[i]
    else:
        df3[i] = df31[i]
for i in df32:
    if(i in df3):
        df3[i] += df32[i]
    else:
        df3[i] = df32[i]
for i in df33:
    if(i in df3):
        df3[i] += df33[i]
    else:
        df3[i] = df33[i]
for i in df34:
    if(i in df3):
        df3[i] += df34[i]
    else:
        df3[i] = df34[i]
for i in df35:
    if(i in df3):
        df3[i] += df35[i]
    else:
        df3[i] = df35[i]
for i in df36:
    if(i in df3):
        df3[i] += df36[i]
    else:
        df3[i] = df36[i]
for i in df37:
    if(i in df3):
        df3[i] += df37[i]
    else:
        df3[i] = df37[i]
for i in df38:
    if(i in df3):
        df3[i] += df38[i]
    else:
        df3[i] = df38[i]
for i in df39:
    if(i in df3):
        df3[i] += df39[i]
    else:
        df3[i] = df39[i]
for i in df310:
    if(i in df3):
        df3[i] += df310[i]
    else:
        df3[i] = df310[i]
for i in df311:
    if(i in df3):
        df3[i] += df311[i]
    else:
        df3[i] = df311[i]
for i in df312:
    if(i in df3):
        df3[i] += df312[i]
    else:
        df3[i] = df312[i]
for i in df313:
    if(i in df3):
        df3[i] += df313[i]
    else:
        df3[i] = df313[i]
for i in df314:
    if(i in df3):
        df3[i] += df314[i]
    else:
        df3[i] = df314[i]
for i in df315:
    if(i in df3):
        df3[i] += df315[i]
    else:
        df3[i] = df315[i]

for i in df3:
    print(i, df3[i])

print("**-*-**-*-*-**-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**--*-*-*-*")


df41 = pd.read_pickle(r'fourth_dict_da1.pickle')
print(len(df41))
df42 = pd.read_pickle(r'fourth_dict_da2.pickle')
print(len(df42))
df43 = pd.read_pickle(r'fourth_dict_da3.pickle')
print(len(df43))
df44 = pd.read_pickle(r'fourth_dict_da4.pickle')
print(len(df44))
df45 = pd.read_pickle(r'fourth_dict_da5.pickle')
print(len(df45))
df46 = pd.read_pickle(r'fourth_dict_da6.pickle')
print(len(df46))
df47 = pd.read_pickle(r'fourth_dict_da7.pickle')
print(len(df47))
df48 = pd.read_pickle(r'fourth_dict_da8.pickle')
print(len(df48))
df49 = pd.read_pickle(r'fourth_dict_da9.pickle')
print(len(df49))
df410 = pd.read_pickle(r'fourth_dict_da10.pickle')
print(len(df410))
df411 = pd.read_pickle(r'fourth_dict_da11.pickle')
print(len(df411))
df412 = pd.read_pickle(r'fourth_dict_da12.pickle')
print(len(df412))
df413 = pd.read_pickle(r'fourth_dict_da13.pickle')
print(len(df413))
df414 = pd.read_pickle(r'fourth_dict_da14.pickle')
print(len(df414))
df415 = pd.read_pickle(r'fourth_dict_da15.pickle')
print(len(df415))

df4 = {}
for i in df41:
    if(i in df4):
        df4[i] += df41[i]
    else:
        df4[i] = df41[i]
for i in df42:
    if(i in df4):
        df4[i] += df42[i]
    else:
        df4[i] = df42[i]
for i in df43:
    if(i in df4):
        df4[i] += df43[i]
    else:
        df4[i] = df43[i]
for i in df44:
    if(i in df4):
        df4[i] += df44[i]
    else:
        df4[i] = df44[i]
for i in df45:
    if(i in df4):
        df4[i] += df45[i]
    else:
        df4[i] = df45[i]
for i in df46:
    if(i in df4):
        df4[i] += df46[i]
    else:
        df4[i] = df46[i]
for i in df47:
    if(i in df4):
        df4[i] += df47[i]
    else:
        df4[i] = df47[i]
for i in df48:
    if(i in df4):
        df4[i] += df48[i]
    else:
        df4[i] = df48[i]
for i in df49:
    if(i in df4):
        df4[i] += df49[i]
    else:
        df4[i] = df49[i]
for i in df410:
    if(i in df4):
        df4[i] += df410[i]
    else:
        df4[i] = df410[i]
for i in df411:
    if(i in df4):
        df4[i] += df411[i]
    else:
        df4[i] = df411[i]
for i in df412:
    if(i in df4):
        df4[i] += df412[i]
    else:
        df4[i] = df412[i]
for i in df413:
    if(i in df4):
        df4[i] += df413[i]
    else:
        df4[i] = df413[i]
for i in df414:
    if(i in df4):
        df4[i] += df414[i]
    else:
        df4[i] = df414[i]
for i in df415:
    if(i in df4):
        df4[i] += df415[i]
    else:
        df4[i] = df415[i]

for i in df4:
    print(i, df4[i])

print("**-*-**-*-*-**-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**--*-*-*-*")

df51 = pd.read_pickle(r'fifth_dict_da1.pickle')
print(len(df51))
df52 = pd.read_pickle(r'fifth_dict_da2.pickle')
print(len(df52))
df53 = pd.read_pickle(r'fifth_dict_da3.pickle')
print(len(df53))
df54 = pd.read_pickle(r'fifth_dict_da4.pickle')
print(len(df54))
df55 = pd.read_pickle(r'fifth_dict_da5.pickle')
print(len(df55))
df56 = pd.read_pickle(r'fifth_dict_da6.pickle')
print(len(df56))
df57 = pd.read_pickle(r'fifth_dict_da7.pickle')
print(len(df57))
df58 = pd.read_pickle(r'fifth_dict_da8.pickle')
print(len(df58))
df59 = pd.read_pickle(r'fifth_dict_da9.pickle')
print(len(df59))
df510 = pd.read_pickle(r'fifth_dict_da10.pickle')
print(len(df510))
df511 = pd.read_pickle(r'fifth_dict_da11.pickle')
print(len(df511))
df512 = pd.read_pickle(r'fifth_dict_da12.pickle')
print(len(df512))
df513 = pd.read_pickle(r'fifth_dict_da13.pickle')
print(len(df513))
df514 = pd.read_pickle(r'fifth_dict_da14.pickle')
print(len(df514))
df515 = pd.read_pickle(r'fifth_dict_da15.pickle')
print(len(df515))

df5 = {}
for i in df51:
    if(i in df5):
        df5[i] += df51[i]
    else:
        df5[i] = df51[i]
for i in df52:
    if(i in df5):
        df5[i] += df52[i]
    else:
        df5[i] = df52[i]
for i in df53:
    if(i in df5):
        df5[i] += df53[i]
    else:
        df5[i] = df53[i]
for i in df54:
    if(i in df5):
        df5[i] += df54[i]
    else:
        df5[i] = df54[i]
for i in df55:
    if(i in df5):
        df5[i] += df55[i]
    else:
        df5[i] = df55[i]
for i in df56:
    if(i in df5):
        df5[i] += df56[i]
    else:
        df5[i] = df56[i]
for i in df57:
    if(i in df5):
        df5[i] += df57[i]
    else:
        df5[i] = df57[i]
for i in df58:
    if(i in df5):
        df5[i] += df58[i]
    else:
        df5[i] = df58[i]
for i in df59:
    if(i in df5):
        df5[i] += df59[i]
    else:
        df5[i] = df59[i]
for i in df510:
    if(i in df5):
        df5[i] += df510[i]
    else:
        df5[i] = df510[i]
for i in df511:
    if(i in df5):
        df5[i] += df511[i]
    else:
        df5[i] = df511[i]
for i in df512:
    if(i in df5):
        df5[i] += df512[i]
    else:
        df5[i] = df512[i]
for i in df513:
    if(i in df5):
        df5[i] += df513[i]
    else:
        df5[i] = df513[i]
for i in df514:
    if(i in df5):
        df5[i] += df514[i]
    else:
        df5[i] = df514[i]
for i in df515:
    if(i in df5):
        df5[i] += df515[i]
    else:
        df5[i] = df515[i]

for i in df5:
    print(i, df5[i])

print("**-*-**-*-*-**-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**--*-*-*-*")

with open("first_dict_da.pickle", "wb") as h1:
    pickle.dump(df1, h1)
with open("second_dict_da.pickle", "wb") as h2:
    pickle.dump(df2, h2)
with open("third_dict_da.pickle", "wb") as h3:
    pickle.dump(df3, h3)
with open("fourth_dict_da.pickle", "wb") as h4:
    pickle.dump(df4, h4)
with open("fifth_dict_da.pickle", "wb") as h5:
    pickle.dump(df5, h5)

df1 = pd.read_pickle(r'first_dict_da.pickle')
print(len(df1))
df2 = pd.read_pickle(r'second_dict_da.pickle')
print(len(df2))
df3 = pd.read_pickle(r'third_dict_da.pickle')
print(len(df3))
df4 = pd.read_pickle(r'fourth_dict_da.pickle')
print(len(df4))
df5 = pd.read_pickle(r'fifth_dict_da.pickle')
print(len(df5))
