#!/usr/bin/env python3
"""cross_judge.py: 异源 judge 复核 M1（事实准确率）。

用 ego-browser 调 Gemini (gemini.google.com) 做独立 judge，
对比本地 27b 自判的 M1 分数，计算一致性。

用法:
  python3 cross_judge.py            # 对所有 runs 跑异源 judge
  python3 cross_judge.py Q1 Q2      # 只跑指定题
"""
import json, os, subprocess, sys, tempfile, time, re
from datetime import datetime, timezone

EGO_BROWSER = "/Users/a1-6/.local/bin/ego-browser"
HERE = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(HERE, "runs")
WORKSPACE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
# gold 文件路径（与 ablation_harness.QUESTIONS 一致）
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


def _run_gemini(prompt_text):
    """通过 ego-browser 调 Gemini，返回 stdout+stderr。"""
    js = f'''
(async () => {{
const task = await taskSpace("cross-judge-{int(time.time())}");
const page = task.page("p1");
await page.goto("https://gemini.google.com/app");
await page.waitForLoadState("networkidle");
await page.waitForTimeout(3000);

// 找到输入框并填入 prompt
const input = page.locator('textarea[aria-label="Send a message"], div.ql-editor, textarea').first();
await input.click();
await page.keyboard.type({json.dumps(prompt_text[:8000])}, {{delay: 0}});
await page.keyboard.press("Enter");

// 等待响应（最多 60s）
await page.waitForTimeout(60000);

// 提取最后一段 AI 回复文本
const text = await page.evaluate(() => {{
  const responses = document.querySelectorAll('div.response-container, div.model-response, [data-test-id="response"]');
  if (responses.length > 0) return responses[responses.length - 1].textContent;
  // fallback: 取页面底部大段文本
  const all = document.body.innerText;
  const lines = all.split('\\n').filter(l => l.trim());
  return lines.slice(-20).join('\\n');
}});

console.log(JSON.stringify({{text: text}}));
}})();
'''
    result = subprocess.run(
        [EGO_BROWSER, "nodejs", "-e", js],
        capture_output=True, text=True, timeout=120,
    )
    out = result.stdout + "\n" + result.stderr
    # 提取 JSON
    for line in reversed(out.strip().splitlines()):
        line = line.strip()
        if line.startswith("{"):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                continue
    raise RuntimeError(f"Gemini judge failed: {out[-200:]}")


def judge_m1(gold_md, answer_text):
    """调 Gemini 做异源 M1 判定，返回 dict。"""
    prompt = JUDGE_PROMPT.format(gold=gold_md[:4000], answer=answer_text[:6000])
    raw = _run_gemini(prompt)
    text = raw.get("text", "")
    # 从 Gemini 回复里提取 JSON
    match = re.search(r'\{[^{}]*"m1"[^{}]*\}', text)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass
    # fallback: 尝试解析整个文本
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"m1": None, "claims_checked": 0, "claims_correct": 0,
                "notes": f"parse_failed: {text[:200]}"}


def main():
    qs = sys.argv[1:] or ["Q1", "Q2", "Q3", "Q4", "Q5"]
    results = []
    for qid in qs:
        gold_path = GOLD_FILES.get(qid)
        if not gold_path or not os.path.exists(gold_path):
            print(f"[skip] {qid}: no gold file")
            continue
        gold = open(gold_path).read()
        for arm in ["S0", "S1", "S2", "S3", "S4", "S5"]:
            for rep in [1, 2]:
                run_path = os.path.join(RUNS_DIR, f"{arm}-{qid}-r{rep}.json")
                if not os.path.exists(run_path):
                    continue
                d = json.load(open(run_path))
                tag = f"{arm}-{qid}-r{rep}"
                print(f"[judge] {tag}...", flush=True)
                try:
                    verdict = judge_m1(gold, d["output_text"])
                    local_m1 = d.get("scores", {}).get("M1")
                    results.append({
                        "tag": tag, "arm": arm, "qid": qid, "rep": rep,
                        "local_m1": local_m1,
                        "gemini_m1": verdict.get("m1"),
                        "claims_checked": verdict.get("claims_checked", 0),
                        "notes": verdict.get("notes", ""),
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                    })
                    print(f"  local={local_m1} gemini={verdict.get('m1')} ({verdict.get('notes','')[:60]})")
                except Exception as e:
                    print(f"  ERROR: {e}")
                    results.append({"tag": tag, "arm": arm, "qid": qid, "rep": rep,
                                     "local_m1": d.get("scores", {}).get("M1"),
                                     "gemini_m1": None, "notes": str(e)[:200]})
                time.sleep(2)  # rate limit

    out_path = os.path.join(RUNS_DIR, "cross-judge-results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nDone. {len(results)} judged → {out_path}")

    # 一致性统计
    valid = [r for r in results if r.get("local_m1") is not None and r.get("gemini_m1") is not None]
    if valid:
        diffs = [abs(r["local_m1"] - r["gemini_m1"]) for r in valid]
        avg_diff = sum(diffs) / len(diffs)
        agree = sum(1 for d in diffs if d < 0.2)
        print(f"\n一致性: {len(valid)} runs, avg|Δ|={avg_diff:.3f}, 一致(<0.2)={agree}/{len(valid)} ({100*agree/len(valid):.0f}%)")


if __name__ == "__main__":
    main()