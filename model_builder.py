from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle

similarity = cosine_similarity(vectors)

top_k = 20
similarity_dict = {}

for i in range(len(similarity)):
    # Get sorted indices (descending)
    sorted_indices = np.argsort(similarity[i])[::-1]
    
    # Remove itself and take top_k
    top_indices = [idx for idx in sorted_indices if idx != i][:top_k]
    
    similarity_dict[i] = top_indices

# Save the smaller file
with open("similarity_dict.pkl", "wb") as f:
    pickle.dump(similarity_dict, f)