# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:05:03 2020

@author: matheus
"""
import numpy as np

class Fila:
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.__valores = np.empty(self.tamanho, dtype=int)
        
    def __fila_vazia(self):
        return self.numero_elementos == 0
    
    def __fila_cheia(self):
        return self.numero_elementos == self.tamanho
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Fila está cheia')
            return
        
        if self.final == self.tamanho -1:
            self.final = -1
        self.final += 1
        self.__valores[self.final] = valor
        self.numero_elementos += 1
        
    
    def desenfileirar(self):
        if self.__fila_vazia():
            print('Fila está vazia')
            return
        
        temp = self.__valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.tamanho:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp
    
    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.__valores[self.inicio]
            
