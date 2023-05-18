import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('datasets/diabets.csv')
df = pd.DataFrame(data)

df_diabetes = df[df['diabetes'] == 1]
df_diabetes['age'].plot(kind='hist', bins=10)
plt.xlabel('Вік')
plt.ylabel('Кількість пацієнтів')
plt.title('Графік залежності наявності діабету від віку')
plt.show()

# Графік залежності паління та діабету
smoking_labels = {'never': 'Ніколи не палив', 'former': 'Колишній курець', 'current': 'Курець'}
df['smoking_history'] = df['smoking_history'].map(smoking_labels)
smoking_diabetes_table = pd.crosstab(df['smoking_history'], df['diabetes'])
smoking_diabetes_table.plot(kind='barh')
plt.xlabel('Кількість пацієнтів')
plt.ylabel('Звичка паління')
plt.title('Графік залежності наявності діабету від паління')
plt.legend(title='Наявність діабету', labels=['Немає', 'Є'])
plt.show()

# Графік проценту діабету у курців
smoking_diabetes_table = pd.crosstab(df['smoking_history'], df['diabetes'])
total_patients = smoking_diabetes_table.sum(axis=1)
smoking_diabetes_table['Відсоток наявності діабету'] = smoking_diabetes_table[1] / total_patients * 100
smoking_diabetes_table['Відсоток наявності діабету'].plot(kind='barh')
plt.xlabel('Відсоток наявності діабету')
plt.ylabel('Звичка паління')
plt.title('Процент діабету у людей в залежності від паління')
plt.show()

# Группировка данных по полу и наличию диабета
gender_diabetes_table = pd.crosstab(df['gender'], df['diabetes'])
df_diabetes = df[df['diabetes'] == 1]
filtered_df = df_diabetes[df_diabetes['gender'].isin(['Male', 'Female'])]
print(gender_diabetes_table)
gender_labels = {'Male': 'Чоловік', 'Female': 'Жінка'}
filtered_df['gender'] = filtered_df['gender'].map(gender_labels)
gender_diabetes_table = pd.crosstab(filtered_df['gender'], filtered_df['diabetes'])
gender_diabetes_table[1].plot(kind='pie', autopct='%1.1f%%')
plt.axis('equal')
plt.title('Діаграмма наявності діабету в залежності від статі')
plt.ylabel('')
plt.show()
