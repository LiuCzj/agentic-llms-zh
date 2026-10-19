import re, pathlib, sys

KEEP = {
    "LLM", "LLMs", "API", "APIs", "PII", "KL", "GKD", "STaR", "SPIN", "CURE", "Matrix",
    "SYNTHLLM", "MetaSynth", "AReaL", "SEA", "TOUCAN", "APIGen", "MT", "WANLI",
    "EvalAssist", "MathGenie", "PersonaHub", "Self", "Instruct", "Natural", "Instructions",
    "Unnatural", "Super", "MATH", "LMentry", "ROUGE", "Dolores", "Maeve", "Bernard",
    "Smallville", "NEVER", "CAMEL", "ChatEval", "ChatDev", "MetaGPT", "AutoGen",
    "SOTOPIA", "MindStorms", "ReConcile", "Overcooked", "Hanabi", "MAgIC",
    "Zephyr", "Bartz", "Anthropic", "Kadrey", "Meta", "Leiden", "LaTeX",
    "Python", "JSON", "logits", "token", "token", "n", "gram", "logit",
    "v", "e", "g", "i", "al", "et", "eq", "fig", "chap", "sec",
    "BALROG", "GPT", "BERT", "CoT", "RL", "SFT", "DPO", "PPO", "MoE",
    "URL", "GPU", "CPU", "AI", "NLP", "SOTA", "ToM", "ToMBench", "ASL", "Agr",
    "AgentBench", "WebArena", "ALFWorld", "ScienceWorld", "Voyager", "Reflexion",
    "Tree", "Thoughts", "ReAct", "AssistGPT", "ToolLLM", "Gorilla", "NIKI",
    "SelfRAG", "RAG", "DPR", "BM25", "FAISS", "LangChain", "LlamaIndex",
}

for f in sys.argv[1:]:
    p = pathlib.Path("build/zh_parts") / f
    if not p.exists():
        print("missing", f)
        continue
    in_v = False
    for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if re.search(r"\\begin\{(minted|lstlisting|verbatim|comment)\}", line):
            in_v = True
            continue
        if re.search(r"\\end\{(minted|lstlisting|verbatim|comment)\}", line):
            in_v = False
            continue
        if in_v or line.strip().startswith("%"):
            continue
        if not re.search(r"[\u4e00-\u9fff]", line):
            continue
        # 去掉命令与数学
        s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^{}]*\})?", " ", line)
        s = re.sub(r"\$[^$]*\$", " ", s)
        s = re.sub(r"\\[a-zA-Z]+", " ", s)
        for w in re.findall(r"[A-Za-z][A-Za-z\-]{3,}", s):
            if w in KEEP:
                continue
            print(f"{f}:{i}  「{w}」  {line.strip()[:90]}")
