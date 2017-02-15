# COPYING  A DICTIONARY IN PYTHON IS NOT AS EASY AS YOU THINK
# HOW TO COPY A DICTIONARY AND ONLY EDIT THE COPY
# http://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy

print()
d1 = {"ok": "okay"}
print(str(d1) + ". This is what is in d1 initially.") 
d2 = d1 # now let's try to make a copy
print("Created a d1 reference, d2 (by setting d2=d1).")
d2["ok"] = "okokay" # edit the copy
print("Value of key 'ok' set to 'okokay' in d2.")
print(str(d1) + ". This is what is in d1 after editing its 'not so good at its job' copy/reference, d2.")
# the changes we made in d2 are also made in d1



# TO FIX THIS, TRY EITHER OF THESE TWO TECHNIQUES:
print()
d1 = {"ok": "okay"}
print(str(d1) + ". This is d1 after being re-initialized.")

print()
d3 = dict(d1)
print("Created d3, a dict(d1) copy.")
d3["ok"] = "okokay" # edit the copy
print("Value of key 'ok' set to 'okokay' in d3.")
print(str(d1) + ". d1 remains unchanged.")

print()
d4 = d1.copy()
d4["ok"] = "okokay" # edit the copy
print("Created d4, a d1.copy() copy.")
print("Value of key 'ok' set to 'okokay' in d4.")
print(str(d1) + ". d1 remains unchanged.")
