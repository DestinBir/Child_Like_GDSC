# Guide des Fichiers

Ce guide distingue le role de chaque fichier dans le dossier `research_design`.

## Notebooks

### `notebooks/child_like_agent_workshop.ipynb`

Notebook principal pour l'atelier.

Utilisez-le si vous voulez:

- un deroulement pedagogique en direct
- une explication melangeant code et sorties
- une experience notebook plus orientee presentation

### `notebooks/child_like_agent_codelab.ipynb`

Notebook explicatif de style codelab.

Utilisez-le si vous voulez:

- un parcours educatif etape par etape
- des explications markdown avec des cellules de code executables
- un notebook qui reprend la logique du script Python autonome

## Script

### `scripts/child_like_agent.py`

Implementation Python autonome.

Utilisez-le si vous voulez:

- une execution locale minimale dans le terminal
- un seul fichier source clair pour la logique du prototype
- un point de depart facile pour des modifications

## Documentation

### `docs/codelab.md`

Document codelab en Markdown.

Utilisez-le si vous voulez:

- un format de tutoriel ecrit
- un document adaptable pour des notes d'atelier ou une publication
- une explication du prototype hors notebook

### `docs/file_guide.md`

Ce fichier.

Utilisez-le si vous voulez:

- une orientation rapide dans le dossier
- une facon de distinguer quel artefact ouvrir en premier

## Ressources Visuelles

### `assets/images/belief_update.png`

Soutient l'explication de l'evolution des croyances.

### `assets/images/confidence_evolution.png`

Soutient l'explication de l'evolution de la confiance au fil du temps.

### `assets/images/feature_space.png`

Soutient l'explication de la vue representationnelle du systeme jouet.

## Workflow Suggere

1. Commencez par `README.md`.
2. Ouvrez `notebooks/child_like_agent_workshop.ipynb` pour l'explication en direct.
3. Utilisez `scripts/child_like_agent.py` pour la version executable la plus simple.
4. Consultez `docs/codelab.md` pour les notes pedagogiques ecrites.
