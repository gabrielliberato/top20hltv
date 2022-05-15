#%%
import pandas as pd
#import plotly.express as px
import json
from matplotlib import pyplot as plt

# %%
with open("../files/rankings.json", encoding = 'utf-8') as f:
    data = json.load(f)
    print(data['rankings'][1]['year'])
# %%
anos = [{'ano': 0,
         'top20': ['' for _ in range(20)],
         'pos': [0 for _ in range(20)]
         }
         for ano in range(2013, 2022)]

for pos, conj in enumerate(data['rankings']):
    anos[pos]['ano'] = conj['year']
    anos[pos]['top20'] = [conj['placings'][k]['player'] for k in range(20)]
    anos[pos]['pos'] = [k for k in range(1, 21)]
# %%
overall = pd.concat([pd.DataFrame(k) for k in anos]).reset_index(drop=True)
display(overall)
# %%
mais_topados = overall['top20'].value_counts().to_frame()

# %%
pd.options.plotting.backend = "plotly"
mais_topados.plot(kind='bar', figsize=(10, 5))
# %%
plt.bar(mais_topados.index, mais_topados['top20'])
plt.show()
# %%
