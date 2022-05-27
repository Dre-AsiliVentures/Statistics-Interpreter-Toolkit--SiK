from statistics import descriptive_stat

prices=[30000,25000,23000,20000,18000,17500,17000,16000,15000,12000]
pearson_kew=descriptive_stat.skewness(prices)
print(pearson_kew)