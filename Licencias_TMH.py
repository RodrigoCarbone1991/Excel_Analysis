# Importo librerías
import pandas as pd
import matplotlib.pyplot as plt

# Leo el archivo Excel
df = pd.read_excel("Status_Licencias.xlsx")

# Reemplazar valores ✓ por 1 y NaN por 0 para hacer conteos
df = df.fillna(0).replace("✔", 1)

# Contar cuántos usuarios tienen cada licencia
licencias = df.iloc[:, 2:].sum()

# Calcular el total de licencias asignadas a usuarios
total_licencias_asignadas = licencias.sum()  # Total de licencias asignadas a usuarios

# Mostrar los conteos por licencia
print(licencias)

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
ax = licencias.plot(kind="bar", color="skyblue")

# Personalizar el gráfico
plt.title("Cantidad de Usuarios por Licencia")
plt.xlabel("Licencia")
plt.ylabel("Número de Usuarios")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Agregar el número de usuarios por encima de cada columna
for i, v in enumerate(licencias):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

# Agregar nombres de usuarios dentro de cada columna, ajustando la posición vertical
for i, col in enumerate(df.columns[2:]):
    usuarios = df[df[col] == 1].iloc[:, 0].tolist()
    usuarios_text = "\n".join(usuarios)
    # Ajustar la posición vertical en función del valor de la barra
    posicion_vertical = licencias[i] * 0.2  # Ajusta este factor según sea necesario
    ax.text(i, posicion_vertical, usuarios_text, ha='center', va='center', fontsize=8, color='black')

# Agregar información adicional en la parte superior del gráfico
info_texto = f"Total de Licecias : {20}\nCantidad de Licencias Asignadas: {total_licencias_asignadas}"
plt.text(0.8, 0.9, info_texto, ha='center', va='bottom', transform=ax.transAxes, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# Mostrar el gráfico
plt.tight_layout()
plt.show()