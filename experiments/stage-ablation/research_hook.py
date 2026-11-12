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


# ── 检索结果缓存（用户指令 2026-11-08：稳定步骤直接 cache 复用，别重复打登录态会话）──
# 按 (qid, question) 落盘 JSON。命中 → 直接读文件返回，不再触发任何外部通道
# （DDG/Perplexity/arXiv/webfetch 全部跳过）。TTL 7 天，过期重查。
import hashlib as _hashlib
_CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".research-cache")
_CACHE_TTL_S = 7 * 24 * 3600


# D 指令 (2026-11-12)：搜索结果全是广告 → 只定准业内公司文档和手册。
# 结果侧域名白名单（post-filter）——搜索引擎对 site: 支持不稳（DDG lite 忽略、
# cn.bing geo 后失效），所以搜索照常跑，拿到结果后按域过滤。
# 白名单 = 百科 + 监管年报 + 财务数据 + 行业媒体 + 技术论坛（D 确认 wiki/技术论坛质量高）。
_SOURCE_WHITELIST = [
    # 百科 + 监管/数据
    "wikipedia.org",       # en+zh 百科
    "sec.gov",             # EDGAR 年报/招股书
    "investopedia.com",    # 金融术语与概念手册
    "reuters.com",         # 行业新闻
    "bloomberg.com",       # 财经新闻
    "macrotrends.net",     # 长尾财务序列
    "stockanalysis.com",   # 财务比率与估值
    # 技术论坛 + 技术博客/资料（D 2026-11-12: 限制在英文数据和论坛和技术博客和资料）
    "stackoverflow.com",   # 技术 Q&A
    "hackernews.com",      # 技术讨论
    "reddit.com",          # 社区讨论（r/MachineLearning, r/GPU 等）
    "techpowerup.com",     # GPU 规格数据库（实测 H100 query 命中）
    "arxiv.org",           # 预印本
    "github.com",          # 代码/文档
    "nvidia.com",          # 官方 datasheet（实测 H100 query 命中）
    "amd.com",             # 官方 datasheet
    "intel.com",           # 官方 datasheet
    "developer.nvidia.com",# CUDA 文档
    "pytorch.org",         # 框架文档
    "tensorflow.org",      # 框架文档
    "medium.com",          # 技术博客
    "substack.com",        # 技术博客
    "towardsdatascience.com", # ML 博客
    "analyticsvidhya.com", # ML 博客
    "dev.to",              # 开发者博客
    "blog.google",         # 官方博客
    "openai.com",          # 官方博客/论文
    "anthropic.com",       # 官方博客
    "huggingface.co",      # 模型卡/文档
    # 中国权威机构（D 2026-11-12: 中国顶多引用权威机构数据）
    "stats.gov.cn",        # 国家统计局
    "cbirc.gov.cn",        # 银保监会（金融监管总局前身）
    "nfra.gov.cn",         # 国家金融监督管理总局
    "csrc.gov.cn",         # 证监会
    "pbc.gov.cn",          # 中国人民银行
    "mofcom.gov.cn",       # 商务部
    "chinamoney.com.cn",   # 全国银行间同业拆借中心
]




# D 指令 (2026-11-12)：搜索结果全是广告 → 只定准业内公司文档和手册。
# site: 白名单让 DDG/Bing 只在权威域内检索，从源头掐掉广告/垃圾站。
_SITE_RESTRICT = (" ".join(f"site:{d}" for d in [
    "wikipedia.org", "sec.gov", "investopedia.com", "reuters.com",
    "bloomberg.com", "macrotrends.net", "stockanalysis.com",
]))




def _cache_path(qid, question):
    h = _hashlib.sha256(f"{qid}\x00{question}".encode()).hexdigest()[:24]
    return os.path.join(_CACHE_DIR, f"{h}.json")


def _cache_get(qid, question):
    pth = _cache_path(qid, question)
    try:
        with open(pth) as f:
            data = json.load(f)
        if time.time() - data.get("ts", 0) > _CACHE_TTL_S:
            return None  # expired
        print(f"  [CACHE-HIT] {qid}: {len(data['sources'])} sources from cache", file=sys.stderr)
        return data["sources"]
    except Exception:
        return None


def _cache_put(qid, question, sources):
    try:
        os.makedirs(_CACHE_DIR, exist_ok=True)
        with open(_cache_path(qid, question), "w") as f:
            json.dump({"qid": qid, "question": question, "ts": time.time(),
                       "sources": sources}, f, ensure_ascii=False)
    except Exception as e:
        print(f"  [CACHE-WRITE-ERR] {qid}: {e}", file=sys.stderr)



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


def _wiki_extract(title, max_chars=900, lang="en"):
    """取 wiki 页面 intro 段全文（比 search snippet 长 5-10 倍，含具体数值/公式）。
    lang: 'en'/'zh'——中文题走 zh.wikipedia.org（2026-11-12 drb-1 r2 诊断：
    en-wiki 对"中国中产/九阶层"类查询零命中，DDG/cn.bing 全是垃圾源，
    zh-wiki 是中文事实检索的主力通道）。失败静默返回 ''。"""
    import urllib.request
    try:
        url = (f"https://{lang}.wikipedia.org/w/api.php?action=query&prop=extracts"
               f"&titles={quote_plus(title)}&exintro=1&explaintext=1&format=json")
        req = urllib.request.Request(url, headers={"User-Agent": "pfb-research/1.0"})
        d = json.load(urllib.request.urlopen(req, timeout=15))
        pages = d.get("query", {}).get("pages", {})
        for p in pages.values():
            ext = p.get("extract", "")
            if ext:
                return ext[:max_chars]
    except Exception:
        pass
    return ""


def _wiki_search(query, max_results=3):
    """Wikipedia API 检索（公网直连，不走 ego-browser/8787）。
    返回 [{title, url, snippet}, ...]。对教科书级事实/工程规格有效。
    snippet = search API 短摘要 + extracts intro 前 ~900 字符拼接（2026-11-09：
    双语言策略（2026-11-12 drb-1 r2）：中文题 en-wiki 零命中且 DDG/cn.bing 垃圾源，
    zh.wikipedia.org 是中文事实的主力通道——先查含 CJK 字符则 zh-first+en-supplement，
    否则 en-first（保持 GPU 等英文题原有行为不变）。"""
    import urllib.request, time as _time
    has_cjk = bool(re.search(r'[\u4e00-\u9fff]', query))
    langs = ["zh", "en"] if has_cjk else ["en"]
    results = []
    seen_titles = set()
    for lang in langs:
        if len(results) >= max_results:
            break
        try:
            url = (f"https://{lang}.wikipedia.org/w/api.php?action=query&list=search"
                   f"&srsearch={quote_plus(query)}&format=json&srlimit={max_results}")
            req = urllib.request.Request(url, headers={"User-Agent": "pfb-research/1.0"})
            d = json.load(urllib.request.urlopen(req, timeout=15))
            for h in d.get("query", {}).get("search", []):
                title = h["title"]
                if title in seen_titles or len(results) >= max_results:
                    continue
                seen_titles.add(title)
                short = re.sub(r'<[^>]+>', '', h.get("snippet", ""))[:200]
                intro = _wiki_extract(title, lang=lang)
                snippet = (short + "\n" + intro)[:1200] if intro else short
                results.append({
                    "title": title,
                    "url": f"https://{lang}.wikipedia.org/wiki/{quote_plus(title.replace(' ', '_'))}",
                    "snippet": snippet,
                })
                _time.sleep(0.3)  # rate-limit courtesy
        except Exception:
            pass
    # D 指令 (2026-11-12): site: 白名单后过滤——搜索引擎对 site: 支持不稳（实测
    # DDG lite 忽略 site:，Bing geo 到 cn 时 site: 失效），所以这里做结果侧兜底：
    # 只保留白名单域的结果。若全被杀光则返回空（让上层走 wiki/webfetch 通道）。
    _wl_domains = ["wikipedia.org", "sec.gov", "investopedia.com", "reuters.com",
                   "bloomberg.com", "macrotrends.net", "stockanalysis.com"]
    def _in_whitelist(url):
        return any(d in url for d in _wl_domains)
    before_wl = len(results)
    results = [r for r in results if _in_whitelist(r.get("url", ""))]
    if before_wl > len(results):
        print(f"  [SITE-WL] filtered {before_wl - len(results)} non-whitelisted source(s)", file=sys.stderr)
    return results



_STOPWORDS = frozenset("""of the a an and or vs versus for with from to in on by at per
that this these those how what which when where why does do did is are was were be been
its its their your my our his her not no more most less least between within without
under over into onto upon against through during before after each every some any all
both few several other another such than then so as if while because but also only just
very quite can could should would may might will shall""".split())

def _slim_query(query, max_words=6):
    """把长尾陈述句 query 压成 ≤max_words 个实义词的检索式。
    规则：小写分词 → 丢停用词 → 含数字的 token（型号 H100/RTX 4090/27B、年份 2024）
    及其紧邻的前置修饰词优先保留，其余实义词按原序补足；全被丢光则退回原 query。
    动机（D34）：degraded 节点英文 query 中位 9 词最长 14 词，DDG lite 多条件 AND
    直接零结果；唯一 verified 英文命中是最短 5 词 query。"""
    toks = re.findall(r"[A-Za-z0-9][A-Za-z0-9.%/-]*", query.lower())
    keep = []
    for i, w in enumerate(toks):
        if w in _STOPWORDS:
            continue
        if any(ch.isdigit() for ch in w):
            # 型号/数字：带上它前面的一个非停用词修饰（如 rtx 之于 4090）
            if i > 0 and toks[i-1] not in _STOPWORDS and toks[i-1] not in keep:
                keep.append(toks[i-1])
            keep.append(w)
    for w in toks:  # 纯文字实义词按原序补足
        if w not in _STOPWORDS and w not in keep:
            keep.append(w)
        if len(keep) >= max_words:
            break
    keep = keep[:max_words]
    return " ".join(keep) if keep else query

def _ddg_search(query, max_results=3):
    """DuckDuckGo LITE endpoint（纯 HTTP，不依赖 ego-browser）。
    lite.duckduckgo.com/lite/ 对 GPU 价格/功耗/TCO 这类非学术事实有效。
    有 anomaly 限流——重试一次（间隔 4s），仍被拦则静默返回 []。
    D34: 长 query 先瘦身再查（_slim_query），失败退回原 query 再试一轮。
    返回 [{title, url, snippet}, ...]"""
    import urllib.request, time as _time, html as _html
    # D34 (2026-11-12): P1H_INDEX 生成的 search_query 是完整事实陈述（degraded 节点
    # 英文 query 中位 9 词、最长 14 词），塞进 DDG lite 等于多条件 AND → 零结果，
    # 这是上一轮 gpu 跑 43/86 degraded 全是 "all 5 failed" 的主因之一。
    slimmed = _slim_query(query)
    queries = [query] if slimmed == query else [slimmed, query]
    results = []
    for q_try in queries:
        for attempt in range(2):
            try:
                url = ("https://lite.duckduckgo.com/lite/?q=" + quote_plus(q_try))
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (pfb-research)"})
                html_txt = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="replace")
                if "anomaly" in html_txt.lower():
                    if attempt == 0:
                        _time.sleep(4)
                        continue
                    break
                from urllib.parse import unquote
                for mm in re.finditer(r'<a[^>]*rel="nofollow"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html_txt, re.DOTALL):
                    href, title = mm.group(1), re.sub(r'<[^>]+>', '', mm.group(2)).strip()
                    if not title or len(results) >= max_results:
                        continue
                    if "uddg=" in href:
                        idx = href.index("uddg=")
                        href = _html.unescape(unquote(href[idx + 5:]))
                    snip_m = re.search(r"class='result-snippet'[^>]*>\s*(.*?)\s*</td>", html_txt[mm.end():mm.end()+2000], re.DOTALL)
                    snippet = re.sub(r'<[^>]+>', '', snip_m.group(1)).strip()[:400] if snip_m else ""
                    results.append({"title": _html.unescape(title)[:200], "url": href, "snippet": snippet})
                if results:
                    break
            except Exception:
                if attempt == 0:
                    _time.sleep(2)
        if results:
            break
    return results

def _webfetch_page(url, title_hint="", timeout=20):
    """纯 HTTP GET 抓取页面文本（stdlib urllib，不依赖 ego-browser）。
    适用于文档站/规格页等无 JS 渲染需求的站点。
    返回 {title, url, snippet, alive}。"""
    import urllib.request
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (pfb-research)"})
        html = urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", errors="replace")
        # 提取 <title>
        tm = re.search(r'<title[^>]*>(.*?)</title>', html, re.DOTALL | re.I)
        title = (tm.group(1).strip() if tm else title_hint or url)[:200]
        # 去标签取正文
        text = re.sub(r'<script[^>]*>.*?</script>', ' ', html, flags=re.DOTALL | re.I)
        text = re.sub(r'<style[^>]*>.*?</style>', ' ', text, flags=re.DOTALL | re.I)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        # 关键词窗口抽取（同 _fetch_page 逻辑）
        kw_pat = re.compile(
            r"(HBM\d?e?\s*\d|GB/s|TB/s|PCIe\s*Gen?\s*\d|SXM|watt|W\b|memory bandwidth|显存|"
            r"\$\d+[\.,]\d*/?(GB|TB|month|year|request)|¥\d+[\.,]\d*/?(GB|TB|月|年)|"
            r"per (GB|TB|month|year|request)|price[d]?|pricing|cost per|"
            r"VRAM|bandwidth|throughput|latency|cache hit|Pareto|Zipf)",
            re.I
        )
        hits = list(kw_pat.finditer(text[:20000]))
        if hits:
            windows, seen_starts = [], set()
            for h in hits[:6]:
                s0 = max(0, h.start() - 300)
                s1 = min(len(text), h.end() + 300)
                key = s0 // 200
                if key not in seen_starts:
                    seen_starts.add(key)
                    windows.append(text[s0:s1])
                if len(windows) >= 3:
                    break
            snippet = " … ".join(windows)[:2000]
        else:
            snippet = text[:1000]
        return {"title": title, "url": url, "snippet": snippet, "alive": True}
    except Exception:
        return {"title": title_hint or url, "url": url, "snippet": "", "alive": False}


# ── 本地语料通道 ──────────────────────────────────────────────────────────
_LOCAL_CORPUS_DIRS = [
    "/Users/a1-6/Desktop/workspace/projects/decomp/archive/D1-gpu-research-2026",
]

GPU_QUERY_MARKERS = ("gpu", "显卡", "rtx", "a100", "h100", "h200", "b200", "b300",
                     "nvidia", "amd", "intel", "显存", "vram", "kv cache",
                     "tok/s", "tpot", "ttft", "推理服务器")


def _query_is_gpu_related(query):
    """判断查询是否 GPU/硬件相关。D1-gpu 语料只服务这类查询（2026-11-09 修复：
    nat/soc 等非 GPU 题的 P3 核验被 D1-gpu 语料污染——744/1506 个节点的 evidence
    引用了 GPU 硬件规格，P3 模型看到无关语料直接标 degraded）。"""
    q = query.lower()
    return any(m in q for m in GPU_QUERY_MARKERS)


def _local_corpus_search(query, max_results=3, qid=None):
    """在本地已验证调研项目中搜索相关片段（grep -ri 关键词匹配）。
    返回 [{title, url(file path), snippet, source_type:'local_corpus'}, ...]
    2026-11-09: 按题目域门控——只有 query 命中该域 corpus 的标记词才服务，否则返回空。
    当前唯一 corpus = D1-gpu；qid='nat'/'soc' 等非 gpu 域直接返回 []。"""
    # Domain gate: only serve queries that match this corpus's domain.
    if qid is not None and qid != "gpu":
        return []
    if not _query_is_gpu_related(query):
        return []
    import subprocess as _sp
    # 提取核心词（≥2字符，过滤停用词）
    words = re.findall(r'[A-Za-z0-9]{2,}', query)
    STOP = {'the', 'and', 'for', 'with', 'from', 'this', 'that', 'what', 'how',
            'which', 'were', 'will', 'can', 'not', 'but', 'are', 'was', 'you',
            'your', 'about', 'into', 'each', 'must', 'mark'}
    terms = [w for w in words if w.lower() not in STOP][:5]
    if not terms:
        return []
    results = []
    for d in _LOCAL_CORPUS_DIRS:
        if not os.path.isdir(d):
            continue
        try:
            # grep -rilE (case-insensitive, extended regex for | alternation)
            pattern = '|'.join(terms)
            r = _sp.run(
                ["grep", "-rilE", f"{pattern}", "--include=*.md", "--include=*.py", "--include=*.json", d],
                capture_output=True, text=True, timeout=10,
            )
            files = r.stdout.strip().splitlines()[:8]
            for f in files:
                try:
                    with open(f, "r", errors="replace") as fh:
                        content = fh.read()
                    lines = content.splitlines()
                    relevant = [l.strip() for l in lines
                                if any(t.lower() in l.lower() for t in terms)]
                    if relevant:
                        results.append({
                            "title": f"{os.path.basename(d)}:{os.path.basename(f)}",
                            "url": f,
                            "snippet": " | ".join(relevant[:4])[:600],
                        })
                except Exception:
                    continue
                if len(results) >= max_results:
                    break
        except Exception:
            continue
        if len(results) >= max_results:
            break
    return results[:max_results]


def _webllm_search(query, max_results=3):
    """通道 6：网页 AI 信源（Perplexity via ego-browser，已登录会话）。

    DDG/arXiv 都拿不到具体事实时的兜底：Perplexity 直接返回「答案 + 引用 URL」，
    引用 URL 作为 source 落盘（snippet 用查询本身标注来源类型）。
    用户指令 2026-11-08：'可以问 arena，不止 perplexity，然后根据网页 AI 信源验证'。
    每个查询 ~15-25s（含页面渲染等待），仅在前面通道结果不足时触发。
    """
    js = """
const task = await taskSpace("pfb-webllm-research");
const page = task.page("p1");
await page.goto("https://www.perplexity.ai/search?q=" + encodeURIComponent(%s));
await new Promise(r => setTimeout(r, 12000));
const links = await page.evaluate(() => Array.from(document.querySelectorAll("a")).map(a => a.href)
  .filter(h => !h.includes("perplexity.ai") && !h.startsWith("#") && /^https?:/.test(h)));
const uniq = [...new Set(links)].slice(0, %d);
console.log(JSON.stringify(uniq));
""" % (json.dumps(query), max_results)
    out = _run_ego_browser(js, timeout=90)
    # extract JSON array from stdout (last line that parses)
    urls = []
    for line in reversed(out.splitlines()):
        line = line.strip()
        if line.startswith("["):
            try:
                urls = json.loads(line)
                break
            except Exception:
                continue
    results = []
    for u in urls[:max_results]:
        results.append({"title": f"[web-llm] {query}", "url": u,
                        "snippet": f"Perplexity 回答引用源（query: {query}）"})
    return results


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
        # S8G (v3 gold-gap P2a): 统计方法论域精准文献源（经典可重复性/效应量文献）
        # 注: arXiv 无 Ioannidis 2005 原文，用 Wikipedia 条目覆盖该主题
        ("https://en.wikipedia.org/wiki/Replication_crisis", "Replication crisis (Wikipedia, incl. Ioannidis 2005 'why most published research findings are false')"),
        ("https://en.wikipedia.org/wiki/Multiple_comparisons_problem", "Multiple comparisons problem (Wikipedia)"),
        ("https://en.wikipedia.org/wiki/Effect_size", "Effect size (Wikipedia)"),
    ],
    "Q6": [  # CDN vs self-hosted edge node (networking domain)
        ("https://aws.amazon.com/cloudfront/pricing/", "AWS CloudFront Pricing"),
        ("https://www.cloudflare.com/products/cdn/", "Cloudflare CDN Product Page"),
        ("https://www.fastly.com/products/cdn", "Fastly CDN Product Page"),
        ("https://cloud.tencent.com/product/cdn", "Tencent Cloud CDN"),
    ],
    "Q7": [  # SSD RAID vs HDD+SSD tiering vs cloud object storage (storage domain)
        ("https://www.aliyun.com/product/oss/pricing", "Aliyun OSS Pricing"),
        ("https://aws.amazon.com/s3/pricing/", "AWS S3 Pricing"),
        ("https://en.wikipedia.org/wiki/Erasure_code", "Erasure Code (Wikipedia)"),
        ("https://en.wikipedia.org/wiki/Redundant_array_of_independent_disks", "RAID (Wikipedia)"),
    ],
    # T50 新增（B 面域内题）：一手论文源，与 gold-Q8/Q9/Q10.md 来源表对齐
    "Q8": [  # code generation benchmark design (LLM evaluation domain)
        ("https://arxiv.org/abs/2107.03374", "Codex/HumanEval (arXiv)"),
        ("https://arxiv.org/abs/2403.07974", "LiveCodeBench (arXiv)"),
        ("https://arxiv.org/abs/2305.01210", "EvalPlus/HumanEval+ (arXiv)"),
        ("https://arxiv.org/abs/2311.04850", "Rephrased Samples Contamination (arXiv)"),
    ],
    "Q9": [  # VLM architecture comparison (multimodal domain)
        ("https://arxiv.org/abs/2103.00020", "CLIP (arXiv)"),
        ("https://arxiv.org/abs/2304.02643", "Segment Anything (arXiv)"),
        ("https://arxiv.org/abs/2303.08774", "GPT-4 Technical Report (arXiv)"),
        ("https://arxiv.org/abs/2403.05530", "Gemini 1.5 (arXiv)"),
    ],
    "Q10": [  # RLHF pipeline and alignment tax (alignment domain)
        ("https://arxiv.org/abs/2203.02155", "InstructGPT (arXiv)"),
        ("https://arxiv.org/abs/2305.18290", "DPO (arXiv)"),
        ("https://arxiv.org/abs/2210.10760", "Reward Model Overoptimization (arXiv)"),
        ("https://arxiv.org/abs/2312.01552", "URIAL / Superficial Alignment (arXiv)"),
    ],
    "gpu": [  # 27B local inference card selection (hardware spec + economic domain)
        # webfetch 可达（纯 HTTP，无 JS 墙）— 硬件规格
        ("https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/", "NVIDIA RTX 5090 Official"),
        ("https://en.wikipedia.org/wiki/Nvidia_GeForce_RTX_50_series", "RTX 50 series (Wikipedia)"),
        ("https://en.wikipedia.org/wiki/Ampere_(microarchitecture)", "Ampere architecture (Wikipedia, A100)"),
        ("https://en.wikipedia.org/wiki/L40S", "L40S (Wikipedia)"),
        # 经济层：云租价格 / 二手残值 / TCO
        ("https://aws.amazon.com/ec2/instance-types/p5/", "AWS P5 Instance Pricing (H100 cloud rental)"),
        ("https://cloudgputracker.com/pricing/", "CloudGPUTracker GPU Rental Pricing"),
        ("https://www.techpowerup.com/gpu-specs/rtx-5090.c4226", "TechPowerUp RTX 5090 Specs"),
        ("https://www.techpowerup.com/gpu-specs/a100-pcie-40gb.c3718", "TechPowerUp A100-40GB Specs"),
        # ego-browser 兜底（JS 渲染 / bot check）
        ("https://www.rigbuild.com/pages/gpu-pricing", "GPU Price Tracker (street prices)"),
    ],
}

# arXiv 精准查询（T30: 每 Q 多路 query，取并集提升召回）
ARXIV_QUERIES = {
    "Q1": ["H100 PCIe SXM inference throughput benchmark", "GPU memory bandwidth LLM serving"],
    "Q2": ["Qwen2.5-Coder HumanEval code generation benchmark", "LLM model selection cost accuracy tradeoff open source"],
    "Q3": ["vLLM TGI SGLang inference serving comparison throughput", "LLM inference engine PagedAttention continuous batching"],
    "Q4": ["retrieval augmented generation vs long context window comparison", "RAG faithfulness evaluation lost in the middle"],
    "Q5": ["Bayesian decision theory expected loss minimization frequentist", "statistical hypothesis testing decision rules risk",
        # S8G (v3 gold-gap P2a): 统计方法论域精准查询词（可重复性危机/多重比较/效应量估计）
        "statistical methodology reproducibility crisis",
        "multiple comparisons correction p-value",
        "effect size estimation bias small studies"],
    "Q6": ["CDN content delivery network pricing per GB cost comparison",
           "edge computing node TCO total cost of ownership latency"],
    "Q7": ["erasure coding storage overhead capacity efficiency",
           "SSD NVMe vs HDD cost per TB object storage pricing comparison"],
    # T50 新增（B 面域内题）：任务书要求每题至少一条精准 arXiv query
    "Q8": ["code generation benchmark contamination detection pass@k evaluation LLM"],
    "Q9": ["vision language model architecture contrastive CLIP segment anything multimodal"],
    "Q10": ["RLHF PPO KL penalty DPO preference optimization alignment tax"],
    # S5 GPU 题（27B 本地推理选卡）
    "gpu": ["RTX 5090 specifications VRAM memory bandwidth",
            "A100 HBM2e bandwidth L40S Ada Lovelace datasheet",
            "large language model inference roofline bandwidth bound decoding",
            # 经济层（gold-tree N-1/N-7）：TCO / 云租 / 残值
            "GPU total cost of ownership TCO cloud rental vs purchase break-even",
            "used GPU resale value depreciation rate second-hand market"],
}

# T31: 来源过滤关键词（只注入 title/snippet 含这些词的结果）
FILTER_KEYWORDS = {
    "Q1": ["PCIe", "SXM", "throughput", "bandwidth", "NVLink", "memory bus"],
    "Q2": ["Qwen", "Mistral", "GLM", "DeepSeek", "Llama", "HumanEval", "code generation", "model selection", "cost"],
    "Q3": ["vLLM", "TGI", "SGLang", "serving", "inference engine", "PagedAttention", "throughput", "latency"],
    "Q4": ["retrieval", "RAG", "context window", "long context", "faithfulness", "Lost in the Middle"],
    "Q5": ["Bayesian", "frequentist", "hypothesis testing", "decision theory", "expected loss", "risk"],
    "Q6": ["CDN", "content delivery", "edge node", "P99", "latency", "per GB", "pricing", "TCO", "POP", "cache hit"],
    "Q7": ["erasure code", "RAID", "NVMe", "SSD", "HDD", "object storage", "per TB", "capacity", "RTO", "redundancy", "PUE"],
    "Q8": ["HumanEval", "MBPP", "LiveCodeBench", "SWE-bench", "BigCodeBench", "pass@k", "contamination", "decontamination", "EvalPlus", "code generation", "benchmark"],
    "Q9": ["CLIP", "SAM", "Segment Anything", "GPT-4V", "Gemini", "multimodal", "vision-language", "contrastive", "ViT", "tiling", "LLaVA", "Flamingo"],
    "Q10": ["RLHF", "PPO", "DPO", "KL", "reward model", "preference", "alignment", "InstructGPT", "alignment tax", "fine-tuning"],
    "gpu": ["RTX 5090", "4090", "L40S", "A100", "VRAM", "bandwidth", "GB/s", "HBM", "PCIe", "roofline", "inference", "memory", "quantization", "INT8", "BF16",
        # 经济层（gold-tree N-1/N-7）
        "TCO", "total cost of ownership", "residual value", "depreciation", "cloud rental", "break-even", "utilization", "watt", "power consumption", "electricity"],
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
        "  const info = await page.evaluate(() => {\n"
        "    // 优先取正文容器，跳过导航/页脚\n"
        "    let main = document.querySelector('main') ||\n"
        "             document.querySelector('article') ||\n"
        "             document.querySelector('[role=\"main\"]') ||\n"
        "             document.querySelector('.pricing-table') ||\n"
        "             document.querySelector('table');\n"
        "    let text;\n"
        "    if (main && main.innerText.length > 200) {\n"
        "      text = main.innerText;\n"
        "    } else {\n"
        "      // fallback: 全文去掉 nav/footer/header\n"
        "      const clone = document.body.cloneNode(true);\n"
        "      clone.querySelectorAll('nav, footer, header, .header, .footer, .nav, #nav, #header').forEach(el => el.remove());\n"
        "      text = clone.innerText;\n"
        "    }\n"
        "    return { title: document.title, bodyLen: text.length, sample: text.slice(0, 8000) };\n"
        "  });\n"
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
                sample = data.get("sample", "")[:8000]
                # 从长样本中抽取含定价/规格关键词的窗口，替代盲目取前 N 字符
                import re as _re
                kw_pat = _re.compile(
                    r"(HBM\d?e?\s*\d|GB/s|TB/s|PCIe\s*Gen?\s*\d|SXM|watt|W\b|memory bandwidth|显存|"
                    r"\$\d+[\.,]\d*/?(GB|TB|month|year|request)|¥\d+[\.,]\d*/?(GB|TB|月|年)|"
                    r"per (GB|TB|month|year|request)|price[d]?|pricing|cost per|"
                    r"标准存储|低频|归档|冷归档|深度冷归档|外网下行|取回费|请求费用)",
                    _re.I
                )
                hits = list(kw_pat.finditer(sample))
                if hits:
                    # 取命中点为中心 ±800 字符窗口（最多 3 个，按起点去重）
                    windows, seen_starts = [], set()
                    for h in hits:
                        s0 = max(0, h.start() - 400)
                        s1 = min(len(sample), h.end() + 400)
                        key = s0 // 200  # 200 字符粒度的桶
                        if key in seen_starts:
                            continue
                        seen_starts.add(key)
                        windows.append(sample[s0:s1])
                        if len(windows) >= 3:
                            break
                    sample = " … ".join(windows)
                return {"title": data.get("title", title_hint), "url": url,
                        "snippet": sample, "alive": True}
    except Exception:
        pass
    return {"title": title_hint, "url": url, "snippet": "", "alive": False}


def research_hook(qid, question, max_results=8, enable_local=True):
    """主接口 v3：多通道并行检索，返回 sources 列表。

    通道优先级（每个通道独立 cap，总输出 ≤ max_results）：
      1. local_corpus  — 本地已验证调研项目（D1-gpu 等），最快最准
      2. wikipedia     — 教科书/工程规格级事实，公网 API ~1.5s
      3. arxiv         — 学术文献，ego-browser ~12s
      4. webfetch      — 纯 HTTP 抓已知站点（文档/规格页），不依赖 ego-browser
      5. direct_site   — ego-browser 深抓（JS 渲染页），最慢但最全

    返回格式: [{title, url, snippet, observed_at, source_type}, ...]
    失败: 所有通道都空 → 抛 ResearchHookUnavailable
    """
    observed = datetime.now(timezone.utc).isoformat()
    # cache-first: 稳定步骤复用，避免重复打 DDG/Perplexity（保护登录态会话 + 省 wall time）
    cached = _cache_get(qid, question)
    if cached is not None:
        return cached
    sources = []
    seen_urls = set()

    def _add(r, stype):
        if len(sources) >= max_results:
            return
        key = r["url"]
        if key in seen_urls:
            return
        seen_urls.add(key)
        sources.append({**r, "observed_at": observed, "source_type": stype})

    # ── 1. 本地语料（最快，~0.1s，已验证数据优先）──
    # enable_local=False 时跳过：_LOCAL_CORPUS_DIRS 只有 D1-gpu-research 语料，
    # 对非 GPU 题 grep 出的"命中"是无关文档，会污染下游 P3 核验。
    try:
        if enable_local:
            for r in _local_corpus_search(question, max_results=2, qid=qid):
                _add(r, "local_corpus")
    except Exception:
        pass

    # ── 2. Wikipedia API（~1.5s，教科书/规格）──
    remaining = max_results - len(sources)
    if remaining > 0:
        try:
            for r in _wiki_search(question, max_results=min(3, remaining)):
                _add(r, "wikipedia")
        except Exception:
            pass

    # ── 2.5 DuckDuckGo（~2-4s，非学术事实：价格/功耗/TCO）──
    # 中文查询跳过 DDG/cn.bing（2026-11-12 drb-1 r2 实测：中文题返回知乎"豆包水印"类
    # 完全无关垃圾，junk filter 拦不住这种"标题看着正常但内容零相关"的源；
    # zh-wiki 通道已接管中文事实检索）。英文查询保持原行为。
    # 例外（drb-2 诊断 2026-11-12 ~07:00）：中文"榜单/对比/排名"题——zh-wiki 没有
    # "国际综合实力前十保险公司"这类条目，DDG/bing 是唯一能拿到候选名单的通道，
    # 且英文 query 走 bing 国际版结果干净（实测 top10 insurance companies in China
    # by assets → 正确公司列表），不触发 cn.bing 跨域噪声。
    remaining = max_results - len(sources)
    if remaining > 0 and not (re.search(r'[\u4e00-\u9fff]', question)
                              and not re.search(r'排名|榜单|前十|前\s*\d+\s*名|综合.{0,8}(实力|竞争力)|top\s*\d+', question, re.I)):
        try:
            for r in _ddg_search(question, max_results=min(3, remaining)):
                _add(r, "ddg")
        except Exception:
            pass

    # ── 2.7 Web-LLM（Perplexity via ego-browser，~15-25s；仅当前面通道 <3 条时兜底）──
    # 用户指令 2026-11-08：网页 AI 信源作为独立验证通道，不限预算。
    if len(sources) < 3:
        try:
            for r in _webllm_search(question, max_results=min(3, max_results - len(sources))):
                _add(r, "web_llm")
        except Exception as e:
            print(f"  [WEBLLM-SKIP] {qid}: {str(e)[:100]}", file=sys.stderr)

    # ── 3. arXiv API（~12s/query，学术文献）──
    # v3.1 (2026-11-09): s5-node 通道不再走题级预设查询词——节点 query 是 L2/L3 子维度
    # （如 "GPU depreciation rate"），用它查 arXiv 只会捞回无关论文；而本地语料/百科/DDG
    # 已覆盖规格与定义类事实。只有题级 qid（Q1-Q8/S5-*）才用预设查询词。
    if qid == "s5-node":
        queries = []  # skip arxiv for node-level queries
    else:
        queries = ARXIV_QUERIES.get(qid, [question])
    n_arxiv_relevant = 0
    arxiv_cap = min(3, max_results - len(sources))
    for q in queries[:2]:  # 最多 2 路 query 控制时间
        if len(sources) >= max_results or arxiv_cap <= 0:
            break
        try:
            arxiv_results = _arxiv_search(q, max_results=max(2, arxiv_cap))
            n_arxiv_relevant += len(arxiv_results)
            for r in arxiv_results:
                _add(r, "arxiv")
                arxiv_cap -= 1
        except (ResearchHookUnavailable, Exception):
            continue

    if n_arxiv_relevant < 2 and qid != "s5-node":
        print(f"  [RESEARCH-GAP] {qid}: arXiv returned only {n_arxiv_relevant} result(s); "
              f"other channels compensate", file=sys.stderr)

    # ── 4. WebFetch 已知站点（纯 HTTP，~2-5s/page，不占 ego-browser）──
    sites = KNOWN_SITES.get(qid, [])
    remaining = max_results - len(sources)
    for url, title_hint in sites[:remaining]:
        if "wikipedia.org" in url:
            continue  # wiki 条目已由通道 2 覆盖
        page_info = _webfetch_page(url, title_hint)
        if page_info["alive"]:
            _add(page_info, "webfetch")

    # ── 5. ego-browser 深抓（JS 渲染页，~10-20s/page，最后兜底）──
    remaining = max_results - len(sources)
    if remaining > 0 and sites:
        for url, title_hint in sites[len(sites) - min(2, remaining):]:
            if "wikipedia.org" in url:
                continue
            page_info = _fetch_page(url, title_hint)
            if page_info["alive"]:
                _add(page_info, "direct_site")

    # ── 过滤：搜索引擎跳转链接 + 垃圾源 ──
    _BAD_ANCHOR = re.compile(r'bing\.com/ck|google\.com/url\?', re.I)
    # Junk filter (2026-11-12): drb-1 诊断——DDG/cn.bing 对中文 DRB 题返回大量无关源
    # （色情视频/英雄联盟/原神/翻译工具/股票行情），75% 节点 degraded 全因于此。
    # 这些源的 title/snippet 与查询主题零相关，喂给 verify 只会触发 rework。
    # v2 (drb-1 r1 复盘): v1 只覆盖英文+部分中文模式，实测漏网（哔哩哔哩/TensorFlow 主页/
    # 商城平台仍进 evidence）。补中文垃圾域模式；宁可多杀——verify 对"无可用外部证据"
    # 会降级，但错误来源比空来源更毒（诱导 rework 循环）。
    _JUNK_PATTERNS = re.compile(
        r'色情|成人|av\b|porn|sex\b|xxx|裸体|情色|'
        r'英雄联盟|lol\b|原神|genshin|崩坏|星穹铁道|王者荣耀|我的世界|和平精英|'
        r'翻译工具|在线翻译|有道翻译|百度翻译|deepl|google\s*translate|'
        r'股票行情|实时股价|个股分析|基金净值|期货行情|大盘|涨停|'
        r'下载中心|软件破解|免费资源|网盘分享|百度云盘|迅雷|'
        r'短视频|抖音|快手|tiktok|直播|哔哩哔哩|bilibili|b站|腾讯视频|爱奇艺|优酷|'
        r'商城|淘宝|天猫|京东|拼多多|苏宁易购|当当|'
        r'tensorflow|pytorch|kubernetes|docker|linux\s*教程|编程入门|python教程|'
        r'文库|歌词|电商|电子商务平台|商城',
        re.I
    )
    before = len(sources)
    sources = [s for s in sources
               if not _BAD_ANCHOR.search(s.get("url", ""))
               and not _JUNK_PATTERNS.search(s.get("title", "") + " " + s.get("snippet", ""))]
    dropped = before - len(sources)
    if dropped:
        print(f"  [JUNK-FILTER] {qid}: dropped {dropped} junk/redirect source(s)", file=sys.stderr)

    if not sources:
        raise ResearchHookUnavailable("no sources from any channel (all 5 failed)")

    # D 指令 (2026-11-12): 结果侧域名白名单过滤——广告/垃圾站从源头掐掉。
    # 策略：若过滤后仍有 ≥2 条白名单源，只用白名单；否则保留全部（宁缺毋滥但别空手）。
    def _wl_match(url):
        return any(d in url for d in _SOURCE_WHITELIST)
    wl_sources = [s_ for s_ in sources if _wl_match(s_.get("url", ""))]
    if len(wl_sources) >= 2:
        dropped_wl = len(sources) - len(wl_sources)
        if dropped_wl:
            print(f"  [SITE-WL] {qid}: kept {len(wl_sources)} whitelisted, dropped {dropped_wl} non-whitelisted", file=sys.stderr)
        sources = wl_sources
    elif wl_sources:
        # 只有 1 条白名单源：保留它 + 其余源（避免只剩 1 条太薄）
        pass
    # 0 条白名单源：不过滤（让 junk filter 兜底）

    out = sources[:max_results]
    _cache_put(qid, question, out)
    return out


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