# Child-Like Agent Research Design

This folder organizes the project into a cleaner research and workshop structure.

It is designed for three use cases:

- explaining the concept in a live workshop
- running the prototype locally
- presenting the idea as a small research-style exploration

## Folder Structure

- `notebooks/`
  Interactive notebooks for workshop delivery and explanatory demos.
- `scripts/`
  Plain Python implementation of the prototype.
- `docs/`
  Written explanation, codelab text, and file guide.
- `assets/images/`
  Visual figures that support explanation and presentation.

## Recommended Starting Points

- Open [notebooks/child_like_agent_workshop.ipynb](./notebooks/child_like_agent_workshop.ipynb) for a workshop-style notebook with explanation.
- Open [notebooks/child_like_agent_codelab.ipynb](./notebooks/child_like_agent_codelab.ipynb) for a codelab-style notebook that mixes teaching notes and runnable code.
- Run [scripts/child_like_agent.py](./scripts/child_like_agent.py) if you want the simplest terminal demo.

## Research Framing

This prototype explores an identity-based learning loop:

`perceive -> decide -> feedback -> evaluate usefulness -> update identity`

The system is intentionally different from reinforcement learning:

- no reward function
- no policy optimization
- no value function
- no separate long-term memory store

Instead, the agent learns by directly changing its own internal identity state.

## Best File For a Demo

If you need one file for a live session, use:

- [notebooks/child_like_agent_workshop.ipynb](./notebooks/child_like_agent_workshop.ipynb)

It satisfies the requirement of having at least one explanatory `.ipynb` dedicated to the child-like agent workshop.
