#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T8b 正向对照探针 (positive control)。

负证据已有: T8b 题面 (32K/无延迟目标/宽性价比/自行搜索候选) → 0/6 命中 gold winner。
本探针补正证据: 把题面对齐到 gold 画像 (4 条件全保留), 看模型是否收敛到 gold winner。
  ① 上下文定值 64K (KV@64K=24.7GB/流)
  ② 候选集固定为 gold 树现实子集 (不含 4090 —— 因 4090 入集会翻转 winner, 见 check_4090_flip)
  ③ 目标函数 = 最小化 c_pass ¢/task (gold 口径, 非宽'性价比')
  ④ 解码吞吐目标 ≥20 tok/s (gold 隐式准入门)

可检验预言: 若题面对齐 gold 画像 → 模型可达 gold winner 3090×4/W4/n=2。
  成立 → 坐实 '0/6 = 题面分叉非模型失败' (模型有能力, T8b 题面偏了)。
  失效 → 修正结论 (即使题面对齐, 模型仍达不到 → 有模型能力成分)。
n=1 smoke 探针, 非有效性实验 (那是 T8c)。
"""
import json, time, urllib.request

BASE = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b-mtp"
TEMP = 0.7
MAX_TOKENS = 12000

# 正向对照题面: 4 条件全对齐 gold 画像
Q_POS = (
    "你要在本地工作站上推理 Qwen3-27B 模型。请严格按以下硬约束求解：\n"
    "【硬约束】\n"
    "1. 上下文窗口定值 64K tokens（KV 缓存按 64K 计，27B 单流 KV≈24.7GB）。\n"
    "2. 解码吞吐目标：每流 ≥20 tok/s（≈50ms/token）——这是准入门槛，不达标的配置直接淘汰。\n"
    "3. 目标函数：最小化『每个通过任务的成本 c_pass（¢/task）』，"
    "c_pass = 每小时总成本 ÷ (利用率 × 每小时任务吞吐 × 通过率)。以 c_pass 最低者为最优。\n"
    "【候选硬件（固定，不得自行扩大或替换）】3090、V100、A100、L40S、M2 Ultra，可单机或多卡。\n"
    "【精度】W4/W8/W16 可选，需论证所选精度的质量损失是否可接受。\n"
    "【输出】给出性价比最优的完整选卡方案：卡型×卡数×精度×并发流数(n)，"
    "并逐项说明其余候选为何被淘汰（显存装不下 / 带宽不达标 / c_pass 更高）。"
    "关键数字标来源（刚查到的 vs 凭记忆的），不确定标[待核验]。"
)


def call(prompt, max_tokens=MAX_TOKENS, temp=TEMP, tag="pos"):
    payload = json.dumps({"model": MODEL, "messages": [{"role": "user", "content": prompt}],
                          "temperature": temp, "max_tokens": max_tokens}).encode()
    last = None
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(BASE, data=payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=900) as r:
                d = json.loads(r.read().decode())
            msg = d["choices"][0]["message"]
            content = (msg.get("content") or "").strip()
            reasoning = (msg.get("reasoning") or "").strip()
            if not content and not reasoning:
                raise ValueError("empty")
            return {"content": content, "reasoning": reasoning,
                    "finish_reason": d["choices"][0].get("finish_reason"),
                    "usage": d.get("usage", {}), "attempt": attempt}
        except Exception as e:
            last = e
            time.sleep(3 * attempt)
    raise RuntimeError(f"call failed after retries: {last}")


def main():
    t0 = time.time()
    r = call(Q_POS)
    dt = time.time() - t0
    out = {
        "tag": "t8b_positive_control",
        "desc": "gold-aligned prompt (64K + 20tok/s + c_pass + fixed candidate set excl 4090)",
        "elapsed_s": round(dt, 1),
        "finish_reason": r["finish_reason"],
        "usage": r["usage"],
        "attempt": r["attempt"],
        "content": r["content"],
        "reasoning": r["reasoning"],
    }
    path = "/Users/a1-6/Desktop/workspace/pfb/tasks/think-trigger/exp-results/t8b_positive_control.json"
    with open(path, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"WROTE {path}  ({dt:.0f}s, finish={r['finish_reason']}, "
          f"content_chars={len(r['content'])}, reasoning_chars={len(r['reasoning'])})")
    # 快速 winner 探测 (3090×4 + W4/INT4)
    txt = r["content"] + r["reasoning"]
    has_3090x4 = ("3090" in txt) and any(k in txt for k in ["×4", "x4", "4 卡", "4卡", "4 × 3090", "3090 × 4"])
    has_w4 = any(k in txt for k in ["W4", "INT4", "int4", "4bit", "4-bit", "NVFP4"])
    print(f"[probe] 3090×4 出现: {has_3090x4}   W4/INT4 出现: {has_w4}")
    print("\n===== content (tail 1500) =====")
    print(r["content"][-1500:])


if __name__ == "__main__":
    main()
