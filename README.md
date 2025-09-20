 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/README.md
index 0000000000000000000000000000000000000000..8e43cce3293694b59996a2f1a8d94a6e446fed9b 100644
--- a//dev/null
+++ b/README.md
@@ -0,0 +1,42 @@
+# Baj Law Group PLLC Immigration Chatbot
+
+This repository contains a conversational assistant that explains common U.S. immigration
+processes in plain language for clients of the Baj Law Group PLLC. The chatbot relies on a
+curated knowledge base of frequently asked questions and keeps short-term memory so it can
+answer follow-up questions about timelines, costs, and consultations.
+
+## Features
+
+- Plain-language answers covering family, employment, humanitarian, and defense topics
+- Educational disclaimer and Baj Law Group PLLC contact information provided automatically
+- Conversation state keeps track of the last topic to handle timing or cost follow-ups
+- Emergency routing message when a user mentions detention, arrest, or other urgent issues
+- Command line interface for quick demos or internal training sessions
+- Unit tests covering greetings, topic matching, follow-up handling, and safety responses
+
+## Getting Started
+
+1. Ensure you have Python 3.10 or later installed.
+2. (Optional) Create and activate a virtual environment.
+3. Run the chatbot interactively:
+
+   ```bash
+   python cli.py
+   ```
+
+4. Type your immigration question. Enter `quit` to exit the session.
+
+## Running Tests
+
+The project uses `pytest` for automated checks. Install pytest and run the suite:
+
+```bash
+pip install pytest
+pytest
+```
+
+## Disclaimer
+
+The chatbot is for educational purposes only and does not create an attorney-client
+relationship. Always contact the Baj Law Group PLLC for advice tailored to your specific
+situation.
 
EOF
)
