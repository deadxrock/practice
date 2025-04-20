import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Завантаження даних
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

tickers = ['GOOG', 'SPY']
data = yf.download(tickers, start=start_date, end=end_date)['Close']
data.dropna(inplace=True)

# Логарифмічна прибутковість
returns = np.log(data / data.shift(1)).dropna()

# Візуалізація прибутковості
plt.figure(figsize=(14, 5))
returns.plot(title='Логарифмічна прибутковість GOOG та SPY')
plt.grid(True)
plt.show()

sample = returns.sample(n=60, random_state=1)

# Кореляція
correlation = sample.corr().iloc[0, 1]
print(f"Коефіцієнт кореляції (GOOG vs SPY): {correlation:.4f}")

# Побудова точкової діаграми
plt.figure(figsize=(7, 5))
sns.scatterplot(x='SPY', y='GOOG', data=sample)
plt.title(f'Кореляція між GOOG та SPY\nКоефіцієнт: {correlation:.4f}')
plt.xlabel('SPY прибутковість')
plt.ylabel('GOOG прибутковість')
plt.grid(True)
plt.show()

# Ручна реалізація лінійної регресії GOOG vs SPY
x = sample['SPY'].values
y = sample['GOOG'].values

# Обчислення коефіцієнтів
x_mean = np.mean(x)
y_mean = np.mean(y)
slope = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
intercept = y_mean - slope * x_mean

print(f"Модель лінійної регресії: GOOG = {intercept:.4f} + {slope:.4f} * SPY")

# Побудова лінії регресії
reg_line = intercept + slope * x

plt.figure(figsize=(7, 5))
plt.scatter(x, y, label='Дані')
plt.plot(x, reg_line, color='red', label='Лінія регресії')
plt.title('Ручна лінійна регресія GOOG vs SPY')
plt.xlabel('SPY прибутковість')
plt.ylabel('GOOG прибутковість')
plt.legend()
plt.grid(True)
plt.show()

# Аналіз SPY (останні 63 дні)
spy_close = data['SPY']
spy_recent = spy_close[-63:]

X_days = np.arange(len(spy_recent))
y_prices = spy_recent.values

# Ручна регресія для тренду
x_m = np.mean(X_days)
y_m = np.mean(y_prices)
slope_trend = np.sum((X_days - x_m) * (y_prices - y_m)) / np.sum((X_days - x_m) ** 2)
intercept_trend = y_m - slope_trend * x_m
trend_line = intercept_trend + slope_trend * X_days
std_dev = np.std(y_prices - trend_line)

# Графік тренду та стандартних відхилень
plt.figure(figsize=(10, 5))
plt.plot(spy_recent.index, y_prices, label='SPY Закриття')
plt.plot(spy_recent.index, trend_line, label='Тренд', color='red')
plt.fill_between(spy_recent.index,
                 trend_line - std_dev,
                 trend_line + std_dev,
                 color='gray', alpha=0.3, label='±1 Std Dev')
plt.title('Тренд SPY (останні 63 дні)')
plt.legend()
plt.grid(True)
plt.show()

# Функція прогнозування ціни SPY
def forecast_spy(days_ahead):
    future_day = len(X_days) + days_ahead
    predicted_price = intercept_trend + slope_trend * future_day
    return predicted_price
