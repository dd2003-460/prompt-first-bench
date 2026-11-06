#!/usr/bin/env python3
"""stage-ablation harness: S0-S5 × Q1-Q5 消融实验 runner + scorer.

纯 stdlib，无第三方依赖。模型调用走本地 27b endpoint (8787)。
S2+ 臂的联网钩子默认 stub（ego-browser 不可用时降级记录）。

用法:
  python ablation_harness.py run --arms S0,S1,S2,S5 --qs Q1,Q2 --n 2
  python ablation_harness.py run --dry-run --arms S0 --qs Q1
  python score.py aggregate runs/ gold/ -> scoring.md
"""
import argparse, json, os, re, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
PFB = os.path.dirname(os.path.dirname(HERE))  # pfb/ (experiments/stage-ablation → experiments → pfb)
WORKSPACE = os.path.dirname(PFB)  # workspace/
RUNS_DIR = os.path.join(HERE, "runs")
LLM_URL = "http://127.0.0.1:8787/v1/chat/completions"
LLM_MODEL = "qwen3.8-27b"
LLM_TIMEOUT = 600
LLM_MAX_TOKENS = 8000

# ── 题目集 ──────────────────────────────────────────────────────────
QUESTIONS = {
    "Q1": {
        "domain": "GPU硬件规格",
        "prompt_file": os.path.join(WORKSPACE, "projects/decomp/experiments/autoresearch-r1/run/prompt-minimal.txt"),
        "gold_file": os.path.join(WORKSPACE, "projects/decomp/experiments/autoresearch-r1/run/gold-facts.md"),
        "search_query": "NVIDIA H100 PCIe vs SXM LLM inference throughput benchmark",
    },
    "Q2": {
        "domain": "模型选型",
        "prompt_file": os.path.join(WORKSPACE, "projects/decomp/bench/runs/t17-generalization/task-model-selection.txt"),
        "gold_file": os.path.join(WORKSPACE, "projects/decomp/bench/gold-model-selection/tree.md"),
        "search_query": "LLM model selection criteria cost latency accuracy tradeoff",
    },
    "Q3": {
        "domain": "推理基础设施",
        "prompt_file": os.path.join(WORKSPACE, "projects/decomp/bench/runs/t17-generalization/task-inference-infra.txt"),
        "gold_file": os.path.join(WORKSPACE, "projects/decomp/bench/gold-inference-infra/tree.md"),
        "search_query": "LLM inference infrastructure GPU serving vLLM TGI comparison",
    },
    "Q4": {
        "domain": "数据处理架构",
        "prompt_file": os.path.join(WORKSPACE, "projects/decomp/bench/runs/t17-generalization/task-rag-vs-longctx.txt"),
        "gold_file": os.path.join(WORKSPACE, "projects/decomp/bench/gold-rag-vs-longctx/tree.md"),
        "search_query": "RAG vs long context window LLM retrieval augmented generation comparison",
    },
    "Q5": {
        "domain": "科研方法论",
        "prompt_file": os.path.join(WORKSPACE, "projects/decomp/bench/runs/t17-generalization/task-methodology.txt"),
        "gold_file": os.path.join(WORKSPACE, "projects/decomp/bench/gold-methodology/tree.md"),
        "search_query": "scientific research methodology hypothesis validation peer review best practices",
    },
}

# ── 阶段 prompt 文件 ────────────────────────────────────────────────
STAGE_FILES = {
    "01": os.path.join(PFB, "loop/prompt-first/01-goal-decomposition.md"),
    "02": os.path.join(PFB, "loop/prompt-first/02-information-research.md"),
    "02.5": os.path.join(PFB, "loop/prompt-first/02.5-cross-check.md"),
    "03": os.path.join(PFB, "loop/prompt-first/03-action-decomposition.md"),
    "04": os.path.join(PFB, "loop/prompt-first/04-execution-verification.md"),
    "04.5": os.path.join(PFB, "loop/prompt-first/04.5-final-review.md"),
}

DECOMP_MODULE = os.path.join(PFB, "loop/modules/decomp-01.md")


def read_file(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def extract_question(prompt_text):
    """从题面文件中提取核心问题段。"""
    # 找 "问题：" 后面的实际内容（r1 prompt-minimal 格式）
    m = re.search(r"问题[：:]\s*(.+?)(?:\n\n请给出|\Z)", prompt_text, re.DOTALL)
    if m:
        return m.group(1).strip()
    # t17 task 文件格式: 有 "## 任务" 或 "任务：" 段
    m = re.search(r"(?:##\s*)?任务[：:]\s*(.+?)(?=\n##|\Z)", prompt_text, re.DOTALL)
    if m:
        return m.group(1).strip()
    # fallback: 整个文件
    return prompt_text.strip()


def extract_decomp_five_steps():
    """提取 decomp-01.md 的「五步方法」节。"""
    text = read_file(DECOMP_MODULE)
    start = text.find("## 五步方法")
    if start < 0:
        return ""
    end = text.find("\n## ", start + 10)
    if end < 0:
        end = len(text)
    return text[start:end].strip()


def build_prompt(arm, qid):
    """按 DESIGN §2 矩阵构造各臂 prompt。"""
    q = QUESTIONS[qid]
    question = extract_question(read_file(q["prompt_file"]))

    if arm == "S0":
        # 裸 prompt: 只有题面 + r1 A-minimal 背景句
        return (
            "你是一名研究员。用户问了一个技术问题，你需要给出回答。\n\n"
            "你能用搜索和工具查资料。规则很简单：\n"
            "- 你知道的，直接说。\n"
            "- 你不确定的、或者只记得个大概的，明说\"这个我不确定/记不清了，需要查一下\"，然后去查。\n"
            "- 不要编具体数字。查不到就承认查不到。\n\n"
            f"问题：{question}\n\n"
            "请给出你的回答，并把你「不确定、需要进一步查证」的点单独列出来。"
        )

    if arm == "S6":
        # S6: 模糊启发式 — 不规定流程步骤，只给思维方向（成璐 2026-11-05 提出）
        # 假设：机械流程表把模型限制在"填表模式"；模糊提示可能激活训练时见过的
        # researcher persona / 第一性原理 / 矛盾驱动推理等更强模式。
        return (
            "你是一名资深研究员，以严谨和洞察力著称。\n\n"
            f"问题：{question}\n\n"
            "思考方式建议（不是固定流程，按你的判断用）：\n"
            "- 先回到第一性原理：这个问题的底层物理/经济/数学约束是什么？\n"
            "- 把影响因素分解开，哪些是主导项、哪些可以忽略？\n"
            "- 特别注意表面合理但实际有问题的说法——找到矛盾点，重点查证和推理。\n"
            "- 对关键数字，区分「官方标称值」和「实际表现」，合理推测偏差方向和幅度。\n"
            "- 查不到的就明说是缺口，不要编。\n\n"
            "你能用搜索和工具查资料。给出你的最终回答，把你「不确定、需要进一步查证」的点单独列出来。"
        )

    if arm == "S7T":
        # S7T: S7 hybrid + tool access (T30)
        # = S6-style fuzzy heuristic prompt + research_hook sources injection
        # Tests the §5.1 "tool-access hypothesis": does web evidence improve M1/M4?
        return (
            "你是一名资深研究员，以严谨和洞察力著称。\n\n"
            f"问题：{question}\n\n"
            "思考方式建议（不是固定流程，按你的判断用）：\n"
            "- 先回到第一性原理：这个问题的底层物理/经济/数学约束是什么？\n"
            "- 把影响因素分解开，哪些是主导项、哪些可以忽略？\n"
            "- 特别注意表面合理但实际有问题的说法——找到矛盾点，重点查证和推理。\n"
            "- 对关键数字，区分「官方标称值」和「实际表现」，合理推测偏差方向和幅度。\n"
            "- 查不到的就明说是缺口，不要编。\n\n"
            "【工具说明】你可以使用 web_search 工具检索信息。"
            "对每个关键主张，把来源标题、URL、观察时间写进你的输出。\n\n"
            "请基于以上来源和工具检索结果回答，引用时标注来源编号。"
            "给出你的最终回答，把你「不确定、需要进一步查证」的点单独列出来。"
        )

    if arm in ("S7F", "S7V"):
        # S7F: S7 hybrid + FILTERED tool access (T31)
        # S7V: same as S7F but with two-pass claim verification (T32)
        return (
            "你是一名资深研究员，以严谨和洞察力著称。\n\n"
            f"问题：{question}\n\n"
            "思考方式建议（不是固定流程，按你的判断用）：\n"
            "- 先回到第一性原理：这个问题的底层物理/经济/数学约束是什么？\n"
            "- 把影响因素分解开，哪些是主导项、哪些可以忽略？\n"
            "- 特别注意表面合理但实际有问题的说法——找到矛盾点，重点查证和推理。\n"
            "- 对关键数字，区分「官方标称值」和「实际表现」，合理推测偏差方向和幅度。\n"
            "- 查不到的就明说是缺口，不要编。\n\n"
            "【工具说明】以下是经过筛选的、与问题直接相关的参考来源。"
            "仅当来源内容明确支持你的某个具体断言时才引用它；"
            "如果来源没有直接回答你的子问题，不要强行关联。\n\n"
            "请基于以上来源回答，引用时标注来源编号并写明该来源具体支持了哪个断言。"
            "给出你的最终回答，把你「不确定、需要进一步查证」的点单独列出来。"
        )

    parts = [f"[阶段 01 — 目标分解]\n"]
    if arm in ("S1",):
        # S1: 01 + decomp 五步法
        five = extract_decomp_five_steps()
        parts.append(five + "\n\n")
    else:
        # S2+: 01 主文件全文
        parts.append(read_file(STAGE_FILES["01"]) + "\n\n")

    if arm in ("S2", "S3", "S4", "S5"):
        parts.append("[阶段 02 — 信息调研]\n")
        parts.append(read_file(STAGE_FILES["02"]) + "\n\n")
        # 工具说明: 告知模型可用 web_search 检索（harness 层预留 research_hook，当前 stub）
        parts.append(
            "【工具说明】你可以使用 web_search 工具检索信息。"
            "对每个关键主张，把来源标题、URL、观察时间写进你的输出。\n\n"
        )

    if arm in ("S3", "S4", "S5"):
        parts.append("[阶段 02.5 — 交叉核对]\n")
        parts.append(read_file(STAGE_FILES["02.5"]) + "\n\n")

    if arm in ("S4", "S5"):
        parts.append("[阶段 03 — 行动分解]\n")
        parts.append(read_file(STAGE_FILES["03"]) + "\n\n")

    if arm == "S5":
        parts.append("[阶段 04 — 执行验证]\n")
        parts.append(read_file(STAGE_FILES["04"]) + "\n\n")
        parts.append("[阶段 04.5 — 终审]\n")
        parts.append(read_file(STAGE_FILES["04.5"]) + "\n\n")

    parts.append(f"\n【待解问题】\n{question}\n")
    parts.append("\n请按上述阶段要求，逐步完成并给出最终回答。")
    return "".join(parts)


# ── LLM 调用 ────────────────────────────────────────────────────────
def call_llm(prompt, max_tokens=LLM_MAX_TOKENS, timeout=LLM_TIMEOUT, retries=1, seed=None, temperature=0):
    payload_dict = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if seed is not None:
        payload_dict["seed"] = seed
    payload = json.dumps(payload_dict).encode()
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(LLM_URL, data=payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read())
            content = data["choices"][0]["message"]["content"]
            usage = data.get("usage", {})
            return content, {
                "in": usage.get("prompt_tokens", 0),
                "out": usage.get("completion_tokens", 0),
            }
        except Exception as e:
            if attempt < retries:
                print(f"  retry {attempt+1}: {e}", file=sys.stderr)
                time.sleep(5)
            else:
                raise


# ── 联网钩子（S2+ 用）────────────────────────────────────────────────
def research_hook(qid, question):
    """ego-browser 真联网检索，返回 sources 列表。
    失败时返回空列表（降级模式，harness 记录降级）。
    """
    try:
        from research_hook import research_hook as _hook
        return _hook(qid, question)
    except Exception as e:
        print(f"  [research_hook] {qid}: unavailable ({e}), degrading to empty", file=sys.stderr)
        return []


def inject_sources_into_prompt(prompt, sources):
    """把来源包注入 S2+ 的 02 阶段说明里。"""
    if not sources:
        return prompt
    src_lines = ["\n【已检索到的来源（来自 ego-browser 真实网页检索）】"]
    for i, s in enumerate(sources, 1):
            snip = s.get("snippet", "")[:500]
            src_lines.append(f"{i}. {s['title']}\n   URL: {s['url']}\n   摘要: {snip}\n   观察时间: {s['observed_at']}")
    src_block = "\n".join(src_lines) + "\n\n请基于以上来源回答，引用时标注来源编号。\n\n"
    # 插在"工具说明"段之后
    marker = "【工具说明】"
    idx = prompt.find(marker)
    if idx >= 0:
        end_idx = prompt.find("\n\n", idx)
        if end_idx < 0:
            end_idx = len(prompt)
        return prompt[:end_idx] + src_block + prompt[end_idx:]
    # fallback: 追加到末尾
    return prompt + src_block


# ── 主 runner ───────────────────────────────────────────────────────
def run_arm(arm, qid, rep, dry_run=False):
    prompt = build_prompt(arm, qid)
    tag = f"{arm}-{qid}-r{rep}"
    out_path = os.path.join(RUNS_DIR, f"{tag}.json")
    if os.path.exists(out_path):
        try:
            with open(out_path) as _f:
                _prev = json.load(_f)
            _len = len(_prev.get("output_text", ""))
            if not _prev.get("error") and _len > 200:
                print(f"  [{tag}] SKIP (exists, {_len} chars)", flush=True)
                return _prev
        except Exception:
            pass

    # S2+ 臂: 先跑真实联网检索，把来源包注入 prompt
    sources = []
    if arm in ("S2", "S3", "S4", "S5", "S7T", "S7F", "S7V") and not dry_run:
        q = QUESTIONS[qid]
        # 优先用预设英文搜索词（Bing locale 更稳定），fallback 到 prompt 提取
        question = q.get("search_query") or extract_question(read_file(q["prompt_file"]))
        print(f"  [{tag}] running research_hook (ego-browser)...", flush=True)
        t_research = time.time()
        sources = research_hook(qid, question)
        wall_research = round(time.time() - t_research, 1)
        print(f"  [{tag}] research done in {wall_research}s, {len(sources)} sources", flush=True)
        # T31: S7F applies keyword filtering before injection
        if arm in ("S7F", "S7V") and sources:
            from research_hook import filter_sources
            filtered = filter_sources(sources, qid)
            print(f"  [{tag}] filter: {len(sources)} → {len(filtered)} sources", flush=True)
            sources = filtered
        if sources:
            prompt = inject_sources_into_prompt(prompt, sources)
        else:
            print(f"  [{tag}] WARNING: no sources (degraded mode)", file=sys.stderr)

    if dry_run:
        print(f"\n{'='*60}\nDRY-RUN {tag}\nprompt length: {len(prompt)} chars\n{'='*60}")
        print(prompt[:500] + "..." if len(prompt) > 500 else prompt)
        return None

    print(f"  [{tag}] calling 27b ({len(prompt)} chars prompt)...", flush=True)
    t0 = time.time()
    # S6/S7/S7T: use temp=0.1 + seed per rep to guarantee diversity
    # (temp=0 greedy decode is fully deterministic for short structured prompts; seed alone is ignored)
    call_seed = None
    call_temp = 0
    if arm in ("S6", "S7", "S7T", "S7F", "S7V"):
        call_seed = hash(f"{arm}-{qid}") % 10000 + rep * 7919
        call_temp = 0.1
    try:
        output, tokens = call_llm(prompt, seed=call_seed, temperature=call_temp)
    except Exception as e:
        print(f"  [{tag}] FAILED: {e}", file=sys.stderr)
        record = {
            "arm": arm, "qid": qid, "rep": rep,
            "model": LLM_MODEL, "params": {"temp": 0, "max_tokens": LLM_MAX_TOKENS},
            "output_text": "", "sources": [], "wall_s": round(time.time() - t0, 1),
            "tokens": {"in": 0, "out": 0}, "error": str(e),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        os.makedirs(RUNS_DIR, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(record, f, ensure_ascii=False, indent=2)
        return record

    wall = round(time.time() - t0, 1)
    print(f"  [{tag}] done in {wall}s, {tokens['out']} tokens out", flush=True)

    # T32: S7V two-pass — second call verifies claims against sources
    pass1_text = output
    if arm == "S7V" and sources:
        verify_prompt = (
            "你刚才回答了一个问题，引用了以下参考来源。现在请逐条核验你的数字断言：\n\n"
            f"【你的初稿答案】\n{output}\n\n"
            f"【参考来源】\n{inject_sources_into_prompt('', sources)}\n\n"
            "核验规则：\n"
            "1. 找出初稿中所有具体数字断言（带宽、吞吐量、百分比、价格等）\n"
            "2. 对每个数字，检查参考来源中是否有明确支持该数字的原文\n"
            "3. 有支持的 → 保留，标注「✓ 来源[N]支持」\n"
            "4. 无支持的 → 删除该数字或改为定性描述，标注「✗ 无来源支持，已删除」\n"
            "5. 不要重新生成整个答案，只修正数字断言部分\n\n"
            "输出格式：先列出核验表（断言 | 来源支持? | 处理），然后给出修正后的完整答案。"
        )
        print(f"  [{tag}] PASS 2: verifying claims ({len(verify_prompt)} chars)...", flush=True)
        t1 = time.time()
        try:
            verified_output, v_tokens = call_llm(verify_prompt, seed=call_seed, temperature=0)
            wall_v = round(time.time() - t1, 1)
            print(f"  [{tag}] PASS 2 done in {wall_v}s, {v_tokens['out']} tokens", flush=True)
            # Extract the corrected answer (after the verification table)
            # The model outputs: [verification table]\n\n[corrected answer]
            # Take everything after the last occurrence of a separator or the final answer section
            lines = verified_output.split('\n')
            # Find where the corrected answer starts (look for markers)
            answer_start = 0
            for i, line in enumerate(lines):
                if any(m in line for m in ['修正后', '最终答案', 'Corrected', 'Final']):
                    answer_start = i + 1
                    break
            corrected = '\n'.join(lines[answer_start:]).strip()
            if len(corrected) < 100:
                # Fallback: use full verified output
                corrected = verified_output
            output = corrected
            tokens = {"in": tokens["in"] + v_tokens["in"], "out": tokens["out"] + v_tokens["out"]}
            wall += wall_v
        except Exception as e:
            print(f"  [{tag}] PASS 2 FAILED (keeping pass 1): {e}", file=sys.stderr)

    record = {
        "arm": arm, "qid": qid, "rep": rep,
        "model": LLM_MODEL, "params": {"temp": 0, "max_tokens": LLM_MAX_TOKENS, **({"seed": call_seed} if call_seed else {})},
        "output_text": output, "sources": sources, "wall_s": wall,
        "tokens": tokens,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    os.makedirs(RUNS_DIR, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
    return record


def main():
    ap = argparse.ArgumentParser(description="stage-ablation harness")
    sub = ap.add_subparsers(dest="cmd")

    run_p = sub.add_parser("run", help="run ablation arms")
    run_p.add_argument("--arms", default="S0", help="comma-separated: S0,S1,S2,S3,S4,S5")
    run_p.add_argument("--qs", default="Q1", help="comma-separated: Q1,Q2,Q3,Q4,Q5")
    run_p.add_argument("--n", type=int, default=2, help="reps per arm×q (default 2)")
    run_p.add_argument("--rep", type=int, default=None, help="run only this specific rep (overrides --n)")
    run_p.add_argument("--dry-run", action="store_true", help="print prompts, no LLM calls")

    args = ap.parse_args()
    if args.cmd == "run":
        arms = [a.strip().upper() for a in args.arms.split(",")]
        qs = [q.strip().upper() for q in args.qs.split(",")]
        total = len(arms) * len(qs) * args.n
        print(f"stage-ablation: {len(arms)} arms × {len(qs)} questions × n={args.n} = {total} runs")
        print(f"  arms: {arms}")
        print(f"  questions: {qs}")
        print(f"  endpoint: {LLM_URL}")
        print(f"  model: {LLM_MODEL}")
        print()
        for arm in arms:
            for qid in qs:
                reps = [args.rep] if args.rep else range(1, args.n + 1)
                for rep in reps:
                    run_arm(arm, qid, rep, dry_run=args.dry_run)
        print(f"\nDone. Run `python score.py aggregate` to score.")
    else:
        ap.print_help()


if __name__ == "__main__":
    main()