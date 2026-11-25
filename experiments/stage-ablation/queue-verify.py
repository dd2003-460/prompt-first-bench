#!/usr/bin/env python3
"""post-pilot-queue 鉴别力核验（第 24 条防空验证）

队列脚本只记 rc 不 abort、无产物级验证——4 步全失败也会输出 QUEUE-DONE。
本脚本补产物级鉴别力：每步产物 存在 + 新鲜(晚于队列启动) + 非退化(内容非空/记录数达标)。
全 PASS 才是真 DONE；任一 FAIL = 该步空跑/失败，QUEUE-DONE 不可信。

用法: python3 queue-verify.py <queue_log_path>
  从 log 提取 QUEUE-START 时间戳做新鲜度基准。
"""
import json, os, re, sys, time

PFB = "/Users/a1-6/Desktop/workspace/pfb"
SA = os.path.join(PFB, "experiments", "stage-ablation")
BJ = os.path.join(PFB, "modules", "B-pipeline-ablation")

# (步骤名, 产物路径, 非退化检查函数)
CHECKS = [
    ("STEP1 L4-disambig", os.path.join(SA, "runs-s5-sm-l4-disambig.json"),
     lambda p: (lambda d: (len((d.get("answer") or "") or (d.get("nodes") or [])) > 0,
                            "n_nodes=%d final_state=%s" % (len(d.get("nodes", [])), d.get("final_state"))))(json.load(open(p)))),
    ("STEP1 L4-disambig-synth", os.path.join(SA, "runs-s5-sm-l4-disambig-synth.json"),
     lambda p: (lambda d: (len((d.get("answer") or "").strip()) > 0,
                            "answer_len=%d" % len((d.get("answer") or "").strip())))(json.load(open(p)))),
    ("STEP2 gptr summary", os.path.join(SA, "runs-gptr-pfb", "summary.json"),
     lambda p: (lambda d: (len(d) > 0, "%d entries" % len(d)))(json.load(open(p)))),
    ("STEP3 J4 adjudicated", os.path.join(BJ, "tjudge1-llm-fallback-all-adjudicated.json"),
     lambda p: (lambda d: (isinstance(d, list) and len(d) > 0, "%d records" % len(d)))(json.load(open(p)))),
    ("STEP4 armC", os.path.join(PFB, "tasks", "learn-to-think", "exp03-armc", "armc_raw_outputs.json"),
     lambda p: (lambda d: ((lambda n: (n >= 3, "%d samples (预期>=3)" % n))(
         len(d["samples"]) if isinstance(d, dict) and "samples" in d
         else (len(d) if isinstance(d, list) else -1))))(json.load(open(p)))),
]

def main():
    if len(sys.argv) < 2:
        print("用法: queue-verify.py <queue_log_path>")
        sys.exit(2)
    log = sys.argv[1]
    # 新鲜度基准: QUEUE-START 时间戳
    base = time.time()
    m = re.search(r"\[(\d{2}):(\d{2}):(\d{2})\] QUEUE-START", open(log).read())
    if m:
        h, mi, s = map(int, m.groups())
        today = time.localtime()
        base = time.mktime((today.tm_year, today.tm_mon, today.tm_mday, h, mi, s, 0, 0, 0))
        print("新鲜度基准: QUEUE-START %02d:%02d:%02d" % (h, mi, s))
    n_pass = 0
    for name, path, check in CHECKS:
        if not os.path.exists(path):
            print("FAIL  %-24s 产物不存在: %s" % (name, os.path.relpath(path, PFB)))
            continue
        mt = os.path.getmtime(path)
        fresh = mt >= base - 5
        if not fresh:
            print("FAIL  %-24s 产物陈旧(mtime 早于队列启动): %s" % (name, os.path.relpath(path, PFB)))
            continue
        try:
            ok, detail = check(path)
        except Exception as e:
            print("FAIL  %-24s 内容解析失败: %s" % (name, e))
            continue
        if ok:
            n_pass += 1
            print("PASS  %-24s %s" % (name, detail))
        else:
            print("FAIL  %-24s 内容退化: %s" % (name, detail))
    print("\n=== %d/%d PASS ===" % (n_pass, len(CHECKS)))
    if n_pass < len(CHECKS):
        print("QUEUE-DONE 不可信: 有步骤空跑/失败，逐 FAIL 项排查")
        sys.exit(1)
    print("真 DONE: 4 步产物全部存在+新鲜+非退化")

if __name__ == "__main__":
    main()
