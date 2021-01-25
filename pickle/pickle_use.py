import pickle
pickle_file = open('example_data.pkl','rb')
example = pickle.load(pickle_file)
print(example)
print(example['Alice'])
