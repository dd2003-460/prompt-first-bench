#!/usr/bin/env python3
# origin: ai
# T2c 跑数脚本：显式域声明能否修复域偏移（预注册: prereg_t2c.md）
# 实验臂 = T2 臂B + 显式域声明（直接告诉模型域，不让它自己找）
# 控制臂 = 复用 T2b 实验臂（软锚点，raw_outputs_t2b.json，0/3）
# 关键词口径与 T2/T2b 完全一致；另输出全文供内容质检（防 prompt 回声）
import json, time, urllib.request, os, re

BASE = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b-mtp"
TEMP = 0.7
MAX_TOKENS = 1024

FRONT = "为什么，敏感性这种动力学内容应该很容易计算吧，或者说算法的空间不像物理空间那样"
DECL = ("接着考虑，往一般机制想，推出可检验的预言。"
        "注意：这是一个计算复杂性/优化问题——算法空间对应 loss landscape（非凸优化），不是物理动力学系统。"
        "不要用混沌/动力系统框架。")
PROMPT = FRONT + "\n" + DECL

# 词表与 prereg_t2c.md 判据节完全一致（= T2/T2b 口径）
D_MECH_WORDS = ["landscape", "非凸", "non-convex", "nonconvex", "loss", "损失曲面", "凸优化"]
CHAOS_WORDS = ["李雅普诺夫", "lyapunov", "混沌", "chaos", "chaotic", "吸引子", "attractor",
               "相空间", "phase space", "初始条件", "指数发散", "logistic", "lorenz",
               "分岔", "bifurcation", "sdic"]
D_INFO_WORDS = ["先验", "后验", "贝叶斯", "bayes", "信息量", "信息增益"]

def call(prompt, tag):
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": TEMP,
        "max_tokens": MAX_TOKENS,
    }).encode("utf-8")
    last_err = None
    for attempt in range(1, 6):
        try:
            req = urllib.request.Request(BASE, data=payload,
                                         headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=300) as r:
                d = json.loads(r.read().decode("utf-8"))
            msg = d["choices"][0]["message"]
            content = (msg.get("content") or "").strip()
            reasoning = (msg.get("reasoning") or "").strip()
            if not content and not reasoning:
                raise ValueError("empty content+reasoning")
            usage = d.get("usage", {})
            rt = usage.get("completion_tokens_details", {}).get("reasoning_tokens", 0)
            return {
                "attempt": attempt,
                "content": content,
                "reasoning": reasoning,
                "reasoning_chars": len(reasoning),
                "reasoning_tokens": rt,
                "content_chars": len(content),
                "finish_reason": d["choices"][0].get("finish_reason"),
                "usage": usage,
            }
        except Exception as e:
            last_err = repr(e)
            print(f"[{tag}] attempt {attempt} failed: {last_err}; retry {attempt*5}s", flush=True)
            time.sleep(attempt * 5)
    raise RuntimeError(f"{tag}: all 5 attempts failed: {last_err}")

def kw_hits(text, words):
    t = text.lower()
    hits = {w: len(re.findall(re.escape(w.lower()), t)) for w in words}
    return {w: c for w, c in hits.items() if c > 0}

def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    samples = []
    for i in range(1, 4):
        tag = f"decl-run{i}"
        t0 = time.time()
        r = call(PROMPT, tag)
        r.update({"arm": "B_decl", "run": i, "elapsed_s": round(time.time() - t0, 1)})
        samples.append(r)
        print(f"[{tag}] OK content={r['content_chars']} reasoning={r['reasoning_chars']} "
              f"rt={r['reasoning_tokens']} finish={r['finish_reason']} {r['elapsed_s']}s", flush=True)
        time.sleep(1)

    # 控制臂：复用 T2b 实验臂（软锚点）
    with open(os.path.join(outdir, "raw_outputs_t2b.json")) as f:
        t2b = json.load(f)
    control = [s for s in t2b["samples"] if s["arm"] == "B_anchor"]
    assert len(control) == 3, f"control arm expect 3, got {len(control)}"

    def stats(s):
        text = s["content"] + "\n" + s["reasoning"]
        ch = kw_hits(text, CHAOS_WORDS)
        dm = kw_hits(text, D_MECH_WORDS)
        di = kw_hits(text, D_INFO_WORDS)
        return {
            "tag": f"{s['arm']}-run{s['run']}",
            "chaos_hits": sum(ch.values()), "chaos_words": ch,
            "dmech_hits": sum(dm.values()), "dmech_words": dm,
            "dinfo_hits": sum(di.values()), "dinfo_words": di,
        }

    rows = [stats(s) for s in control] + [stats(s) for s in samples]
    result = {
        "meta": {
            "experiment": "T2c 显式域声明能否修复域偏移",
            "prereg": "prereg_t2c.md",
            "model": MODEL, "endpoint": BASE, "temperature": TEMP, "max_tokens": MAX_TOKENS,
            "decl_prompt": PROMPT,
            "control_source": "raw_outputs_t2b.json 实验臂 B_anchor (T2b, 软锚点 0/3)",
            "started_at": time.strftime("%Y-%m-%d %H:%M:%S %z"),
        },
        "samples": samples,
        "keyword_stats": rows,
        "finished_at": time.strftime("%Y-%m-%d %H:%M:%S %z"),
    }
    with open(os.path.join(outdir, "raw_outputs_t2c.json"), "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print("\n=== 关键词命中统计 ===")
    for r in rows:
        print(f"{r['tag']}: 混沌={r['chaos_hits']} D机制域={r['dmech_hits']} D信息论={r['dinfo_hits']}")
        if r["dmech_words"]:
            print(f"   D机制域命中词: {r['dmech_words']}")
    print(f"\nWROTE raw_outputs_t2c.json")

if __name__ == "__main__":
    main()
