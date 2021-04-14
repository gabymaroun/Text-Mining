Mode de déploiement du projet Text Mining    
2020/2021

Bédère Manon et Maroun Gaby


Dans ce dossier vous trouverez plusieurs parties: 

1. Le dossier Dela qui contient les dictionnaires envoyés par le professeur et les trois dictionnaires que nous avons créés pour les mots pivot, les verbes de mouvement et les verbe de perception grâce aux trois listes données par le professeur. Le code python qui nous a été utile pour créer ces dictionnaires est présent dans le dossier principal au nom de "textmining_codepython_dictionnaires "

2. Le dossier Graph contient tous les graphes que nous avons créé. Il y en a en tout 9.
    * graphedistance : Permet de retrouver les ditances ou les heures dans les textes
    * grapheoffset : Repère tous les mots qui préciseront le mot pivot ( à droite, en haut, à proximité ....)
    * grapheverbemouv : Permet de repérer les verbes de mouvement présent dans le dictionnaire des verbes de mouvement 
    * grapheverbepercept : Permet de retrouver les verbes de perception présent dans le dictionnaire des verbes de perception
    * graphenomderue : Permet de récupérer les noms de rue dans le texte
    * graphemotpivot : Graphe qui permet de retrouver les mots-pivot présent dans le dictionnaire des mots pivot
    * grapheENE : Graphe regroupant la plupart des graphe pour retrouver les entités nominales
    * graphemotcompose: Repère les mots-composés
    * grapheapostrophe: Repère les mots avec des apostrophes

3. Le dossier Corpus contient les différent texte qui seront ensuite souvient à la cascade pour en faire une annotation du texte

4. Le dossier CasSys contient la cascade qui permet d'obtenir l'annotation des graphes.

5. Le dossier Résultats_Annotation_corpus contient les résultat obtenu sur Unitex lorsqu'on applique la cascade.

6. Le dossier Résultats_Annotation_corpus_XML contient les résultats de l’annotation transcrits dans un fichier de type XML et visualisables dans un navigateur grâce à une 
feuille de style CSS.

7. Le dossier Résultats_Rappel_Precision_F1score contient les résultats avec les scores pour le rappel, la précision et la Fmesure sur les textes annotés. La méthode appliquée est aussi expliquée.



Pour exécuter les graphes et la cascade dans Unitex, il faut :

1. Récupérer dans les dossiers "Graph, Dela, CasSys et Corpus" les différents fichiers présents et les mettre exactement dans les mêmes dossiers sur votre ordinateur au dossier Unitex.

2. Aller dans Unitex (si vous êtes sur Linux, vous pouvez écrire dans un terminal : "/opt/Unitex-GramLab-3.1/App/Unitex" pour pouvoir ouvrir le logiciel)

 
3. Ouvrir nos 5 dictionnaires (ceux présents dans le dossier dico et faire un après l'autre) et suivre la méthode suivante:
    * Ouvrir un dictionnaire dans Dela
    * Faire "Check Format.."
    * et ensuite faire "Compress into FST"

4. Ouvrir un texte dans "Text" et faire le prétraitement du texte c'est à dire la tokenization

5. Puis, dans "Text", cliquer sur "Apply Lexical Ressources"
    * cliquer ensuite sur "clear"
    * Puis choisir les 5 dictionnaires à utiliser

6. Enfin, vous pouvez soit 
    * Appliquer un graphe en particulier sur le texte : Aller dans "Text" --> "Locate Pattern" --> "Choisir son graphe" --> Mettre "Merge with input text" et faire "Search". 
  Puis pour finir cliquer sur "Build concordance".
    * Appliquer la cascade sur le texte : Aller dans "Text" --> "Apply CasSys Cascade" --> Choisir sa cascade puis faire "Launch".  Puis pour finir cliquer sur "Build concordance". 









