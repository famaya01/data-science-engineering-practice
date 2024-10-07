import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import time

# --------------------------------------------------------------------------
# LRU cache implementation from scratch
# --------------------------------------------------------------------------

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)  
        self.tail = Node(0, 0)  
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _move_to_head(self, node: Node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> Node:
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int):
        node = self.cache.get(key)
        if not node:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)
            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            node.value = value
            self._move_to_head(node)


class ModelLRUCache:
    def __init__(self, model, capacity: int):
        self.model = model
        self.cache = LRUCache(capacity)

    def get_model_predictions(self, inputs):
        key = tuple(inputs)
        if self.cache.get(key) != -1:
            return self.cache.get(key)
        else:
            prediction = self._generate_prediction(inputs)
            self.cache.put(key, prediction)
            return prediction

    def _generate_prediction(self, inputs):
        formatted_inputs = pd.DataFrame.from_dict({"followers": [inputs[0]], 
                                                   "num_genres": [inputs[1]]})
        return self.model.predict(formatted_inputs)[0]

# read and prepare the dataset
artists = pd.read_csv("data/spotify_600k/artists.csv")
artists = artists.dropna().reset_index(drop=True)
artists['num_genres'] = artists.genres.map(len)
features = ["followers", "num_genres"]

# Train the model
start = time.time()
forest_model = RandomForestRegressor(n_estimators=300,
                                     min_samples_split=40,
                                     max_depth=3,
                                     verbose=1,
                                     n_jobs=3)
forest_model.fit(artists[features], artists.popularity)
end = time.time()
print("Model training runtime: ", end - start)


# Create a model cache with a capacity of 10
model_cache = ModelLRUCache(forest_model, capacity=10)

# Test the model predictions with and without cache
inputs = (2, 4)

start = time.time()
print(model_cache.get_model_predictions(inputs))
end = time.time()
print("Model predictions runtime (w/o cache): ", end - start)

start = time.time()
print(model_cache.get_model_predictions(inputs))
end = time.time()
print("Model predictions runtime (w/ cache): ", end - start)
