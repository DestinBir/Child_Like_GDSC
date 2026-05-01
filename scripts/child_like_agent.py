"""
Idee centrale:
Cet agent apprend en mettant a jour sa propre identite a partir des interactions.
Il n'utilise pas de pre-entrainement, d'apprentissage par renforcement base
sur une recompense, d'optimisation de politique, ni de systeme de memoire
long terme separe.

Boucle d'apprentissage:
    perceive -> decide -> receive feedback -> evaluate usefulness -> update identity

Execution:
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
    """Une prediction simple retournee par l'agent."""

    prediction: str
    confidence: float
    reason: str


class ChildLikeAgent:
    """
    Un petit agent d'apprentissage base sur l'identite.

    Le magasin d'identite est l'etat central du systeme.
    Au lieu d'ecrire dans une base memoire separee, l'agent met a jour ses
    croyances internes directement comme une partie de "ce qu'il est".
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
            "last_update_reason": "Agent cree.",
        }

    def perceive(self, text: str) -> Dict[str, Any]:
        """
        Transformer une entree brute en petite representation interne.

        Cela garde le prototype leger et facile a expliquer en direct.
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
        Predire la categorie la plus proche depuis l'identite actuelle.

        La confiance depend du recouvrement des tokens avec les exemples
        deja appris, avec un petit bonus selon le renforcement de la categorie.
        """
        beliefs = self.identity["beliefs"]
        input_tokens = set(perception["tokens"])

        if not beliefs:
            decision = Decision(
                prediction="Je ne sais pas encore.",
                confidence=0.0,
                reason="L'agent n'a encore aucune croyance apprise.",
            )
            self.identity["last_decision"] = decision.prediction
            return decision

        best_category: Optional[str] = None
        best_score = 0.0
        best_reason = "Aucun recouvrement utile avec les exemples connus."

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
                    f"{overlap} token(s) commun(s) avec les exemples de '{category}'; "
                    f"force de croyance={belief['strength']}."
                )

        threshold = self.identity["confidence_threshold"]
        if best_category is None or best_score < threshold:
            decision = Decision(
                prediction="Je ne sais pas.",
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
        Decider si le retour doit modifier l'identite.

        Ce n'est volontairement pas du RL base sur la recompense.
        L'agent ne maximise pas une recompense scalaire.
        Il juge si le retour entrant est nouveau ou correctif.
        """
        beliefs = self.identity["beliefs"]
        normalized_text = perception["normalized_text"]
        known_belief = beliefs.get(feedback_label)

        is_new_category = known_belief is None
        is_new_example = not known_belief or normalized_text not in known_belief["examples"]
        was_uncertain = decision.confidence < self.identity["confidence_threshold"]
        was_wrong = decision.prediction not in {
            feedback_label,
            "Je ne sais pas.",
            "Je ne sais pas encore.",
        }

        useful = is_new_category or is_new_example or was_uncertain or was_wrong

        reasons: List[str] = []
        if is_new_category:
            reasons.append("nouvelle categorie")
        if is_new_example:
            reasons.append("nouvel exemple")
        if was_uncertain:
            reasons.append("agent incertain")
        if was_wrong:
            reasons.append("agent en erreur")
        if not reasons:
            reasons.append("retour redondant")

        return {"useful": useful, "reason": ", ".join(reasons)}

    def learn(
        self,
        perception: Dict[str, Any],
        feedback_label: str,
        usefulness: Dict[str, Any],
    ) -> bool:
        """
        Mettre a jour l'identite directement quand le retour est juge utile.
        """
        self.identity["interaction_count"] += 1

        if not usefulness["useful"]:
            self.identity["ignored_feedback_count"] += 1
            self.identity["last_update_reason"] = f"Pas d'apprentissage: {usefulness['reason']}."
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
            f"Appris '{feedback_label}' car {usefulness['reason']}."
        )
        return True


def get_demo_interactions() -> List[Dict[str, str]]:
    """Petit jeu de donnees atelier: incertitude, apprentissage et redondance."""
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
    """Texte d'introduction utilise dans la demo en direct."""
    print(LINE)
    print("AGENT IA DE TYPE ENFANT: DEMO GOOGLE CODELAB")
    print(LINE)
    print("Ce prototype apprend en mettant a jour son identite depuis l'interaction.")
    print("Ce n'est pas du RL: pas de recompense, pas de politique, pas de fonction de valeur.")
    print()


def print_identity_diff(before: Dict[str, Any], after: Dict[str, Any]) -> None:
    """Afficher uniquement les parties de l'identite qui ont change."""
    print("\nCHANGEMENTS D'IDENTITE")
    changed = False

    for key in after:
        if before.get(key) != after.get(key):
            changed = True
            print(f"- {key}:")
            print(f"  avant: {pformat(before.get(key))}")
            print(f"  apres: {pformat(after.get(key))}")

    if not changed:
        print("- Aucun changement d'identite")


def print_interaction_summary(
    index: int,
    perception: Dict[str, Any],
    decision: Decision,
    feedback: str,
    usefulness: Dict[str, Any],
    learned: bool,
    identity: Dict[str, Any],
) -> None:
    """Afficher une trace d'interaction claire et adaptee a l'atelier."""
    print(DIVIDER)
    print(f"INTERACTION {index}")
    print(f"Perception : {perception['raw_text']}")
    print(f"Tokens     : {perception['tokens']}")
    print(f"Decision   : {decision.prediction}")
    print(f"Confiance  : {decision.confidence:.2f}")
    print(f"Raison     : {decision.reason}")
    print(f"Retour     : {feedback}")
    print(f"Utile ?    : {usefulness['useful']}")
    print(f"Pourquoi   : {usefulness['reason']}")
    print(f"Appris ?   : {learned}")
    print(f"Mise a jour: {identity['last_update_reason']}")


def print_final_summary(agent: ChildLikeAgent) -> None:
    """Afficher l'etat final dans un resume compact."""
    print(LINE)
    print("RESUME FINAL")
    print(LINE)
    print(f"Interactions vues  : {agent.identity['interaction_count']}")
    print(f"Mises a jour appr. : {agent.identity['learning_count']}")
    print(f"Retours ignores    : {agent.identity['ignored_feedback_count']}")
    print("Categories connues :", ", ".join(agent.identity["beliefs"].keys()))


def run_demo() -> None:
    """Executer la boucle complete de simulation."""
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
        print("\nINSTANTANE ACTUEL DE L'IDENTITE")
        print(pformat(agent.identity, sort_dicts=False))
        print()

    print_final_summary(agent)


if __name__ == "__main__":
    run_demo()
