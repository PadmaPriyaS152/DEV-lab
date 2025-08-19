import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# ------------------ Data ------------------
world_data = pd.DataFrame({
    'Country': ['United States of America', 'Canada', 'India', 'Brazil', 'China'],
    'Value': [100, 150, 200, 80, 120]
})

india_states_data = pd.DataFrame({
    'State': ['Maharashtra', 'Karnataka', 'Tamil Nadu', 'Uttar Pradesh', 'Gujarat'],
    'Value': [50, 75, 60, 40, 30]
})

india_districts_data = pd.DataFrame({
    'District': ['Mumbai', 'Bengaluru', 'Chennai', 'Lucknow', 'Ahmedabad'],
    'Value': [20, 30, 25, 15, 10]
})

# ------------------ Load Maps ------------------
# World map (from geopandas built-in)
world_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Placeholder: using world_map for India states & districts (replace with actual shapefiles if available)
india_states_map = world_map[world_map['name'] == 'India']
india_districts_map = world_map[world_map['name'] == 'India']

# ------------------ Merge Data ------------------
world_data_geo = world_map.merge(world_data, how='left', left_on='name', right_on='Country')

# For India, since we don't have real state/district shapefiles here, just using placeholder
india_states_data_geo = india_states_map.copy()
india_states_data_geo['Value'] = None

india_districts_data_geo = india_districts_map.copy()
india_districts_data_geo['Value'] = None

# ------------------ Plot ------------------
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# World map
axs[0].set_title('World Data')
world_data_geo.boundary.plot(ax=axs[0], color="black")
world_data_geo.plot(column='Value', ax=axs[0], legend=True,
                    legend_kwds={'label': "Values by Country"})

# India states (placeholder)
axs[1].set_title('India States Data')
india_states_data_geo.boundary.plot(ax=axs[1], color="black")
india_states_data_geo.plot(column='Value', ax=axs[1], legend=True,
                           legend_kwds={'label': "Values by State"})

# India districts (placeholder)
axs[2].set_title('India Districts Data')
india_districts_data_geo.boundary.plot(ax=axs[2], color="black")
india_districts_data_geo.plot(column='Value', ax=axs[2], legend=True,
                              legend_kwds={'label': "Values by District"})

plt.tight_layout()
plt.show()
