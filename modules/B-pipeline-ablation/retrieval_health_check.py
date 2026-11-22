#!/usr/bin/env python3
"""retrieval_health_check.py — 检索通道健康度哨兵 (2026-11-23)

背景: research_hook 多通道检索会静默失败(返回空源, 不抛异常), run 正常完成
但 70-90% search 节点无源 (idea2 r3 窗口事故, 见 T-JUDGE-1-L3-20261123.md §7)。
本脚本对已落盘的 run 做事后健康度检查:
  - SITE-WL 日志行数 (stdout 里检索白名单过滤行, 健康 run 应有数十行)
  - search 节点空源率 (run JSON 里 retrieval_sources 为空的占比)
阈值: 空源率 > 50% 或 SITE-WL < 5 → FLAG (该 run 的 vsr/post_retrieval_accuracy
等检索依赖指标不可信, 需排除或重跑)。

用法:
  python3 retrieval_health_check.py <run.json> <run.stdout> [...]
  python3 retrieval_health_check.py --dir <rep-scan 目录>   (批量)
"""
import sys, os, json, glob, re

THRESH_EMPTY = 0.50   # 空源率阈值
THRESH_WL = 5         # SITE-WL 行数下限


def check_one(rj, rs):
    d = json.load(open(rj))
    s = [n for n in d.get("nodes", []) if n.get("source") == "search"]
    e = [n for n in s if not (n.get("retrieval_sources") or [])]
    empty_rate = len(e) / len(s) if s else 0.0
    wl = 0
    if os.path.exists(rs):
        wl = open(rs, encoding="utf-8", errors="ignore").read().count("SITE-WL")
    flag = (empty_rate > THRESH_EMPTY) or (wl < THRESH_WL)
    return {
        "run": os.path.basename(rj),
        "n_search": len(s),
        "empty": len(e),
        "empty_rate": round(empty_rate, 3),
        "site_wl_lines": wl,
        "FLAG": flag,
    }


def main():
    args = sys.argv[1:]
    rows = []
    if args and args[0] == "--dir":
        d = args[1]
        for rj in sorted(glob.glob(os.path.join(d, "rep-*.json"))):
            rs = re.sub(r"-\d{8}-\d{6}\.json$", ".stdout", rj)
            rows.append(check_one(rj, rs))
    else:
        for i in range(0, len(args) - 1, 2):
            rows.append(check_one(args[i], args[i + 1]))
    n_flag = 0
    for r in rows:
        mark = "FLAG" if r["FLAG"] else "ok  "
        if r["FLAG"]:
            n_flag += 1
        print(f"{mark} {r['run']:32s} search={r['n_search']:4d} "
              f"empty={r['empty_rate']:.0%} SITE-WL={r['site_wl_lines']}")
    print(f"\n{n_flag}/{len(rows)} flagged (阈值: 空源率>{THRESH_EMPTY:.0%} 或 SITE-WL<{THRESH_WL})")
    sys.exit(1 if n_flag else 0)


if __name__ == "__main__":
    main()
