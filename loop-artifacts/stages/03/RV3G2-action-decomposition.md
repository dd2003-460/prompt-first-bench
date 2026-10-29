# 阶段 03：行动分解 — RUBRIC-V3-FULL-AUDIT / G2

> goal: rubric-v3-audit-g2 · 2026-10-30
> owner 标注：agent = ralph loop 自主执行；user = 需成璐决策

## 行动清单（DAG）

| # | 行动 | owner | 依赖 | 验收方式 |
|---|------|-------|------|----------|
| A1 | 落盘根因分类报告 `bench/rubric-v3/ablation/g2-rootcause.md`：F1-F4 四因素结论 + Q1-Q3 修正后的归因 + R4 同族边界声明，每条带 evidence（文件路径+JSON path/行号） | agent | 02.5 完成 | 文件存在；每条结论可追溯到具体数据点 |
| A2 | 附完整 31 节点对照表（node/hr/p̃_orig/p̃_new/w2_orig/w2_new/w3_orig/w3_new/Δw3/gold标记）到 g2-rootcause.md 附录 | agent | A1 | 31 行齐全，数字与 JSON 精确一致（脚本核验） |
| A3 | 写修复方案三选项（供 G6 定稿选择，本 goal 不实施）：O1 改判据口径（top-10 或 gold 平均排名）/ O2 加第三 judge 重测（R5.2-third-scorer 衔接）/ O3 接受降级（W3 不进正式公式，rubric-v3 定稿为 W1-only + W3 标 experimental） | agent | A1 | 每选项含成本/收益/风险一行 |
| A4 | commit + push 分支 ralph/rubric-v3-audit-g2 + ls-remote 验证 | agent | A1-A3 | git ls-remote 可见分支指向新 commit |
| A5 | 更新 tasks/goal-queue.md：G2 子 goal 标记完成（注：goal-queue 只列大 goal，此处在大 goal 行下补 G2 进度注记） | agent | A4 | queue 文件有 G2 完成记录 |

## 关键判读分支（预注册，防事后合理化）

- 若 A2 核验发现任何 w2/w3 复算 mismatch → 回 02 重查 F1（公式层重新入候选）。
- 若 A1 写作中发现 02.5 的 (a)/(b) 归因无法用数据切分（即无法指出哪些席位交换由哪个源导致）→ 登记信息边界，归因合并表述，不硬拆。

## 不做的事（边界）

- 不改任何冻结文件（hit-matrix/prior-estimates/judge-blindtest/stats-*）
- 不实施任何修复方案（留给 G3/G6）
- 不动 gold set（r71b 冻结）
- 不开第三 judge（外部阻塞，属 R5.2-third-scorer）