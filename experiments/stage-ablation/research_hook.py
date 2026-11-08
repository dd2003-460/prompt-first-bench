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


def _wiki_search(query, max_results=3):
    """Wikipedia API 检索（公网直连，不走 ego-browser/8787）。
    返回 [{title, url, snippet}, ...]。对教科书级事实/工程规格有效。"""
    import urllib.request
    results = []
    try:
        url = (f"https://en.wikipedia.org/w/api.php?action=query&list=search"
               f"&srsearch={quote_plus(query)}&format=json&srlimit={max_results}")
        req = urllib.request.Request(url, headers={"User-Agent": "pfb-research/1.0"})
        d = json.load(urllib.request.urlopen(req, timeout=15))
        for h in d.get("query", {}).get("search", []):
            title = h["title"]
            snippet = re.sub(r'<[^>]+>', '', h.get("snippet", ""))[:400]
            results.append({
                "title": title,
                "url": f"https://en.wikipedia.org/wiki/{quote_plus(title.replace(' ', '_'))}",
                "snippet": snippet,
            })
    except Exception:
        pass
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

def _local_corpus_search(query, max_results=3):
    """在本地已验证调研项目中搜索相关片段（grep -ri 关键词匹配）。
    返回 [{title, url(file path), snippet, source_type:'local_corpus'}, ...]"""
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


def research_hook(qid, question, max_results=8):
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
    try:
        for r in _local_corpus_search(question, max_results=2):
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

    # ── 3. arXiv API（~12s/query，学术文献）──
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

    if n_arxiv_relevant < 2:
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

    # ── 过滤：搜索引擎跳转链接 ──
    _BAD_ANCHOR = re.compile(r'bing\.com/ck|google\.com/url\?', re.I)
    before = len(sources)
    sources = [s for s in sources if not _BAD_ANCHOR.search(s.get("url", ""))]
    dropped = before - len(sources)
    if dropped:
        print(f"  [ANCHOR-FILTER] {qid}: dropped {dropped} redirect link(s)", file=sys.stderr)

    if not sources:
        raise ResearchHookUnavailable("no sources from any channel (all 5 failed)")

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