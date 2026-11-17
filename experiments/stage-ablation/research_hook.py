#!/usr/bin/env python3
"""Research hooks for arXiv, GitHub REST, official docs, and community sources.

General search engines are intentionally avoided. GitHub's public REST search is
called directly; official documentation and community pages use the existing
logged-in ego-browser session. Each channel fails independently so the harness
can retain partial results or record ResearchHookUnavailable.
"""
import json, os, re, shutil, subprocess, sys, time
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus, urlencode, urlparse
from urllib.request import Request, urlopen

EGO_BROWSER = os.environ.get("EGO_BROWSER", "/Users/a1-6/.local/bin/ego-browser")


class ResearchHookUnavailable(Exception):
    pass


def _run_ego_browser(js_code, timeout=120):
    """执行 ego-browser nodejs 脚本，返回 stdout。失败抛异常。"""
    browser = EGO_BROWSER if os.path.exists(EGO_BROWSER) else shutil.which("ego-browser")
    if not browser:
        raise ResearchHookUnavailable(
            f"ego-browser not found (EGO_BROWSER={EGO_BROWSER!r}, PATH lookup failed)"
        )
    result = subprocess.run(
        [browser, "nodejs", "-e", js_code],
        capture_output=True, text=True, timeout=timeout,
    )
    if result.returncode != 0:
        raise ResearchHookUnavailable(f"ego-browser exit {result.returncode}: {result.stderr[:300]}")
    return result.stdout + "\n" + result.stderr


def _arxiv_search(query, max_results=5):
    """通过 ego-browser 访问 arXiv API，返回 [{title, url, snippet}, ...]

    v2.2: 多策略查询提升精度——
    1. 完整 query（all:）
    2. 标题限定（ti:）—— 只匹配标题含关键词的论文，大幅减少噪声
    3. 取前 N 篇去重合并
    """
    encoded_full = quote_plus(query)
    # 标题限定：提取核心词（去掉 "vs"、"LLM inference throughput" 这类通用后缀）
    core_words = re.findall(r'[A-Za-z0-9]{3,}', query)
    # 过滤掉太通用的词
    STOP = {'the', 'and', 'for', 'with', 'from', 'this', 'that', 'what', 'how',
            'llm', 'inference', 'throughput', 'performance', 'benchmark', 'gpu'}
    specific = [w for w in core_words if w.lower() not in STOP]
    ti_query = ' AND '.join(f'ti:{w}' for w in specific[:4]) if specific else f'ti:{core_words[0]}'
    encoded_ti = quote_plus(ti_query)

    space_name = f"arxiv-{int(time.time())}"
    js = (
        "(async () => {\n"
        f'const task = await taskSpace("{space_name}");\n'
        'const page = task.page("p1");\n'
        # 第一路：完整 query
        f'await page.goto("http://export.arxiv.org/api/query?search_query=all:{encoded_full}&start=0&max_results={max_results}&sortBy=relevance", {{waitUntil: "domcontentloaded"}});\n'
        'await new Promise(r => setTimeout(r, 3000));\n'
        'let xml1 = await page.evaluate(() => document.body.innerText);\n'
        'console.log("===FULL===" + xml1);\n'
        # 第二路：标题限定
        f'await page.goto("http://export.arxiv.org/api/query?search_query={encoded_ti}&start=0&max_results={max_results}&sortBy=relevance", {{waitUntil: "domcontentloaded"}});\n'
        'await new Promise(r => setTimeout(r, 3000));\n'
        'let xml2 = await page.evaluate(() => document.body.innerText);\n'
        'console.log("===TITLE===" + xml2);\n'
        '})();'
    )
    stdout = _run_ego_browser(js, timeout=90)

    def parse_entries(xml_block):
        entries = []
        for match in re.finditer(r'<entry>(.*?)</entry>', xml_block, re.DOTALL):
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
        return entries

    # 解析两路结果
    full_block = stdout.split("===FULL===")[1].split("===TITLE===")[0] if "===FULL===" in stdout else ""
    title_block = stdout.split("===TITLE===")[1] if "===TITLE===" in stdout else ""
    full_entries = parse_entries(full_block)
    title_entries = parse_entries(title_block)

    # 合并去重（标题限定优先——更精准）
    seen_urls = set()
    merged = []
    for e in title_entries + full_entries:
        if e["url"] not in seen_urls:
            seen_urls.add(e["url"])
            merged.append(e)
    return merged[:max_results]


def _search_limit(max_results):
    """Normalize public search limits and avoid unexpectedly large API/browser runs."""
    try:
        limit = int(max_results)
    except (TypeError, ValueError):
        raise ValueError("max_results must be an integer")
    if limit < 1:
        raise ValueError("max_results must be at least 1")
    return min(limit, 25)


def _round_robin_results(result_groups, max_results):
    """Combine source groups fairly, preserving order within each group."""
    limit = _search_limit(max_results)
    groups = [list(group or []) for group in result_groups]
    merged, seen = [], set()
    for index in range(max((len(group) for group in groups), default=0)):
        for group in groups:
            if index >= len(group):
                continue
            result = group[index]
            url = result.get("url", "")
            key = url or json.dumps(result, sort_keys=True, ensure_ascii=False)
            if key in seen:
                continue
            seen.add(key)
            merged.append(result)
            if len(merged) >= limit:
                return merged
    return merged


def _github_search(query, max_results=5):
    """Search GitHub repositories, issues, and pull requests with the REST API.

    Uses GITHUB_TOKEN or GH_TOKEN when available; anonymous public search is used
    otherwise (with GitHub's lower unauthenticated rate limit). Code search is
    attempted only when authenticated because GitHub requires authentication for
    that endpoint. Results use research_hook's {title, url, snippet} shape.
    """
    limit = _search_limit(max_results)
    query = str(query or "").strip()
    if not query:
        raise ValueError("query must not be empty")

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "prompt-first-bench-research-hook/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    searches = [
        ("repository", "repositories", query),
        ("issue", "issues", f"{query} is:issue"),
        ("pull_request", "issues", f"{query} is:pr"),
    ]
    if token:
        searches.append(("code", "code", query))

    groups, errors = [], []
    for kind, endpoint, search_query in searches:
        # Leave GitHub's default best-match ranking enabled; sorting by update time
        # can push unrelated recent issues ahead of query-relevant results.
        params = urlencode({"q": search_query, "per_page": limit})
        url = f"https://api.github.com/search/{endpoint}?{params}"
        request = Request(url, headers=headers)
        try:
            with urlopen(request, timeout=20) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            # Keep partial results; one restricted endpoint (especially code search)
            # should not block repositories/issues/PRs.
            errors.append(f"{kind}: HTTP {exc.code}")
            continue
        except (URLError, TimeoutError, OSError, ValueError) as exc:
            errors.append(f"{kind}: {type(exc).__name__}")
            continue

        items = []
        for item in payload.get("items", []):
            if kind == "repository":
                title = item.get("full_name") or item.get("name") or "GitHub repository"
                snippet = item.get("description") or ""
                result_url = item.get("html_url", "")
            elif kind == "code":
                repo = (item.get("repository") or {}).get("full_name", "")
                title = f"{repo}/{item.get('path', item.get('name', 'code result'))}".strip("/")
                snippet = item.get("text_matches", [{}])[0].get("fragment", "") if item.get("text_matches") else ""
                result_url = item.get("html_url", "")
            else:
                title = item.get("title") or "GitHub issue"
                snippet = re.sub(r"\s+", " ", item.get("body") or "").strip()[:500]
                result_url = item.get("html_url", "")
            if not result_url:
                continue
            items.append({
                "title": re.sub(r"\s+", " ", title).strip()[:240],
                "url": result_url,
                "snippet": snippet[:500],
                "source_type": f"github_{kind}",
                "source": "GitHub REST API",
                "updated_at": item.get("updated_at"),
            })
        groups.append(items)

    results = _round_robin_results(groups, limit)
    if not results:
        detail = "; ".join(errors) if errors else "all search endpoints returned no matches"
        raise ResearchHookUnavailable(f"GitHub search unavailable: {detail}")
    return results


def _ego_browser_search(query, max_results=5):
    """Search Stack Overflow, Reddit, and Hacker News through ego-browser.

    The browser uses its existing logged-in session. Network/UI failures are
    isolated per site; useful results from another site are still returned.
    """
    limit = _search_limit(max_results)
    query = str(query or "").strip()
    if not query:
        raise ValueError("query must not be empty")
    encoded = quote_plus(query)
    targets = [
        {"site": "stackoverflow", "url": f"https://stackoverflow.com/search?q={encoded}"},
        {"site": "reddit", "url": f"https://www.reddit.com/search/?q={encoded}&type=link"},
        {"site": "hackernews", "url": f"https://hn.algolia.com/api/v1/search?query={encoded}&tags=story&hitsPerPage={limit}"},
    ]
    js = (
        "(async () => {\n"
        f"const targets = {json.dumps(targets)};\n"
        f"const task = await taskSpace(\"community-search-{int(time.time()*1000)}\");\n"
        "const page = task.page(\"p1\");\n"
        "const output = [];\n"
        "for (const target of targets) {\n"
        "  try {\n"
        "    await page.goto(target.url, {waitUntil: 'domcontentloaded', timeout: 20000});\n"
        "    await new Promise(r => setTimeout(r, 1200));\n"
        "    if (target.site === 'hackernews') {\n"
        "      const raw = await page.evaluate(() => document.body.innerText);\n"
        "      const data = JSON.parse(raw);\n"
        "      output.push({site: target.site, items: (data.hits || []).map(h => ({\n"
        "        title: h.title || h.story_title || h.comment_text || 'Hacker News result',\n"
        "        url: h.url || ('https://news.ycombinator.com/item?id=' + h.objectID),\n"
        "        snippet: h.story_text || h.comment_text || h.title || ''\n"
        "      }))});\n"
        "    } else {\n"
        "      const items = await page.evaluate(() => {\n"
        "        const host = location.hostname;\n"
        "        const links = [...document.querySelectorAll('a[href]')];\n"
        "        return links.map(a => {\n"
        "          const href = new URL(a.getAttribute('href'), location.href).href;\n"
        "          const title = (a.innerText || a.textContent || '').trim().replace(/\\s+/g, ' ');\n"
        "          const card = a.closest('.s-post-summary') || a.closest('article') || a.closest('[data-testid]') || a.parentElement;\n"
        "          const snippet = (card && card.innerText || '').trim().replace(/\\s+/g, ' ');\n"
        "          return {title, url: href, snippet};\n"
        "        }).filter(x => x.title.length > 5 && (\n"
        "          (host.includes('stackoverflow.com') && /\\/questions\\//.test(x.url)) ||\n"
        "          (host.includes('reddit.com') && /\\/comments\\//.test(x.url))\n"
        "        )).slice(0, 20);\n"
        "      });\n"
        "      output.push({site: target.site, items});\n"
        "    }\n"
        "  } catch (e) { output.push({site: target.site, error: String(e.message || e)}); }\n"
        "}\n"
        "console.log('__EGO_RESULTS__' + JSON.stringify(output));\n"
        "})().catch(e => console.log('__EGO_RESULTS__' + JSON.stringify({error: String(e.message || e)})));"
    )
    stdout = _run_ego_browser(js, timeout=100)
    marker = "__EGO_RESULTS__"
    if marker not in stdout:
        raise ResearchHookUnavailable("ego-browser returned no result payload")
    try:
        payload = json.loads(stdout.rsplit(marker, 1)[1].strip().splitlines()[0])
    except (IndexError, ValueError) as exc:
        raise ResearchHookUnavailable(f"could not parse ego-browser results: {exc}")
    if isinstance(payload, dict):
        payload = []

    groups = []
    for site_result in payload:
        site = site_result.get("site", "community")
        group = []
        for item in site_result.get("items", []):
            if not item.get("url") or not item.get("title"):
                continue
            group.append({
                "title": re.sub(r"\s+", " ", item["title"]).strip()[:240],
                "url": item["url"],
                "snippet": re.sub(r"\s+", " ", item.get("snippet", "")).strip()[:500],
                "source_type": f"ego_browser_{site}",
                "source": site,
            })
        groups.append(group)
    results = _round_robin_results(groups, limit)
    if not results:
        errors = [x.get("error") for x in payload if x.get("error")]
        detail = "; ".join(errors) if errors else "all community searches returned no results"
        raise ResearchHookUnavailable(f"ego-browser search unavailable: {detail}")
    return results


def _official_docs_search(query, max_results=5):
    """Visit official documentation search pages and extract documentation links.

    Searches PyTorch, TensorFlow, and Hugging Face docs directly through the
    existing ego-browser session; it does not rely on a general search engine.
    """
    limit = _search_limit(max_results)
    query = str(query or "").strip()
    if not query:
        raise ValueError("query must not be empty")
    encoded = quote_plus(query)
    targets = [
        {"site": "pytorch", "url": f"https://pytorch.org/docs/stable/search.html?q={encoded}"},
        {"site": "tensorflow", "url": f"https://www.tensorflow.org/s/results?q={encoded}"},
        {"site": "huggingface", "url": f"https://huggingface.co/docs/transformers/main/en/search?query={encoded}"},
    ]
    js = (
        "(async () => {\n"
        f"const targets = {json.dumps(targets)};\n"
        f"const task = await taskSpace(\"official-docs-{int(time.time()*1000)}\");\n"
        "const page = task.page(\"p1\");\n"
        "const output = [];\n"
        "for (const target of targets) {\n"
        "  try {\n"
        "    await page.goto(target.url, {waitUntil: 'domcontentloaded', timeout: 20000});\n"
        "    await new Promise(r => setTimeout(r, 1000));\n"
        "    const data = await page.evaluate(() => {\n"
        "      const title = document.title || '';\n"
        "      const links = [...document.querySelectorAll('a[href]')].map(a => {\n"
        "        const url = new URL(a.getAttribute('href'), location.href).href;\n"
        "        const text = (a.innerText || a.textContent || '').trim().replace(/\\s+/g, ' ');\n"
        "        const card = a.closest('li') || a.closest('article') || a.closest('[class*=result]') || a.parentElement;\n"
        "        const snippet = (card && card.innerText || '').trim().replace(/\\s+/g, ' ');\n"
        "        return {title: text, url, snippet};\n"
        "      }).filter(x => x.title.length > 5 && (\n"
        "        /(^|\\.)pytorch\\.org$/.test(new URL(x.url).hostname) ||\n"
        "        /(^|\\.)tensorflow\\.org$/.test(new URL(x.url).hostname) ||\n"
        "        /(^|\\.)huggingface\\.co$/.test(new URL(x.url).hostname)\n"
        "      ));\n"
        "      return {pageTitle: title, pageUrl: location.href, body: document.body.innerText.slice(0, 500), links};\n"
        "    });\n"
        "    output.push({site: target.site, ...data});\n"
        "  } catch (e) { output.push({site: target.site, error: String(e.message || e)}); }\n"
        "}\n"
        "console.log('__OFFICIAL_DOCS__' + JSON.stringify(output));\n"
        "})().catch(e => console.log('__OFFICIAL_DOCS__' + JSON.stringify({error: String(e.message || e)})));"
    )
    stdout = _run_ego_browser(js, timeout=100)
    marker = "__OFFICIAL_DOCS__"
    if marker not in stdout:
        raise ResearchHookUnavailable("ego-browser returned no official-docs payload")
    try:
        payload = json.loads(stdout.rsplit(marker, 1)[1].strip().splitlines()[0])
    except (IndexError, ValueError) as exc:
        raise ResearchHookUnavailable(f"could not parse official-docs results: {exc}")
    if isinstance(payload, dict):
        payload = []

    terms = [term.lower() for term in re.findall(r"[A-Za-z0-9_+-]{2,}", query)]
    groups = []
    for site_result in payload:
        site = site_result.get("site", "official_docs")
        group = []
        for item in site_result.get("links", []):
            parsed = urlparse(item.get("url", ""))
            host = parsed.hostname or ""
            if not any(host == domain or host.endswith("." + domain) for domain in ("pytorch.org", "tensorflow.org", "huggingface.co")):
                continue
            title = re.sub(r"\s+", " ", item.get("title", "")).strip()
            if not title:
                continue
            snippet = re.sub(r"\s+", " ", item.get("snippet", "")).strip()[:500]
            text = f"{title} {snippet}".lower()
            relevance = sum(1 for term in terms if term in text)
            group.append({
                "title": title[:240], "url": item["url"], "snippet": snippet,
                "source_type": f"official_docs_{site}", "source": site,
                "relevance": relevance,
            })
        group.sort(key=lambda item: item.get("relevance", 0), reverse=True)
        for item in group:
            item.pop("relevance", None)
        groups.append(group)
    results = _round_robin_results(groups, limit)
    if not results:
        errors = [x.get("error") for x in payload if x.get("error")]
        detail = "; ".join(errors) if errors else "no official documentation result links found"
        raise ResearchHookUnavailable(f"official docs search unavailable: {detail}")
    return results


# 已知站点（T17 通用化域）—— 按 Q 映射 (T30-fix: 修正 Q2/Q4 错误指向)
KNOWN_SITES = {
    "Q1": [  # H100 PCIe vs SXM inference
        ("https://www.nvidia.com/en-us/data-center/h100/", "NVIDIA H100 Official"),
        ("https://www.thundercompute.com/blog/nvidia-h100-specs-full-guide", "ThunderCompute H100 Specs"),
        ("https://cloudgputracker.com/compare/nvidia-h100-vs-nvidia-h100-pcie/", "CloudGPUTracker H100 Compare"),
    ],
    "Q2": [  # LLM model selection (Qwen/Mistral/GLM/DeepSeek/Llama)
        ("https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard", "HF Open LLM Leaderboard"),
        ("https://artificialanalysis.ai/models", "Artificial Analysis Model Rankings"),
    ],
    "Q3": [  # Inference serving frameworks (vLLM/TGI/SGLang)
        ("https://docs.vllm.ai/en/latest/getting_started/installation/index.html", "vLLM Documentation"),
        ("https://github.com/sgl-project/sglang", "SGLang GitHub"),
        ("https://huggingface.co/docs/text-generation-inference/index", "TGI Documentation"),
    ],
    "Q4": [  # RAG vs long context window
        ("https://arxiv.org/abs/2307.03172", "Lost in the Middle (arXiv)"),
        ("https://arxiv.org/abs/2312.10997", "RAG vs Long Context Survey (arXiv)"),
    ],
    "Q5": [  # Bayesian vs frequentist decision theory
        ("https://arxiv.org/abs/2305.06980", "LLM Training Efficiency (arXiv)"),
        ("https://en.wikipedia.org/wiki/Bayesian_inference", "Bayesian Inference (Wikipedia)"),
    ],
}

# arXiv 精准查询（T30: 每 Q 多路 query，取并集提升召回）
ARXIV_QUERIES = {
    "Q1": ["H100 PCIe SXM inference throughput benchmark", "GPU memory bandwidth LLM serving"],
    "Q2": ["Qwen2.5-Coder HumanEval code generation benchmark", "LLM model selection cost accuracy tradeoff open source"],
    "Q3": ["vLLM TGI SGLang inference serving comparison throughput", "LLM inference engine PagedAttention continuous batching"],
    "Q4": ["retrieval augmented generation vs long context window comparison", "RAG faithfulness evaluation lost in the middle"],
    "Q5": ["Bayesian decision theory expected loss minimization frequentist", "statistical hypothesis testing decision rules risk"],
}

# T31: 来源过滤关键词（只注入 title/snippet 含这些词的结果）
FILTER_KEYWORDS = {
    "Q1": ["PCIe", "SXM", "throughput", "bandwidth", "NVLink", "memory bus"],
    "Q2": ["Qwen", "Mistral", "GLM", "DeepSeek", "Llama", "HumanEval", "code generation", "model selection", "cost"],
    "Q3": ["vLLM", "TGI", "SGLang", "serving", "inference engine", "PagedAttention", "throughput", "latency"],
    "Q4": ["retrieval", "RAG", "context window", "long context", "faithfulness", "Lost in the Middle"],
    "Q5": ["Bayesian", "frequentist", "hypothesis testing", "decision theory", "expected loss", "risk"],
}


def filter_sources(sources, qid):
    """T31: 只保留 title+snippet 含 FILTER_KEYWORDS[qid] 中至少一个词的来源。"""
    kws = FILTER_KEYWORDS.get(qid, [])
    if not kws:
        return sources  # 无关键词定义 → 不过滤
    passed = []
    for s in sources:
        text = (s.get('title', '') + ' ' + s.get('snippet', '')).lower()
        if any(kw.lower() in text for kw in kws):
            passed.append(s)
    return passed


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
    """主检索接口：汇总 arXiv、GitHub、官方文档、社区和已知站点。

    每个通道独立失败、互不阻塞；按通道轮询合并，避免 arXiv 或某个站点
    占满 max_results。返回统一的 {title, url, snippet, observed_at, source_type}。
    """
    limit = _search_limit(max_results)
    observed = datetime.now(timezone.utc).isoformat()
    groups = {"arxiv": [], "github": [], "official": [], "community": [], "direct": []}

    # 1. arXiv API：多查询去重合并，保留原有权威文献检索。
    queries = ARXIV_QUERIES.get(qid, [question])
    seen_arxiv = set()
    for search_query in queries:
        if len(groups["arxiv"]) >= limit:
            break
        try:
            for result in _arxiv_search(search_query, max_results=limit):
                if result.get("url") and result["url"] not in seen_arxiv:
                    seen_arxiv.add(result["url"])
                    groups["arxiv"].append({
                        **result, "observed_at": observed, "source_type": "arxiv"
                    })
                    if len(groups["arxiv"]) >= limit:
                        break
        except ResearchHookUnavailable:
            continue

    # 2. GitHub REST API：公共搜索无需 token；若 token 存在则也尝试 code search。
    try:
        groups["github"] = [
            {**result, "observed_at": observed}
            for result in _github_search(question, max_results=limit)
        ]
    except ResearchHookUnavailable:
        pass

    # 3. 官方文档直访与 4. 社区浏览器搜索；环境缺少浏览器时分别降级。
    try:
        groups["official"] = [
            {**result, "observed_at": observed}
            for result in _official_docs_search(question, max_results=limit)
        ]
    except ResearchHookUnavailable:
        pass
    try:
        groups["community"] = [
            {**result, "observed_at": observed}
            for result in _ego_browser_search(question, max_results=limit)
        ]
    except ResearchHookUnavailable:
        pass

    # 5. 原有 QID 对应站点保持兼容。
    for url, title_hint in KNOWN_SITES.get(qid, []):
        try:
            page_info = _fetch_page(url, title_hint)
        except Exception:
            continue
        if page_info.get("alive"):
            groups["direct"].append({
                **page_info, "observed_at": observed, "source_type": "direct_site"
            })

    sources = _round_robin_results(
        [groups[name] for name in ("arxiv", "github", "official", "community", "direct")],
        limit,
    )
    if not sources:
        raise ResearchHookUnavailable(
            "no sources from any channel (arXiv, GitHub API, official docs, ego-browser, direct sites)"
        )
    return sources


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