 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/chatbot/bot.py
index 0000000000000000000000000000000000000000..e4556b3ddf39edd20cf9ba4e89eaf9b0bfef10ec 100644
--- a//dev/null
+++ b/chatbot/bot.py
@@ -0,0 +1,353 @@
+"""Immigration-focused chatbot tailored for Baj Law Group PLLC."""
+
+from __future__ import annotations
+
+from dataclasses import dataclass, field
+import re
+from typing import List, Sequence
+
+
+@dataclass(frozen=True)
+class Topic:
+    """Represents a topic the chatbot can address."""
+
+    name: str
+    keywords: frozenset[str]
+    response: str
+    follow_up: str | None = None
+    timeline_note: str | None = None
+    cost_note: str | None = None
+
+    def score(self, tokens: set[str]) -> int:
+        return sum(1 for keyword in self.keywords if keyword in tokens)
+
+
+@dataclass
+class ConversationState:
+    """Tracks conversational context for more natural answers."""
+
+    disclaimer_given: bool = False
+    last_topic: str | None = None
+    last_topic_timeline: str | None = None
+    last_topic_cost: str | None = None
+    follow_up_shared: bool = False
+    history: List[str] = field(default_factory=list)
+
+
+class LegalChatBot:
+    """A rule-based assistant that speaks in plain language about immigration law."""
+
+    _GOODBYE_KEYWORDS = {"bye", "goodbye", "quit", "exit"}
+    _EMERGENCY_KEYWORDS = {"detained", "arrested", "custody", "raid", "deadline", "deadline"}
+    _TIMELINE_KEYWORDS = {"long", "time", "timeline", "wait", "processing", "slow", "status"}
+    _COST_KEYWORDS = {"cost", "fee", "fees", "price", "pay", "retainer", "afford"}
+
+    def __init__(self) -> None:
+        self._topics = self._build_topics()
+        self._state = ConversationState()
+        self._disclaimer = (
+            "This chat offers general guidance only and is not legal advice. For personal help, "
+            "contact the Baj Law Group PLLC at (206) 555-0123 or visit bajlawgroup.com/contact."
+        )
+        self._closing = (
+            "Thank you for speaking with the Baj Law Group PLLC. When you are ready, reach out "
+            "and we will create a plan together."
+        )
+
+    @staticmethod
+    def _normalize(text: str) -> List[str]:
+        cleaned = re.sub(r"[^a-z0-9\s]", " ", text.lower())
+        return [token for token in cleaned.split() if token]
+
+    @staticmethod
+    def _build_topics() -> Sequence[Topic]:
+        tagline = (
+            "We will learn your history, prepare the paperwork, and keep you updated at every "
+            "step."
+        )
+        return [
+            Topic(
+                name="greeting",
+                keywords=frozenset({"hello", "hi", "hey", "greetings", "hola"}),
+                response=(
+                    "Hello! I am the Baj Law Group PLLC immigration guide. Ask me any question "
+                    "about visas, green cards, or defending your status and I will explain the "
+                    "basics."
+                ),
+                follow_up=(
+                    "You can type topics like family visa, work visa, green card, asylum, or "
+                    "citizenship to get started."
+                ),
+            ),
+            Topic(
+                name="family_immigration",
+                keywords=frozenset(
+                    {
+                        "spouse",
+                        "marriage",
+                        "fiancé",
+                        "fiance",
+                        "family",
+                        "parent",
+                        "child",
+                        "petition",
+                        "i-130",
+                        "k1",
+                        "k-1",
+                        "relative",
+                    }
+                ),
+                response=(
+                    "Family members who are U.S. citizens or permanent residents can often sponsor "
+                    "loved ones. We collect proof of the relationship, help with forms like the "
+                    "I-130 or I-485, and get you ready for the interview. "
+                    + tagline
+                ),
+                timeline_note=(
+                    "Family cases move at different speeds depending on the visa category and "
+                    "the consulate. We review processing times and build a schedule so you know "
+                    "what to expect."
+                ),
+                cost_note=(
+                    "During a consult we break down government fees, legal fees, and payment "
+                    "plans so you can plan with confidence."
+                ),
+            ),
+            Topic(
+                name="employment_visa",
+                keywords=frozenset(
+                    {
+                        "work",
+                        "employment",
+                        "employer",
+                        "h1b",
+                        "h-1b",
+                        "l1",
+                        "l-1",
+                        "o1",
+                        "o-1",
+                        "tn",
+                        "sponsor",
+                        "job",
+                    }
+                ),
+                response=(
+                    "Work visas require a committed employer and strong planning. We coordinate "
+                    "with HR, file the prevailing wage steps, and prepare petitions that explain "
+                    "why you qualify. "
+                    + tagline
+                ),
+                timeline_note=(
+                    "Many work visas have strict filing windows. We map those dates so no "
+                    "deadlines are missed."
+                ),
+            ),
+            Topic(
+                name="green_card",
+                keywords=frozenset({"green", "permanent", "residence", "i-485", "adjustment", "residency"}),
+                response=(
+                    "Getting a green card usually happens in stages: petition, waiting for a visa "
+                    "number, and interview or consular processing. We organize evidence, prepare "
+                    "you for questions, and respond quickly to any requests. "
+                    + tagline
+                ),
+                timeline_note=(
+                    "Processing times change often. We check the visa bulletin and local office "
+                    "reports so you know the likely timing."
+                ),
+            ),
+            Topic(
+                name="citizenship",
+                keywords=frozenset({"citizenship", "naturalization", "n400", "n-400", "oath", "civics"}),
+                response=(
+                    "Most people can apply for naturalization after holding a green card for three "
+                    "to five years. We review travel history, help with the N-400, and practice "
+                    "for the civics test and interview. "
+                    + tagline
+                ),
+                timeline_note=(
+                    "Interview scheduling varies by local office. We request updates if things run "
+                    "long."
+                ),
+            ),
+            Topic(
+                name="asylum",
+                keywords=frozenset({"asylum", "fear", "persecution", "refugee", "credible"}),
+                response=(
+                    "If you fear harm in your home country, asylum may protect you. We gather "
+                    "evidence, explain the one-year filing rule, and prepare testimony so your "
+                    "story is clear and strong. "
+                    + tagline
+                ),
+            ),
+            Topic(
+                name="removal_defense",
+                keywords=frozenset({"deportation", "removal", "court", "ice", "detention", "nta"}),
+                response=(
+                    "When the government starts removal court, you still have rights. We review the "
+                    "Notice to Appear, identify defenses, and stand with you at every hearing. "
+                    + tagline
+                ),
+            ),
+            Topic(
+                name="daca",
+                keywords=frozenset({"daca", "dreamer", "renewal", "renew", "childhood"}),
+                response=(
+                    "DACA renewals must be filed early to avoid gaps. We double-check continuous "
+                    "presence, travel history, and all required fees so nothing is missed. "
+                    + tagline
+                ),
+                timeline_note=(
+                    "We track your renewal window and prepare reminders so protection stays in place."
+                ),
+            ),
+            Topic(
+                name="waiver",
+                keywords=frozenset({"waiver", "601", "601a", "212", "pardon", "hardship", "unlawful"}),
+                response=(
+                    "Hardship waivers ask the government to forgive immigration problems because of "
+                    "the severe impact on qualifying family. We collect medical, financial, and "
+                    "emotional evidence to tell that story clearly. "
+                    + tagline
+                ),
+            ),
+            Topic(
+                name="humanitarian",
+                keywords=frozenset({"u visa", "uva", "u-visa", "t visa", "t-visa", "violence", "crime", "vawa"}),
+                response=(
+                    "Survivors of crime or abuse may qualify for humanitarian visas like U, T, or "
+                    "VAWA. We work with you and law enforcement to document what happened and keep "
+                    "you safe during the process. "
+                    + tagline
+                ),
+            ),
+            Topic(
+                name="travel",
+                keywords=frozenset({"travel", "advance", "parole", "trip", "abroad", "vacation"}),
+                response=(
+                    "Travel while an immigration case is pending can be risky. We review your "
+                    "status, request advance parole when needed, and explain how to re-enter "
+                    "without issues. "
+                    + tagline
+                ),
+            ),
+            Topic(
+                name="consultation",
+                keywords=frozenset(
+                    {
+                        "appointment",
+                        "consult",
+                        "consultation",
+                        "call",
+                        "contact",
+                        "speak",
+                        "book",
+                        "schedule",
+                        "meeting",
+                        "phone",
+                    }
+                ),
+                response=(
+                    "We are ready to meet you virtually or in person. During the consultation we "
+                    "listen closely, spot any risks, and design a personalized plan."
+                ),
+                follow_up=(
+                    "You can call (206) 555-0123 or submit the secure form at bajlawgroup.com/contact."
+                ),
+            ),
+        ]
+
+    def reset(self) -> None:
+        """Reset the conversation state, useful for new sessions or tests."""
+        self._state = ConversationState()
+
+    def respond(self, message: str) -> str:
+        """Return a supportive answer for the provided client message."""
+
+        self._state.history.append(message)
+        if not message.strip():
+            return (
+                "Please share a bit more about your immigration question so I can point you in the "
+                "right direction."
+            )
+
+        tokens_list = self._normalize(message)
+        if not tokens_list:
+            return "I did not catch that. Could you rephrase your immigration question in plain words?"
+
+        tokens = set(tokens_list)
+
+        if tokens & self._GOODBYE_KEYWORDS:
+            return self._closing
+
+        if tokens & self._EMERGENCY_KEYWORDS:
+            return (
+                "This sounds urgent. Please call the Baj Law Group PLLC right away at (206) "
+                "555-0123 so an attorney can help immediately."
+            )
+
+        topic = self._match_topic(tokens)
+        if topic:
+            self._state.last_topic = topic.name
+            self._state.last_topic_timeline = topic.timeline_note
+            self._state.last_topic_cost = topic.cost_note
+            response = topic.response
+            if not self._state.disclaimer_given:
+                response = f"{response} {self._disclaimer}"
+                self._state.disclaimer_given = True
+            if topic.follow_up and not self._state.follow_up_shared:
+                response = f"{response} {topic.follow_up}"
+                self._state.follow_up_shared = True
+            return response
+
+        timeline_help = self._timeline_follow_up(tokens)
+        if timeline_help:
+            return timeline_help
+
+        cost_help = self._cost_follow_up(tokens)
+        if cost_help:
+            return cost_help
+
+        fallback = (
+            "Immigration rules can be confusing. Tell me a bit more about your situation or "
+            "schedule a consultation so we can review documents together."
+        )
+        if not self._state.disclaimer_given:
+            fallback = f"{fallback} {self._disclaimer}"
+            self._state.disclaimer_given = True
+        return fallback
+
+    def _match_topic(self, tokens: set[str]) -> Topic | None:
+        best_topic: Topic | None = None
+        best_score = 0
+        for topic in self._topics:
+            score = topic.score(tokens)
+            if score > best_score:
+                best_score = score
+                best_topic = topic
+        return best_topic if best_score > 0 else None
+
+    def _timeline_follow_up(self, tokens: set[str]) -> str | None:
+        if not (tokens & self._TIMELINE_KEYWORDS):
+            return None
+        if not self._state.last_topic_timeline:
+            return None
+        response = self._state.last_topic_timeline
+        if not self._state.disclaimer_given:
+            response = f"{response} {self._disclaimer}"
+            self._state.disclaimer_given = True
+        return response
+
+    def _cost_follow_up(self, tokens: set[str]) -> str | None:
+        if not (tokens & self._COST_KEYWORDS):
+            return None
+        if not self._state.last_topic_cost:
+            return None
+        response = self._state.last_topic_cost
+        if not self._state.disclaimer_given:
+            response = f"{response} {self._disclaimer}"
+            self._state.disclaimer_given = True
+        return response
+
+
+__all__ = ["LegalChatBot", "ConversationState", "Topic"]
 
EOF
)
