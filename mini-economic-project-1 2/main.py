import pandas as pd
import matplotlib.pyplot as plt
import os

# Διαβάζουμε τα δεδομένα CPI από το αρχείο
df = pd.read_csv('data/cpi.csv')

# Προβολή των πρώτων γραμμών για έλεγχο
print(df.head())

# Δημιουργία φακέλου 'plots' αν δεν υπάρχει
if not os.path.exists('plots'):
    os.makedirs('plots')

# Δημιουργία γραφήματος
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['CPI'], marker='o')
plt.title('Δείκτης Τιμών Καταναλωτή (CPI)')
plt.xlabel('Ημερομηνία')
plt.ylabel('CPI')
plt.grid(True)
plt.tight_layout()

# Αποθήκευση εικόνας στον φάκελο 'plots'
plt.savefig('plots/cpi_chart.png')

# Εμφάνιση γραφήματος
plt.show()
