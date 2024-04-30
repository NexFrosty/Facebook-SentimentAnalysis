from google_play_scraper import Sort, reviews_all
import pandas as pd
import numpy as np

g_reviews = reviews_all(
    "com.facebook.katana",
    sleep_milliseconds=0, 
    sort=Sort.NEWEST, 
)

g_df = pd.DataFrame(np.array(g_reviews), columns=['review'])
g_df2 = g_df.join(pd.DataFrame(g_df.pop('review').tolist()))

g_df2.drop(columns=['userImage', 'reviewCreatedVersion'], inplace=True)
g_df2.rename(columns={'userName': 'username', 'at': 'date', 'score': 'rating', 'content': 'comments'}, inplace=True)

g_df2_subset = g_df2[['username', 'date', 'rating', 'comments']]
g_df2_subset['date'] = pd.to_datetime(g_df2_subset['date']).dt.strftime('%Y-%m-%d')
g_df2_subset['comments'] = g_df2_subset['comments'].str.lower()

g_df2_subset.to_excel('D:\Facebook_reviews.xlsx', index=False)
print("Data exported to 'Facebook_reviews.xlsx'")






