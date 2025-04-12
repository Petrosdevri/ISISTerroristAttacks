import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

df = pd.read_excel('ISIS Terrorist Attacks in 2024.xlsx', sheet_name='Φύλλο1')

fig, ax = plt.subplots(figsize=(12, 10), subplot_kw={'projection': ccrs.PlateCarree()})

ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.BORDERS, linestyle=':')

ax.set_extent([-20, 160, -40, 60])

for index, row in df.iterrows():
    if pd.notna(row['Coordinates']):
        lat, lon = map(float, row['Coordinates'].split(','))
        ax.plot(lon, lat, 'ro', markersize=3, transform=ccrs.PlateCarree(), label='Attack' if index == 0 else '')

plt.title('ISIS Terrorist Attacks in 2024', fontsize=15)
plt.legend(loc='upper right', title='Legend')

plt.savefig('ISIS Terrorist Attacks in 2024.png', dpi=300, bbox_inches='tight')
plt.show()