
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('optimization_results.csv')

# Plot Yield vs. Batch
plt.figure(figsize=(6, 4))
plt.plot(df['Batch'], df['Yield (%)'], marker='o')
plt.xlabel('Batch Number')
plt.ylabel('Yield (%)')
plt.title('Yield of Aspirin vs. Batch')
plt.grid(True)
plt.tight_layout()
plt.savefig('yield_vs_batch.png')
plt.show()

# Display the best simulation energy
best = df.loc[df['Simulation Energy (a.u.)'].idxmin()]
print(f'Best batch: {best["Batch"]}, Energy: {best["Simulation Energy (a.u.)"]}')
