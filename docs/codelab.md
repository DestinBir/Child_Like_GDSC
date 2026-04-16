
# Build a Child-Like AI Agent in Python

## Overview
Duration: 2

In this codelab, you'll build a minimal prototype of a "child-like AI agent" that learns continuously from interaction.

Unlike many AI systems, this prototype does not use:

- large pretrained models
- reward-based reinforcement learning
- a separate long-term memory database

Instead, the agent evolves by updating its own internal identity state over time.

What you'll learn:

- how to model identity as the core state of an agent
- how to implement a simple `perceive -> decide -> feedback -> update` loop
- how to let the agent say "I don't know" when confidence is low
- how to decide whether new information is useful before learning it
- how this approach differs from reinforcement learning

What you'll build:

- one Python script: `child_like_agent.py`
- one workshop-friendly simulation you can run locally

## Why This Is Not Reinforcement Learning
Duration: 2

This prototype is intentionally simple so the learning mechanism is easy to explain.

In reinforcement learning, an agent usually:

- takes an action
- receives a scalar reward
- updates a policy or value estimate to maximize future reward

This codelab does something different.

Here, the agent:

- perceives an input
- makes a prediction with confidence
- receives feedback
- judges whether the feedback is useful
- updates its identity directly

There is no reward signal, no policy gradient, and no optimization loop.

Positive
: The learning logic is visible and easy to inspect.

Positive
: The evolving identity makes the agent's state easy to explain live.

## Prerequisites
Duration: 1

You only need:

- Python 3.9 or newer
- a terminal
- a text editor

No external packages are required.

## Project Files
Duration: 1

This codelab uses the following files:

- `child_like_agent.py` - the runnable prototype
- `codelab.md` - this Google Codelab-style guide

The Python script is intentionally self-contained for easy demos and workshops.

## Run the Prototype
Duration: 2

From the project folder, run:

```bash
python3 child_like_agent.py
```

You should see:

- a step-by-step interaction log
- predictions and confidence values
- usefulness checks before learning
- identity changes after each interaction
- a final summary of what the agent learned

## Understand the Identity Store
Duration: 3

The identity store is the heart of the agent.

It includes:

- `beliefs`: learned categories and examples
- `interaction_count`: total interactions seen
- `learning_count`: how many times identity changed
- `ignored_feedback_count`: how many times feedback was skipped
- `confidence_threshold`: when to say "I don't know"
- `last_update_reason`: a plain-language explanation of the last change

This is important because the agent does not save experiences in a separate memory module.
Its learning is represented directly in the identity itself.

## Step 1: Perceive Input
Duration: 3

The `perceive()` function transforms raw text into a small internal representation.

In this prototype, perception extracts:

- the raw text
- a normalized lowercase string
- a token list
- token count

This keeps the logic simple while still making the learning loop concrete.

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

## Step 2: Decide With Confidence
Duration: 4

The `decide()` function compares input tokens against the examples already stored in identity.

It then:

- picks the best matching category
- computes a rough confidence score
- returns `"I don't know"` if confidence is below threshold

This is the child-like behavior we want for the workshop:
the agent should not pretend to know something it cannot justify.

Negative
: If confidence is too low, the agent should avoid overclaiming.

## Step 3: Evaluate Usefulness Before Learning
Duration: 4

The `evaluate_usefulness()` function is one of the key ideas in this prototype.

The agent does not blindly learn every piece of feedback.
Instead, it asks whether the feedback is useful.

Feedback is considered useful when it:

- introduces a new category
- adds a new example
- corrects a wrong decision
- helps when the agent was uncertain

That means learning is selective, not automatic.

## Step 4: Update Identity
Duration: 4

The `learn()` function updates the agent's identity directly.

If feedback is useful, the script:

- creates the category if needed
- stores the new example
- increases that category's strength
- records why the update happened

If feedback is not useful, the agent does not change identity and logs that the feedback was redundant.

This gives you a very visible notion of development over time.

## Step 5: Watch the Learning Loop
Duration: 3

The simulation loop processes a small sequence of interactions.

For each interaction, the script shows:

- perception
- decision
- confidence
- feedback
- usefulness judgment
- learning decision
- identity diff

This makes it easy to narrate the live demo and point at each stage of the loop.

## Workshop Checkpoint
Duration: 2

At this point, verify that you can explain the following:

1. Why the agent says `"I don't know"` early on.
2. Why repeated feedback may later be ignored as redundant.
3. Why updating identity is different from storing a separate memory log.
4. Why this prototype is not reinforcement learning.

If you can explain those four points, the demo is ready for a workshop.

## Suggested Live Demo Script
Duration: 3

A simple way to present this codelab:

1. Start by showing that the agent knows nothing.
2. Run the first few examples and point out the low-confidence behavior.
3. Show how the identity store changes after each interaction.
4. Highlight a later case where the agent becomes more confident.
5. End with a redundant example to show selective learning.

This progression makes the learning dynamics easy to follow.

## Next Ideas
Duration: 2

If you want to extend the prototype later, you could add:

- an interactive input mode for live audience examples
- simple forgetting or identity drift rules
- conflict handling when feedback disagrees with older beliefs
- multiple identity traits beyond category beliefs

Keep the system small enough that participants can still understand every update.

## Summary
Duration: 1

You built a minimal child-like AI agent in Python that:

- learns continuously from interaction
- updates its own identity over time
- decides whether feedback is useful before learning
- uses uncertainty instead of bluffing
- stays simple enough for a workshop demo

You now have a compact example of identity-based learning that is easy to run locally and easy to explain.
