# -*- coding: utf-8 -*-
import mlconjug
import os
import spacy
import codecs
from pathlib import Path
# import fr_core_news_md


class Text_mining(object):

    """
    Created on 10/2/2021

    @author: Manon Bedere & Gaby Maroun

    Cette classe peut être utilisée pour :
        dictionary: créez un dictionnaire à partir d'un fichier .txt de verbes en ajoutant leurs temps.
        dictionary_percept: créez un dictionnaire à partir d'un fichier .txt de verbes de perceptions en ajoutant leurs temps.
        dic_lexique: créer un dictionnaire avec des mots à partir d'un fichier .txt

    """
    def __init__(self, langue="fr"):
        self.conjugator = mlconjug.Conjugator(language=langue)
        self.nlp = spacy.load("fr_core_news_md") #model with 95% accuracy
        # self.nlp = fr_core_news_md.load()
    
    def dictionary(self,path_input, path_output):
        file_input = codecs.open(path_input, "r+", 'utf-8')
        
        if Path(path_output).is_file():
            if os.stat(path_output).st_size == 0:
                file_output = open(path_output, "w+")
            else:
             file_output = open(path_output, "a")
             
        else:
             file_output = open(path_output, "w")

        for line in file_input :
            word = line.split()[0]
            verb = self.conjugator.conjugate(word)
            forms = verb.iterate()
            for index in range(len(forms)):
                variable = forms[index][len(forms[index])-1]+","+word+","+".motion\n"
                file_output.write(variable)
        
        file_input.close()  
        file_output.close()
        return "Path vers le nouveau dict de verbes: %s"%(path_output)

    def dictionary_percept(self, path_input, path_output):
        file_input = codecs.open(path_input, "r+", 'utf-8')

        if Path(path_output).is_file():
            if os.stat(path_output).st_size == 0:
                file_output = open(path_output, "w+")
            else:
                file_output = open(path_output, "a")

        else:
            file_output = open(path_output, "w")

        for line in file_input:
            word = line.split()[0]
            verb = self.conjugator.conjugate(word)
            forms = verb.iterate()
            for index in range(len(forms)):
                variable = forms[index][len(forms[index]) - 1] + "," + word + "," + ".percept\n"
                file_output.write(variable)

        file_input.close()
        file_output.close()
        return "Path vers le nouveau dict de perceptions: %s" % (path_output)
    
    def dic_lexique(self, path_input, path_output):
        file_input = codecs.open(path_input, "r+", 'utf-8')
        if Path(path_output).is_file():
            if os.stat(path_output).st_size == 0 :
                file_output =open(path_output, "w+")
            else:
             file_output = open(path_output, "a")            
        else:
             file_output = open(path_output, "w")
        
        doc = self.nlp(file_input.read())
        for word in doc:
            # tag = word.pos_
            lemma = word.lemma_
            variable =str(word)+","+str(lemma)+",.motPivot\n"
            file_output.write(variable)

                
        file_input.close()  
        file_output.close() 
        return "Path pour le nouveau dict de lexiques: %s"%(path_output)

if __name__ == "__main__":
    

    file="C:/Users/gabym/Desktop/Semestre 3 UPPA/Text Mining/Projet/"

    project = Text_mining()

    project.dictionary(file+"V-deplace-2020-21.txt",
                        file+"V-deplace-2020-21.dic")

    project.dic_lexique(file+"lexique-mots-pivots2020-21.txt",
                        file+"lexique-mots-pivots2020-21.dic")

    project.dictionary_percept(file+"V-percep2020-21.txt",
                                file+"V-percep2020-21.dic")
