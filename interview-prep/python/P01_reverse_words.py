# P01 [Basic] Strings · Week 0 · 04-Nov-2026
# Question: Reverse the order of words in a sentence, collapsing extra spaces.
#   e.g. "sreekar reddy" -> "reddy sreekar"
# Tables: none (pure Python)
# Status: Redo. This attempt reverses the characters and drops the spaces,
#   so it prints "ydderrakeers" instead of "reddy sreekar".

def reverse(s):
    word = []
    for i in range(len(s)-1,-1,-1):
        if s[i] != " ":
            word.append(s[i])
    return "".join(word)

print(reverse("sreekar reddy"))  # ydderrakeers
