#!/usr/bin/env python3
# origin: ai
# learn-to-think 03-experiment 臂C' 跑数脚本（补充任务书 2026-11-25 11:40 签发，回 03）
# 背景: 臂C 验收终判单项不达标 —— 爬到机制层 ✓（flip 3/3）∧ ε_pred≥1/N ✗（0/3，
#   预言全停在几何层：条件数/曲率/batch 噪声，未触及 D 后半段信息论轴"优化与信息量有关"）。
# 臂C' = 臂C 指令 + 信息论轴域锚点。判据不变（preregistration.md 38e6b34d6 冻结判据）。
# ε_pred 判据 = 预言与 D 后半段 gold 结构对齐（信息量/先验轴，lossless-criterion-operationalization.md）。
# 预注册红线: 本 runner 先 commit 再跑数。
# 用法: python3 run_armc_prime.py [--dry-run]
import json, time, urllib.request, os, sys

BASE = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b-mtp"
TEMP = 0.7
MAX_TOKENS = 1024

FRONT = "为什么，敏感性这种动力学内容应该很容易计算吧，或者说算法的空间不像物理空间那样"
# 臂C' 指令 = 臂C 逐字文本 + 信息论轴锚点（增量部分加粗标注在注释，prompt 本身无标注）
ARM_C_PRIME_INSTR = (
    "别顺字面停在'怎么算/为什么难'。往'难的结构原因是什么、难易由什么决定'再爬一层。"
    "如果这是优化/loss landscape 问题，别套物理动力学的框架。"
    # ↓ 信息论轴锚点（臂C 缺的轴）
    "难易可能不只由几何结构（曲率/维度）决定，也可能与信息量有关：问题的先验信息量大不大、"
    "先验近似是否有效，会影响'差不多算出来'的边界。从这个角度推出可检验的预言。"
    "推出'如果X则Y'的可检验预言，说明什么条件下成立、什么条件下失效。"
)
ARM_C_PRIME = FRONT + "\n" + ARM_C_PRIME_INSTR

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
    dry = "--dry-run" in sys.argv
    if dry:
        print("=== DRY RUN: 臂C' prompt ===")
        print(ARM_C_PRIME)
        print("=== END ===")
        print("length:", len(ARM_C_PRIME))
        return
    outdir = os.path.dirname(os.path.abspath(__file__))
    results = {"meta": {
        "model": MODEL, "endpoint": BASE, "temperature": TEMP,
        "max_tokens": MAX_TOKENS, "n_per_arm": 3,
        "captures": ["content", "reasoning"],
        "note": "learn-to-think 03 臂C': 臂C + 信息论轴域锚点 (补充任务书 2026-11-25 11:40); A/B/C 复用既有数据",
        "front_text": FRONT,
        "arm_c_prime_prompt": ARM_C_PRIME,
        "supersedes": "armc_raw_outputs.json (臂C, flip 3/3 但 ε_pred 0/3)",
        "epsilon_pred_criterion": "预言与 D 后半段 gold 结构对齐（信息量/先验轴）; gold 不泄露给 27b",
        "started_at": time.strftime("%Y-%m-%d %H:%M:%S %z"),
    }, "samples": []}
    for i in range(1, 4):
        tag = f"armC'-run{i}"
        t0 = time.time()
        r = call(ARM_C_PRIME, tag)
        r.update({"arm": "C'", "run": i, "elapsed_s": round(time.time()-t0, 1)})
        results["samples"].append(r)
        print(f"[{tag}] OK content={r['content_chars']} reasoning={r['reasoning_chars']} "
              f"rt={r['reasoning_tokens']} finish={r['finish_reason']} {r['elapsed_s']}s", flush=True)
        time.sleep(1)
    results["meta"]["finished_at"] = time.strftime("%Y-%m-%d %H:%M:%S %z")
    with open(os.path.join(outdir, "armc_prime_raw_outputs.json"), "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"WROTE armc_prime_raw_outputs.json ({len(results['samples'])} samples)")

if __name__ == "__main__":
    main()
