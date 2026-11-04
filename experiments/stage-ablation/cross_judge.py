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
    "Q1": os.path.join(HERE, "gold", "Q1.md"),
    "Q2": os.path.join(HERE, "gold", "Q2.md"),
    "Q3": os.path.join(HERE, "gold", "Q3.md"),
    "Q4": os.path.join(HERE, "gold", "Q4.md"),
    "Q5": os.path.join(HERE, "gold", "Q5.md"),
}

JUDGE_PROMPT = """你是一个严格的事实核查员。请对照【标准答案】评估【模型回答】的事实准确率（M1）。

评分规则：
1. 计数单位 = 关键断言（一个完整逻辑结论/判断 = 一条）。同一结论的多个数值支撑算一条；独立的可证伪命题各算一条。典型：硬件题 5-15 条/答案；方法论题 4-10 条/答案。
2. 每条关键断言与标准答案对比：正确=1，部分正确=0.5，错误/无依据=0。
3. M1 范围 = 原始事实断言 + 可复算推导（给定前提可验证的计算链）。纯主观判断/偏好表达不计入 M1。
4. 若答案以方法论/推导为主（无外部可查事实），则评估其内部逻辑一致性与推导正确性（与 gold 结构对齐度）。仅当答案为空、拒答或完全无关时 M1=0。

输出 JSON（不要其他文字）：
{{"m1": <0-1 float>, "claims_checked": <int>, "claims_correct": <float>, "notes": "<一句话说明>"}}

【标准答案】
{gold}

【模型回答】
{answer}
"""


class QuotaExhausted(Exception):
    pass


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

// 点击主输入框（Perplexity 首页，role=textbox 即"问任何事情..."输入区）
await page.click('[role="textbox"]', {{ label: "主输入框" }});
await page.waitForTimeout(500);

// 检测免费额度耗尽（中文/英文两种文案），提前失败不空等
const quota = await page.evaluate(() => {{ const b = document.body ? document.body.innerText : ""; return b || ""; }});
if (quota.includes("免费搜索次数上限") || /free (search )?(limit|allowance)/i.test(quota)) {{
  console.log(JSON.stringify({{ text: "QUOTA_EXHAUSTED", quota: true }}));
  return;
}}

// 若输入框已有残留文本（页面复用/重定向后未清空），先全选删除
await page.keyboard.press("Meta+a");
await page.waitForTimeout(200);
await page.keyboard.press("Backspace");
await page.waitForTimeout(300);

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

// 等待响应（最多 120s）：轮询检测 "已完成" 标记，出现即停
let respText = "";
// 额度耗尽检测（要求完整句式，避免首页残留旧文案误判）
const checkQuota = async () => {{
  const b = await page.evaluate(() => document.body.innerText || "");
  return b.includes("您已达到免费搜索次数上限") || (b.includes("免费搜索次数上限") && b.includes("重置"));
}};
if (await checkQuota()) {{ console.log(JSON.stringify({{ text: "QUOTA_EXHAUSTED", quota: true }})); return; }}

for (let w = 0; w < 24; w++) {{
  await page.waitForTimeout(5000);
  const body = await page.evaluate(() => document.body.innerText || "");
  if (body.includes("您已达到免费搜索次数上限") || (body.includes("免费搜索次数上限") && body.includes("重置"))) {{ console.log(JSON.stringify({{ text: "QUOTA_EXHAUSTED", quota: true }})); return; }}
  // 回复里出现 JSON 评分标记即视为完成（"已完成"标记可能因 UI 版本不出现）
  if (/"m1"|\\"m1\\"/.test(body)) {{ respText = body; break; }}
}}
if (!respText) respText = await page.evaluate(() => document.body.innerText || "");

// 提取回复（找 "已完成" 标记后的文本）
const text = await page.evaluate((fullBody) => {{
  const idx = fullBody.lastIndexOf('已完成');
  if (idx > -1) return fullBody.slice(idx, idx + 3000);
  const lines = fullBody.split('\\n').filter(l => l.trim());
  return lines.slice(-40).join('\\n');
}}, respText);

console.log(JSON.stringify({{text: text}}));
}})();
'''
    try:
        result = subprocess.run(
            [EGO_BROWSER, "nodejs", "-e", js],
            capture_output=True, text=True, timeout=300,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError("ego-browser call timed out (300s)")
    finally:
        os.unlink(prompt_file)

    out = result.stdout + "\n" + result.stderr
    for line in reversed(out.strip().splitlines()):
        line = line.strip()
        if line.startswith("{"):
            try:
                d = json.loads(line)
                if d.get("quota"):
                    raise QuotaExhausted("Perplexity free tier exhausted")
                return d
            except json.JSONDecodeError:
                continue
    raise RuntimeError(f"Perplexity judge failed: {out[-300:]}")


def judge_m1(gold_md, answer_text):
    """调 Perplexity 做异源 M1 判定，返回 dict。带重试（瞬时失败不烧 tag）。"""
    prompt = JUDGE_PROMPT.format(gold=gold_md[:4000], answer=answer_text[:6000])
    last_err = None
    for attempt in range(3):
        try:
            raw = _run_perplexity(prompt)
        except QuotaExhausted:
            raise
        except Exception as e:
            last_err = e
            time.sleep(5 * (attempt + 1))
            continue
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
            # 回复被截断/未含 JSON → 视为瞬时失败，resume 会重跑该 tag
            return {"m1": None, "claims_checked": 0, "claims_correct": 0,
                    "notes": f"transient_error: incomplete_response: {text[:200]}"}
    return {"m1": None, "claims_checked": 0, "claims_correct": 0,
            "notes": f"transient_error_after_3_retries: {str(last_err)[:150]}"}


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

    # 断点续跑：加载已有结果，跳过已完成的 tag（perplexity_m1 非 None）
    out_path = os.path.join(RUNS_DIR, "cross-judge-results.json")
    results = []
    done_tags = set()
    if os.path.exists(out_path):
        try:
            raw_results = json.load(open(out_path))
            # 失败记录（m1=None 且 notes 含 transient/parse_failed/Command）重跑，不占位
            results = [r for r in raw_results
                       if r.get("perplexity_m1") is not None
                       or "transient" not in str(r.get("notes", ""))]
            done_tags = {r["tag"] for r in results if r.get("perplexity_m1") is not None}
            dropped = len(raw_results) - len(results)
            print(f"Resuming: {len(done_tags)} already judged, will skip; {dropped} failed entries re-queued")
        except (json.JSONDecodeError, KeyError):
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
                if tag in done_tags:
                    print(f"[skip] {tag} (already judged)", flush=True)
                    continue
                print(f"[judge] {tag}... ({count+1}/{limit})", flush=True)
                try:
                    verdict = judge_m1(gold, d["output_text"])
                    if verdict.get("quota"):
                        print("  QUOTA_EXHAUSTED — stopping (will resume next round)")
                        break
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
                except QuotaExhausted:
                    print("  QUOTA_EXHAUSTED — stopping (resumes after tier reset)")
                    break
                except Exception as e:
                    print(f"  ERROR: {str(e)[:150]}")
                    results.append({"tag": tag, "arm": arm, "qid": qid, "rep": rep,
                                     "local_m1": local_scores.get(tag, {}).get("M1"),
                                     "perplexity_m1": None, "notes": f"transient_error: {str(e)[:200]}"})
                time.sleep(3)  # rate limit
                # 增量保存（每完成一个 run 就写盘，防崩）
                with open(out_path, "w") as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)
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