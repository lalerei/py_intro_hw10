import random
import pandas as pd

# Задача 44:ниже представлен код генерирующий DataFrame, которая состоит
# всего из 1 столбца.Ваша задача перевести его в one hot вид (без get_dummies)
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()
# Формат сдачи: ссылка на пулл в свой репозиторий.

lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})
data.head()

peculiar = data["whoAmI"].unique()
one_hot = pd.DataFrame()

for value in peculiar:
    one_hot[value] = (data["whoAmI"] == value).astype(int)
print(one_hot.head())
