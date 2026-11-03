#!/usr/bin/env python3
"""research_hook: ego-browser 真联网检索，返回来源包 JSON。

供 ablation_harness.py 的 S2+ 臂调用。
流程：ego-browser nodejs → DuckDuckGo HTML 搜索 → 提取 top-5 结果 → 返回 sources_json。
若 ego-browser 不可用 → 抛 ResearchHookUnavailable（harness 捕获后降级记录）。
"""
import json, os, subprocess, sys, tempfile, time
from datetime import datetime, timezone

EGO_BROWSER = "/Users/a1-6/.local/bin/ego-browser"


class ResearchHookUnavailable(Exception):
    pass


def _run_ego_browser(js_code, timeout=120):
    """执行 ego-browser nodejs 脚本，返回 stdout。失败抛异常。"""
    if not os.path.exists(EGO_BROWSER):
        raise ResearchHookUnavailable(f"ego-browser not found at {EGO_BROWSER}")
    # 直接内联 JS 到 -e 参数（ego-browser nodejs 只接受一个 source）
    result = subprocess.run(
        [EGO_BROWSER, "nodejs", "-e", js_code],
        capture_output=True, text=True, timeout=timeout,
    )
    if result.returncode != 0:
        raise ResearchHookUnavailable(f"ego-browser exit {result.returncode}: {result.stderr[:300]}")
    # ego-browser 可能把 console.log 输出写到 stderr（与 notice 混在一起）
    return result.stdout + "\n" + result.stderr


def _build_search_js(query, space_name):
    """构造 Bing 搜索的 JS 脚本（DuckDuckGo HTML 已失效）。"""
    from urllib.parse import quote_plus
    encoded = quote_plus(query)
    return f'''
(async () => {{
const task = await taskSpace("{space_name}");
const page = task.page("p1");
const url = "https://www.bing.com/search?q={encoded}&count=5&mkt=en-US&setlang=en";
await page.goto(url);
await page.waitForLoadState("domcontentloaded");

// Bing 结果: li.b_algo 里的 h2 a (标题+URL) + p (摘要)
// 提取 u= 参数（base64url），Python 侧解码
const results = await page.evaluate(() => {{
  const items = [];
  document.querySelectorAll("li.b_algo").forEach((el) => {{
    const a = el.querySelector("h2 a");
    const p = el.querySelector("p");
    if (a) {{
      let b64u = "";
      try {{ b64u = new URL(a.href).searchParams.get("u") || ""; }} catch(e) {{}}
      items.push({{
        title: a.textContent.trim(),
        b64u: b64u,
        raw_url: a.href,
        snippet: p ? p.textContent.trim() : ""
      }});
    }}
  }});
  return items.slice(0, 5);
}});

console.log(JSON.stringify(results));
}})();
'''


def research_hook(qid, question, max_results=5):
    """主接口：对 question 做真实网页检索，返回 sources 列表。

    返回格式: [{"title": str, "url": str, "snippet": str, "observed_at": ISO}, ...]
    失败: 抛 ResearchHookUnavailable
    """
    space_name = f"ablation-{qid}-{int(time.time())}"
    js = _build_search_js(question, space_name)
    stdout = _run_ego_browser(js, timeout=120)

    # 解析最后一条 JSON 行
    lines = [l.strip() for l in stdout.strip().splitlines() if l.strip()]
    raw = None
    for line in reversed(lines):
        if line.startswith("[") or line.startswith("{"):
            try:
                raw = json.loads(line)
                break
            except json.JSONDecodeError:
                continue
    if raw is None:
        raise ResearchHookUnavailable(f"no JSON in ego-browser output: {stdout[-200:]}")

    if isinstance(raw, dict):
        raw = [raw]

    observed = datetime.now(timezone.utc).isoformat()
    sources = []
    for item in raw[:max_results]:
        if not isinstance(item, dict):
            continue
        # 直接用 raw_url（Bing 跳转链接）—— M6 存活检查时 GET 它即可
        url = item.get("raw_url", "")
        if not url:
            continue
        sources.append({
            "title": item.get("title", ""),
            "url": url,
            "snippet": item.get("snippet", "")[:500],
            "observed_at": observed,
        })
    return sources


if __name__ == "__main__":
    # 自测: python3 research_hook.py "H100 PCIe vs SXM throughput"
    q = sys.argv[1] if len(sys.argv) > 1 else "H100 PCIe vs SXM LLM inference throughput"
    print(f"Researching: {q}")
    try:
        srcs = research_hook("Q1", q)
        print(json.dumps(srcs, indent=2, ensure_ascii=False))
        print(f"\n{len(srcs)} sources found")
    except ResearchHookUnavailable as e:
        print(f"UNAVAILABLE: {e}", file=sys.stderr)
        sys.exit(1)