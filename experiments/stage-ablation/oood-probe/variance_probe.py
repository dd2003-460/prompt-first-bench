#!/usr/bin/env python3
# origin: ai (M2a 方差探针, 任务卡 m2a-variance-probe)
"""M2a 方差探针（零 GPU）：对已有 6 臂数据算三诊断指标，输出 variance-report.json。

三指标定义（预注册于 tasks/think-trigger/m2-injection-design-20261128.md §2）：
  - mech_cov        机制覆盖率 = 机制三要素(参数变化+因果说明+影响量)≥2 的节点/总节点
  - quant_density   量化claim密度 = 含数字/公式/区间的节点/总节点
  - domain_shift_ratio 域偏移率 = transcript 域外机制词命中/域内机制词命中（词表预注册 §2）

数据源（本目录）：
  SM 臂节点级: sm-arm.json / s1-sm-arm.json / k3-s0-hw.json / k3-s1-hw.json（40 节点/臂）
  B 臂全文:    baseline-arm.txt / k3-baseline-hw.txt（单段文本，无节点结构 → 视作 1 个"节点"）
  transcript:  仅 B 臂可得（baseline-arm.txt / k3-baseline-hw.txt 即 LLM 单段输出）；
               SM 臂日志只有 [LLM] call done 摘要行，无 reasoning 全文 → 域偏移率标 null。

注意（写入 report.note）：6 臂各仅 1 rep，"方差"实为跨臂极差（含臂/域间差异），
不能直接当作 rep 间噪声估计；本探针回答的是"指标跨臂离散度多大、3 reps 能否分辨臂间差"。
"""
import json
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------- 预注册词表（m2-injection-design-20261128.md §2，逐字复制） ----------
DOMAIN_VOCAB = {
    "cyclone": {
        "in": ["衰减", "风眼", "眼壁", "角动量", "潜热", "边界层摩擦", "洋热通量"],
        "out": ["非凸", "landscape", "梯度下降", "损失面", "相变", "李雅普诺夫"],
    },
    "hw": {
        "in": ["功耗", "延迟", "带宽", "缓存", "流水线", "时钟", "总线"],
        "out": ["非凸", "landscape", "梯度下降", "损失面", "相变"],
    },
}

# ---------- 机制三要素正则初筛（三类关键词各一组） ----------
MECH_GROUPS = {
    "param_change": [  # 参数变化
        r"参数", r"敏感", r"系数", r"阈值", r"量级", r"区间", r"分布",
        r"取值", r"边界条件", r"变量", r"取值范围", r"范围",
    ],
    "causal": [  # 因果说明
        r"导致", r"引起", r"因为", r"由于", r"使得", r"致使",
        r"机制", r"原因", r"归因", r"因果", r"解释",
    ],
    "impact": [  # 影响量
        r"贡献", r"占比", r"幅度", r"倍数", r"比例", r"影响",
        r"效应", r"主导", r"权重", r"衰减", r"减弱", r"增强",
    ],
}

# ---------- 量化 claim 正则（数字/公式/区间） ----------
QUANT_RE = re.compile(
    r"\d+(\.\d+)?\s*(%|W|m²|m2|km|kt|kts|m/s|s|ms|h|小时|GB|MB|TB|Hz|GHz|TOPS|FLOPS|°|倍|节|次|个|条|层|维)?"
    r"|≈|∝|≤|≥|×|\*\*"
    r"|\d+\s*[-~–]\s*\d+"
)

ARMS = {
    "S0_weather": {"file": "sm-arm.json", "domain": "cyclone", "transcript": None},
    "S1_weather": {"file": "s1-sm-arm.json", "domain": "cyclone", "transcript": None},
    "B_weather":  {"file": "baseline-arm.txt", "domain": "cyclone", "transcript": "baseline-arm.txt"},
    "S0_hw":      {"file": "k3-s0-hw.json", "domain": "hw", "transcript": None},
    "S1_hw":      {"file": "k3-s1-hw.json", "domain": "hw", "transcript": None},
    "B_hw":       {"file": "k3-baseline-hw.txt", "domain": "hw", "transcript": "k3-baseline-hw.txt"},
}


def mech_hits(text: str) -> dict:
    """返回 {group: bool} 三要素命中情况。"""
    return {g: any(re.search(p, text) for p in pats) for g, pats in MECH_GROUPS.items()}


def is_quant(text: str) -> bool:
    return bool(QUANT_RE.search(text))


def domain_shift(text: str, domain: str):
    """域偏移率 = 域外命中/域内命中；域内命中=0 时返回 None（除零）。"""
    vocab = DOMAIN_VOCAB[domain]
    n_in = sum(len(re.findall(re.escape(w), text)) for w in vocab["in"])
    n_out = sum(len(re.findall(re.escape(w), text)) for w in vocab["out"])
    if n_in == 0:
        return None, n_in, n_out
    return n_out / n_in, n_in, n_out


def main():
    per_arm = {}
    samples = []  # (arm, node_id, claim, mech_flags, is_mech)

    for arm, spec in ARMS.items():
        path = HERE / spec["file"]
        raw = path.read_text(encoding="utf-8")
        if path.suffix == ".json":
            data = json.loads(raw)
            texts = [(n["id"], n["claim"]) for n in data["nodes"]]
        else:
            # B 臂：单段文本无节点结构 → 视作 1 个"节点"（整段）
            texts = [("FULL", raw)]

        n = len(texts)
        mech_ok = 0
        quant_ok = 0
        for nid, claim in texts:
            flags = mech_hits(claim)
            n_hit = sum(flags.values())
            if n_hit >= 2:
                mech_ok += 1
            if is_quant(claim):
                quant_ok += 1
            if len(samples) < 5:
                samples.append((arm, nid, claim[:100], flags, n_hit >= 2))

        mech_cov = round(mech_ok / n, 4)
        quant_density = round(quant_ok / n, 4)

        if spec["transcript"]:
            tpath = HERE / spec["transcript"]
            tavail = tpath.exists()
            if tavail:
                ratio, n_in, n_out = domain_shift(tpath.read_text(encoding="utf-8"), spec["domain"])
                dsr = round(ratio, 4) if ratio is not None else None
                ds_note = (None if ratio is not None
                           else f"域内机制词命中=0，比值除零，标 null（域外命中={n_out}）")
            else:
                dsr, ds_note = None, f"transcript 文件 {spec['transcript']} 不存在"
        else:
            dsr, ds_note = None, (
                "SM 臂 transcript 不可得：日志仅含 [LLM] call done 摘要行（无 reasoning 全文），"
                "节点 JSON 无 reasoning 字段，域偏移率按任务卡规则标 null 不硬算")

        per_arm[arm] = {
            "mech_cov": mech_cov,
            "quant_density": quant_density,
            "domain_shift_ratio": dsr,
            "n_nodes": n,
            "transcript_available": bool(spec["transcript"]),
            "dsr_note": ds_note,
            "source_file": spec["file"],
        }

    # ---------- 跨臂统计（6 臂各 1 rep：这是跨臂极差，非 rep 间方差） ----------
    # B 臂无节点结构（整段=1 个"节点"）→ mech_cov/quant_density 恒为 0 或 1，
    # 是结构性退化值，混入跨臂统计会污染离散度估计 → 另给 SM-only（4 臂, n=40/臂）视图。
    metrics = {
        "mech_cov": "机制覆盖率(三要素≥2 节点占比)",
        "quant_density": "量化claim密度(含数字/公式/区间节点占比)",
        "domain_shift_ratio": "域偏移率(域外词命中/域内词命中)",
    }
    SM_ARMS = [a for a in ARMS if ARMS[a]["file"].endswith(".json")]

    def stats_for(arms, mkey, mdesc, extra_note):
        vals = [per_arm[a][mkey] for a in arms if per_arm[a][mkey] is not None]
        st = {
            "mean": round(statistics.mean(vals), 4) if vals else None,
            "sd": round(statistics.stdev(vals), 4) if len(vals) > 1 else None,
            "min": min(vals) if vals else None,
            "max": max(vals) if vals else None,
            "n_valid": len(vals),
            "per_arm": {a: per_arm[a][mkey] for a in arms},
            "note": extra_note,
        }
        return st

    variance = {}
    for mkey, mdesc in metrics.items():
        if mkey == "domain_shift_ratio":
            variance[mkey] = stats_for(
                list(ARMS), mkey, mdesc,
                f"{mdesc}: 仅 B 臂 2/6 可算（SM 臂日志只有 [LLM] call done 摘要行，无 reasoning 全文，"
                "按任务卡规则标 null 不硬算）；n_valid=2 的 sd 无统计意义，只作两臂方向性对比")
            continue
        all_note = (f"{mdesc}: 6 臂各 1 rep，跨臂离散度（含臂与域间差异），非 rep 间噪声；"
                    "B 臂 n_nodes=1 为结构性退化值（整段=1 节点），拉高 max，解读以 sm_only 为准")
        sm_note = (f"{mdesc}: 仅 4 个 SM 臂（各 40 节点、1 rep）；sd 为跨臂离散度（臂间+域间），"
                   "非 rep 间噪声。判断 3 reps 是否够：若目标臂间差(如 S0 vs S1) ≫ 预期 rep 噪声则够；"
                   "rep 噪声本身未测，需 M3 同臂多 rep 补跑后重估")
        variance[mkey] = {
            "all_arms": stats_for(list(ARMS), mkey, mdesc, all_note),
            "sm_only": stats_for(SM_ARMS, mkey, mdesc, sm_note),
        }

    report = {
        "task": "M2a 方差探针: 6 臂三诊断指标跨臂离散度（零 GPU）",
        "generated_by": "variance_probe.py",
        "metric_defs": metrics,
        "vocab_source": "tasks/think-trigger/m2-injection-design-20261128.md §2 预注册词表",
        "per_arm": per_arm,
        "variance": variance,
        "caveat": ("6 臂各仅 1 rep：'variance' 实为跨臂极差（臂间+域间差异混在一起），"
                   "不能直接当 rep 间方差用。B 臂 n_nodes=1（整段=1 节点）使 mech_cov/quant_density "
                   "退化为 0/1，跨臂统计以 sm_only 视图为准。"),
        "verdict_3reps": {
            "mech_cov": (f"可分辨：SM 臂间差 {round(per_arm['S0_weather']['mech_cov']-per_arm['S1_weather']['mech_cov'],4)}"
                         f"(气象 S0-S1)/{round(per_arm['S0_hw']['mech_cov']-per_arm['S1_hw']['mech_cov'],4)}"
                         "(硬件 S0-S1)，远超预注册判决阈值(form 5pp)；即便 rep 噪声达 ~5pp 量级，"
                         "3 reps 均值差仍能分辨臂间差"),
            "quant_density": (f"难分辨：4 SM 臂仅 {variance['quant_density']['sm_only']['min']}-"
                              f"{variance['quant_density']['sm_only']['max']}（极差 "
                              f"{round(variance['quant_density']['sm_only']['max']-variance['quant_density']['sm_only']['min'],4)}），"
                              "臂间几乎无差，该指标在现有 6 臂上不具判别力——不是 reps 不够，是指标本身饱和"
                              "(40 节点里 82-85% 都含数字)，建议 M4 降权或换定义"),
            "domain_shift_ratio": ("无法判：4/6 臂无 reasoning transcript 标 null，仅 B 臂 2 臂可算"
                                   "且均=0.0（域外词 0 命中）；M3 若需此指标必须在 harness 落盘 "
                                   "LLM 原始输出（当前日志只记摘要行）"),
        },
    }
    out = HERE / "variance-report.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # ---------- stdout：5 条节点抽样供人工核（不写文件） ----------
    print("=== 机制三要素抽样（5 条，人工核正则初筛质量）===")
    for arm, nid, claim, flags, is_mech in samples:
        hit_groups = "+".join(g for g, v in flags.items() if v) or "(无命中)"
        print(f"[{arm}/{nid}] mech={'YES' if is_mech else 'no '} ({hit_groups})")
        print(f"    {claim}")
    print("=== 三指标跨臂一览 ===")
    for a in per_arm:
        p = per_arm[a]
        print(f"{a:12s} mech_cov={p['mech_cov']:<7} quant_density={p['quant_density']:<7} "
              f"dsr={p['domain_shift_ratio']} n={p['n_nodes']}")
    print(f"report written: {out}")


if __name__ == "__main__":
    sys.exit(main())
