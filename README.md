# Avalam_Alpha_Zero

Afin d'entraîner le modèle, télécharger pytorch_classification:

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

Afin de comprendre le modèle que j'ai utilisé, je vous conseille la lecture de l'article! Quelques précisions néanmoins:

Afin de lancer l'apprentissage, lancer le fichier main.py, vous pouvez notamment avoir accès une version différente limitant la profondeur de descente dans le mcts à 30 en mettant limited = True 

numIters correspond au nombre de fois ou je cherche un nouveau réseau qui va potentiellement remplacer l'ancien si il le bat, c'est la grande boucle, j'ai mis 80.

numEps est le nombre de parties avec lui meme qu'effectue le réseau/mcts (ils sont toujours par couple) avec lui même lorsque ce nouveau réseau s'entraîne (avant de défier l'ancien), c'est la boucle interne à chaque itération (numIters), je l'ai affecté à 70.

numMCTSSim est la dernière sous boucle qui porte bien son nom: elle décrit le nombre de recherche depuis un état s effectué dans un MCTS (non pas la profondeur de descente qui va par défaut jusqu'aux états terminaux ou inconnu, mais bien le nombre de fois ou j'effectue ma recherche depuis la root constitué de l'état du plateau, il s'agit de developper notre arbre en plus d'affiner la recherche).


Le fichier Combat.py permet de comparer mon réseau créé avec un greedy, un random, un autre réseau entraîné sur un nimIters différent ou vous meme! Un dossier temp se créera, créer en un dans la directory si vous avez un problème.

Si vous souhaitez que je vous envoie le modèle entraîné sur 29 générations, n'hésitez pas à me contactez:
maestratilouis@gmail.com