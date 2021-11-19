kws = ["buffer overflow",
       "segfault",
       "core bugfix",
       "abort",
       "memory leak",
       "kernel"
       "resource leak"
       "thread"
       "race"]

lines = AllFix.readlines()
for line in lines:
    if (any(kw in line for kw in kws)):
        SeriousFix.write(line + '\n')
