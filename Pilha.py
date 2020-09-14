# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:58:56 2020

@author: matheus
"""

import numpy as np

class Pilha:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__topo = -1
        self.__valores = np.empty(self.__tamanho, dtype=int)

    def __pilha_cheia(self):
        if self.__topo == self.__tamanho -1:
            return True
        else:
            return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('Pilha cheia!')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print('Pilha vazia')
        else:
            self.__topo -= 1

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1