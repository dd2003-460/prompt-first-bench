#!/usr/bin/env python3
"""R7 · hard-constraint 保全校验器

压缩可以删字，不可以删规则。本脚本把 7 个核心文件里**必须存在**的规范化约束
逐条 grep 一遍，任何一条缺失即 exit 1 —— 用于「宁可少压不可错压」的机检。

清单来源：R7 之前（commit 0b59c40）的 7 个文件逐条人工提取的 normative 句；
每条给出「约束语义」+「可接受的措辞片段集合（任一命中即可）」。

用法：python3 verify-constraints.py [--json]
退出码：0 = 全部保留；1 = 有缺失
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
LOOP = REPO / "loop" / "prompt-first"

# (文件, 约束 ID, 语义, 可接受片段[])
CHECKS = [
    # ---- 00 通用 ----
    ("00-common-review.md", "C01", "回退不豁免 loop：6 阶段一个不少", ["6 阶段一个不少"]),
    ("00-common-review.md", "C02", "只做当前阶段", ["只做当前阶段"]),
    ("00-common-review.md", "C03", "Reviewer 回执是唯一质量输入", ["唯一质量输入"]),
    ("00-common-review.md", "C04", "Commander 不得覆盖 revise", ["不得用自己判断覆盖 revise"]),
    ("00-common-review.md", "C05", "只有 pass 才能写完成标记", ["返回 pass 才能写完成标记"]),
    ("00-common-review.md", "C06", "不得手写 stage-review / verdict", ["不得手写 `stage-review`"]),
    ("00-common-review.md", "C07", "禁止循环思考", ["禁止**循环思考"]),
    ("00-common-review.md", "C08", "不得硬编码模型参数", ["不得硬编码"]),
    ("00-common-review.md", "C09", "不确定是否达标必须 revise", ["不确定是否达标"]),
    ("00-common-review.md", "C10", "repair_stage 指向需补输入的阶段", ["repair_stage"]),
    ("00-common-review.md", "C11", "路由块格式", ["verdict: pass", "verdict: revise", "repair_stage:"]),
    ("00-common-review.md", "C12", "只有阻塞缺陷可 revise", ["只有前者触发 revise"]),

    # ---- 01 ----
    ("01-goal-decomposition.md", "C13", "正交且覆盖的分解", ["正交", "覆盖"]),
    ("01-goal-decomposition.md", "C14", "三类条件（已提供/可推导/需研究）", ["人类已提供", "仍需研究"]),
    ("01-goal-decomposition.md", "C15", "未知不得伪装成默认值", ["不得把未知伪装成默认值"]),
    ("01-goal-decomposition.md", "C16", "递归到原子 + 停止条件", ["叶子", "不能再分解"]),
    ("01-goal-decomposition.md", "C17", "候选集冻结（防漂移）", ["候选集冻结", "冻结集合"]),
    ("01-goal-decomposition.md", "C18", "候选集漂移 = revise, repair_stage 01", ["repair_stage` 写 01"]),
    ("01-goal-decomposition.md", "C19", "复合空缺须拆子问题", ["复合空缺"]),
    ("01-goal-decomposition.md", "C20", "未验证不得写成确定事实", ["确定事实"]),
    ("01-goal-decomposition.md", "C21", "预算以用户总预算为约束", ["总预算为约束"]),

    # ---- 02 ----
    ("02-information-research.md", "C22", "只围绕 01 空缺搜集", ["只围绕这些空缺"]),
    ("02-information-research.md", "C23", "网页 LLM 只提供线索不是事实来源", ["不是事实来源"]),
    ("02-information-research.md", "C24", "来源记录六要素", ["URL", "发布/更新时间", "实际观察时间", "不确定性"]),
    ("02-information-research.md", "C25", "≥2 独立来源", ["2 个相互独立来源"]),
    ("02-information-research.md", "C26", "易变事实 7 天窗口", ["最近 7 天内"]),
    ("02-information-research.md", "C27", "失败不是证据", ["不是证据"]),
    ("02-information-research.md", "C28", "WebSearch 最多换一次关键词", ["最多换一次关键词"]),
    ("02-information-research.md", "C29", "WebFetch 上限 4 个 URL", ["最多 4 个"]),
    ("02-information-research.md", "C30", "本阶段不写最终推荐", ["不写最终推荐"]),
    ("02-information-research.md", "C31", "证据来源完备：URL+时间戳缺一降级", ["快照时间戳", "存在性断言-未核验"]),

    # ---- 02.5 ----
    ("02.5-cross-check.md", "C32", "不强行收敛", ["不强行收敛"]),
    ("02.5-cross-check.md", "C33", "对抗核验", ["对抗核验"]),
    ("02.5-cross-check.md", "C34", "两个硬边界", ["数学理论瓶颈", "个人信息搜集瓶颈"]),
    ("02.5-cross-check.md", "C35", "禁止把对方意见当终局", ["禁止把「对方说 pass/有效」当终局"]),
    ("02.5-cross-check.md", "C36", "至少一轮主动质疑", ["至少一轮主动质疑"]),

    # ---- 03 ----
    ("03-action-decomposition.md", "C37", "只用已通过 Reviewer 的证据", ["只使用已通过 Reviewer 的证据"]),
    ("03-action-decomposition.md", "C38", "每步五要素", ["输入、动作、依赖、预期产出、验收方式"]),
    ("03-action-decomposition.md", "C39", "owner 标注 user/agent", ["owner 标注", "user", "agent"]),
    ("03-action-decomposition.md", "C40", "未标 owner = revise", ["未标 owner", "revise"]),
    ("03-action-decomposition.md", "C41", "循环依赖须消除", ["循环依赖"]),
    ("03-action-decomposition.md", "C42", "关键失败有替代路径与停止条件", ["替代路径和停止条件"]),

    # ---- 04 ----
    ("04-execution-verification.md", "C43", "记录命令/文件/输出/观察/失败", ["命令、修改文件、输出、观察、失败"]),
    ("04-execution-verification.md", "C44", "逐项对照 03 验收方式", ["逐项对照阶段 03 的验收方式"]),
    ("04-execution-verification.md", "C45", "需要外部事实回 02", ["回到阶段 02"]),
    ("04-execution-verification.md", "C46", "重试上限 2 次", ["失败重试上限 2 次"]),
    ("04-execution-verification.md", "C47", "同一命令不超过 3 轮", ["不超过 3 轮"]),
    ("04-execution-verification.md", "C48", "不降低标准/不提前验收/不伪造", ["不降低标准", "不提前验收", "不伪造结果"]),
    ("04-execution-verification.md", "C49", "失败处理四步", ["如实记录", "评估对后续步骤的影响", "不掩盖"]),

    # ---- 04.5 ----
    ("04.5-final-review.md", "C50", "反方角度复核", ["从反方角度"]),
    ("04.5-final-review.md", "C51", "完整链条核对", ["完整链条"]),
    ("04.5-final-review.md", "C52", "结论不超出证据", ["超出证据支持范围"]),
    ("04.5-final-review.md", "C53", "明确回退阶段", ["回退阶段"]),
    ("04.5-final-review.md", "C54", "可交接", ["继续工作"]),
]


def main() -> int:
    missing = []
    for fname, cid, meaning, needles in CHECKS:
        p = LOOP / fname
        text = p.read_text(encoding="utf-8") if p.exists() else ""
        if not text:
            missing.append({"file": fname, "id": cid, "why": "file missing", "meaning": meaning})
            continue
        absent = [n for n in needles if n not in text]
        if absent:
            missing.append({"file": fname, "id": cid, "why": f"missing: {absent}", "meaning": meaning})

    ok = not missing
    out = {"checker": "verify-constraints.py", "checks": len(CHECKS),
           "missing": missing, "exit": 0 if ok else 1}
    if "--json" in sys.argv:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(f"hard constraints checked: {len(CHECKS)}")
        if missing:
            print(f"MISSING ({len(missing)}):")
            for m in missing:
                print(f"  - [{m['id']}] {m['file']}: {m['why']}  ({m['meaning']})")
        print(f"\nRESULT: {'PASS' if ok else 'FAIL'} (exit {out['exit']})")
    return out["exit"]


if __name__ == "__main__":
    sys.exit(main())
