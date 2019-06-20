import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation, performance_metrics
from fbprophet.plot import plot_cross_validation_metric

df = pd.read_csv('../data/avocado.csv')
df = df[['Date', 'AveragePrice']].dropna()

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

daily_df = df.resample('D').mean()
d_df = daily_df.reset_index().dropna()
sns.set()

plt.plot(d_df['Date'], d_df['AveragePrice'])
plt.title('Avocado Prices')
plt.xlabel('Date')
plt.ylabel('Average Price')
# plt.show()

d_df.columns=['ds', 'y']


m = Prophet()
m.fit(d_df)

future = m.make_future_dataframe(periods=90) # forecast for 90 days
forecast = m.predict(future)
f = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

fig1 = m.plot(forecast)
fig1.savefig('fig1.png')

fig2 = m.plot_components(forecast)
fig2.savefig('fig2.png')

df_cv = cross_validation(m, horizon='90 days')
df_p = performance_metrics(df_cv)
# print(df_p.head(5))

fig3 = plot_cross_validation_metric(df_cv, metric='mape')
fig3.savefig('fig3.png')
