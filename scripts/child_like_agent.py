"""
Core idea:
This agent learns by updating its own identity from interaction.
It does not use pretraining, reward-based reinforcement learning,
policy optimization, or a separate long-term memory system.

Learning loop:
    perceive -> decide -> receive feedback -> evaluate usefulness -> update identity

Run:
    python3 child_like_agent.py
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pprint import pformat
from typing import Any, Dict, List, Optional


LINE = "=" * 78
DIVIDER = "-" * 78


@dataclass
class Decision:
    """A simple prediction returned by the agent."""

    prediction: str
    confidence: float
    reason: str


class ChildLikeAgent:
    """
    A tiny identity-based learning agent.

    The identity store is the central state of the system.
    Instead of writing to a separate memory database, the agent updates its
    internal beliefs directly as part of "who it is."
    """

    def __init__(self) -> None:
        self.identity: Dict[str, Any] = {
            "name": "Milo",
            "version": "codelab-prototype-1",
            "beliefs": {},
            "interaction_count": 0,
            "learning_count": 0,
            "ignored_feedback_count": 0,
            "confidence_threshold": 0.60,
            "last_decision": None,
            "last_update_reason": "Agent created.",
        }

    def perceive(self, text: str) -> Dict[str, Any]:
        """
        Turn raw input into a tiny internal representation.

        This keeps the prototype lightweight and easy to explain live.
        """
        normalized = text.strip().lower()
        tokens = [token.strip(".,!?") for token in normalized.split() if token.strip(".,!?")]

        return {
            "raw_text": text,
            "normalized_text": normalized,
            "tokens": tokens,
            "token_count": len(tokens),
        }

    def decide(self, perception: Dict[str, Any]) -> Decision:
        """
        Predict the best matching category from current identity.

        Confidence is based on token overlap with previously learned examples
        plus a small boost from how often that category has been reinforced.
        """
        beliefs = self.identity["beliefs"]
        input_tokens = set(perception["tokens"])

        if not beliefs:
            decision = Decision(
                prediction="I don't know yet.",
                confidence=0.0,
                reason="The agent has no learned beliefs yet.",
            )
            self.identity["last_decision"] = decision.prediction
            return decision

        best_category: Optional[str] = None
        best_score = 0.0
        best_reason = "No useful overlap with known examples."

        for category, belief in beliefs.items():
            example_tokens = set()
            for example in belief["examples"]:
                example_tokens.update(example.split())

            overlap = len(input_tokens & example_tokens)
            coverage = overlap / max(len(input_tokens), 1)
            strength_bonus = min(1.0, 0.4 + 0.1 * belief["strength"])
            score = coverage * strength_bonus

            if score > best_score:
                best_category = category
                best_score = score
                best_reason = (
                    f"Matched {overlap} token(s) with '{category}' examples; "
                    f"belief strength={belief['strength']}."
                )

        threshold = self.identity["confidence_threshold"]
        if best_category is None or best_score < threshold:
            decision = Decision(
                prediction="I don't know.",
                confidence=round(best_score, 2),
                reason=best_reason,
            )
            self.identity["last_decision"] = decision.prediction
            return decision

        decision = Decision(
            prediction=best_category,
            confidence=round(best_score, 2),
            reason=best_reason,
        )
        self.identity["last_decision"] = decision.prediction
        return decision

    def evaluate_usefulness(
        self,
        perception: Dict[str, Any],
        decision: Decision,
        feedback_label: str,
    ) -> Dict[str, Any]:
        """
        Decide whether the feedback should change the identity.

        This is intentionally not reward-based RL.
        The agent is not maximizing a scalar reward.
        It is judging whether the incoming feedback is novel or corrective.
        """
        beliefs = self.identity["beliefs"]
        normalized_text = perception["normalized_text"]
        known_belief = beliefs.get(feedback_label)

        is_new_category = known_belief is None
        is_new_example = not known_belief or normalized_text not in known_belief["examples"]
        was_uncertain = decision.confidence < self.identity["confidence_threshold"]
        was_wrong = decision.prediction not in {
            feedback_label,
            "I don't know.",
            "I don't know yet.",
        }

        useful = is_new_category or is_new_example or was_uncertain or was_wrong

        reasons: List[str] = []
        if is_new_category:
            reasons.append("new category")
        if is_new_example:
            reasons.append("new example")
        if was_uncertain:
            reasons.append("agent was uncertain")
        if was_wrong:
            reasons.append("agent was wrong")
        if not reasons:
            reasons.append("redundant feedback")

        return {"useful": useful, "reason": ", ".join(reasons)}

    def learn(
        self,
        perception: Dict[str, Any],
        feedback_label: str,
        usefulness: Dict[str, Any],
    ) -> bool:
        """
        Update identity directly when the feedback is judged useful.
        """
        self.identity["interaction_count"] += 1

        if not usefulness["useful"]:
            self.identity["ignored_feedback_count"] += 1
            self.identity["last_update_reason"] = f"No learning: {usefulness['reason']}."
            return False

        beliefs = self.identity["beliefs"]
        example = perception["normalized_text"]

        if feedback_label not in beliefs:
            beliefs[feedback_label] = {"examples": [], "strength": 0}

        if example not in beliefs[feedback_label]["examples"]:
            beliefs[feedback_label]["examples"].append(example)

        beliefs[feedback_label]["strength"] += 1
        self.identity["learning_count"] += 1
        self.identity["last_update_reason"] = (
            f"Learned '{feedback_label}' because {usefulness['reason']}."
        )
        return True


def get_demo_interactions() -> List[Dict[str, str]]:
    """Small workshop dataset that shows uncertainty, learning, and redundancy."""
    return [
        {"input": "apple is a fruit", "feedback": "fruit"},
        {"input": "banana is a fruit", "feedback": "fruit"},
        {"input": "carrot is a vegetable", "feedback": "vegetable"},
        {"input": "spinach is a vegetable", "feedback": "vegetable"},
        {"input": "dog is an animal", "feedback": "animal"},
        {"input": "pear is a fruit", "feedback": "fruit"},
        {"input": "truck is a vehicle", "feedback": "vehicle"},
        {"input": "cat is an animal", "feedback": "animal"},
        {"input": "lettuce is a vegetable", "feedback": "vegetable"},
        {"input": "plane is a vehicle", "feedback": "vehicle"},
        {"input": "mango is a fruit", "feedback": "fruit"},
        {"input": "rock is a mineral", "feedback": "mineral"},
        {"input": "banana is a fruit", "feedback": "fruit"},
    ]


def print_banner() -> None:
    """Intro text used in the live demo."""
    print(LINE)
    print("CHILD-LIKE AI AGENT: GOOGLE CODELAB DEMO")
    print(LINE)
    print("This prototype learns by updating identity from interaction.")
    print("It is not reinforcement learning: no reward, no policy, no value function.")
    print()


def print_identity_diff(before: Dict[str, Any], after: Dict[str, Any]) -> None:
    """Print only the parts of identity that changed after an interaction."""
    print("\nIDENTITY CHANGES")
    changed = False

    for key in after:
        if before.get(key) != after.get(key):
            changed = True
            print(f"- {key}:")
            print(f"  before: {pformat(before.get(key))}")
            print(f"  after : {pformat(after.get(key))}")

    if not changed:
        print("- No identity changes")


def print_interaction_summary(
    index: int,
    perception: Dict[str, Any],
    decision: Decision,
    feedback: str,
    usefulness: Dict[str, Any],
    learned: bool,
    identity: Dict[str, Any],
) -> None:
    """Display one clear workshop-friendly interaction trace."""
    print(DIVIDER)
    print(f"INTERACTION {index}")
    print(f"Perception: {perception['raw_text']}")
    print(f"Tokens    : {perception['tokens']}")
    print(f"Decision  : {decision.prediction}")
    print(f"Confidence: {decision.confidence:.2f}")
    print(f"Reason    : {decision.reason}")
    print(f"Feedback  : {feedback}")
    print(f"Useful?   : {usefulness['useful']}")
    print(f"Why learn : {usefulness['reason']}")
    print(f"Learned?  : {learned}")
    print(f"Update    : {identity['last_update_reason']}")


def print_final_summary(agent: ChildLikeAgent) -> None:
    """Display final state in a compact summary."""
    print(LINE)
    print("FINAL SUMMARY")
    print(LINE)
    print(f"Interactions seen : {agent.identity['interaction_count']}")
    print(f"Learning updates  : {agent.identity['learning_count']}")
    print(f"Ignored feedback  : {agent.identity['ignored_feedback_count']}")
    print("Known categories  :", ", ".join(agent.identity["beliefs"].keys()))


def run_demo() -> None:
    """Run the full simulation loop."""
    agent = ChildLikeAgent()
    print_banner()

    for index, item in enumerate(get_demo_interactions(), start=1):
        before_identity = deepcopy(agent.identity)

        perception = agent.perceive(item["input"])
        decision = agent.decide(perception)
        usefulness = agent.evaluate_usefulness(perception, decision, item["feedback"])
        learned = agent.learn(perception, item["feedback"], usefulness)

        print_interaction_summary(
            index=index,
            perception=perception,
            decision=decision,
            feedback=item["feedback"],
            usefulness=usefulness,
            learned=learned,
            identity=agent.identity,
        )
        print_identity_diff(before_identity, agent.identity)
        print("\nCURRENT IDENTITY SNAPSHOT")
        print(pformat(agent.identity, sort_dicts=False))
        print()

    print_final_summary(agent)


if __name__ == "__main__":
    run_demo()
