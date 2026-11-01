# 当前 goal @ r158 (2026-11-01)

## 【目标】
RV3G1-semantic-rejudge：对 75 样本 cell 做 fresh-context 盲重判 h，报语义一致率（核心新增 = h=0 漏判方向），回填 G1-contradiction-audit.md §1。

## 【阶段】
A 取 goal ✅ → B 执行 1-loop（阶段 1 输入冻结 ✅ / 阶段 2 arena 派发 ⏳ / 阶段 3 分析回填 ⏳）→ C 收口找下一个

## 【SOP 索引】
tasks/RV3G1-semantic-rejudge.md + .claude/skills/arena-outsource/SKILL.md

## 【验收标准】
rejudge-results.json(75条) + rejudge-analysis.json(h=0 子集一致率+翻转清单+κ) + G1 §1 回填 + 回执；冻结件零触碰，七脚本全绿。

## 【失败降级】
arena 不可用 → 本地自答 conf −0.2 标注（规则先行防锚定）。
