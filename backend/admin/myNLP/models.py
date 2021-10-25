import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import csv
from admin.common.models import ValueObject

class NaverMovie(object):
    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/myNLP/data/'

    def web_scraping(self):
        ctx = self.vo.context
        driver = webdriver.Chrome(f'{ctx}chromedriver')
        driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_divs = soup.find_all('div', attrs={'class', 'tit3'})
        products = [[div.a.string for div in all_divs]]
        with open(f'{ctx}naver_movie_dataset.csv', 'w', encoding='UTF-8', newline='') as f:
            wr = csv.writer(f)
            wr.writerows(products)
        driver.close()





class MyImdb(object):
    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/myNLP/data/'

    def decode_reviews(self, text, reverse_word_index):
        return ''.join([reverse_word_index.get(i, '?') for i in text])

    def imdb_process(self):
        imdb = keras.datasets.imdb
        (train_X, train_Y), (test_X, test_Y) = imdb.load_data(num_words=10000)
        word_index = imdb.get_word_index()
        word_index = {k: (v+3) for k, v in word_index.items()}
        word_index["<PAD>"] = 0
        word_index["<START>"] = 1
        word_index["<UNK>"] = 2
        word_index["<UNUSED>"] = 3
        reverse_word_index = dict([(v, k) for (k, v) in word_index.items()])
        # print(reverse_word_index)
        temp = self.decode_reviews(test_X[1], reverse_word_index)
        train_X = keras.preprocessing.sequence.pad_sequences(train_X, value=word_index['<PAD>'], padding='post', maxlen=256)
        test_X = keras.preprocessing.sequence.pad_sequences(train_X, value=word_index['<PAD>'], padding='post', maxlen=256)
        vacab_size = 10000
        model = keras.Sequential()
        model.add(keras.layers.Embedding(vacab_size, 16, input_shape=(None,)))
        model.add(keras.layers.GlobalAvgPool1D())
        model.add(keras.layers.Dense(16, activation=tf.nn.relu))
        model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))
        model.compile(optimizer=tf.optimizers.Adam(), loss='binary_crossentropy', metrics=['acc'])
        x_val = train_X[:10000]
        partial_X_train = train_X[10000:]
        y_val = train_Y[:10000]
        partial_Y_train = train_Y[10000:]
        history = model.fit(partial_X_train, partial_Y_train, epochs=40, batch_size=512, validation_data=(x_val, y_val))
        result = model.evaluate(test_X, test_Y)
        print(f'{result}')

        history_dict = history.history
        history_dict.keys()
        acc = history_dict['acc']
        val_acc = history_dict['val_acc']
        loss = history_dict['loss']
        val_loss = history_dict['val_loss']
        epochs = range(1, len(acc) + 1)
        print('==============')
        # "bo"는 "파란색 점"입니다
        plt.plot(epochs, loss, 'bo', label='Training loss')
        # b는 "파란 실선"입니다
        plt.plot(epochs, val_loss, 'b', label='Validation loss')
        plt.title('Training and validation loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()

        # plt.show()
        # plt.savefig(f'{self.vo.context}imdb_test.png')
        plt.clf()  # 그림을 초기화합니다

        plt.plot(epochs, acc, 'bo', label='Training acc')
        plt.plot(epochs, val_acc, 'b', label='Validation acc')
        plt.title('Training and validation accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.savefig(f'{self.vo.context}imdb_nlp.png')