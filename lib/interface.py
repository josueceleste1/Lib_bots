# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:10:33 2020

@author: josue
"""
import webbrowser
import pyautogui
import time
import os
import fnmatch
import shutil

def mover_e_clicar(x, y):
    #Clickar no campo de comentario
    pyautogui.moveTo(x,y, duration=0.25)
    time.sleep(1)
    pyautogui.click(x,y, button='left', duration=0.25)
    time.sleep(1)

def digitar_algo(texto):
    #Digita um texto
    pyautogui.typewrite(texto)
    time.sleep(1)
    
def scroll_do_mouse(x):
    #scroll para baixo -x
    #scroll para cima x
    pyautogui.scroll(x) 
    
def mover_arquivo(arquivo, origem, destino):
    #Define a pasta inicial, onde o google chrome faz o download de arquivos
    os.chdir(origem)
    recent_download_file_name = ''
    
    # Procurando pelo arquivo na pasta de origem
    for entry in os.listdir('.'):
      if fnmatch.fnmatch(entry, arquivo): #pequisando pelo arquivo
        recent_download_file_name = arquivo #caso encontre ele guarda na variavel
        print('Encontrado!')
        print(entry)
    
    #Caso exista, ele ira mover
    if recent_download_file_name != '':  
        print('Movendo...', recent_download_file_name)
        #movo para o local de destino
        shutil.move(recent_download_file_name, destino+arquivo) 
        print('Completo!')


    
    
    
    
    
    
    
    
    
    
    
    