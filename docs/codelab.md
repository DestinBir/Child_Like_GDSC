
# Construire un Agent IA de Type Enfant en Python

## Vue d'ensemble
Duration: 2

Dans ce codelab, vous allez construire un prototype minimal d'"agent IA de type enfant" qui apprend en continu a partir des interactions.

Contrairement a de nombreux systemes d'IA, ce prototype n'utilise pas:

- de grands modeles pre-entraines
- l'apprentissage par renforcement base sur une recompense
- une base de memoire long terme separee

A la place, l'agent evolue en mettant a jour son propre etat interne d'identite au fil du temps.

Ce que vous allez apprendre:

- comment modeliser l'identite comme etat central de l'agent
- comment implementer une boucle simple `perceive -> decide -> feedback -> update`
- comment permettre a l'agent de dire "Je ne sais pas" quand la confiance est faible
- comment decider si une nouvelle information est utile avant de l'apprendre
- en quoi cette approche differe de l'apprentissage par renforcement

Ce que vous allez construire:

- un script Python: `child_like_agent.py`
- une simulation adaptee aux ateliers, executable en local

## Pourquoi ce n'est pas de l'Apprentissage par Renforcement
Duration: 2

Ce prototype est volontairement simple afin que le mecanisme d'apprentissage soit facile a expliquer.

En apprentissage par renforcement, un agent:

- effectue une action
- recoit une recompense scalaire
- met a jour une politique ou une estimation de valeur pour maximiser la recompense future

Ce codelab propose une approche differente.

Ici, l'agent:

- percoit une entree
- fait une prediction avec un niveau de confiance
- recoit un retour
- juge si ce retour est utile
- met a jour directement son identite

Il n'y a ni signal de recompense, ni gradient de politique, ni boucle d'optimisation.

Positive
: La logique d'apprentissage est visible et facile a inspecter.

Positive
: L'identite evolutive rend l'etat de l'agent facile a expliquer en direct.

## Prerequis
Duration: 1

Vous avez seulement besoin de:

- Python 3.9 ou plus recent
- un terminal
- un editeur de texte

Les dependances externes sont listees dans `requirements.txt`.

## Fichiers du Projet
Duration: 1

Ce codelab utilise les fichiers suivants:

- `child_like_agent.py` - le prototype executable
- `codelab.md` - ce guide au format type Google Codelab

Le script Python est volontairement autonome pour faciliter les demos et les ateliers.

## Executer le Prototype
Duration: 2

Depuis le dossier du projet, executez:

```bash
python3 child_like_agent.py
```

Vous devriez voir:

- un journal des interactions pas a pas
- des predictions et des scores de confiance
- des verifications d'utilite avant l'apprentissage
- des changements d'identite apres chaque interaction
- un resume final de ce que l'agent a appris

## Comprendre le Magasin d'Identite
Duration: 3

Le magasin d'identite est le coeur de l'agent.

Il inclut:

- `beliefs`: categories et exemples appris
- `interaction_count`: nombre total d'interactions observees
- `learning_count`: nombre de fois ou l'identite a change
- `ignored_feedback_count`: nombre de fois ou le retour a ete ignore
- `confidence_threshold`: seuil pour dire "Je ne sais pas"
- `last_update_reason`: explication en langage naturel de la derniere modification

Ce point est important car l'agent ne sauvegarde pas ses experiences dans un module memoire separe.
Son apprentissage est represente directement dans son identite.

## Etape 1: Percevoir l'Entree
Duration: 3

La fonction `perceive()` transforme le texte brut en une petite representation interne.

Dans ce prototype, la perception extrait:

- le texte brut
- une chaine normalisee en minuscules
- une liste de tokens
- le nombre de tokens

Cela garde une logique simple tout en rendant la boucle d'apprentissage concrete.

```python
def perceive(self, text: str) -> Dict[str, Any]:
    normalized = text.strip().lower()
    tokens = [token.strip(".,!?") for token in normalized.split() if token.strip(".,!?")]
    return {
        "raw_text": text,
        "normalized_text": normalized,
        "tokens": tokens,
        "token_count": len(tokens),
    }
```

## Etape 2: Decider Avec Confiance
Duration: 4

La fonction `decide()` compare les tokens d'entree avec les exemples deja stockes dans l'identite.

Ensuite, elle:

- choisit la categorie la plus proche
- calcule un score de confiance approximatif
- renvoie `"Je ne sais pas"` si la confiance est sous le seuil

Ce comportement de type enfant est ce que nous voulons pour l'atelier:
l'agent ne doit pas pretendre savoir ce qu'il ne peut pas justifier.

Negative
: Si la confiance est trop faible, l'agent doit eviter de sur-affirmer.

## Etape 3: Evaluer l'Utilite Avant d'Apprendre
Duration: 4

La fonction `evaluate_usefulness()` est l'une des idees cles de ce prototype.

L'agent n'apprend pas aveuglement chaque retour.
A la place, il se demande si ce retour est utile.

Un retour est considere utile lorsqu'il:

- introduit une nouvelle categorie
- ajoute un nouvel exemple
- corrige une decision incorrecte
- aide lorsque l'agent etait incertain

Cela signifie que l'apprentissage est selectif, pas automatique.

## Etape 4: Mettre a Jour l'Identite
Duration: 4

La fonction `learn()` met a jour directement l'identite de l'agent.

Si le retour est utile, le script:

- cree la categorie si necessaire
- stocke le nouvel exemple
- augmente la force de cette categorie
- enregistre la raison de la mise a jour

Si le retour n'est pas utile, l'agent ne change pas d'identite et consigne que le retour etait redondant.

Cela donne une notion tres visible de l'evolution au fil du temps.

## Etape 5: Observer la Boucle d'Apprentissage
Duration: 3

La boucle de simulation traite une petite sequence d'interactions.

Pour chaque interaction, le script montre:

- perception
- decision
- confiance
- retour
- evaluation d'utilite
- decision d'apprentissage
- differences d'identite

Cela facilite la narration de la demo en direct et la mise en evidence de chaque etape de la boucle.

## Point de Controle Atelier
Duration: 2

A ce stade, verifiez que vous pouvez expliquer les points suivants:

1. Pourquoi l'agent dit `"Je ne sais pas"` au debut.
2. Pourquoi des retours repetes peuvent ensuite etre ignores comme redondants.
3. Pourquoi la mise a jour de l'identite est differente d'un journal memoire separe.
4. Pourquoi ce prototype n'est pas de l'apprentissage par renforcement.

Si vous pouvez expliquer ces quatre points, la demo est prete pour un atelier.

## Script de Demo en Direct Suggere
Duration: 3

Une facon simple de presenter ce codelab:

1. Commencez en montrant que l'agent ne sait rien.
2. Lancez les premiers exemples et soulignez le comportement de faible confiance.
3. Montrez comment le magasin d'identite change apres chaque interaction.
4. Mettez en avant un cas plus tardif ou l'agent devient plus confiant.
5. Terminez avec un exemple redondant pour montrer l'apprentissage selectif.

Cette progression rend la dynamique d'apprentissage facile a suivre.

## Idees Suivantes
Duration: 2

Si vous voulez etendre le prototype plus tard, vous pouvez ajouter:

- un mode d'entree interactif pour des exemples proposes par le public
- des regles simples d'oubli ou de derive d'identite
- une gestion des conflits quand le retour contredit des croyances plus anciennes
- plusieurs traits d'identite au-dela des croyances de categorie

Gardez le systeme assez petit pour que les participants puissent toujours comprendre chaque mise a jour.

## Resume
Duration: 1

Vous avez construit un agent IA de type enfant minimal en Python qui:

- apprend en continu a partir des interactions
- met a jour sa propre identite au fil du temps
- decide si le retour est utile avant d'apprendre
- utilise l'incertitude au lieu de bluffer
- reste assez simple pour une demo d'atelier

Vous avez maintenant un exemple compact d'apprentissage base sur l'identite, facile a executer en local et facile a expliquer.
