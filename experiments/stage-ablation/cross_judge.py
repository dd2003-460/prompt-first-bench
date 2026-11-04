#!/usr/bin/env python3
"""cross_judge.py: 异源 judge 复核 M1（事实准确率）。

用 ego-browser 调 Perplexity (perplexity.ai) 做独立 judge，
对比本地 27b 自判的 M1 分数，计算一致性。

Gemini 网页版在 ego-lite 会话中不可用（/app 被重定向回 landing page），
Perplexity 已验证可用（2026-11-04）。

用法:
  python3 cross_judge.py            # 对所有 runs 跑异源 judge
  python3 cross_judge.py Q1 Q2      # 只跑指定题
  python3 cross_judge.py Q1 --limit 5  # 每题最多 5 个 run
"""
import json, os, subprocess, sys, time, re, tempfile
from datetime import datetime, timezone

EGO_BROWSER = "/Users/a1-6/.local/bin/ego-browser"
HERE = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(HERE, "runs")
WORKSPACE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
GOLD_FILES = {
    "Q1": os.path.join(WORKSPACE, "projects/decomp/experiments/autoresearch-r1/run/gold-facts.md"),
    "Q2": os.path.join(WORKSPACE, "projects/decomp/bench/gold-model-selection/tree.md"),
    "Q3": os.path.join(WORKSPACE, "projects/decomp/bench/gold-inference-infra/tree.md"),
    "Q4": os.path.join(WORKSPACE, "projects/decomp/bench/gold-rag-vs-longctx/tree.md"),
}

JUDGE_PROMPT = """你是一个严格的事实核查员。请对照【标准答案】评估【模型回答】的事实准确率。

评分规则：
- 逐条检查模型回答中的关键事实断言（数字、规格、结论）
- 每条断言与标准答案对比：正确=1，部分正确=0.5，错误/无依据=0
- M1 = 正确断言数 / 总断言数
- 如果模型回答中没有可验证的事实断言（纯方法论/空话），M1=0 并标注 no_factual_claims

输出 JSON（不要其他文字）：
{{"m1": <0-1 float>, "claims_checked": <int>, "claims_correct": <int>, "notes": "<一句话说明>"}}

【标准答案】
{gold}

【模型回答】
{answer}
"""


def _run_perplexity(prompt_text):
    """通过 ego-browser 调 Perplexity，返回回复文本。"""
    # 把 prompt 写入临时文件，避免 JS 字符串转义问题
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
        f.write(prompt_text)
        prompt_file = f.name

    js = f'''
(async () => {{
const task = await taskSpace("cross-judge-{int(time.time())}");
const page = task.page("p1");
await page.goto("https://www.perplexity.ai/", {{ timeout: 30000, waitUntil: "domcontentloaded" }});
await page.waitForTimeout(8000);

// 读取 prompt 文件
const fs = require('fs');
const prompt = fs.readFileSync({json.dumps(prompt_file)}, 'utf-8');

// 点击输入框 [role="textbox"]
await page.click('[role="textbox"]');
await page.waitForTimeout(500);

// 输入 prompt（分块，每块 200 字符）
const chunks = prompt.match(/./g) || [];
let i = 0;
for (; i < chunks.length; i += 200) {{
  const chunk = chunks.slice(i, i + 200).join('');
  await page.keyboard.type(chunk, {{ delay: 0 }});
}}
await page.waitForTimeout(500);

// 按 Enter 发送
await page.keyboard.press("Enter");

// 等待响应（最多 90s）
await page.waitForTimeout(90000);

// 提取回复（找 "已完成" 标记后的文本）
const text = await page.evaluate(() => {{
  const body = document.body.innerText;
  const idx = body.lastIndexOf('已完成');
  if (idx > -1) return body.slice(idx, idx + 2000);
  const lines = body.split('\\n').filter(l => l.trim());
  return lines.slice(-30).join('\\n');
}});

console.log(JSON.stringify({{text: text}}));
}})();
'''
    try:
        result = subprocess.run(
            [EGO_BROWSER, "nodejs", "-e", js],
            capture_output=True, text=True, timeout=180,
        )
    finally:
        os.unlink(prompt_file)

    out = result.stdout + "\n" + result.stderr
    for line in reversed(out.strip().splitlines()):
        line = line.strip()
        if line.startswith("{"):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                continue
    raise RuntimeError(f"Perplexity judge failed: {out[-300:]}")


def judge_m1(gold_md, answer_text):
    """调 Perplexity 做异源 M1 判定，返回 dict。"""
    prompt = JUDGE_PROMPT.format(gold=gold_md[:4000], answer=answer_text[:6000])
    raw = _run_perplexity(prompt)
    text = raw.get("text", "")
    # 从 Perplexity 回复里提取 JSON
    match = re.search(r'\{[^{}]*"m1"[^{}]*\}', text)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"m1": None, "claims_checked": 0, "claims_correct": 0,
                "notes": f"parse_failed: {text[:200]}"}


def _load_local_scores():
    """从 scoring.md 解析 per-run scores。"""
    content = open(os.path.join(HERE, "scoring.md")).read()
    scores = {}
    for line in content.split('\n'):
        m = re.match(r'\|\s*(S\d)\s*\|\s*Q(\d)\s*\|\s*r(\d)\s*\|', line)
        if m:
            parts = [p.strip().replace('**','') for p in line.split('|')]
            tag = f'{m.group(1)}-Q{m.group(2)}-r{m.group(3)}'
            try:
                scores[tag] = {
                    'M1': float(parts[4]), 'M2': float(parts[5]),
                    'M3': float(parts[6]), 'M4': float(parts[7]),
                    'M5': float(parts[8]), 'M6': float(parts[9]),
                    'total': float(parts[10]),
                }
            except (ValueError, IndexError):
                pass
    return scores


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    limit = 10**9
    for i, a in enumerate(sys.argv[1:], 1):
        if a == "--limit" and i < len(sys.argv) - 1:
            limit = int(sys.argv[i + 1])

    qs = args or ["Q1", "Q2", "Q3", "Q4", "Q5"]
    local_scores = _load_local_scores()
    print(f"Loaded {len(local_scores)} local scores from scoring.md")
    results = []
    for qid in qs:
        gold_path = GOLD_FILES.get(qid)
        if not gold_path or not os.path.exists(gold_path):
            print(f"[skip] {qid}: no gold file")
            continue
        gold = open(gold_path).read()
        count = 0
        for arm in ["S0", "S1", "S2", "S3", "S4", "S5"]:
            for rep in [1, 2, 3]:
                if count >= limit:
                    break
                run_path = os.path.join(RUNS_DIR, f"{arm}-{qid}-r{rep}.json")
                if not os.path.exists(run_path):
                    continue
                d = json.load(open(run_path))
                tag = f"{arm}-{qid}-r{rep}"
                print(f"[judge] {tag}... ({count+1}/{limit})", flush=True)
                try:
                    verdict = judge_m1(gold, d["output_text"])
                    local_s = local_scores.get(tag, {})
                    local_m1 = local_s.get("M1")
                    results.append({
                        "tag": tag, "arm": arm, "qid": qid, "rep": rep,
                        "local_m1": local_m1,
                        "perplexity_m1": verdict.get("m1"),
                        "claims_checked": verdict.get("claims_checked", 0),
                        "notes": verdict.get("notes", ""),
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                    })
                    print(f"  local={local_m1} perplexity={verdict.get('m1')} ({verdict.get('notes','')[:60]})")
                    count += 1
                except Exception as e:
                    print(f"  ERROR: {str(e)[:150]}")
                    results.append({"tag": tag, "arm": arm, "qid": qid, "rep": rep,
                                     "local_m1": local_scores.get(tag, {}).get("M1"),
                                     "perplexity_m1": None, "notes": str(e)[:200]})
                time.sleep(3)  # rate limit
            if count >= limit:
                break

    out_path = os.path.join(RUNS_DIR, "cross-judge-results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nDone. {len(results)} judged → {out_path}")

    valid = [r for r in results if r.get("local_m1") is not None and r.get("perplexity_m1") is not None]
    if valid:
        diffs = [abs(r["local_m1"] - r["perplexity_m1"]) for r in valid]
        avg_diff = sum(diffs) / len(diffs)
        agree = sum(1 for d in diffs if d < 0.2)
        print(f"\n一致性: {len(valid)} runs, avg|Δ|={avg_diff:.3f}, 一致(<0.2)={agree}/{len(valid)} ({100*agree/len(valid):.0f}%)")


if __name__ == "__main__":
    main()