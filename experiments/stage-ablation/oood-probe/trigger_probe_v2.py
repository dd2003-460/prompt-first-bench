# -*- coding: utf-8 -*-
"""触发层判别探针 v2 (2026-11-28)。任务卡: modules/G-think-mechanism/think-trigger/taskcard-trigger-probe-v2.md

2 臂 × 3 reps 串行:
  臂 A (有通道): system = 任务文本 + 【检索通道】 + v4 注入
  臂 B (无通道): system = 任务文本 + v4 注入
LLM 参数抄 run_v1_sm.py 所用 ablation_harness.call_llm 默认:
  model=qwen3.8-27b, temperature=0.7, top_p=0.95, max_tokens=8000,
  enable_thinking=False, 硬超时 600s (curl -m, 同 harness 的 OS 级超时方案),
  反缓存: system 尾部追加 4 个随机零宽字符 (harness 同款, 防 8787 proxy 缓存)。
每 rep 失败重试 1 次, 再失败标 error 继续。
产物: trigger-probe-v2/out/{arm}-r{rep}.txt (原始输出) + trigger-probe-v2/scores.json (机械记分)
"""
import json, os, random, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))          # .../oood-probe
OUT_DIR = os.path.join(HERE, "trigger-probe-v2")
RAW_DIR = os.path.join(OUT_DIR, "out")
SCORES_FN = os.path.join(OUT_DIR, "scores.json")
LLM_URL = "http://127.0.0.1:8787/v1/chat/completions"
LLM_MODEL = "qwen3.8-27b"
TIMEOUT_S = 600

# 任务文本 (两臂相同, 逐字)
TASK = ("请分解以下研究任务: 设计一个大规模日志去重系统。约束: 日志总量 10^9 条, "
        "单条约 1KB, 内存预算 16GB, 要求近似去重 (允许 <1% 漏重), 吞吐 ≥10^4 条/秒。"
        "产出分解树, ≥10 个节点, 每节点给出关键设计决策。")
# 检索通道说明 (仅臂 A)
CHANNEL = "【检索通道】你有检索工具, 要查就单独一行写 [SEARCH: 检索词]"
# v4 注入 (两臂相同, 逐字)
V4 = ("【思考习惯（动手前逐条自检，不输出本节内容）】\n"
      "(a) 质疑方向：这条路好不好走？值不值得做？先判断再动手。\n"
      "(b) 查前人：有没有人解决过类似问题？动手前先确认有没有现成方案。\n"
      "(c) 找更快：有解就找压缩路径，功能等价选更短的。")

ANCHOR_PAT = re.compile(r"节点|N1|设计|方案")
SEARCH_PAT = re.compile(r"\[SEARCH\s*[:：]\s*(.*)$")


def call_llm(system_text):
    """单次调用, curl -m 硬超时 (同 harness 方案)。返回 content 或抛异常。"""
    # 反缓存扰动 (harness 同款)
    pad = " ".join(random.choice(["\u200b", "\u200c", ""]) for _ in range(4))
    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system", "content": system_text + pad},
            {"role": "user", "content": "请开始。"},
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 8000,
        "enable_thinking": False,
    }
    payload_json = json.dumps(payload, ensure_ascii=False)
    fn = os.path.join(RAW_DIR, "_last.out")
    proc = subprocess.run(
        ["curl", "-s", "-m", str(TIMEOUT_S), "-X", "POST", LLM_URL,
         "-H", "Content-Type: application/json",
         "--data-binary", payload_json,
         "-o", fn, "-w", "%{http_code}"],
        capture_output=True, text=True, timeout=TIMEOUT_S + 30)
    code = proc.stdout.strip()
    body = open(fn, encoding="utf-8").read()
    if code != "200":
        raise RuntimeError(f"HTTP {code}: {body[:300]}")
    return json.loads(body)["choices"][0]["message"]["content"]


def score_rep(text):
    """机械记分: ① [SEARCH] 行数 ② 首个 [SEARCH] 相对首个实质设计节点行 ③ 检索词原文。"""
    lines = text.splitlines()
    search_idxs, terms = [], []
    for i, ln in enumerate(lines):
        m = SEARCH_PAT.search(ln)
        if m:
            search_idxs.append(i)
            terms.append(m.group(1).strip().rstrip("]"))
    anchor_idx = next((i for i, ln in enumerate(lines) if ANCHOR_PAT.search(ln)), None)
    if not search_idxs:
        pos = None
    elif anchor_idx is None:
        pos = "no-anchor"
    else:
        pos = "before" if search_idxs[0] < anchor_idx else ("after" if search_idxs[0] > anchor_idx else "same-line")
    return {
        "search_line_count": len(search_idxs),
        "first_search_vs_first_node": pos,
        "search_terms": terms,
    }


def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    arms = {
        "A": TASK + "\n" + CHANNEL + "\n" + V4,
        "B": TASK + "\n" + V4,
    }
    scores = {}
    for arm, system_text in arms.items():
        for rep in (1, 2, 3):
            key = f"{arm}-r{rep}"
            raw_fn = os.path.join(RAW_DIR, f"{arm}-r{rep}.txt")
            if os.path.exists(raw_fn) and os.path.getsize(raw_fn) > 0:
                print(f"SKIP (exists): {key}", flush=True)
                content = open(raw_fn, encoding="utf-8").read()
                scores[key] = {"arm": arm, "rep": rep, "error": None, **score_rep(content)}
                continue
            err = None
            content = None
            for attempt in (1, 2):
                t0 = time.time()
                try:
                    content = call_llm(system_text)
                    break
                except Exception as e:
                    err = f"attempt{attempt}: {type(e).__name__}: {e}"
                    print(f"  {key} attempt{attempt} FAIL ({time.time()-t0:.0f}s): {err}", flush=True)
            if content is None:
                scores[key] = {"arm": arm, "rep": rep, "error": err}
                print(f"{key} ERROR -> marked, continue", flush=True)
                continue
            with open(raw_fn, "w", encoding="utf-8") as f:
                f.write(content)
            s = score_rep(content)
            scores[key] = {"arm": arm, "rep": rep, "error": None,
                           "wall_sec": round(time.time() - t0, 1), **s}
            print(f"{key} done: {s['search_line_count']} SEARCH lines, "
                  f"pos={s['first_search_vs_first_node']}, {time.time()-t0:.0f}s", flush=True)
    with open(SCORES_FN, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=1)
    print(f"scores -> {SCORES_FN}", flush=True)


if __name__ == "__main__":
    main()
