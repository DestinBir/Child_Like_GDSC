# Conception de Recherche de l'Agent de Type Enfant

Ce dossier organise le projet dans une structure plus claire pour la recherche et les ateliers.

Il est pense pour trois cas d'usage:

- expliquer le concept pendant un atelier en direct
- executer le prototype en local
- presenter l'idee comme une petite exploration de type recherche

## Structure du Dossier

- `notebooks/`
  Notebooks interactifs pour l'animation d'atelier et les demonstrations explicatives.
- `scripts/`
  Implementation Python du prototype.
- `docs/`
  Explications ecrites, texte du codelab et guide des fichiers.
- `assets/images/`
  Figures visuelles qui soutiennent l'explication et la presentation.

## Points de Depart Recommandes

- Ouvrez [notebooks/child_like_agent_workshop.ipynb](./notebooks/child_like_agent_workshop.ipynb) pour un notebook de style atelier avec explications.
- Ouvrez [notebooks/child_like_agent_codelab.ipynb](./notebooks/child_like_agent_codelab.ipynb) pour un notebook de style codelab qui melange notes pedagogiques et code executable.
- Lancez [scripts/child_like_agent.py](./scripts/child_like_agent.py) si vous voulez la demo terminal la plus simple.

## Cadre de Recherche

Ce prototype explore une boucle d'apprentissage basee sur l'identite:

`perceive -> decide -> feedback -> evaluate usefulness -> update identity`

Le systeme est volontairement different de l'apprentissage par renforcement:

- pas de fonction de recompense
- pas d'optimisation de politique
- pas de fonction de valeur
- pas de memoire long terme separee

A la place, l'agent apprend en modifiant directement son propre etat d'identite interne.

## Meilleur Fichier Pour une Demo

Si vous avez besoin d'un seul fichier pour une session en direct, utilisez:

- [notebooks/child_like_agent_workshop.ipynb](./notebooks/child_like_agent_workshop.ipynb)

Il repond a l'exigence d'avoir au moins un fichier `.ipynb` explicatif dedie a l'atelier de l'agent de type enfant.
