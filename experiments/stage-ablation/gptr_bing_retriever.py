"""Bing retriever for GPT-Researcher — monkeypatch, no framework source modified.

Why: the built-in duckduckgo/ddgs retrievers route through mojeek.com which is
unreachable from this network (verified timeout). Bing works (0.8s, verified).
This registers a 'bing' retriever into gpt_researcher's registry so
RETRIEVER="bing" picks it up. Lives in our repo, not site-packages.
"""
import re
import urllib.parse
import urllib.request


def _parse_bing(html):
    """Extract result links + snippets from Bing search HTML."""
    out = []
    # bing organic results live in <li class="b_algo"> blocks
    for block in re.findall(r'<li class="b_algo".*?</li>', html, re.S):
        m = re.search(r'<h2[^>]*>\s*<a[^>]+href="(http[^"]+)"[^>]*>(.*?)</a>', block)
        if not m:
            continue
        href = m.group(1)
        title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        sm = re.search(r'<p[^>]*>(.*?)</p>', block, re.S)
        snippet = re.sub(r"<[^>]+>", "", sm.group(1)).strip() if sm else ""
        out.append({"href": href, "title": title, "body": snippet[:500]})
    return out


class BingRetriever:
    requires_scraping = True  # snippets are short; let GR fetch full pages

    def __init__(self, query, query_domains=None):
        self.query = query
        self.query_domains = query_domains or None

    def search(self, max_results=5):
        url = "https://www.bing.com/search?q=" + urllib.parse.quote(self.query)
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
        )
        html = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "ignore")
        results = _parse_bing(html)[:max_results]
        if self.query_domains:
            doms = {d.lstrip(".") for d in self.query_domains}
            results = [r for r in results if any(d in r["href"] for d in doms)]
        return results


def install():
    from gpt_researcher.retrievers import get_retriever_registry

    try:
        reg = get_retriever_registry()
        reg.register("bing", BingRetriever)
        return True
    except Exception as e:
        print(f"[gptr-bing] registry install failed ({e}); falling back to module attr")
        import gpt_researcher.actions.query_processing as qp
        qp.BING_RETRIEVER = BingRetriever
        return False


if __name__ == "__main__":
    ok = install()
    r = BingRetriever("NVIDIA H200 TDP watts")
    res = r.search(3)
    print(f"install={ok} results={len(res)}")
    for x in res:
        print(" ", x["href"][:80], "|", x["title"][:50])