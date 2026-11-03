# P01 [Basic] Strings · Week 0 · 04-Nov-2026
# Question: Reverse the order of words in a sentence, collapsing extra spaces.
#   e.g. "sreekar reddy" -> "reddy sreekar"
# Tables: none (pure Python)
# Status: Solved with hint (2nd attempt).
# Note: split(" ") keeps empty strings for repeated spaces, so
#   "  sreekar   reddy " -> " reddy   sreekar  ". Plain split() would collapse them.

def word_reverse(s):
    l = s.split(" ")
    l = l[::-1]
    return " ".join(l)

print(word_reverse("sreekar reddy"))  # reddy sreekar
