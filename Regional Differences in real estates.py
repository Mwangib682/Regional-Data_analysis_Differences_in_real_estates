#IMPORTING THE LIBRARIES TO USE
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
df1 = pd.read_csv("data/brasil-real-estate-1.csv")
df1.head()

#inspect df1 using the info and head methods
df1 = pd.read_csv("data/brasil-real-estate-1.csv")
df1.info()

#Drop all rows with NaN values from the DataFrame df1
df1 = pd.read_csv("data/brasil-real-estate-1.csv")
df1.dropna(inplace = True)
df1.info()

#"lat-lon" column to create two separate columns in df1: "lat" and "lon"
df1.dropna(inplace = True)
df1[["lat","lon"]] = df1["lat-lon"].str.split(",", expand = True).astype(float)
df1.head()

#Use the "place_with_parent_names" column to create a "state" column for df1
df1.dropna(inplace = True)
df1[["lat","lon"]] = df1["lat-lon"].str.split(",", expand = True).astype(float)
df1["state"] = df1["place_with_parent_names"].str.split("|", expand = True)[2]
df1.head()

#Transform the "price_usd" column of df1 so that all values are floating-point numbers instead of strings.
df1.dropna(inplace = True)
df1[["lat","lon"]] = df1["lat-lon"].str.split(",", expand = True).astype(float)

df1["state"] = df1["place_with_parent_names"].str.split("|", expand = True)[2]

df1.dropna(inplace = True)
df1["price_usd"] = (
    df1["price_usd"]
    .str.replace("$", " ", regex = False)
    .str.replace(",", "")
    .astype(float)
)
df1.head()

#Drop the "lat-lon" and "place_with_parent_names" columns from df1
df1.dropna(inplace = True)
df1[["lat","lon"]] = df1["lat-lon"].str.split(",", expand = True).astype(float)

df1["state"] = df1["place_with_parent_names"].str.split("|", expand = True)[2]

df1.dropna(inplace = True)
df1["price_usd"] = (
    df1["price_usd"]
    .str.replace("$", " ", regex = False)
    .str.replace(",", "")
    .astype(float)
)

df1.drop(columns = ["place_with_parent_names", "lat-lon"], inplace = True)
df1.to_csv("data/brasil-real-estate.csv")

df1.head()

#Import the CSV file brasil-real-estate-2.csv into the DataFrame df2
df2 = pd.read_csv("data/brasil-real-estate-2.csv")
df2.head()

#Use the "price_brl" column to create a new column named "price_usd". (Keep in mind that, when this data was collected in 2015 and 2016, a US dollar cost 3.19 Brazilian reals.)
df2 = pd.read_csv("data/brasil-real-estate-2.csv")

df2["price_usd"] = (
    (df2["price_brl"]/3.19)
    .round(2)
)
df2.head()

#Drop the "price_brl" column from df2, as well as any rows that have NaN values.
df2["price_usd"] = (
    (df2["price_brl"]/3.19)
    .round(2)
)
df2.dropna(inplace = True)
df2.drop(columns = ["price_brl"], inplace = True)
df2.to_csv("data/brasil-real-estate.csv")
df2.head()

#Concatenate df1 and df2 to create a new DataFrame named df.
df3 = pd.concat([df1, df2])
print("df shape:", df.shape)
df.to_csv("data/brasil-real-estate-clean.csv")

#create a scatter_mapbox showing the location of the properties in df
df = pd.read_csv("data/brasil-real-estate-clean.csv")
fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    center={"lat": -14.2, "lon": -51.9},  # Map will be centered on Brazil
    width=600,
    height=600,
    hover_data=["price_usd"],  # Display price when hovering mouse over house
)
fig.update_layout(mapbox_style="open-street-map")
fig.show()

#Use the describe method to create a DataFrame summary_stats with the summary statistics for the "area_m2" and "price_usd" columns.
summary_stats = df[["area_m2", "price_usd"]].describe()
summary_stats

#Create a histogram of "price_usd". Make sure that the x-axis has the label "Price [USD]", the y-axis has the label "Frequency", and the plot has the title "Distribution of Home Prices". Use Matplotlib (plt).
# Build histogram
plt.hist(df["price_usd"])
# Label axes
plt.xlabel(["Price [USD]"])
plt.ylabel(["Frequency"])
# Add title
plt.title("Distribution of Home Prices")

#Create a horizontal boxplot of "area_m2". Make sure that the x-axis has the label "Area [sq meters]" and the plot has the title "Distribution of Home Sizes". Use Matplotlib (plt).
# Build box plot
plt.boxplot(df["area_m2"], vert = False)
# Label x-axis
plt.xlabel("Area [Sq meters]")
# Add title
plt.title("Distribution of Home Sizes")

#Use the groupby method to create a Series named mean_price_by_region
df = pd.read_csv("data/brasil-real-estate-clean.csv")
mean_price_by_region = df.groupby("region")["price_usd"].mean().sort_values()
mean_price_by_region.head()

#Use mean_price_by_region to create a bar chart
mean_price_by_region.plot(
    kind = "bar",
    xlabel = "Region",
    ylabel = "Mean Price [USD]",
    title = "Mean Home Price by Region"
)

#Create a DataFrame df_south that contains all the homes from df that are in the "South" region
df = pd.read_csv("data/brasil-real-estate-clean.csv")
df_south =  df3.loc[df3['region'] == 'South']
df_south.info()

#`value_counts` method to create a Series `homes_by_state`
homes_by_state = df_south["state"].value_counts()
homes_by_state

#Create a scatter plot showing price vs. area for the state in df_south that has the largest number of properties
#df = pd.read_csv("data/brasil-real-estate-clean.csv")
# Subset data
df_south_rgs = df3[df3["state"]=="Rio Grande do Sul"]
# Build scatter plot
plt.scatter(x=df_south_rgs["area_m2"], y=df_south_rgs["price_usd"])
# Label axes
plt.xlabel("Area[sq meters]")
plt.ylabel("price [USD]")
# Add title
plt.title("Rio Grande do Sul: Price vs. Area")
p_correlation = df_south_rgs["area_m2"].corr(df_south_rgs["price_usd"])

#Create a dictionary south_states_corr
south_states_corr = df_south["area_m2"].corr(df_south["price_usd"]).astype(dict)
south_states_corr.info()

