# Abstract

This project presents a minimal research-style prototype of a child-like AI agent that learns by updating its own internal identity state over time. Instead of relying on a pretrained model, a separate long-term memory, or reinforcement learning, the agent follows a simple loop: perceive an input, make a decision with confidence, receive feedback, evaluate whether the feedback is useful, and update identity only when the information is worth learning.

The main contribution of the prototype is its emphasis on visible, inspectable learning. The agent can say "I do not know" when confidence is low, which makes uncertainty explicit rather than hidden behind forced predictions. Feedback is not treated as automatically valuable; the system checks whether it introduces a new category, adds a new example, corrects an error, or helps resolve uncertainty before changing the identity state.

This design makes the learning process easy to explain in an educational setting and useful for workshops or live demonstrations. It offers a compact alternative framing for agent adaptation: not policy optimization, but identity evolution through selective interaction-driven updates.
