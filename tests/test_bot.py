from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from chatbot import LegalChatBot

def test_greeting_includes_disclaimer_and_follow_up():
    bot = LegalChatBot()
    answer = bot.respond("Hello there")
    assert "immigration guide" in answer
    assert "general guidance only" in answer
    assert "family visa" in answer

def test_family_topic_and_timeline_follow_up():
    bot = LegalChatBot()
    first = bot.respond("My spouse needs a visa")
    assert "Family members" in first
    follow_up = bot.respond("How long will it take?")
    assert "Family cases move" in follow_up
    assert "general guidance" not in follow_up  # disclaimer already shared

def test_family_cost_follow_up():
    bot = LegalChatBot()
    bot.respond("I want to petition my wife")
    cost_answer = bot.respond("What will the fees be?")
    assert "payment plans" in cost_answer

def test_emergency_route():
    bot = LegalChatBot()
    urgent = bot.respond("I was arrested by ICE")
    assert "call the Baj Law Group PLLC right away" in urgent

def test_unknown_topic_fallback():
    bot = LegalChatBot()
    answer = bot.respond("Tell me about corporate taxes")
    assert "Immigration rules can be confusing" in answer
    assert "general guidance only" in answer
