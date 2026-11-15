#!/usr/bin/env python3
"""T-PR-15 AC8：把 survey 的 4 条 final 结论发给 ≥2 个不同 LLM 服务做交叉核验。

设计约束（任务书【失败降级】）：
- 沙箱/无 endpoint 时**不伪造回执**：全部记为 status=dispatch_failed 并写进 JSON。
- Lead 在本机跑时只需设置环境变量，脚本自动把真实回答写入同一 JSON 的 receipts。
- 只发"待核验主张 + 反例要求"，不发本文结论段落（防锚定，02.5 要求）。

用法（Lead 本机）：
  export PFB_LLM_A_URL=http://127.0.0.1:8787/v1/chat/completions
  export PFB_LLM_A_MODEL=qwen3.8-27b
  export PFB_LLM_B_URL=http://127.0.0.1:8788/v1/chat/completions   # 必须是不同底座
  export PFB_LLM_B_MODEL=<second-family-model>
  python3 research/web-llm/run_crosscheck.py            # 就地更新 JSON
  python3 research/web-llm/run_crosscheck.py --dry-run  # 只打印将发送的内容
"""
import json, os, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "text-objective-crosscheck.json")

CLAIMS = [
    {
        "id": "K1",
        "claim": "Goodhart's law 是比 specification gaming 与 reward hacking 更宽的框架；后两者是它在特定设定下的实例（而非并列概念）。",
        "ask": "请给出支持与反对各 2 条，并指出是否有反例文献（要求可检索的 arXiv ID 或 DOI）。",
    },
    {
        "id": "K2",
        "claim": "LLM 在 prompt/评估场景下的 hack 形态可归为五类：格式/长度刷分、关键词 stuffing、自评 inflation、judge sycophancy、benchmark 污染；前四类都作用于『文字条款 + 判者』这一层。",
        "ask": "请判断该五分类是否有遗漏类别（尤其是『利用评测 harness 而非判者』），并给可检索来源。",
    },
    {
        "id": "K3",
        "claim": "『文字目标比数值目标更容易被 hack』缺乏同实验对照证据；更准确的表述是『可操纵接口数量 × 优化压力』。",
        "ask": "请找反例：是否存在同实验内比较文字条款目标与数值目标 hack 率的研究？",
    },
    {
        "id": "K4",
        "claim": "只改 prompt/判据、不改权重时，最有效的防御是给覆盖度型（recall）代理加精度/冗余项 + 硬预算约束，而非 reward clipping。",
        "ask": "请给出反例或更强的替代方案（例如无需改权重却比 precision term 更有效的手段），并给来源。",
    },
]

SERVICES = [
    ("A", "PFB_LLM_A_URL", "PFB_LLM_A_MODEL", "qwen3.8-27b"),
    ("B", "PFB_LLM_B_URL", "PFB_LLM_B_MODEL", "unset"),
]

PROMPT_TMPL = (
    "你是独立的文献核查员。下面是一条待核验主张，**请不要假设它正确**。\n\n"
    "主张：{claim}\n\n任务：{ask}\n\n"
    "要求：① 只给可检索来源（arXiv ID / DOI / 会议论文），不要泛泛而谈；"
    "② 明确列出与该主张矛盾或限制其适用范围的反例；③ 最后一行给 'VERDICT: 支持|部分支持|反驳|证据不足'。"
)


def call(url, model, prompt, timeout=25):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_tokens": 900,
    }).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"], round(time.time() - t0, 2)


def main():
    dry = "--dry-run" in sys.argv
    prev = {}
    if os.path.exists(OUT):
        prev = json.load(open(OUT, encoding="utf-8"))
    doc = {
        "task": "T-PR-15",
        "artifact": "web-llm cross-check receipts (AC8)",
        "nature": "网页/本地 LLM 回答仅是审阅线索，不是权威事实来源。",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "claims": CLAIMS,
        "services": [],
        "receipts": [],
        "contradictions": prev.get("contradictions", []),
        "ac8_status": "pending",
        "usage_limit": "未取得回执的服务一律记 dispatch_failed；不得把未取回的回答写成已验证事实。",
    }
    for sid, url_env, model_env, default_model in SERVICES:
        url = os.environ.get(url_env)
        model = os.environ.get(model_env, default_model)
        svc = {"id": sid, "url_env": url_env, "model": model if url else None,
               "transport": "http_openai_compatible", "configured": bool(url)}
        if dry:
            print(f"[{sid}] url={url} model={model}")
            doc["services"].append(svc)
            for c in CLAIMS:
                print("-" * 60)
                print(PROMPT_TMPL.format(claim=c["claim"], ask=c["ask"]))
            continue
        if not url:
            svc.update(status="dispatch_failed", error=f"env {url_env} not set (sandbox has no LLM endpoint)")
            doc["services"].append(svc)
            for c in CLAIMS:
                doc["receipts"].append({"claim_id": c["id"], "service": sid, "status": "dispatch_failed",
                                        "error": svc["error"]})
            continue
        doc["services"].append(svc)
        for c in CLAIMS:
            prompt = PROMPT_TMPL.format(claim=c["claim"], ask=c["ask"])
            rec = {"claim_id": c["id"], "service": sid, "asked_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            try:
                text, secs = call(url, model, prompt)
                rec.update(status="ok", latency_s=secs, answer=text,
                           verdict=text.strip().splitlines()[-1] if text.strip() else "")
            except urllib.error.URLError as e:
                rec.update(status="error", error=f"URLError: {e}")
            except Exception as e:  # noqa: BLE001
                rec.update(status="error", error=f"{type(e).__name__}: {e}")
            doc["receipts"].append(rec)
        svc["status"] = "ok" if all(r.get("status") == "ok" for r in doc["receipts"] if r["service"] == sid) else "error"
    ok = sum(1 for r in doc["receipts"] if r.get("status") == "ok")
    doc["ac8_status"] = "satisfied" if ok >= len(CLAIMS) * 2 else ("partial" if ok else "not_satisfied")
    doc["ac8_note"] = f"ok_receipts={ok}, required={len(CLAIMS)*2}"
    if dry:
        return
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(f"written {OUT} ac8_status={doc['ac8_status']} {doc['ac8_note']}")


if __name__ == "__main__":
    main()
