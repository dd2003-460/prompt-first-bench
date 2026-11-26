#!/usr/bin/env python3
# origin: ai
# T8c 跑数脚本：pfb 六阶段 vs 直接求解（GPU 选卡题，token-matched 73728/臂上限）
# 题面 = t8c-spec-final.md §4 冻结版（commit 2c16f644f），下方 Q 逐字转录，勿改
# 预注册 = t8c-preregistration.md（判据 commit 8c168c2a4）
# 相对 T8b 的改动（spec §5 runner 改造点，commit 5c32910ea）：
#   1. Q 换成 §4 冻结题面（定值 64K / 候选集定死 3090+V100 / c_pass 公式全列 / n=floor(n_cards/2)）
#   2. MAX_A 16384 -> 73728（token-matched：两臂预算上限相等，B 臂 6×12288 硬结构决定上限；2026-11-26 post-hoc 修复）
#   3. Arm A' user message = 题面全文（不拼 DIRECT 后缀——§4 输出要求已含来源标注条款）
#   4. STAGES 六阶段指令复用 T8b 不动；输出 raw_outputs_t8c.json + t8c_stages/ sidecar
# 不得直接改 run_exp_t8b.py（T8b 数据可追溯性）
import json, time, urllib.request, os, re, sys

BASE = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b-mtp"
TEMP = 0.7
MAX_A = 73728  # Arm A' 单次（= 72K 预算上限，预注册 §1, 2026-11-26 post-hoc）
MAX_B = 12288  # Arm B' 每阶段（6×12288=73728, 2026-11-26 post-hoc 修复截断）
MAX_B_REVIEW = 16384  # 04.5 复核阶段单独上限（2026-11-27 修复：run3-04.5 reasoning
                      # 14866 tok 撞 12288 截断；归因=复核阶段输出长度方差 2.6×，非复读。
                      # 服务端 probe 证 max_tokens=32768 可接受，16384 覆盖 run3 实测
                      # 14866 留 10% 余量。仅 04.5 生效，其余阶段仍 12288，token-matched
                      # 名义上限不变（B 臂实测 29-41K ≪ 73728））

# ===== §4 冻结题面（t8c-spec-final.md commit 2c16f644f，逐字转录）=====
Q = (
    "你要在本地工作站上部署 Qwen3-27B 模型推理。严格按以下约束与成本模型求解\n"
    "（本题面已给出全部所需数字，不需要也不允许外部查询）：\n"
    "\n"
    "【硬约束】\n"
    "1. 上下文窗口定值 64K tokens（KV 缓存按 64K 计，27B 单流 KV ≈ 24.7 GB/流）。\n"
    "2. 解码吞吐目标：每流 ≥20 tok/s（≈50 ms/token）。不达标的配置直接淘汰（带宽准入门，见下）。\n"
    "3. 并发约定：n = floor(n_cards / 2)（2 卡/流，部署约定，不是自由优化变量）。\n"
    "4. 目标函数：最小化 c_pass（每个通过任务的成本，¢/task）。c_pass 最低的配置为最优。\n"
    "\n"
    "【候选硬件（固定，不得自行扩大或替换）】\n"
    "  RTX 3090    显存 24 GB   峰值带宽 936 GB/s   峰值算力(FP16 non-tensor) 71 TFLOPS   TDP 350 W   单价 $1050\n"
    "  V100 SXM2   显存 32 GB   峰值带宽 900 GB/s   峰值算力(FP16 non-tensor) 125 TFLOPS  TDP 250 W   单价 $704（¥5000）\n"
    "卡数：单机 2-4 卡。精度：W4/W8/W16 可选（权重体积 W4=14 GB / W8=27 GB / W16=54 GB），\n"
    "需论证所选精度的质量损失是否可接受。\n"
    "\n"
    "【两道准入门（不满足即淘汰）】\n"
    "- 显存门：(W_bytes + n×24.7) / n_cards ≤ 单卡显存。\n"
    "- 带宽门：每卡有效带宽 = 峰值带宽×0.80 ≥ 每卡需求 20×(W_bytes + n×24.7)/n_cards。\n"
    "  等价固定阈值（一卡一流口径）：W4 ≥ 774 GB/s，W8 ≥ 1034 GB/s，W16 ≥ 1574 GB/s（峰值带宽口径）。\n"
    "\n"
    "【c_pass 公式与参数（按此公式计算，勿自改口径）】\n"
    "  c_pass = c_hour / (U × λ_raw × G) × 100          [¢/task]\n"
    "  c_hour = 摊销 + 电费 + 故障                        [$ / 小时, 整机]\n"
    "  gpu_price = 单价 × n_cards                        [整机 GPU 总价, 不是单卡价!]\n"
    "  摊销   = (gpu_price + 2000 − gpu_price×0.40) / 26280\n"
    "  电费   = (n_cards×TDP + 300) / 1000 × 0.12\n"
    "  故障   = 0.20 × gpu_price / 26280\n"
    "  λ_raw  = 3600 / t_task                            [task/小时]\n"
    "  t_task = t_prefill + t_decode / n                 [秒]\n"
    "  t_prefill = 594e12 / (n_cards × TF_peak × 0.45 × 0.81)\n"
    "  t_decode  = 655 × (W_bytes + n×24.7) / (n_cards × BW_peak × 0.80 × 0.81)\n"
    "参数含义：U=0.35 利用率；G=0.68 通过率；2000$ 4卡主机；0.40 残值率；26280h 3年摊销；\n"
    "0.20 三年故障概率；594 TFLOP prefill 算力；655 输出 token 数；0.45 MFU；\n"
    "0.81 多卡互联效率；0.80 带宽效率；0.12 $/kWh 电价。\n"
    "\n"
    "【输出要求】\n"
    "1. 枚举所有通过两道门的可行配置（卡型×卡数×精度×n），逐个算出 c_pass。\n"
    "2. 给出最优选卡方案（c_pass 最低者）：卡型×卡数×精度×n。\n"
    "3. 逐项说明其余候选为何被淘汰（显存装不下 / 带宽不达标 / c_pass 更高）。\n"
    "4. 论证所选精度的质量损失是否可接受。\n"
    "5. 关键数字标来源（题面给定 vs 你推导的），不确定标 [待核验]。\n"
)
# =====================================================================

STAGES = {
 "01": "这是 pfb 六阶段流程的第 01 阶段（目标分解）。正交分解此问题：列出所有影响决策的正交因子，检查正交完备（不正交→合并，不完备→引入新因子），标注每个因子是过滤门/排序键/横切因子。只输出分解。",
 "02": "第 02 阶段（取证）。基于上面的分解，为每个关键因子给出具体数值/事实（型号、显存、带宽、价格、功耗、TCO 项）。每个数字标来源：[权重内知识] 或 [待核验]。不确定就标[待核验]，不编造。",
 "02.5": "第 02.5 阶段（交叉核验）。对 02 的证据做信度+效度检查：哪些是一手（可复现/官方规格）、哪些是二手（转述）？二手的关键数字是否可校准（bias 方向可识别）？不可校准的标[需一手]。输出核验后的证据表。",
 "03": "第 03 阶段（行动分解）。基于核验后的证据，列出得出最终推荐所需的推导步骤（只依赖已核验证据），每步标注依赖哪个证据。",
 "04": "第 04 阶段（执行）。按 03 的步骤逐项执行推导，给出候选方案的具体 TCO 计算与性价比排序。逐项对照验收。",
 "04.5": "第 04.5 阶段（复核）。往返无损检查：结论是否回应了原始问题（D 问的是什么，你解的是不是那个）？列出前提假设与边界条件，最终推荐写成条件性（若 X 则 A，若 Y 则 B）。发现新适用条件→标注换基。",
}

def call(messages, max_tokens, tag):
    payload = json.dumps({"model": MODEL, "messages": messages,
                          "temperature": TEMP, "max_tokens": max_tokens}).encode()
    last_err = None
    for attempt in range(1, 6):
        try:
            length_retries = 0
            while True:
                req = urllib.request.Request(BASE, data=payload, headers={"Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=900) as r:
                    d = json.loads(r.read().decode())
                msg = d["choices"][0]["message"]
                content = (msg.get("content") or "").strip()
                reasoning = (msg.get("reasoning") or "").strip()
                if not content and not reasoning:
                    raise ValueError("empty")
                fr = d["choices"][0].get("finish_reason")
                # finish_reason==length（reasoning 截断）：同 prompt 同 max_tokens 重采样，独立计数 ≤2 次
                # （不计入上面异常重试的 5 次上限）；累计 3 次（首次+2 重试）仍 length → 返回 last，
                # 保留 finish_reason='length'，由上层 eval 按预注册判 indeterminate，harness 不改标签
                if fr != "length" or length_retries >= 2:
                    break
                length_retries += 1
                print(f"[{tag}] finish_reason=length (截断), length retry {length_retries}/2 (同 prompt 同 max_tokens 重采样)", flush=True)
            return {"content": content, "reasoning": reasoning,
                    "content_chars": len(content), "reasoning_chars": len(reasoning),
                    "finish_reason": fr,
                    "usage": d.get("usage", {}), "attempt": attempt,
                    "length_retries": length_retries}
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

def save_stage_sidecar(run_i, sid, r, outdir):
    """每 stage 增量落盘：即使 run 中途崩溃，前面 stage 的文本也可从 sidecar 恢复"""
    sd = os.path.join(outdir, "t8c_stages")
    os.makedirs(sd, exist_ok=True)
    spath = os.path.join(sd, f"B{run_i}_{sid}.json")
    json.dump(r, open(spath, "w"), ensure_ascii=False, indent=2)

def cost(u):
    return u.get("completion_tokens", 0) if isinstance(u, dict) else 0

def run_arm_a():
    samples = []
    for i in range(1, 4):
        tag = f"A-direct-run{i}"
        t0 = time.time()
        r = call([{"role": "user", "content": Q}], MAX_A, tag)
        r.update({"arm": "A_direct", "run": i, "elapsed_s": round(time.time() - t0, 1),
                  "repeat5": repeat_score(r["content"] + r["reasoning"]),
                  "completion_tokens": cost(r["usage"])})
        samples.append(r)
        print(f"[{tag}] OK content={r['content_chars']} finish={r['finish_reason']} "
              f"tok={r['completion_tokens']} repeat5={r['repeat5']} {r['elapsed_s']}s", flush=True)
        time.sleep(1)
    return samples

def run_arm_b(result, outpath):
    outdir = os.path.dirname(os.path.abspath(outpath))
    samples = []
    for i in range(1, 4):
        tag = f"B-pfb-run{i}"
        msgs = [{"role": "user", "content": Q}]
        stage_outs = {}
        total_t0 = time.time()
        tot_tok = 0
        for sid, instr in STAGES.items():
            st0 = time.time()
            cap = MAX_B_REVIEW if sid == "04.5" else MAX_B  # 04.5 单独提上限（见 MAX_B_REVIEW 注释）
            r = call(msgs + [{"role": "user", "content": instr}], cap, f"{tag}-{sid}")
            r.update({"stage": sid, "elapsed_s": round(time.time() - st0, 1),
                      "repeat5": repeat_score(r["content"] + r["reasoning"]),
                      "completion_tokens": cost(r["usage"])})
            stage_outs[sid] = r
            save_stage_sidecar(i, sid, r, outdir)
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
        result["arm_b"] = samples
        json.dump(result, open(outpath, "w"), ensure_ascii=False, indent=2)
        print(f"WROTE arm_b run{i} (incremental)", flush=True)
    return samples

def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    outpath = os.path.join(outdir, "raw_outputs_t8c.json")
    result = {"meta": {"experiment": "T8c pfb 六阶段 vs 直接求解（token-matched 73728/臂上限，题面三歧义已消解, 2026-11-26 重锚定）",
                       "spec": "t8c-spec-final.md (题面冻结 2c16f644f)",
                       "prereg": "t8c-preregistration.md (判据冻结 8c168c2a4)",
                       "model": MODEL, "endpoint": BASE,
                       "temperature": TEMP, "max_a": MAX_A, "max_b": MAX_B,
                      "max_b_review_045": MAX_B_REVIEW,
                       "token_matched_budget": 73728,
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
        run_arm_b(result, outpath)
        result["finished_at"] = time.strftime("%Y-%m-%d %H:%M:%S %z")
        json.dump(result, open(outpath, "w"), ensure_ascii=False, indent=2)
        print("WROTE arm_b + finished", flush=True)

if __name__ == "__main__":
    main()
