import re, pathlib, sys

CH = sys.argv[1]
PARTS = sys.argv[2:]
B = pathlib.Path("build/zh_parts")
o = pathlib.Path("src") / CH
o = o.read_text(encoding="utf-8").splitlines()
z = "".join(B.joinpath(p).read_text(encoding="utf-8") for p in PARTS).splitlines()


def k(lines, pat):
    r = []
    for l in lines:
        r += re.findall(pat, l)
    return r


pats = {
    "cite/citet/citep": r"\\(?:cite|citep|citet)\{([^}]*)\}",
    "label": r"\\label\{([^}]*)\}",
    "ref": r"\\ref\{([^}]*)\}",
    "includegraphics": r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}",
    "url": r"\\url\{([^}]*)\}",
    "href": r"\\href\{([^}]*)\}",
    "bibliography": r"\\bibliography\{([^}]*)\}",
    "bibliographystyle": r"\\bibliographystyle\{([^}]*)\}",
    "emph": r"\\emph\{([^}]*)\}",
    "textit": r"\\textit\{([^}]*)\}",
    "bracket-em": r"\{\\em ([^}]*)\}",
    "begin/end env": r"\\(?:begin|end)\{([^}]*)\}",
    "chapter": r"\\chapter(?:\[[^\]]*\])?\{([^}]*)\}",
    "section": r"\\section\*?\{([^}]*)\}",
    "subsection": r"\\subsection\*?\{([^}]*)\}",
    "paragraph": r"\\paragraph\{([^}]*)\}",
}

print(f"{'项目':<20}{'原文':>6}{'译文':>6}  一致?")
ok = True
for n, p in pats.items():
    a, b = k(o, p), k(z, p)
    same = a == b
    ok &= same
    print(f"{n:<20}{len(a):>6}{len(b):>6}  {'OK' if same else 'DIFF'}")
    if not same:
        sa, sb = set(a), set(b)
        if sa - sb:
            print("     仅原文:", sorted(sa - sb)[:6])
        if sb - sa:
            print("     仅译文:", sorted(sb - sa)[:6])


def eqs(lines):
    s = "\n".join(lines)
    out = []
    for m in re.finditer(r"\\begin\{(equation|align|align\*)\}(.*?)\\end\{\1\}", s, re.S):
        out.append(re.sub(r"\s+", " ", m.group(2)).strip())
    return out


oe, ze = eqs(o), eqs(z)
eqok = oe == ze
print(f"\n公式 {len(oe)}/{len(ze)} 逐字一致: {'OK' if eqok else 'DIFF'}")
if not eqok:
    for i, (x, y) in enumerate(zip(oe, ze)):
        if x != y:
            print(f"  [{i}]\n   原:{x}\n   译:{y}")

bad = 0
in_v = False
for i, l in enumerate(z, 1):
    if re.search(r"\\begin\{(minted|lstlisting|verbatim|comment)\}", l):
        in_v = True
        continue
    if re.search(r"\\end\{(minted|lstlisting|verbatim|comment)\}", l):
        in_v = False
        continue
    if in_v or l.strip().startswith("%"):
        continue
    body = l
    for esc in ("\\#", "\\&", "\\_", "\\%", "\\$"):
        body = body.replace(esc, "")
    body = re.sub(r"\$[^$]*\$", "", body)
    body = re.sub(r"\\verb\|[^|]*\|", "", body)
    if "#" in body:
        print(f"     ! 未转义# 第{i}行")
        bad += 1
print(f"未转义 # : {'OK' if bad == 0 else str(bad)}")
print("\n总体:", "结构完全一致" if ok and eqok and bad == 0 else "有差异")
