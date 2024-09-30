from bertopic import BERTopic
import hdbscan
from umap import UMAP

# Create an adjusted HDBSCAN model
hdbscan_model = hdbscan.HDBSCAN(min_cluster_size=2, min_samples=1)

# Adjust UMAP parameters
umap_model = UMAP(n_neighbors=2, n_components=2, min_dist=0.1)

# Create a BERTopic instance with the adjusted models
topic_model = BERTopic(hdbscan_model=hdbscan_model, umap_model=umap_model)

# Sample documents
docs = [
    "I love programming in Python.",
    "Machine learning and artificial intelligence are fascinating.",
    "Python is great for data science and machine learning.",
    "Natural language processing enables computers to understand text.",
    "Topic modeling helps discover themes in documents."
    "XXX"
]

# Fit the BERTopic model on the documents
topics, probs = topic_model.fit_transform(docs)

# View topic information
topic_info = topic_model.get_topic_info()
print(topic_info)

# View words contributing to each topic
for topic_num in topic_info['Topic']:  # Use 'Topic' instead of 'topic'
    if topic_num != -1:  # Ignore outlier topic labeled as -1
        print(f"Topic {topic_num}: {topic_model.get_topic(topic_num)}")
