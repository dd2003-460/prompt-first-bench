#!/usr/bin/env python3
# origin: ai
# T8b 跑数脚本：pfb 六阶段 vs 直接求解（GPU 选卡题，预注册 prereg_t8b.md）
# 相对 T8a 的改动：A max_tokens 4096->16384；B 每阶段 1536->4096；新增成本追踪(总 completion tokens)
# 目的：消除 T8a 的截断 confound（6 份全撞 token 上限），让两臂都能自然收尾
import json, time, urllib.request, os, re, sys

BASE = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b-mtp"
TEMP = 0.7
MAX_A = 16384   # Arm A 单次
MAX_B = 4096    # Arm B 每阶段

Q = ("你要在本地工作站上推理 Qwen3-27B 模型，不设硬性延迟指标（延迟是性能变量，由硬件和部署配置决定，不作为前置约束）；"
     "上下文窗口 ≥ 32K tokens 作为容量下限保留。权重精度不限（BF16/FP8/INT8/NVFP4/W4 均可），但必须论证所选精度的质量损失是否可接受。"
     "候选硬件：自行搜索确定值得考虑的完整候选集——覆盖你认为所有可能影响性价比排序的架构、代际、容量档位和价格区间"
     "（包括消费级、数据中心级、以及任何你认为值得纳入比较的非典型方案）。同时评估单卡与多卡方案的 TCO 差异（如 2× 消费卡 vs 1× 数据卡）。"
     "给出性价比最优的完整选卡方案。要求：思考必须最完整，确认没有遗漏任何影响决策的维度；每个关键数字标注来源（刚查到的 vs 凭记忆的），"
     "不确定的标 [待核验]；最终推荐必须是条件性的，不能给无条件排名。")

STAGES = {
 "01": "这是 pfb 六阶段流程的第 01 阶段（目标分解）。正交分解此问题：列出所有影响决策的正交因子，检查正交完备（不正交→合并，不完备→引入新因子），标注每个因子是过滤门/排序键/横切因子。只输出分解。",
 "02": "第 02 阶段（取证）。基于上面的分解，为每个关键因子给出具体数值/事实（型号、显存、带宽、价格、功耗、TCO 项）。每个数字标来源：[权重内知识] 或 [待核验]。不确定就标[待核验]，不编造。",
 "02.5": "第 02.5 阶段（交叉核验）。对 02 的证据做信度+效度检查：哪些是一手（可复现/官方规格）、哪些是二手（转述）？二手的关键数字是否可校准（bias 方向可识别）？不可校准的标[需一手]。输出核验后的证据表。",
 "03": "第 03 阶段（行动分解）。基于核验后的证据，列出得出最终推荐所需的推导步骤（只依赖已核验证据），每步标注依赖哪个证据。",
 "04": "第 04 阶段（执行）。按 03 的步骤逐项执行推导，给出候选方案的具体 TCO 计算与性价比排序。逐项对照验收。",
 "04.5": "第 04.5 阶段（复核）。往返无损检查：结论是否回应了原始问题（D 问的是什么，你解的是不是那个）？列出前提假设与边界条件，最终推荐写成条件性（若 X 则 A，若 Y 则 B）。发现新适用条件→标注换基。",
}
DIRECT = "完整解决此问题，给出性价比最优的完整选卡方案。要求：思考最完整不遗漏维度；关键数字标来源（刚查到的 vs 凭记忆的），不确定标[待核验]；最终推荐须条件性。"

def call(messages, max_tokens, tag):
    payload = json.dumps({"model": MODEL, "messages": messages,
                          "temperature": TEMP, "max_tokens": max_tokens}).encode()
    last_err = None
    for attempt in range(1, 6):
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
                    "content_chars": len(content), "reasoning_chars": len(reasoning),
                    "finish_reason": d["choices"][0].get("finish_reason"),
                    "usage": d.get("usage", {}), "attempt": attempt}
        except Exception as e:
            last_err = repr(e)
            print(f"[{tag}] attempt {attempt} failed: {last_err}; retry {attempt*5}s", flush=True)
            time.sleep(attempt * 5)
    raise RuntimeError(f"{tag}: all 5 attempts failed: {last_err}")

def repeat_score(t):
    words = re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z]+', t.lower())
    if len(words) < 20: return 0
    seen = {}; maxrep = 0
    for i in range(len(words) - 5):
        g = tuple(words[i:i+5]); seen[g] = seen.get(g, 0) + 1; maxrep = max(maxrep, seen[g])
    return maxrep

def cost(u):
    return u.get("completion_tokens", 0) if isinstance(u, dict) else 0

def run_arm_a():
    samples = []
    for i in range(1, 4):
        tag = f"A-direct-run{i}"
        t0 = time.time()
        r = call([{"role": "user", "content": Q + "\n\n" + DIRECT}], MAX_A, tag)
        r.update({"arm": "A_direct", "run": i, "elapsed_s": round(time.time() - t0, 1),
                  "repeat5": repeat_score(r["content"] + r["reasoning"]),
                  "completion_tokens": cost(r["usage"])})
        samples.append(r)
        print(f"[{tag}] OK content={r['content_chars']} finish={r['finish_reason']} "
              f"tok={r['completion_tokens']} repeat5={r['repeat5']} {r['elapsed_s']}s", flush=True)
        time.sleep(1)
    return samples

def run_arm_b():
    samples = []
    for i in range(1, 4):
        tag = f"B-pfb-run{i}"
        msgs = [{"role": "user", "content": Q}]
        stage_outs = {}
        total_t0 = time.time()
        tot_tok = 0
        for sid, instr in STAGES.items():
            st0 = time.time()
            r = call(msgs + [{"role": "user", "content": instr}], MAX_B, f"{tag}-{sid}")
            r.update({"stage": sid, "elapsed_s": round(time.time() - st0, 1),
                      "repeat5": repeat_score(r["content"] + r["reasoning"]),
                      "completion_tokens": cost(r["usage"])})
            stage_outs[sid] = r
            tot_tok += cost(r["usage"])
            print(f"[{tag}-{sid}] OK content={r['content_chars']} finish={r['finish_reason']} "
                  f"tok={r['completion_tokens']} repeat5={r['repeat5']} {r['elapsed_s']}s", flush=True)
            if r["repeat5"] > 3:
                print(f"[{tag}-{sid}] WARNING: 疑似复读循环 repeat5={r['repeat5']}", flush=True)
            msgs.append({"role": "assistant", "content": r["content"] or r["reasoning"][:500]})
            time.sleep(1)
        final = stage_outs["04.5"]
        samples.append({
            "arm": "B_pfb", "run": i,
            "final": final,
            "stages": stage_outs,
            "total_elapsed_s": round(time.time() - total_t0, 1),
            "total_completion_tokens": tot_tok,
            "final_content": final["content"],
            "final_reasoning": final["reasoning"],
        })
        print(f"[{tag}] DONE total_tok={tot_tok} elapsed={samples[-1]['total_elapsed_s']}s", flush=True)
    return samples

def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    outpath = os.path.join(outdir, "raw_outputs_t8b.json")
    result = {"meta": {"experiment": "T8b pfb 六阶段 vs 直接求解（GPU 选卡题，token 上限修订）",
                       "prereg": "prereg_t8b.md", "model": MODEL, "endpoint": BASE,
                       "temperature": TEMP, "max_a": MAX_A, "max_b": MAX_B,
                       "started_at": time.strftime("%Y-%m-%d %H:%M:%S %z")},
              "arm_a": [], "arm_b": []}
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("all", "a"):
        result["arm_a"] = run_arm_a()
        json.dump(result, open(outpath, "w"), ensure_ascii=False, indent=2)
        print("WROTE arm_a", flush=True)
    if mode in ("all", "b"):
        if mode == "b" and os.path.exists(outpath):
            result = json.load(open(outpath))
        result["arm_b"] = run_arm_b()
        result["finished_at"] = time.strftime("%Y-%m-%d %H:%M:%S %z")
        json.dump(result, open(outpath, "w"), ensure_ascii=False, indent=2)
        print("WROTE arm_b + finished", flush=True)

if __name__ == "__main__":
    main()
