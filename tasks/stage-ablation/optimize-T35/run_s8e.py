#!/usr/bin/env python3
"""T35 阶段B：S8E pilot runner（Q1+Q4 × 2 reps = 4 runs）。

设计要点：
- 复用 ablation_harness.py 的 QUESTIONS / extract_question / read_file /
  inject_sources_into_prompt / LLM_URL / LLM_MODEL，不改任何已有文件。
- S8E = S7F/S7V 的 prompt 骨架，把"每条数字断言必须标注来源句、无来源则不写"
  嵌进【既有节点】（5 条思考建议 + 工具说明段 + 结尾作答要求）内部，
  **不新增独立段落、不追加附录、不调用 Pass2**：单次生成。
- 来源离线取自对应 S7V-Q{q}-r{rep}.json 的 sources 字段（与 S7V 完全同一批来源，
  保证 S8E vs S7V 的唯一变量是"验证规则实现方式 + 调用次数"）。不联网检索。
- 端点调用用 curl --noproxy '*'（等效于 urllib 禁代理，规避 ClashX），
  --max-time 110（单 run 硬上限 <120s）；任一 run 超时/失败即停止扩展并记录降级。
- 参数：temp=0.1 + seed（复用 harness 公式）、max_tokens=2000（控时）。
- 所有新文件只落在 optimize-T35/ 下。
"""
import json, os, sys, subprocess, time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)  # experiments/stage-ablation/
sys.path.insert(0, BASE)
from ablation_harness import (
    QUESTIONS, extract_question, read_file,
    inject_sources_into_prompt, LLM_URL, LLM_MODEL,
)

RUNS_OUT = os.path.join(HERE, "runs")
PROMPTS_OUT = os.path.join(HERE, "prompts")
os.makedirs(RUNS_OUT, exist_ok=True)
os.makedirs(PROMPTS_OUT, exist_ok=True)

# ── S8E prompt 模板 ────────────────────────────────────────────────
# 与 harness build_prompt("S7F"/"S7V") 的差异仅在下面 4 处「嵌入句」，
# 均为在既有节点内改写/追加，不新增任何独立段落或附录。
S8E_TEMPLATE = """你是一名资深研究员，以严谨和洞察力著称。

问题：{question}

思考方式建议（不是固定流程，按你的判断用）：
- 先回到第一性原理：这个问题的底层物理/经济/数学约束是什么？
- 把影响因素分解开，哪些是主导项、哪些可以忽略？
- 特别注意表面合理但实际有问题的说法——找到矛盾点，重点查证和推理。
- 对关键数字，区分「官方标称值」和「实际表现」，合理推测偏差方向和幅度；写下的每个数字都要能在下面来源里找到支持它的原句，找不到就只做定性描述、不写这个数字。
- 查不到的就明说是缺口，不要编；凡是写下数字断言，必须紧跟其后标注它所依据的来源原句（形如「[来源N] 原句…」），来源里没有对应原句的数字一律不写。

【工具说明】以下是经过筛选的、与问题直接相关的参考来源。仅当来源内容明确支持你的某个具体断言时才引用它；如果来源没有直接回答你的子问题，不要强行关联；每条含数字的断言都要能指回这里的某条来源原句。

请基于以上来源回答，引用时标注来源编号并写明该来源具体支持了哪个断言；每条数字断言后面紧跟其来源原句，无来源原句支撑的数字改为定性描述或不写。给出你的最终回答，把你「不确定、需要进一步查证」的点单独列出来。"""


def call_llm_curl(prompt, seed, max_tokens=2000, timeout=110):
    """单次生成；curl --noproxy '*' 规避 ClashX；--max-time < 120s。"""
    payload = json.dumps({
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "max_tokens": max_tokens,
        "seed": seed,
    }, ensure_ascii=False)
    cmd = [
        "curl", "-s", "--noproxy", "*", "--max-time", str(timeout),
        "-X", "POST", LLM_URL, "-H", "Content-Type: application/json",
        "-d", payload,
    ]
    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10)
    wall = round(time.time() - t0, 1)
    if r.returncode != 0:
        raise RuntimeError(f"curl rc={r.returncode} stderr={r.stderr[:200]}")
    data = json.loads(r.stdout)
    content = data["choices"][0]["message"]["content"]
    usage = data.get("usage", {})
    return content, {
        "in": usage.get("prompt_tokens", 0),
        "out": usage.get("completion_tokens", 0),
    }, wall


def main():
    plan = [(q, r) for q in ("Q1", "Q4") for r in (1, 2)]
    print(f"T35 S8E pilot: {len(plan)} runs  Q1/Q4 × r1/r2  single-pass  max_tokens=2000  temp=0.1+seed")
    print(f"  endpoint={LLM_URL}  model={LLM_MODEL}  curl --noproxy '*'  --max-time 110")
    print(f"  (等效 harness 参数；本脚本不联网检索，sources 取自已有 S7V run JSON)\n")

    degraded = None
    n_ok = 0
    for qid, rep in plan:
        tag = f"S8E-{qid}-r{rep}"
        question = extract_question(read_file(QUESTIONS[qid]["prompt_file"]))
        # 与 S7V 完全相同的同一 rep 来源
        src_path = os.path.join(BASE, "runs", f"S7V-{qid}-r{rep}.json")
        src_run = json.load(open(src_path, encoding="utf-8"))
        sources = src_run.get("sources", [])

        prompt = S8E_TEMPLATE.format(question=question)
        prompt = inject_sources_into_prompt(prompt, sources)
        with open(os.path.join(PROMPTS_OUT, tag + ".txt"), "w", encoding="utf-8") as f:
            f.write(prompt)

        seed = hash(f"S8E-{qid}") % 10000 + rep * 7919
        rec = {
            "arm": "S8E", "qid": qid, "rep": rep,
            "model": LLM_MODEL,
            "params": {"temp": 0.1, "max_tokens": 2000, "seed": seed, "passes": 1},
            "output_text": "", "sources": sources,
            "prompt_len": len(prompt), "prompt_file": os.path.join(PROMPTS_OUT, tag + ".txt"),
            "wall_s": 0, "tokens": {"in": 0, "out": 0},
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        try:
            out, tokens, wall = call_llm_curl(prompt, seed)
            rec.update({"output_text": out, "tokens": tokens, "wall_s": wall})
            n_ok += 1
            print(f"  [{tag}] OK  prompt={len(prompt)}ch  sources={len(sources)}  "
                  f"seed={seed}  wall={wall}s  tok_out={tokens['out']}")
        except Exception as e:
            degraded = f"{tag}: {e}"
            rec["error"] = str(e)
            print(f"  [{tag}] FAILED/DEGRADED: {e}")
        with open(os.path.join(RUNS_OUT, tag + ".json"), "w", encoding="utf-8") as f:
            json.dump(rec, f, ensure_ascii=False, indent=2)
        if degraded:
            print(f"\n  >>> DEGRADED: 单 run 超时/失败，按任务书立即停止扩展（conf 0.2）。")
            break

    print(f"\nDone. ok={n_ok}/{len(plan)}  degraded={degraded}")
    with open(os.path.join(HERE, "run-status.json"), "w", encoding="utf-8") as f:
        json.dump({"plan": len(plan), "ok": n_ok, "degraded": degraded}, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
