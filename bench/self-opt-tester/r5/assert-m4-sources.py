#!/usr/bin/env python3
"""assert-m4-sources.py — RV3G3cdx-m4-assert-lint（r152 U1 机判落地）

判定语义权威源：bench/rubric-v3/m4-independent-source-definition.md §3 U1 规格。
本脚本对该文档 D1-D5 条款做**机械可判子集**的机判；不可机判部分（D1(i) provider
维度在 v2 packet 下、D4 达标裁量）如实降级，不代判。

检查项（§3 U1 (a)(b)(c) + X3 双条件并联，04.5 W2 承接）：
(a) nature 枚举校验 ∈ {external, local-measured, transcription} —— FAIL 级
(b) 同 run 内 source 归一（小写 + 去日期括号）重复 = SIGNAL（疑似同源拆条，D2(γ)/M1）
(c) D2/D3 关键词扫描：
    - nature=transcription ⇒ D2(β) 自动排除（引用即不重查，零新增验证）
    - 「转引|经.*blog|二手」命中 ⇒ D3 折减标记输出（机制生效；conf 上限 0.7 为暂定值，
      待成璐确认——本脚本只标折不改值，不把 0.7 当硬阈值写入任何判定）
    - X3 负向通道陈述排除 = **双条件并联**：conf=null 且 claim/source 含负向关键词
      （不可达/无源/unverified/无外部/无网络）才自动排除；单独任一命中 = SIGNAL 人工复核
(v3 模式追加) provider/channel 字段校验：packet 含 U2 schema v3 字段时执行完整实跑
    （provider 必填非空 str / channel ∈ 四值枚举 / nature-channel 映射冲突 = SIGNAL）；
    v2 存量 packet 缺字段 ⇒ 降级运行（跳过 provider 维度，U3 激活条件），SIGNAL 声明。

用法：python3 assert-m4-sources.py [packet.json ...]
  缺省对象 = r5/evidence-packet-r4-v2.json（v2 存量回归基线）。
exit 0 = 全部 FAIL 级断言通过（SIGNAL 不参与 exit code，signal-only 报告）
exit 1 = 存在 FAIL 级断言失败（打印失败项）
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_PACKETS = [ROOT / "bench/self-opt-tester/r5/evidence-packet-r4-v2.json"]

NATURE_ENUM = {"external", "local-measured", "transcription"}
CHANNEL_ENUM = {"web-search", "llm-receipt", "local-measured", "file-read"}
# nature → 允许 channel 集合（template v3 P6 规则；冲突 = SIGNAL 非 FAIL）
NATURE_CHANNEL_MAP = {
    "transcription": {"llm-receipt", "file-read"},
    "local-measured": {"local-measured", "file-read"},
    "external": {"web-search", "llm-receipt"},
}
# D3 转引标记（定义文档 §1 D3：「转引」「经 <X> blog」「二手」）
RE_TRANSIT = re.compile(r"转引|经\s*\S+\s*blog|二手")
# X3 负向通道陈述关键词（定义文档 §4.2：关键词近似，误排/漏排风险登记在案）
RE_NEGATIVE = re.compile(r"不可达|无源|unverified|无外部|无网络")
# source 归一：小写 + 去日期括号（如 "(2026-06-18)" / "（2026-05-14）"）
RE_DATE_PAREN = re.compile(r"[\(（]\s*\d{4}-\d{2}-\d{2}\s*[\)）]")

failures = []
signals = []  # (label, detail)


def check(label, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(label)


def signal(label, detail):
    print(f"SIGNAL {label} — {detail}")
    signals.append((label, detail))


def normalize_source(src):
    s = RE_DATE_PAREN.sub("", src or "").lower()
    return re.sub(r"\s+", " ", s).strip()


def iter_packets(paths):
    for p in paths:
        p = Path(p)
        if not p.is_file():
            check(f"packet exists: {p}", False, "文件不存在")
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            check(f"packet parseable: {p.name}", False, str(e))
            continue
        runs = data.get("runs", {})
        if not isinstance(runs, dict) or not runs:
            check(f"packet has runs: {p.name}", False, "runs 缺失或为空")
            continue
        yield p, data, runs


def lint_packet(path, data, runs):
    name = path.name
    is_v3 = any(
        isinstance(s, dict) and ("provider" in s or "channel" in s)
        for rd in runs.values()
        for s in (rd.get("P6_cross_validation", {}).get("independent_sources") or [])
    )
    mode = "v3 完整实跑" if is_v3 else "v2 降级运行（provider 维度跳过，U3 激活条件未满足）"
    print(f"\n=== {name} [{mode}] ===")
    if not is_v3:
        signal(f"{name}: schema-version",
               "packet 无 provider/channel 字段 ⇒ 降级运行：D1(i) provider 维度不可机判，"
               "归簇按可判维度 (ii)/(iii)（定义文档 D1 降级态归簇规则）；"
               "U2 schema v3 落地后新 packet 方可完整实跑")

    for run_name in sorted(runs):
        p6 = runs[run_name].get("P6_cross_validation", {})
        sources = p6.get("independent_sources") or []
        tag = f"{name}:{run_name}"

        # ---- (a) nature 枚举校验 ----
        for i, s in enumerate(sources):
            nat = s.get("nature")
            check(f"{tag}[{i}] nature ∈ enum", nat in NATURE_ENUM, f"got {nat!r}")

        # ---- (b) source 归一重复 = SIGNAL ----
        seen = {}
        for i, s in enumerate(sources):
            key = normalize_source(s.get("source"))
            if key in seen:
                signal(f"{tag}[{i}] source-dup",
                       f"与 [{seen[key]}] 归一后相同（{key[:60]!r}…）⇒ 疑似同源拆条（D2(γ)/回测 M1）")
            else:
                seen[key] = i

        # ---- (c) D2/D3/X3 关键词扫描 ----
        for i, s in enumerate(sources):
            nat = s.get("nature")
            conf = s.get("conf")
            text = " ".join(str(s.get(k) or "") for k in ("claim", "source"))
            if nat == "transcription":
                signal(f"{tag}[{i}] D2-beta-exclude",
                       "nature=transcription ⇒ 上轮回执转录，自动排除不计独立源（引用即不重查）")
            m = RE_TRANSIT.search(text)
            if m:
                signal(f"{tag}[{i}] D3-transit-mark",
                       f"转引标记命中 {m.group(0)!r} ⇒ D3 折减标记（机制生效；conf 上限 0.7 为暂定值待裁定，本脚本不改值）")
            neg_hit = bool(RE_NEGATIVE.search(text))
            null_conf = conf is None
            if null_conf and neg_hit:
                signal(f"{tag}[{i}] X3-exclude",
                       "conf=null 且负向通道关键词命中 ⇒ 双条件并联成立，自动排除（负向陈述非验证条目）")
            elif null_conf != neg_hit:
                signal(f"{tag}[{i}] X3-review",
                       f"仅单条件命中（conf_null={null_conf}, kw={neg_hit}）⇒ 不自动排除，SIGNAL 人工复核")

        # ---- v3 追加：provider/channel 字段校验 ----
        if is_v3:
            for i, s in enumerate(sources):
                prov = s.get("provider")
                ch = s.get("channel")
                check(f"{tag}[{i}] provider 必填非空 str",
                      isinstance(prov, str) and prov.strip() != "", f"got {prov!r}")
                check(f"{tag}[{i}] channel ∈ enum", ch in CHANNEL_ENUM, f"got {ch!r}")
                nat = s.get("nature")
                if nat in NATURE_CHANNEL_MAP and ch in CHANNEL_ENUM and ch not in NATURE_CHANNEL_MAP[nat]:
                    signal(f"{tag}[{i}] nature-channel-conflict",
                           f"nature={nat!r} 与 channel={ch!r} 映射冲突（template v3 P6 规则）⇒ 人工复核")


def main(argv):
    paths = argv or DEFAULT_PACKETS
    n_packets = 0
    for path, data, runs in iter_packets(paths):
        n_packets += 1
        lint_packet(path, data, runs)

    print(f"\n=== {len(failures)} FAIL / {len(signals)} SIGNAL（{n_packets} packet）===")
    if failures:
        print("FAIL 项：")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print("PASS（SIGNAL 为 signal-only 报告，不参与 exit code）")
    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])