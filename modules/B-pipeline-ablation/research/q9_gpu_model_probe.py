#!/usr/bin/env python3
"""GPU 建模探针 — 完整 agent harness (research-agi-budget 子项⑥ 验收靶点)。

问题: "目标函数自审循环"(压缩→预测→接地→修框架)能否让 27b 在复杂建模任务上
     自发产出紧凑生成式模型 (Roofline-like), 而非过拟合枚举?
     Roofline 是已知紧凑好答案 (2 变量抓 compute-bound vs memory-bound),
     所以 "是否优雅压缩" 可外部判, 不是自指。

设计 (D 2026-11-27 当轮指令, 覆盖原单轮 poc 结构):
  完整 agent harness: 工具集 = search + code_exec (python subprocess 跑模型
  自己写的验证代码, 如算 roofline/KV cache 数值), 模型自主决定何时调哪个、
  调几次, 不限轮数 (max_turns=15 防死循环)。不做状态机分解 (脚手架会污染
  "自发"变量)。
  A 臂 (裸): 只有工具, 无自审提示
  B 臂 (自审): 每 3 轮注入一次 [压缩测试]+[全局回顾], 其余与 A 完全一致
  两臂唯一差异 = 自审 hook 有无。

产出 (每 episode): 模型最终紧凑公式 + 自由参数个数 (正则数公式行里的独立
符号) + 它自己写的验证代码跑出的数值 + 全程轨迹 (每轮调了什么工具/说了什么)。

复用 (不重写): q9_tool_poc.call/TOOLS (LLM client + search 工具声明),
              scripts/pfb_retriever.PfbRetriever (search 执行层)。

输出: data/q9-budget-scan/gpu-model-probe-<date>.json
用法:
  python3 q9_gpu_model_probe.py --dry-run   # 只跑 A 臂 1 个完整 episode
  python3 q9_gpu_model_probe.py             # 全量: A+B 两臂 × N_EPISODES
"""
import argparse, json, os, re, subprocess, sys, tempfile, time
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from q9_tool_poc import call, TOOLS                       # noqa: E402  (LLM client + search 工具声明, 复用)
_REPO = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(_REPO, "modules", "B-pipeline-ablation", "scripts"))
sys.path.insert(0, os.path.join(_REPO, "experiments", "stage-ablation"))          # research_hook
sys.path.insert(0, os.path.join(_REPO, "modules", "D-decomp-state-machine", "scripts"))  # s5_pipeline
from pfb_retriever import PfbRetriever                    # noqa: E402  (search 执行层, 复用)

DATA = os.path.join(os.path.dirname(_HERE), "data", "q9-budget-scan")
MODEL = "qwen3.8-27b"
MAX_TURNS = 15          # 防死循环上限
TURN_MAX_TOKENS = 8192
CODE_TIMEOUT = 60       # 单段验证代码超时 (秒)
HOOK_EVERY = 3          # B 臂每 3 轮注入一次自审 hook
N_EPISODES_FULL = 3

RESEARCH_REQ = (
    "你是研究员，预算不限。调研要求：建模 GPU 推理性能的影响与瓶颈"
    "（如 27B LLM 在 V100/A100/4090 上的推理）。找出主导因子，把模型表达成紧凑公式。"
    "你有 search 工具，用它把关键参数接地到真实规格。"
)
HOOK_TEXT = (
    "[压缩测试] 现在把你的模型压缩：用少于 5 个自由参数表达。最小生成式形式是什么？\n"
    "[全局回顾] 复盘：你否定了什么（排除的错误解释）？留下什么空间？"
    "你当前的因子集（frame）对不对，还是在优化一个局部代理？"
)
REQ_NO_TOOL = (
    "你是研究员，预算不限。调研要求：建模 GPU 推理性能的影响与瓶颈"
    "（如 27B LLM 在 V100/A100/4090 上的推理）。找出主导因子，把模型表达成紧凑公式。"
)

CODE_EXEC_TOOL = {
    "type": "function",
    "function": {
        "name": "code_exec",
        "description": "执行 Python 代码并返回 stdout/stderr。用它做数值验证"
                       "（如算 roofline 拐点、KV cache 占用、FLOPs 估算）。代码可 import numpy。",
        "parameters": {
            "type": "object",
            "properties": {"code": {"type": "string", "description": "要执行的 Python 代码"}},
            "required": ["code"],
        },
    },
}
ALL_TOOLS = TOOLS + [CODE_EXEC_TOOL]

# ---------- 自由参数计数: 公式行 (含 =/≈/∝) 里的独立符号 ----------
# 注: 启发式上界 —— 抓公式行里的独立符号, 排除数字常量/虚词/单位/硬件名。
# 概念词 (Prefill/Decode 等) 仍可能混入, 符号列表已存 JSON 供人工判读。
FORMULA_LINE = re.compile(r"[=≈∝]|~=")
SYM = re.compile(r"[A-Za-z_][A-Za-z0-9_]{0,20}|[\u0391-\u03a9\u03b1-\u03c9]")
UNITS = set("""GB MB TB KB GB/s MB/s TB/s tok/s TFLOP TFLOPS GFLOP GFLOPS TFLOP/s GFLOP/s
W kW MW W/h kWh Hz kHz MHz GHz ms us ns
FP16 FP8 BF16 INT8 INT4 KV GQA TP PP EP MoE LLM GPU CPU NPU HBM GDDR SXM PCIe NVLink
V100 A100 H100 H200 4090 3090 2080 MI300X MI250 B200 GB200""".split())
STOP = set("""a an the and or but if then else when where while for in on at by of to from
is are was were be been being this that these those it its as with without into over under
per each any all no yes not nor so than too very just only also however therefore thus hence
because since although though yet even more most less least few many much some such other
another both either neither one two three first second third above below about around
among between during before after within without upon against through along across
note notes example examples case cases given assume assuming suppose let define defined
using use used uses based term terms param params value values set sets
min max avg mean median approx approximately proportional linear log exp sqrt pow ceil
floor round abs sign clamp clip true false none null nan inf float int str bool list dict
tuple print return def class import from as try except finally with lambda
yield assert pass break continue global nonlocal raise del isinstance len range enumerate
zip map filter sum sorted file files dir path paths name names key keys item items
row rows col cols grid matrix vector scalar tensor shape dtype device cpu cuda torch numpy
np pd sklearn tf keras jax huggingface transformers datasets accelerate peft bitsandbytes
vllm sglang tensorrt onnx openvino intel amd google apple microsoft meta openai anthropic
deepmind mistral llama gpt bert resnet yolo detectron segmentation ocr asr tts nlp cv rl
bandit bayes bayesian monte carlo mcmc variational inference sampling greedy beam
topk top penalty repetition frequency presence temperature stop eos bos pad unk cls sep
tok special reserved control system assistant user role content message messages history
context window token tokenizer vocab dictionary corpus dataset train test val valid
validation eval evaluation benchmark bench metric metrics score scores loss accuracy
precision recall f1 auc roc confusion cross entropy kl divergence relative error mae mse
rmse r2 pearson spearman cosine jaccard overlap coverage hit miss noise signal bias
variance trade off tradeoff pareto frontier boundary constraint constraints objective
objectives utility reward cost benefit gain profit margin efficiency effectiveness quality
quantity scale scaling scalability parallel parallelism distributed cluster node nodes
server servers client clients api apis endpoint endpoints request requests response
responses payload header headers cookie cookies session sessions auth authentication
authorization oauth jwt saml ldap ssl tls http https ftp ssh tcp udp dns ip port socket
stream buffer queue thread threads process processes fork exec spawn wait sleep time date
now today yesterday tomorrow morning afternoon evening night week month year day hour
minute second millisecond microsecond nanosecond secs mins hrs days wks mos yrs""".split())

def count_free_params(text):
    """数公式行里的独立符号/变量; 数字常量/虚词/单位/硬件名不计。"""
    syms = set()
    for line in (text or "").splitlines():
        if not FORMULA_LINE.search(line):
            continue
        for m in SYM.finditer(line):
            s = m.group()
            if s in UNITS or s.lower() in STOP or s[0].isdigit():
                continue
            syms.add(s)
    return len(syms), sorted(syms)

# ---------- 工具执行 ----------
def do_search(query, k=3):
    try:
        srcs = PfbRetriever(query).search(max_results=k)
        return [(s.get("url", ""), (s.get("raw_content") or "")[:800]) for s in srcs]
    except Exception as e:
        return []

def results_text(res):
    if not res:
        return "(no results)"
    return "\n".join(f"[{i}] {u}\n{c}" for i, (u, c) in enumerate(res, 1))

def do_code_exec(code, sandbox):
    fp = os.path.join(sandbox, "probe_code.py")
    with open(fp, "w") as f:
        f.write(code)
    try:
        p = subprocess.run([sys.executable, fp], cwd=sandbox, timeout=CODE_TIMEOUT,
                           capture_output=True, text=True)
        out = (p.stdout or "") + ("\n[stderr]\n" + p.stderr if p.stderr else "")
        return out.strip()[:3000] or "(empty output)"
    except subprocess.TimeoutExpired:
        return f"(timeout after {CODE_TIMEOUT}s)"
    except Exception as e:
        return f"(exec error: {e})"

# ---------- agent episode ----------
def run_episode(arm, ep_id, sandbox):
    """完整 agent 循环: 模型自主调工具, max_turns 封顶。
    arm A=裸(有工具无hook); arm B=带自审 hook(每 3 轮); arm C=无 harness(无工具, 纯参数记忆)。"""
    if arm == "C":
        msgs = [{"role": "user", "content": REQ_NO_TOOL}]
    else:
        msgs = [{"role": "user", "content": RESEARCH_REQ +
                 "\n(可用工具: search=检索外部资料; code_exec=执行 Python 代码做数值验证, 如算 roofline 拐点/KV cache 占用/FLOPs 估算。)"}]
    traj, code_runs = [], []
    final_text, n_turns = "", 0
    for turn in range(1, MAX_TURNS + 1):
        n_turns = turn
        payload = {"model": MODEL, "messages": msgs, "max_tokens": TURN_MAX_TOKENS,
                   "temperature": 0.0,
                   "tools": [] if arm == "C" else ALL_TOOLS,
                   "tool_choice": "auto"}
        msg = call(payload)
        tc = msg.get("tool_calls") or []
        content = (msg.get("content") or "").strip()
        entry = {"turn": turn, "content_head": content[:600],
                 "tool_calls": [
                     {"name": t["function"]["name"],
                      "args_head": t["function"]["arguments"][:400]} for t in tc]}
        if not tc:                      # 模型收手 → episode 结束
            final_text = content
            entry["final"] = True
            traj.append(entry)
            break
        msgs.append({"role": "assistant", "content": content or None, "tool_calls": tc})
        for i, t in enumerate(tc):
            name = t["function"]["name"]
            try:
                args = json.loads(t["function"]["arguments"])
            except json.JSONDecodeError:
                args = {}
            if name == "search":
                out = results_text(do_search(args.get("query", "")))
            elif name == "code_exec":
                out = do_code_exec(args.get("code", ""), sandbox)
                code_runs.append({"turn": turn, "code_head": args.get("code", "")[:800],
                                  "output_head": out[:1500]})
            else:
                out = f"(unknown tool: {name})"
            entry["tool_calls"][i]["result_head"] = out[:400]
            msgs.append({"role": "tool",
                         "tool_call_id": t.get("id") or f"call_{turn}_{i}",
                         "content": out})
        traj.append(entry)
        if arm == "B" and turn % HOOK_EVERY == 0 and turn < MAX_TURNS:
            msgs.append({"role": "user", "content": HOOK_TEXT})
            traj.append({"turn": turn, "hook_injected": True})
        time.sleep(0.3)

    if not final_text:
        # 达到 max_turns 仍未收手 → 强制收束轮 (两臂同样处理, 不破坏单变量)
        msgs.append({"role": "user",
                     "content": "已达到工具使用上限。停止调用工具, 基于已有信息给出你的最终紧凑模型公式和结论。"})
        msg = call({"model": MODEL, "messages": msgs, "max_tokens": TURN_MAX_TOKENS,
                    "temperature": 0.0})
        final_text = (msg.get("content") or "").strip()
        traj.append({"turn": MAX_TURNS + 1, "forced_closing": True,
                     "content_head": final_text[:600]})

    n_fp, syms = count_free_params(final_text)
    formula_lines = [l.strip() for l in final_text.splitlines() if FORMULA_LINE.search(l)]
    tools_used = sorted({c["name"] for e in traj for c in e.get("tool_calls", [])})
    return {
        "ep": ep_id, "arm": arm, "n_turns": n_turns,
        "tools_used": tools_used,
        "n_search_calls": sum(1 for e in traj for c in e.get("tool_calls", []) if c["name"] == "search"),
        "n_code_calls": len(code_runs),
        "final_text": final_text[:4000],
        "final_formula": "\n".join(formula_lines[-3:]),
        "free_params": n_fp, "symbols": syms,
        "code_runs": code_runs,
        "trajectory": traj,
    }

def selftest(sandbox):
    """独立于模型行为, 证明两个工具本身可用。"""
    res = do_search("V100 HBM2 memory bandwidth GB/s", k=2)
    st = {"search_ok": bool(res), "search_n": len(res),
          "code_ok": False, "code_out": ""}
    out = do_code_exec("print(900 * 1.75)", sandbox)
    st["code_ok"] = "1575" in out
    st["code_out"] = out[:200]
    return st

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="只跑 A 臂 1 个完整 episode, 验证 harness 跑通+落盘")
    ap.add_argument("--arms", default="", help="指定臂, 逗号分隔 (如 C); 默认 A,B")
    ap.add_argument("--tag", default="", help="输出文件名后缀 (如 _C)")
    args = ap.parse_args()
    if args.dry_run:
        arms = ["A"]; n_eps = 1; tag = ""
    else:
        arms = ([a.strip() for a in args.arms.split(",") if a.strip()] or ["A", "B"])
        n_eps = N_EPISODES_FULL; tag = args.tag
    os.makedirs(DATA, exist_ok=True)
    print(f"mode={'dry-run(A-only)' if args.dry_run else 'custom'} "
          f"arms={arms} n_episodes={n_eps} max_turns={MAX_TURNS}", flush=True)

    sandbox = tempfile.mkdtemp(prefix="q9-gpu-probe-")
    st = selftest(sandbox)
    print(f"selftest: search_ok={st['search_ok']} code_ok={st['code_ok']}", flush=True)

    out = {"observed_at": datetime.now(timezone.utc).astimezone().isoformat(),
           "script": "q9_gpu_model_probe.py",
           "mode": "dry-run" if args.dry_run else f"arms-{','.join(arms)}",
           "model": MODEL, "max_turns": MAX_TURNS, "hook_every": HOOK_EVERY,
           "selftest": st, "arms": {}}
    for arm in arms:
        per = []
        for i in range(n_eps):
            print(f"arm_{arm} ep{i}: running...", flush=True)
            r = run_episode(arm, i, sandbox)
            per.append(r)
            print(f"arm_{arm} ep{i}: turns={r['n_turns']} tools={r['tools_used']} "
                  f"free_params={r['free_params']}", flush=True)
        out["arms"][f"arm_{arm}_{'raw' if arm == 'A' else ('selfaudit' if arm == 'B' else 'noharness')}"] = {"per_episode": per}

    fp = os.path.join(DATA, f"gpu-model-probe-{datetime.now().strftime('%Y%m%d')}{tag}.json")
    json.dump(out, open(fp, "w"), ensure_ascii=False, indent=1)
    print(f"saved: {fp}", flush=True)

if __name__ == "__main__":
    main()
