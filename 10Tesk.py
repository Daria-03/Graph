import pandas as pd
import random
from sklearn.preprocessing import OneHotEncoder

# Создаем список с повторяющимися значениями 'robot' и 'human'

lst = ['robot'] * 10
lst += ['human'] * 10

# Перемешиваем значения в списке случайным образом

random.shuffle(lst)

# Создаем DataFrame 'data' с одним столбцом 'whoAmI' из списка lst

data = pd.DataFrame({'whoAmI': lst})

# Создаем экземпляр класса OneHotEncoder с параметром sparse_output=False

encoder = OneHotEncoder(sparse_output=False)

# Применяем OneHotEncoder к столбцу 'whoAmI' в DataFrame 'data'

one_hot = encoder.fit_transform(data[['whoAmI']])

# Создаем DataFrame 'one_hot_df' с преобразованными значениями 'one hot'
# и задаем названия столбцов с помощью encoder.categories_[0]

one_hot_df = pd.DataFrame(one_hot, columns=encoder.categories_[0])

# Объединяем исходный DataFrame 'data' с DataFrame 'one_hot_df' по столбцам

data_encoded = pd.concat([data, one_hot_df], axis=1)

# Выводим первые несколько строк преобразованного DataFrame 'data_encoded'

print(data_encoded.head())