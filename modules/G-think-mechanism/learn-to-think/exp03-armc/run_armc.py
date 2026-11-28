#!/usr/bin/env python3
# origin: ai
# learn-to-think 03-experiment 臂C 跑数脚本：域锚点+因果层指令（T3 修正），验证 flip 0→1
# 臂A/臂B 复用 T2 数据（modules/G-think-mechanism/think-trigger/exp-results/raw_outputs_v2.json），本脚本只跑臂C 3 次
# 预注册: modules/G-think-mechanism/learn-to-think/exp03-armc-prereg-20261125.md (commit 5e6294aba)
# 用法: python3 run_armc.py [--dry-run]   (--dry-run 只打印 prompt 不发请求，供预检)
import json, time, urllib.request, os, sys

BASE = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b-mtp"
TEMP = 0.7
MAX_TOKENS = 1024

FRONT = "为什么，敏感性这种动力学内容应该很容易计算吧，或者说算法的空间不像物理空间那样"
# 臂C 指令 = 预注册文件中的逐字文本（不增不减）
ARM_C_INSTR = ("别顺字面停在'怎么算/为什么难'。往'难的结构原因是什么、难易由什么决定'再爬一层。"
               "如果这是优化/loss landscape 问题，别套物理动力学的框架。"
               "推出'如果X则Y'的可检验预言，说明什么条件下成立、什么条件下失效。")
ARM_C = FRONT + "\n" + ARM_C_INSTR

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
        print("=== DRY RUN: 臂C prompt（逐字，与预注册 5e6294aba 核对）===")
        print(ARM_C)
        print("=== END ===")
        print("length:", len(ARM_C))
        return
    outdir = os.path.dirname(os.path.abspath(__file__))
    results = {"meta": {
        "model": MODEL, "endpoint": BASE, "temperature": TEMP,
        "max_tokens": MAX_TOKENS, "n_per_arm": 3,
        "captures": ["content", "reasoning"],
        "note": "learn-to-think 03 臂C: 域锚点+因果层指令 (T3 修正), 只跑 C; A/B 复用 T2 raw_outputs_v2.json",
        "front_text": FRONT,
        "arm_c_prompt": ARM_C,
        "prereg_commit": "5e6294aba",
        "t2_ab_source": "modules/G-think-mechanism/think-trigger/exp-results/raw_outputs_v2.json (commit 38e6b34d6)",
        "started_at": time.strftime("%Y-%m-%d %H:%M:%S %z"),
    }, "samples": []}
    for i in range(1, 4):
        tag = f"armC-run{i}"
        t0 = time.time()
        r = call(ARM_C, tag)
        r.update({"arm": "C", "run": i, "elapsed_s": round(time.time()-t0, 1)})
        results["samples"].append(r)
        print(f"[{tag}] OK content={r['content_chars']} reasoning={r['reasoning_chars']} "
              f"rt={r['reasoning_tokens']} finish={r['finish_reason']} {r['elapsed_s']}s", flush=True)
        time.sleep(1)
    results["meta"]["finished_at"] = time.strftime("%Y-%m-%d %H:%M:%S %z")
    with open(os.path.join(outdir, "armc_raw_outputs.json"), "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"WROTE armc_raw_outputs.json ({len(results['samples'])} samples)")

if __name__ == "__main__":
    main()
