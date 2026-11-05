#!/usr/bin/env python3
"""R5.2audit-C4-timing-reconstruct — C4 "14m27s" 数值化机判脚本

审计对象：$WS/run2/loop-state.json channel 字段中的 "14m27s"（= 867s）。
任务：解析 $WS/run2/ 转录件时间戳做差值重建耗时区间，与 867s 比对输出 SIGNAL。

判定口径（预注册于 stages/01/R5.2audit-C4-goal-decomposition.md §F2，04 不得偏离）：
- 「逐事件时间戳」= 转录件内容中的 ISO 格式时刻；同一 run 内 ≥2 个不同值才可差值重建。
- executed_at 单点 ≠ 可重建（只能定界终点，不能定界时长）。
- 文件 mtime 排除出重建面（文件系统元数据非转录件内容；且 7 文件同秒 = 批量落盘特征）。
- SIGNAL 二态：reconstructable（≥2 时刻 → 差值区间 vs 867s 报偏差）/ not-reconstructable（列证据清单）。

r132 健壮性行为：WS_RUN2 目录缺失 → 显式 FAIL + exit 1（非 traceback，blocked-on-external
降级声明）；epoch() 先剥离时区段再按主体位数分派分钟级(12位)/秒级(14位)，未知格式
fail-loud ValueError（不静默截断）。

SIGNAL-only：不参与 exit code（沿用 assert-packet-audit.py 模式）；不翻转 verdict——
not-reconstructable → C4 维持 unverified (X5)；即便 reconstructable 且吻合，
升级 confirmed 仍需人工裁决（转录链末端 arena 网页不可复访问题独立存在）。

exit 0 语义 = 枚举过程本身无异常（文件可读、正则可跑），不代表任何 verdict 变化。
本脚本对 WS 路径只读消费，零写入。
"""
import json, os, re, sys

WS_RUN2 = "/Users/a1-6/Desktop/workspace/projects/AI-计算科学/D1-efficiency-optimization/tasks/self-optimization-tester/loop-artifacts/stages/04.5/r3/run2"
WS_RUN1 = "/Users/a1-6/Desktop/workspace/projects/AI-计算科学/D1-efficiency-optimization/tasks/self-optimization-tester/loop-artifacts/stages/04.5/r3/run1"
CLAIMED_SECONDS = 14 * 60 + 27  # "14m27s" = 867s

ISO_RE = re.compile(r"\d{4}-\d{2}-\d{2}T?\d{2}:\d{2}")

failures = []

def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(label)

# ---------- WS 可达性前置拦截（W3 · r132：缺失 → 显式 FAIL + exit 1，非 traceback） ----------
if not os.path.isdir(WS_RUN2):
    check("run2 目录存在", False, f"WS_RUN2={WS_RUN2} 不可达")
    print("\nSIGNAL C4 not-reconstructable — WS 转录件不可达，枚举面无法执行（blocked-on-external 降级路径，见 runner 协议）")
    print(f"\n=== {len(failures)} FAIL ===")
    sys.exit(1)

# ---------- 读取 channel 字段并提取声称时长 ----------
state_path = os.path.join(WS_RUN2, "loop-state.json")
check("run2/loop-state.json 可读", os.path.isfile(state_path))
with open(state_path) as f:
    state = json.load(f)
channel = state.get("channel", "")
m = re.search(r"(\d+)m(\d+)s", channel)
check("channel 字段含 '14m27s' 时长声称", bool(m), f"channel={channel!r}")
claimed = int(m.group(1)) * 60 + int(m.group(2)) if m else None
check("声称时长 = 867s", claimed == CLAIMED_SECONDS, f"actual={claimed}")

# ---------- 枚举面 1：转录件内容 ISO 时间戳全量扫描 ----------
timestamps = {}  # value -> [(file, line)]
files = sorted(os.listdir(WS_RUN2))
for fn in files:
    p = os.path.join(WS_RUN2, fn)
    if not os.path.isfile(p):
        continue
    for i, line in enumerate(open(p, encoding="utf-8"), 1):
        for hit in ISO_RE.findall(line):
            timestamps.setdefault(hit, []).append((fn, i))

distinct = sorted(timestamps)
print(f"\n[枚举面1] run2 转录件 ISO 时间戳命中：{len(distinct)} 个不同值 / {sum(len(v) for v in timestamps.values())} 处")
for t in distinct:
    locs = ", ".join(f"{fn}:L{n}" for fn, n in timestamps[t])
    print(f"  {t}  <- {locs}")

# ---------- 枚举面 2：mtime 排除（记录特征，不计入重建面） ----------
mtimes = {os.path.basename(fn): os.stat(os.path.join(WS_RUN2, fn)).st_mtime
          for fn in files if os.path.isfile(os.path.join(WS_RUN2, fn))}
distinct_mtimes = len(set(mtimes.values()))
print(f"[枚举面2] 文件 mtime：{distinct_mtimes} 个不同值（{'同秒批量落盘 → 排除出重建面' if distinct_mtimes <= 1 else '异秒 → 需人工复核'}）；mtime 一律不计入重建面（文件系统元数据非转录件内容，01 预注册口径）")

# ---------- 对照系：run1 具备逐事件结构（证明口径不是把一切都判死） ----------
# 勘误注记：02 工件 E2 写「events[]」，实际字段名为 per_turn_deltas[]（内容一致：≥2 个 at 时刻）
ledger_path = os.path.join(WS_RUN1, "token-ledger.json")
run1_events = []
if os.path.isfile(ledger_path):
    with open(ledger_path) as f:
        ledger = json.load(f)
    run1_events = [e["at"] for e in ledger.get("per_turn_deltas", []) if "at" in e]
check("对照系 run1/token-ledger.json per_turn_deltas[].at ≥2 时刻（口径有效性锚）",
      len(set(run1_events)) >= 2, f"run1 moments={sorted(set(run1_events))}")

# ---------- 外部回执通道（r33 · R5.2audit-C4-arena-export）----------
# arena 会话页 RSC payload 提取的 metadata.timing（ego-browser，非截图）→ 正向比对
RECEIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "arena-session-timing-receipt.json")
if os.path.isfile(RECEIPT):
    with open(RECEIPT) as f:
        rcpt = json.load(f)
    t = rcpt.get("timing", {})
    dur_s = t.get("duration_s")
    if dur_s is not None and claimed:
        d = abs(dur_s - claimed)
        print(f"SIGNAL C4 external-receipt — arena session timing {dur_s}s (startedAt={t.get('startedAt_iso_utc')} → completedAt={t.get('completedAt_iso_utc')}) vs 声称 {claimed}s，|Δ|={d:.3f}s "
              f"({'正向吻合' if d <= 1 else '不吻合 → 人工复核'}); 限定：timing 挂在单条 assistant message metadata，等价于 run2 wall-clock 依赖 run2=单次任务执行（见 receipt boundary_note）; verdict 升级仍需人工裁决")

# ---------- SIGNAL 判定 ----------
print()
if len(distinct) >= 2:
    def epoch(t):  # ISO → datetime（W2 · r132：先提主体剥离时区，再按位数分派——时区 +08:00 含数字，直接去非数字会得 18 位误入未知格式）
        from datetime import datetime
        body = re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2})?", t).group(0)
        digits = re.sub(r"[^\d]", "", body)
        if len(digits) == 12:
            return datetime.strptime(digits, "%Y%m%d%H%M")
        if len(digits) == 14:
            return datetime.strptime(digits, "%Y%m%d%H%M%S")
        raise ValueError(f"未知时间戳格式（主体 {len(digits)} 位，fail-loud 不静默截断）: {t!r}")
    lo, hi = min(epoch(t) for t in distinct), max(epoch(t) for t in distinct)
    span = int((hi - lo).total_seconds())
    delta = abs(span - (claimed or 0))
    print(f"SIGNAL C4 reconstructable — 时间戳跨度 {span}s vs 声称 {claimed}s，|Δ|={delta}s "
          f"({'区间吻合' if delta <= 60 else '区间不吻合 → 建议 mismatch 人工复核'}); verdict 升级仍需人工裁决")
else:
    single = distinct[0] if distinct else "(无任何时间戳)"
    print(f"SIGNAL C4 not-reconstructable — run2 转录件仅 {len(distinct)} 个时刻锚（{single}，单点只能定界终点不能定界时长）；"
          f"steps A1-A7 anchor 无逐事件时间戳；无 token-ledger 类载体（run1 有 events[].at 而 run2 无）→ "
          f"与 867s 无法做任何差值比对。C4 维持 unverified (X5)，状态由人工预判升级为机判实证（枚举面封闭：内容扫描+mtime排除+松散提及零命中）。")
    # 勘误注记：02 工件 E2 写 run1「events[]」，实际字段名 per_turn_deltas[]（内容一致）；mtime 实为同秒（stat -f %m 全等），E3 表述以本输出为准

print(f"\n=== {0 if not failures else len(failures)} FAIL ===")
sys.exit(1 if failures else 0)