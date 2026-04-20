# Child-Like Agent (GDSC Research Demo)

A compact educational project that demonstrates a **child-like learning loop** in Python.
Instead of reinforcement learning, the agent updates its internal identity directly from interaction feedback.

## Project Description

This repository is designed for:

- live workshops and demos
- local experimentation with a simple executable prototype
- explaining identity-driven learning in a clear, inspectable way

Core loop:

`perceive -> decide -> feedback -> evaluate usefulness -> update identity`

## Why This Project Is Different

This prototype intentionally does **not** use:

- reward-based reinforcement learning
- policy optimization
- value functions
- separate long-term memory storage

The agent learns by modifying its own identity state (`beliefs`, confidence behavior, and update reasons).

## Repository Structure

- `scripts/`  
  Executable Python prototype (`child_like_agent.py`).
- `notebooks/`  
  Workshop and codelab notebooks for interactive teaching.
- `docs/`  
  Written documentation (`codelab.md`, `file_guide.md`).
- `assets/images/`  
  Visual assets used in explanations.

## Quick Start

### 1) Prerequisites

- Python 3.9+
- pip

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the terminal demo

```bash
python scripts/child_like_agent.py
```

## Recommended Entry Points

- Workshop notebook: [`notebooks/child_like_agent_workshop.ipynb`](./notebooks/child_like_agent_workshop.ipynb)
- Codelab notebook: [`notebooks/child_like_agent_codelab.ipynb`](./notebooks/child_like_agent_codelab.ipynb)
- Script demo: [`scripts/child_like_agent.py`](./scripts/child_like_agent.py)

## Documentation

- Codelab guide: [`docs/codelab.md`](./docs/codelab.md)
- File orientation guide: [`docs/file_guide.md`](./docs/file_guide.md)

## Contributing

Contributions are welcome.
Please read [`CONTRIBUTING.md`](./CONTRIBUTING.md) before opening an issue or pull request.

## Code of Conduct

This project follows a community code of conduct:
[`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)

## Security

Please review [`SECURITY.md`](./SECURITY.md) for how to report vulnerabilities.

## License

This project is licensed under the MIT License.
See [`LICENSE`](./LICENSE) for details.
