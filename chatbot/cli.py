 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/cli.py
index 0000000000000000000000000000000000000000..ba24e38ae02e388a13b21eaf3fde1ace56288a67 100644
--- a//dev/null
+++ b/cli.py
@@ -0,0 +1,25 @@
+"""Simple command line interface for the Baj Law Group PLLC chatbot."""
+
+from chatbot import LegalChatBot
+
+
+def main() -> None:
+    bot = LegalChatBot()
+    print("Welcome to the Baj Law Group PLLC immigration helper. Type 'quit' to exit.\n")
+    while True:
+        try:
+            user_input = input("You: ")
+        except (KeyboardInterrupt, EOFError):
+            print("\nBot: " + bot.respond("quit"))
+            break
+
+        if user_input.strip().lower() in {"quit", "exit", "bye"}:
+            print("Bot: " + bot.respond(user_input))
+            break
+
+        response = bot.respond(user_input)
+        print(f"Bot: {response}\n")
+
+
+if __name__ == "__main__":
+    main()
 
EOF
)
