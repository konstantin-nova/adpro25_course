caco = pd.read_csv("../Files/Cacophony_sales.csv")
caco['date'] = pd.to_datetime(caco['date'], format)
caco.sort_values(by='date', inlplace='True')

fig, ax = plt.subplots(figsize=(15,6))

astro.plot(x='date', y='sales', ax=ax, label='Astronomy')
barb.plot(x='date', y='sales', ax=ax, label='Barbecuer')
caco.plot(x='date', y='sales', ax=ax, label='Cacophony')

plt.show()