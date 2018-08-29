# Avalam_Alpha_Zero

Afin d'entra�ner le mod�le, t�l�charger pytorch_classification:

# pytorch-classification
Classification on CIFAR-10/100 and ImageNet with PyTorch.

## Features
* Unified interface for different network architectures
* Multi-GPU support
* Training progress bar with rich info
* Training log and training curve visualization code (see `./utils/logger.py`)

## Install
* Install [PyTorch](http://pytorch.org/)
* Clone recursively
  ```
  git clone --recursive https://github.com/bearpaw/pytorch-classification.git

Afin de comprendre le mod�le que j'ai utilis�, je vous conseille la lecture de l'article! Quelques pr�cisions n�anmoins:

Afin de lancer l'apprentissage, lancer le fichier main.py, vous pouvez notamment avoir acc�s une version diff�rente limitant la profondeur de descente dans le mcts � 30 en mettant limited = True 

numIters correspond au nombre de fois ou je cherche un nouveau r�seau qui va potentiellement remplacer l'ancien si il le bat, c'est la grande boucle, j'ai mis 80.

numEps est le nombre de parties avec lui meme qu'effectue le r�seau/mcts (ils sont toujours par couple) avec lui m�me lorsque ce nouveau r�seau s'entra�ne (avant de d�fier l'ancien), c'est la boucle interne � chaque it�ration (numIters), je l'ai affect� � 70.

numMCTSSim est la derni�re sous boucle qui porte bien son nom: elle d�crit le nombre de recherche depuis un �tat s effectu� dans un MCTS (non pas la profondeur de descente qui va par d�faut jusqu'aux �tats terminaux ou inconnu, mais bien le nombre de fois ou j'effectue ma recherche depuis la root constitu� de l'�tat du plateau, il s'agit de developper notre arbre en plus d'affiner la recherche).


Le fichier Combat.py permet de comparer mon r�seau cr�� avec un greedy, un random, un autre r�seau entra�n� sur un nimIters diff�rent ou vous meme! Un dossier temp se cr�era, cr�er en un dans la directory si vous avez un probl�me.

Si vous souhaitez que je vous envoie le mod�le entra�n� sur 29 g�n�rations, n'h�sitez pas � me contactez:
maestratilouis@gmail.com