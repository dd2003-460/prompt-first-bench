#!/usr/bin/env python3
"""research_hook v2: arXiv API + 已知站点直访（不依赖搜索引擎）。

背景：Bing/DDG/Startpage 在 ego-browser 环境下全部不可用（垃圾结果/空/验证墙），
但直接访问 arxiv.org、nvidia.com 等站点正常。v2 改为：
1. arXiv API 检索（学术文献）
2. 已知站点直访（厂商规格页/benchmark 站）
3. 返回 sources_json 供 harness S2+ 臂使用

若 ego-browser 不可用 → 抛 ResearchHookUnavailable（harness 捕获后降级记录）。
"""
import json, os, re, subprocess, sys, time
from datetime import datetime, timezone
from urllib.parse import quote_plus

EGO_BROWSER = "/Users/a1-6/.local/bin/ego-browser"


class ResearchHookUnavailable(Exception):
    pass


def _run_ego_browser(js_code, timeout=120):
    """执行 ego-browser nodejs 脚本，返回 stdout。失败抛异常。"""
    if not os.path.exists(EGO_BROWSER):
        raise ResearchHookUnavailable(f"ego-browser not found at {EGO_BROWSER}")
    result = subprocess.run(
        [EGO_BROWSER, "nodejs", "-e", js_code],
        capture_output=True, text=True, timeout=timeout,
    )
    if result.returncode != 0:
        raise ResearchHookUnavailable(f"ego-browser exit {result.returncode}: {result.stderr[:300]}")
    return result.stdout + "\n" + result.stderr


def _arxiv_search(query, max_results=5):
    """通过 ego-browser 访问 arXiv API，返回 [{title, url, snippet}, ...]"""
    # 用完整 query（URL-encode），sortBy=relevance
    encoded = quote_plus(query)
    space_name = f"arxiv-{int(time.time())}"
    js = (
        "(async () => {\n"
        f'const task = await taskSpace("{space_name}");\n'
        'const page = task.page("p1");\n'
        f'await page.goto("http://export.arxiv.org/api/query?search_query=all:{encoded}&start=0&max_results={max_results}&sortBy=relevance", {{waitUntil: "domcontentloaded"}});\n'
        'await new Promise(r => setTimeout(r, 3000));\n'
        'const xml = await page.evaluate(() => document.body.innerText);\n'
        'console.log(xml);\n'
        '})();'
    )
    stdout = _run_ego_browser(js, timeout=60)
    # 解析 Atom XML（简单正则提取 entry）
    entries = []
    for match in re.finditer(r'<entry>(.*?)</entry>', stdout, re.DOTALL):
        block = match.group(1)
        title_m = re.search(r'<title>(.*?)</title>', block, re.DOTALL)
        link_m = re.search(r'<id>(.*?)</id>', block)
        summary_m = re.search(r'<summary>(.*?)</summary>', block, re.DOTALL)
        if title_m and link_m:
            entries.append({
                "title": re.sub(r'\s+', ' ', title_m.group(1)).strip()[:200],
                "url": link_m.group(1).strip(),
                "snippet": re.sub(r'\s+', ' ', summary_m.group(1)).strip()[:500] if summary_m else "",
            })
    return entries[:max_results]


# 已知站点（GPU 调研域）—— 按 Q 映射
KNOWN_SITES = {
    "Q1": [  # H100 PCIe vs SXM
        ("https://www.nvidia.com/en-us/data-center/h100/", "NVIDIA H100 Official"),
        ("https://www.thundercompute.com/blog/nvidia-h100-specs-full-guide", "ThunderCompute H100 Specs"),
        ("https://cloudgputracker.com/compare/nvidia-h100-vs-nvidia-h100-pcie/", "CloudGPUTracker H100 Compare"),
        ("https://www.runpod.io/guides/nvidia-h100-gpu", "RunPod H100 Guide"),
    ],
    "Q2": [  # A100 specs
        ("https://www.nvidia.com/en-us/data-center/a100/", "NVIDIA A100 Official"),
        ("https://www.thundercompute.com/blog/nvidia-a100-specs", "ThunderCompute A100 Specs"),
    ],
    "Q3": [  # LLM inference cost
        ("https://www.together.ai/pricing", "Together AI Pricing"),
        ("https://replicate.com/pricing", "Replicate Pricing"),
        ("https://cloudgputracker.com/", "CloudGPUTracker"),
    ],
    "Q4": [  # GPU cluster networking
        ("https://www.nvidia.com/en-us/networking/infiniband/", "NVIDIA InfiniBand"),
        ("https://www.mellanox.com/products/infinibad-networking", "Mellanox Networking"),
    ],
    "Q5": [  # Training vs inference workload
        ("https://arxiv.org/abs/2305.06980", "LLM Training Efficiency (arXiv)"),
        ("https://arxiv.org/abs/2211.05102", "Efficient LLM Inference (arXiv)"),
    ],
}


def _fetch_page(url, title_hint, timeout=30):
    """直接访问 URL，确认存活并提取标题。"""
    space_name = f"fetch-{int(time.time()*1000)}"
    js = (
        "(async () => {\n"
        f"const task = await taskSpace(\"{space_name}\");\n"
        "const page = task.page(\"p1\");\n"
        "try {\n"
        f"  await page.goto(\"{url}\", {{waitUntil: \"domcontentloaded\", timeout: 20000}});\n"
        "  await new Promise(r => setTimeout(r, 2000));\n"
        "  const info = await page.evaluate(() => ({\n"
        "    title: document.title,\n"
        "    bodyLen: document.body.innerText.length,\n"
        "    sample: document.body.innerText.slice(0, 300)\n"
        "  }));\n"
        "  console.log(JSON.stringify(info));\n"
        "} catch(e) {\n"
        "  console.log(JSON.stringify({error: e.message}));\n"
        "}\n"
        "})();"
    )
    try:
        stdout = _run_ego_browser(js, timeout=timeout)
        lines = [l.strip() for l in stdout.strip().splitlines() if l.strip().startswith("{")]
        if lines:
            data = json.loads(lines[-1])
            if "error" not in data and data.get("bodyLen", 0) > 100:
                return {"title": data.get("title", title_hint), "url": url,
                        "snippet": data.get("sample", "")[:300], "alive": True}
    except Exception:
        pass
    return {"title": title_hint, "url": url, "snippet": "", "alive": False}


def research_hook(qid, question, max_results=5):
    """主接口：arXiv API + 已知站点直访，返回 sources 列表。

    返回格式: [{"title": str, "url": str, "snippet": str, "observed_at": ISO, "source_type": str}, ...]
    失败: 抛 ResearchHookUnavailable
    """
    observed = datetime.now(timezone.utc).isoformat()
    sources = []

    # 1. arXiv API 检索
    try:
        arxiv_results = _arxiv_search(question, max_results=max_results)
        for r in arxiv_results:
            sources.append({**r, "observed_at": observed, "source_type": "arxiv"})
    except ResearchHookUnavailable:
        pass  # arXiv 失败不阻塞，继续已知站点

    # 2. 已知站点直访
    sites = KNOWN_SITES.get(qid, [])
    for url, title_hint in sites:
        if len(sources) >= max_results:
            break
        page_info = _fetch_page(url, title_hint)
        if page_info["alive"]:
            page_info["observed_at"] = observed
            page_info["source_type"] = "direct_site"
            sources.append(page_info)

    if not sources:
        raise ResearchHookUnavailable("no sources from any channel (arXiv + direct sites all failed)")

    return sources[:max_results]


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else "H100 PCIe vs SXM LLM inference throughput"
    qid = sys.argv[2] if len(sys.argv) > 2 else "Q1"
    print(f"Researching ({qid}): {q}")
    try:
        srcs = research_hook(qid, q)
        print(json.dumps(srcs, indent=2, ensure_ascii=False))
        print(f"\n{len(srcs)} sources found")
    except ResearchHookUnavailable as e:
        print(f"UNAVAILABLE: {e}", file=sys.stderr)