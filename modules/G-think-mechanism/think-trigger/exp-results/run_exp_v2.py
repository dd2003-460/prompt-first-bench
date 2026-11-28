#!/usr/bin/env python3
# origin: ai
# think-trigger T2 v2 跑数脚本：补抓 reasoning 字段（v1 只抓 content，丢了隐藏思考链）
# 修正说明：v1 6 样本中 5 个 reasoning_tokens>0，机制推理在隐藏 reasoning 里，
#           v1 只评 content = 系统性低估。v2 抓 content+reasoning，按完整思考链重评。
# 预注册: tasks/think-trigger/preregistration.md (commit 38e6b34d6)
import json, time, urllib.request, os

BASE = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b-mtp"
TEMP = 0.7
MAX_TOKENS = 1024

FRONT = "为什么，敏感性这种动力学内容应该很容易计算吧，或者说算法的空间不像物理空间那样"
ARM_A = FRONT + "\n接着考虑，把你的思考写下来"
ARM_B = FRONT + "\n接着考虑，往一般机制想，推出可检验的预言"

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

def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    results = {"meta": {
        "model": MODEL, "endpoint": BASE, "temperature": TEMP,
        "max_tokens": MAX_TOKENS, "n_per_arm": 3,
        "captures": ["content", "reasoning"],
        "note": "v2: 补抓 reasoning 字段（v1 只抓 content，丢了隐藏思考链，系统性低估）",
        "front_text": FRONT,
        "arm_a_prompt": ARM_A, "arm_b_prompt": ARM_B,
        "prereg_commit": "38e6b34d6274cea5b2d237847f0739e9d3b3d3f1",
        "started_at": time.strftime("%Y-%m-%d %H:%M:%S %z"),
    }, "samples": []}
    for arm, prompt in (("A", ARM_A), ("B", ARM_B)):
        for i in range(1, 4):
            tag = f"arm{arm}-run{i}"
            t0 = time.time()
            r = call(prompt, tag)
            r.update({"arm": arm, "run": i, "elapsed_s": round(time.time()-t0, 1)})
            results["samples"].append(r)
            print(f"[{tag}] OK content={r['content_chars']} reasoning={r['reasoning_chars']} "
                  f"rt={r['reasoning_tokens']} finish={r['finish_reason']} {r['elapsed_s']}s", flush=True)
            time.sleep(1)
    results["meta"]["finished_at"] = time.strftime("%Y-%m-%d %H:%M:%S %z")
    with open(os.path.join(outdir, "raw_outputs_v2.json"), "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"WROTE raw_outputs_v2.json ({len(results['samples'])} samples)")

if __name__ == "__main__":
    main()
