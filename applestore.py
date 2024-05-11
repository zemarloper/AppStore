import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
apps = pd.read_csv("C:\MAIN\Tableu Proj\AppleStore.csv")

apps.info()

apps.shape

apps

apps.user_rating.value_counts()

apps.cont_rating.value_counts()

apps.price.value_counts()

apps.drop(columns=['currency'], inplace=True)

more_col_todrop = ['sup_devices.num','ipadSc_urls.num','lang.num','vpp_lic']

apps.drop(columns=more_col_todrop, inplace=True)

new_cols_dict= {
    'id':'app_id',
    'track_name': 'app_name',
    'size_bytes': 'byte_size',
    'price':'price_usd',
    'rating_count_tot': 'total_RC',
    'rating_count_ver': 'RC_vers',
    'user_rating': 'user_rating',
    'user_rating_ver': 'UR_vers',
    'ver': 'version',
    'cont_rating': 'cont_rating',
    'prime_genre': 'genre'    
}

apps.rename(new_cols_dict,axis=1,inplace=True)

apps.head()

plt.figure(figsize=(10, 6))
sns.violinplot(x='cont_rating', y='user_rating', data=apps, inner='quartile', palette='muted')
plt.title('User Ratings Distribution by Content Rating')
plt.xlabel('Content Rating')
plt.ylabel('User Rating')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
genre_order = apps['genre'].value_counts().index
sns.barplot(x=apps['genre'].value_counts().values, y=genre_order, palette='coolwarm')
plt.title('Distribution of Apps by Genre')
plt.xlabel('Number of Apps')
plt.ylabel('Genre')
plt.show()


top_10_apps = apps.sort_values(by=['total_RC', 'user_rating'], ascending=[False, False]).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(y='app_name', x='total_RC', data=top_10_apps, palette='viridis')
plt.title('Top 10 Apps by Total Rating Count')
plt.xlabel('Total Rating Count')
plt.ylabel('App Name')
plt.xticks(ticks=plt.xticks()[0], labels=[f'{int(x):,}' for x in plt.xticks()[0]])
plt.show()


plt.figure(figsize=(12, 8))
corr_matrix = apps.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='GnBu', linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()


apps['price_bins'] = pd.cut(apps['price_usd'], bins=[0, 1, 5, 10, 50, 100, 1000], labels=['Free', '0.99-4.99', '5-9.99', '10-49.99', '50-99.99', '100+'])
price_user_pivot = apps.pivot_table(index='price_bins', columns='user_rating', values='app_id', aggfunc='count')
plt.figure(figsize=(10, 6))
sns.heatmap(price_user_pivot, annot=True, fmt='.0f', cmap='mako', linewidths=0.5)
plt.title('Heatmap of Price vs. User Rating')
plt.xlabel('User Rating')
plt.ylabel('Price Range (USD)')
plt.show()


avg_rating_price = apps.groupby('price_bins')['user_rating'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x='price_bins', y='user_rating', data=avg_rating_price, marker='o', markersize=8, linewidth=2.5, color='blue')
plt.title('Average User Rating by Price Range', fontsize=16)
plt.xlabel('Price Range (USD)', fontsize=14)
plt.ylabel('Average User Rating', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

apps.to_excel('appstore_final.xlsx', sheet_name='Data')

