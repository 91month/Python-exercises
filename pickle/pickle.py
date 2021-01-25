import pickle
example = {'Alice': '2341',
           'Beth': '9102',
           'Cecil': '3258',
           'Dfrt': '4521',
           'Efgh': '788',
           'Flice': '241',
           'Geth': '902',
           'Hecil': '358',
           'Ifrt': '421',
           'Jfgh': '78',
           'Klice': '341',
           'Leth': '102',
           'Mecil': '258',
           'Nfrt': '521',
           'Ofgh': '88',
           'Plice': '41',
           'Qeth': '02',
           'Recil': '58',
           'Sfrt': '21',
           'Tfgh': '8'}
pickle_file= open('example_data.pkl','wb')
pickle.dump(example,pickle_file)
pickle_file.close()

