#!/usr/bin/env python3
"""M1a: 提取 OOD 探针六臂注入前机械指标基线 (零判断, 只搬运+整理).

源文件 (6):
  metrics-2x2.json          K4a 六臂机械记分聚合 (最新, 2026-11-27T22:49)
  metrics-s0-cyclone.json   P2 S0 cyclone 臂记分
  metrics-s1-cyclone.json   P2 S1 cyclone 臂记分
  k3-baseline-hw.json       K3 B 臂 hw 元数据 (chars/sec)
  k3-s0-hw.json             K3 S0 hw 臂 SM 树
  k3-s1-hw.json             K3 S1 hw 臂 SM 树

确定性规则 (非判断): 同一字段出现在多个源文件且数值不一致时,
取 mtime 最新的文件的值, 并向 stdout 打印 CONFLICT 警告 (供人工复核).
幂等: 输出纯由 6 个源文件决定, 重跑结果相同 (覆盖写).
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    with open(os.path.join(BASE, name), encoding="utf-8") as f:
        return json.load(f)


def mtime(name):
    return os.path.getmtime(os.path.join(BASE, name))


def pick(candidates):
    """candidates: [(filename, value), ...]; value 为 None 的候选跳过."""
    avail = [(fn, v) for fn, v in candidates if v is not None]
    if not avail:
        return None
    vals = set(v for _, v in avail)
    if len(vals) > 1:
        chosen = max(avail, key=lambda fv: mtime(fv[0]))[1]
        print("CONFLICT %s: %s -> 取 %r (mtime 最新)" % (vals, avail, chosen))
        return chosen
    return avail[0][1]


def main():
    m22 = load("metrics-2x2.json")
    s0c = load("metrics-s0-cyclone.json")
    s1c = load("metrics-s1-cyclone.json")
    k3b = load("k3-baseline-hw.json")
    k3s0 = load("k3-s0-hw.json")
    k3s1 = load("k3-s1-hw.json")

    a = m22["arms"]
    uc = m22["hardware_unit_cov"]["unit_cov"]
    gc = m22["hardware_unit_cov"]["gate_cov"]
    mc = m22["weather_mech"]["mech_cov"]

    F22 = "metrics-2x2.json"
    FS0 = "metrics-s0-cyclone.json"
    FS1 = "metrics-s1-cyclone.json"
    FBH = "k3-baseline-hw.json"
    FS0H = "k3-s0-hw.json"
    FS1H = "k3-s1-hw.json"

    arms = {
        "s0_cyclone": {
            "domain": "cyclone",
            "llm_calls": pick([(F22, a["S0_weather"]["llm_calls"]),
                               (FS0, s0c["sm_llm_calls"])]),
            "wall_s": pick([(F22, a["S0_weather"]["wall_sec"]),
                            (FS0, s0c["sm_wall_sec"])]),
            "mech_cov": pick([(F22, mc["S0_weather"]),
                              (FS0, s0c["sm_mech_cov"])]),
            "quant_claims": pick([(F22, a["S0_weather"]["quant_claims"]),
                                  (FS0, s0c["sm_quant_claims"])]),
            "unit_cov": None,
            "gate_cov": None,
            "source_files": [F22, FS0],
        },
        "s1_cyclone": {
            "domain": "cyclone",
            "llm_calls": pick([(F22, a["S1_weather"]["llm_calls"]),
                               (FS1, s1c["sm_llm_calls"])]),
            "wall_s": pick([(F22, a["S1_weather"]["wall_sec"]),
                            (FS1, s1c["sm_wall_sec"])]),
            "mech_cov": pick([(F22, mc["S1_weather"]),
                              (FS1, s1c["sm_mech_cov"])]),
            "quant_claims": pick([(F22, a["S1_weather"]["quant_claims"]),
                                  (FS1, s1c["sm_quant_claims"])]),
            "unit_cov": None,
            "gate_cov": None,
            "source_files": [F22, FS1],
        },
        "baseline_cyclone": {
            "domain": "cyclone",
            "llm_calls": pick([(F22, a["B_weather"]["llm_calls"])]),
            "wall_s": pick([(F22, a["B_weather"]["wall_sec"])]),
            "mech_cov": pick([(F22, mc["B_weather"]),
                              (FS0, s0c["base_mech_cov"])]),
            "quant_claims": pick([(F22, a["B_weather"]["quant_claims"]),
                                  (FS0, s0c["base_quant_claims"])]),
            "unit_cov": None,
            "gate_cov": None,
            "source_files": [F22, FS0],
        },
        "s0_hw": {
            "domain": "hardware",
            "llm_calls": pick([(F22, a["S0_hw"]["llm_calls"])]),
            "wall_s": pick([(F22, a["S0_hw"]["wall_sec"]),
                            (FS0H, k3s0["wall_sec"])]),
            "mech_cov": None,
            "quant_claims": pick([(F22, a["S0_hw"]["quant_claims"])]),
            "unit_cov": pick([(F22, uc["S0_hw"]["covered"])]),
            "gate_cov": pick([(F22, gc["S0_hw"]["covered"])]),
            "source_files": [F22, FS0H],
        },
        "s1_hw": {
            "domain": "hardware",
            "llm_calls": pick([(F22, a["S1_hw"]["llm_calls"])]),
            "wall_s": pick([(F22, a["S1_hw"]["wall_sec"]),
                            (FS1H, k3s1["wall_sec"])]),
            "mech_cov": None,
            "quant_claims": pick([(F22, a["S1_hw"]["quant_claims"])]),
            "unit_cov": pick([(F22, uc["S1_hw"]["covered"])]),
            "gate_cov": pick([(F22, gc["S1_hw"]["covered"])]),
            "source_files": [F22, FS1H],
        },
        "baseline_hw": {
            "domain": "hardware",
            "llm_calls": pick([(F22, a["B_hw"]["llm_calls"])]),
            "wall_s": pick([(F22, a["B_hw"]["wall_sec"]),
                            (FBH, k3b[0]["sec"])]),
            "mech_cov": None,
            "quant_claims": pick([(F22, a["B_hw"]["quant_claims"])]),
            "unit_cov": pick([(F22, uc["B_hw"]["covered"])]),
            "gate_cov": pick([(F22, gc["B_hw"]["covered"])]),
            "source_files": [F22, FBH],
        },
    }

    out = {"arms": arms}
    outpath = os.path.join(BASE, "baseline-pre-injection.json")
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("WROTE %s (%d arms)" % (outpath, len(arms)))


if __name__ == "__main__":
    main()
