#!/usr/bin/env python3
"""gptr 检索层桥接：把 s5 的 research_hook + ego-direct 接进 gptr。

控制变量：s5 和 gptr 共享同一个检索层（research_hook + ego-direct），
消融对比只测 pipeline 结构差异，不混入检索能力差异。

用法：
    from pfb_retriever import install_pfb_retriever
    install_pfb_retriever()  # monkey-patch gptr 的 get_retriever
    os.environ["RETRIEVER"] = "pfb"

接口：
    PfbRetriever(query, query_domains=None).search(max_results=5)
    → [{url, raw_content}, ...]  (requires_scraping=False)
"""
import os
import sys

# 确保能 import 同目录的 research_hook / s5_pipeline
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)


class PfbRetriever:
    """gptr retriever，底层用 s5 的 research_hook + ego-direct。

    requires_scraping=False：返回已抓取的内容（raw_content），gptr 不再二次 scrape。
    """
    requires_scraping = False

    def __init__(self, query, query_domains=None):
        self.query = query
        # qid 决定 research_hook 的通道选择（gpu 题启用 local_corpus + gpu_specs）
        self.qid = os.environ.get("PFB_QID", "s5-node")

    def search(self, max_results=5):
        results = []
        seen = set()

        # 通道 1: research_hook（多通道：wiki/ddg/bing/arxiv/webfetch/webllm）
        try:
            from research_hook import research_hook
            for s in research_hook(self.qid, self.query,
                                   max_results=max_results, enable_local=False):
                url = s.get("url", "")
                if not url or url in seen:
                    continue
                seen.add(url)
                results.append({
                    "url": url,
                    "raw_content": (s.get("snippet", "") or s.get("title", ""))[:3000],
                })
        except Exception as e:
            print(f"  [PFB-RETRIEVER] research_hook failed: {e}", flush=True)

        # 通道 2: ego-direct 兜底（wiki API + ego-browser 直访权威站）
        if len(results) < 2:
            try:
                from s5_pipeline import _ego_direct_fetch
                for s in _ego_direct_fetch(self.query, self.qid):
                    url = s.get("url", "")
                    if not url or url in seen:
                        continue
                    seen.add(url)
                    results.append({
                        "url": url,
                        "raw_content": (s.get("snippet", "") or s.get("title", ""))[:3000],
                    })
            except Exception as e:
                print(f"  [PFB-RETRIEVER] ego-direct failed: {e}", flush=True)

        if not results:
            print(f"  [PFB-RETRIEVER] ALL CHANNELS EMPTY for query: {self.query[:80]}", flush=True)
        else:
            print(f"  [PFB-RETRIEVER] {len(results)} sources for: {self.query[:60]}", flush=True)
        return results[:max_results]


def install_pfb_retriever():
    """monkey-patch gptr 的 get_retriever，让 'pfb' 名字返回 PfbRetriever。"""
    import gpt_researcher.actions.retriever as _ret

    _orig_get_retriever = _ret.get_retriever

    def _patched_get_retriever(name):
        if name == "pfb":
            return PfbRetriever
        return _orig_get_retriever(name)

    _ret.get_retriever = _patched_get_retriever
    # 同时 patch get_retrievers（它内部调 get_retriever，但为了安全也 patch 一下）
    # get_retrievers 里用的是模块级 get_retriever，所以 patch 模块属性就够了
    print("[PFB-RETRIEVER] installed: gptr 'pfb' → s5 research_hook + ego-direct", flush=True)


if __name__ == "__main__":
    # smoke test：直接调 PfbRetriever.search，不走 gptr
    install_pfb_retriever()
    r = PfbRetriever("GPU inference TCO comparison consumer vs datacenter", query_domains=None)
    srcs = r.search(max_results=5)
    print(f"\n=== smoke test: {len(srcs)} sources ===")
    for i, s in enumerate(srcs, 1):
        print(f"  [{i}] {s['url'][:80]}")
        print(f"      content: {s['raw_content'][:100]}...")
