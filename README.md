# stemming algorithm

This approach is to use a Machine learning algorithm to stem the words in a given text. The algorithm is trained on a corpus of words and their stemmed versions. The algorithm is then used to stem the words in a given text.

## How to use

```python
python main.py
```

## Improvements
To further improve the algorithm, the following can be done:

- At the moment, the porter stemmers algorithm is used to create a list of corpus of words that is then fed into the algorithm.

- Get a large corpus of words and their stemmed versions and train the algorithm on it.
then replace the following lines of code 
```python 
# results = [("dance", "dance",), ("dancing", "dance"), ("danced", "dance"),("dancer", "dance"),]
```
with the new corpus.