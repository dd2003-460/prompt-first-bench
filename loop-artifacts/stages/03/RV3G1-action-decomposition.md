# 阶段 03：行动分解 — RUBRIC-V3-FULL-AUDIT / G1

> goal: rubric-v3-audit-g1 · 2026-10-30
> owner 标注：agent = ralph loop 自主执行；user = 需成璐决策

## 行动清单（DAG）

| # | 行动 | owner | 依赖 | 验收方式 |
|---|------|-------|------|----------|
| A1 | 机判脚本 `scripts/assert-g1-audit.py` + 样本清单 `scripts/g1-sample-cells.json` 落盘并跑通（A1-A4 PASS + S1-S4 SIGNAL，exit 0，确定性可复算） | agent | 02.5 完成 | 重跑 exit 0 且输出逐位一致（seed 固定）——**注：r108 已随 G2 收口入库，本步骤为核验而非新建** |
| A2 | 矛盾清单交付物 `bench/rubric-v3/ablation/G1-contradiction-audit.md`：C1-C4 四类矛盾，每条带 evidence（JSON path / file:line / 脚本输出行），含双 judge 全量 31 节点对照表 + 四方案（W2/W3 × orig/new）分数与 top-5 表 | agent | A1 | 文件存在；每条矛盾可追溯到具体数据点；数字与脚本输出一致 |
| A3 | 六阶段 loop 工件补齐（01/02/02.5/03/04/04.5，前缀 RV3G1-）+ tasks/current-goal.md 改写为本 goal | agent | A1, A2 | stages/<N>/ 下六个文件齐全 |
| A4 | commit + push 分支 ralph/rubric-v3-audit-g1 + ls-remote 验证 | agent | A2, A3 | git ls-remote 可见分支指向新 commit |
| A5 | 更新 tasks/goal-queue.md：大 goal 行补 G1 完成注记（保持队首目标不勾选，G3-G6 未完）+ CONTINUE_MSG 更新 | agent | A4 | queue 有 G1 完成记录；断点指向 G3 |

## 关键判读分支（预注册，防事后合理化）

- 若 A1 核验重跑出现任何 FAIL → 回 02 重查 F1（数据自洽假设崩塌，矛盾清单全部作废重做）。
- 若 A2 写作中发现 C4 的 top-5 diff 与 judge-blindtest-r1.json 落盘值不一致 → 以 JSON 落盘值为准修正本文档（冻结文件是事实源，文档跟随）。
- 若发现 S1 有任一 cell 核验失败 → 该 cell 升级为「h=1 判定无文本锚点」矛盾条目（C5 新增类），不得静默跳过。

## 不做的事（边界）

- 不改任何冻结文件（hit-matrix/prior-estimates/judge-blindtest/stats-*/gold-tree/runs-C0-*）
- 不做语义级独立重判（工具纪律禁 subagent；登记降级，建议后续走 arena 通道）
- 不写 C4 的根因分析（移交 G2，已完成于 g2-rootcause.md；本 goal 只引用不复述）
- 不动 gold set（r71b 冻结）、不实施任何修复方案（留给 G3/G6）