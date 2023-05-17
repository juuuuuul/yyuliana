import pandas as pd
from scipy.stats import kstest, norm

import matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv('experimentaldata.csv')
values = data['weight']
kstest_result = kstest(values, 'norm', (values.mean(), values.std()))

if kstest_result.pvalue > 0.05:
    print("Данные соответствуют нормальному распределению.")
else:
    print("Данные не соответствуют нормальному распределению.")

print(kstest_result)

data.plot.kde()
plt.show()