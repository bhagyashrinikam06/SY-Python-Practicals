import re

words = ["stupid", "hate", "fool"]

text = "You are stupid and this service is full of hate."
result = re.sub(r"\b(" + "|".join(words) + r")\b", "****", text, flags=re.I)

print(result)
