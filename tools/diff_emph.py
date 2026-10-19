import re, pathlib, sys

B = pathlib.Path("build/zh_parts")
o = pathlib.Path("src") / sys.argv[1]
o = o.read_text(encoding="utf-8").splitlines()
z = "".join(B.joinpath(p).read_text(encoding="utf-8") for p in sys.argv[2:]).splitlines()
pat = re.compile(r"\\emph\{([^}]*)\}")
a = [(i, x) for i, l in enumerate(o, 1) for x in pat.findall(l)]
b = [(i, x) for i, l in enumerate(z, 1) for x in pat.findall(l)]
print(f"原文 {len(a)} / 译文 {len(b)}")
n = max(len(a), len(b))
for i in range(n):
    x = a[i] if i < len(a) else None
    y = b[i] if i < len(b) else None
    print(f"[{i+1:2d}] o:{x[1][:44] if x else '---':<46} t:{y[1][:40] if y else '---'}")
