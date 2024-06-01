import pandas as pd

corpus	= pd.read_csv("./corpus.txt", sep = '\t')
mtz		= pd.read_csv("./mtz_exemplo.txt", sep = '\t')

corpus_formated		= corpus.dropna()
mtz_formated		= mtz[mtz.select_dtypes("number").columns]

mtz_trans = mtz_formated.transpose()

print("--------------------")
print("MTZ_FORMATED: ")
print(mtz_formated)
print("--------------------")
print("MTZ_TRANS: ")
print(mtz_trans)
print("--------------------")


print(mtz_formated.dot(mtz_trans))


# corpus_transposed	= corpus_formated.transpose()

# mtz_simu = mtz_ex.dot(mtz_ex.transpose())
