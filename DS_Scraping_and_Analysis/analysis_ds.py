import pandas as pd
import os
import pickle

df11 = pd.read_pickle(r'first_dict_ds1.pickle')
print(len(df11))
df12 = pd.read_pickle(r'first_dict_ds2.pickle')
print(len(df12))
df13 = pd.read_pickle(r'first_dict_ds3.pickle')
print(len(df13))
df14 = pd.read_pickle(r'first_dict_ds4.pickle')
print(len(df14))
df15 = pd.read_pickle(r'first_dict_ds5.pickle')
print(len(df15))
df16 = pd.read_pickle(r'first_dict_ds6.pickle')
print(len(df16))
df17 = pd.read_pickle(r'first_dict_ds7.pickle')
print(len(df17))
df18 = pd.read_pickle(r'first_dict_ds8.pickle')
print(len(df18))
df19 = pd.read_pickle(r'first_dict_ds9.pickle')
print(len(df19))


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


for i in df1:
    print(i, df1[i])

print("**-*-**-*-*-**-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**--*-*-*-*")

df21 = pd.read_pickle(r'second_dict_ds1.pickle')
print(len(df21))
df22 = pd.read_pickle(r'second_dict_ds2.pickle')
print(len(df22))
df23 = pd.read_pickle(r'second_dict_ds3.pickle')
print(len(df23))
df24 = pd.read_pickle(r'second_dict_ds4.pickle')
print(len(df24))
df25 = pd.read_pickle(r'second_dict_ds5.pickle')
print(len(df25))
df26 = pd.read_pickle(r'second_dict_ds6.pickle')
print(len(df26))
df27 = pd.read_pickle(r'second_dict_ds7.pickle')
print(len(df27))
df28 = pd.read_pickle(r'second_dict_ds8.pickle')
print(len(df28))
df29 = pd.read_pickle(r'second_dict_ds9.pickle')
print(len(df29))


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


for i in df2:
    print(i, df2[i])

print("**-*-**-*-*-**-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**--*-*-*-*")


df31 = pd.read_pickle(r'third_dict_ds1.pickle')
print(len(df31))
df32 = pd.read_pickle(r'third_dict_ds2.pickle')
print(len(df32))
df33 = pd.read_pickle(r'third_dict_ds3.pickle')
print(len(df33))
df34 = pd.read_pickle(r'third_dict_ds4.pickle')
print(len(df34))
df35 = pd.read_pickle(r'third_dict_ds5.pickle')
print(len(df35))
df36 = pd.read_pickle(r'third_dict_ds6.pickle')
print(len(df36))
df37 = pd.read_pickle(r'third_dict_ds7.pickle')
print(len(df37))
df38 = pd.read_pickle(r'third_dict_ds8.pickle')
print(len(df38))
df39 = pd.read_pickle(r'third_dict_ds9.pickle')
print(len(df39))

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

for i in df3:
    print(i, df3[i])

print("**-*-**-*-*-**-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**--*-*-*-*")


df41 = pd.read_pickle(r'fourth_dict_ds1.pickle')
print(len(df41))
df42 = pd.read_pickle(r'fourth_dict_ds2.pickle')
print(len(df42))
df43 = pd.read_pickle(r'fourth_dict_ds3.pickle')
print(len(df43))
df44 = pd.read_pickle(r'fourth_dict_ds4.pickle')
print(len(df44))
df45 = pd.read_pickle(r'fourth_dict_ds5.pickle')
print(len(df45))
df46 = pd.read_pickle(r'fourth_dict_ds6.pickle')
print(len(df46))
df47 = pd.read_pickle(r'fourth_dict_ds7.pickle')
print(len(df47))
df48 = pd.read_pickle(r'fourth_dict_ds8.pickle')
print(len(df48))
df49 = pd.read_pickle(r'fourth_dict_ds9.pickle')
print(len(df49))

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

for i in df4:
    print(i, df4[i])

print("**-*-**-*-*-**-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**--*-*-*-*")

df51 = pd.read_pickle(r'fifth_dict_ds1.pickle')
print(len(df51))
df52 = pd.read_pickle(r'fifth_dict_ds2.pickle')
print(len(df52))
df53 = pd.read_pickle(r'fifth_dict_ds3.pickle')
print(len(df53))
df54 = pd.read_pickle(r'fifth_dict_ds4.pickle')
print(len(df54))
df55 = pd.read_pickle(r'fifth_dict_ds5.pickle')
print(len(df55))
df56 = pd.read_pickle(r'fifth_dict_ds6.pickle')
print(len(df56))
df57 = pd.read_pickle(r'fifth_dict_ds7.pickle')
print(len(df57))
df58 = pd.read_pickle(r'fifth_dict_ds8.pickle')
print(len(df58))
df59 = pd.read_pickle(r'fifth_dict_ds9.pickle')
print(len(df59))

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

for i in df5:
    print(i, df5[i])

print("**-*-**-*-*-**-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-**--*-*-*-*")

with open("first_dict_ds.pickle", "wb") as h1:
    pickle.dump(df1, h1)
with open("second_dict_ds.pickle", "wb") as h2:
    pickle.dump(df2, h2)
with open("third_dict_ds.pickle", "wb") as h3:
    pickle.dump(df3, h3)
with open("fourth_dict_ds.pickle", "wb") as h4:
    pickle.dump(df4, h4)
with open("fifth_dict_ds.pickle", "wb") as h5:
    pickle.dump(df5, h5)

df1 = pd.read_pickle(r'first_dict_ds.pickle')
print(len(df1))
df2 = pd.read_pickle(r'second_dict_ds.pickle')
print(len(df2))
df3 = pd.read_pickle(r'third_dict_ds.pickle')
print(len(df3))
df4 = pd.read_pickle(r'fourth_dict_ds.pickle')
print(len(df4))
df5 = pd.read_pickle(r'fifth_dict_ds.pickle')
print(len(df5))
