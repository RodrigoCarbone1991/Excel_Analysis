import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Licencias.xlsx", sheet_name = "PRODUCCION")


# Reemplazar valores ✓ por 1 y NaN por 0 para hacer conteos
df = df.fillna(0).replace("si", 1)

# Contar cuántos usuarios tienen cada licencia
licencias = df.iloc[:, 2:].sum()

# Mostrar los conteos por licencia
print(licencias)

# Crear el gráfico de barras
plt.figure(figsize = (10, 6))
licencias.plot(kind = "bar", color = "skyblue")

# Personalizar el gráfico
plt.title("Cantidad de Usuarios Licencia")
plt.xlabel("Licencia")
plt.ylabel("Número de Usuarios")
plt.xticks(rotation = 0)
plt.grid(axis = "y", linestyle = "--", alpha  =0.7)

# Mostrar el gráfico
plt.show()


