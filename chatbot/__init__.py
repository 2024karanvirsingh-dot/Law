 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/chatbot/__init__.py
index 0000000000000000000000000000000000000000..3f4bc1d25df6811cac504f8ef459eebb8c73aa86 100644
--- a//dev/null
+++ b/chatbot/__init__.py
@@ -0,0 +1,5 @@
+"""Immigration-focused legal chatbot package for Baj Law Group PLLC."""
+
+from .bot import ConversationState, LegalChatBot, Topic
+
+__all__ = ["LegalChatBot", "ConversationState", "Topic"]
 
EOF
)
