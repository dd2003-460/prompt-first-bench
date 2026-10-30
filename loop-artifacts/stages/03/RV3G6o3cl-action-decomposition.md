# 阶段 03：行动分解 — RV3G6-o3-claim-list

> goal: O3 gold 节点转原子 claim 清单 · 分支 ralph/rv3g6-o3-claim-list · 2026-10-30
> owner 标注：agent = runner 可自主执行 / user = 需成璐决策（写 APPROVALS 不阻塞）

## 行动表

| # | 行动 | owner | 依赖 | 验收 |
|---|------|-------|------|------|
| A1 | 起草 `bench/rubric-v3/o3-claim-list.md` §1（背景 + 三失败模式，吸收 02.5 M-1 修正：「多数数值不逐字匹配、W4 14GB 单值例外」+ A1c 双向失效表述） | agent | 02/02.5 | 每失败模式带 run 原文 evidence；无外部主张 |
| A2 | 起草 o3-claim-list.md §2（31 条 claim，按 02 §1.4 底稿定稿措辞；吸收 02.5 A1a N-3.2.2 锚定每流口径 / A3a N-5 放宽为淘汰动作 / A3b N-0 双句结构） | agent | A1 | 31 节点全覆盖；每条 claim 过三属性自检（自含/可二值/方向内嵌）；不含 gold-tree 专有数值（断言脚本机判） |
| A3 | 起草 o3-claim-list.md §3（映射一致性指标 M1/M2 正式定义 + 分母声明 + NA 处理 + identity-baseline 标签 + h=0 方向无判别力声明） | agent | A2 | 公式可机算；口径声明与 02.5 A2a/A2b 一致 |
| A4 | 起草 o3-claim-list.md §4（多判者协议：N=3 / ≥2/3 即过、1/3 即不过、无平票态 / κ 在条目层 vs 本协议聚合层的分工） | agent | A2 | 三要素齐全；与 R-02 κ 门禁不重复不矛盾 |
| A5 | 起草 o3-claim-list.md §5（使用边界：S2 同源偏置限定语沿用 AUDIT §6 / claim 措辞人工审定状态 = 未审定登记 / U1 补数路径指向 RV3G1-semantic-rejudge）+ §6（冻结声明：修改 = 新 goal + APPROVALS） | agent | A3 | S2 限定语 byte-exact 引用 AUDIT §6 原文 |
| A6 | 新增 `bench/rubric-v3/ablation/scripts/assert-o3-claim-list.py`（结构完整性：① 31 节点 ID 全出现且各对应非空 claim 行；② claim 文本不含 gold-tree 专有数值白名单外的数字——白名单 = {1, 2, 3} 这类结构性小数的豁免规则需显式列出；③ M1/M2 基线值从 hit-matrix.json 复算并与 o3-claim-list.md §3 声明值一致；④ DRAFT v2 L71 已替换（grep 旧判据措辞不存在 + 新引用存在）） | agent | A2-A5 | exit 0；FAIL 时输出具体违规行 |
| A7 | 编辑 `DRAFT-rubric-v3-v2.md`：L71 命中判据行替换为 claim 级判据引用（保留 h_v 符号）+ O3 节新增 `[batch2: R-13]` 已提前落地状态行（02.5 A4b 裁决：新增而非更新） | agent | A5 | grep 验证：旧措辞「节点 ID 对得上」全文消失；h_v 符号仍在 L66 公式区 |
| A8 | `revision-log-batch1.md` 追加 R-13 条目（范围切割说明：R-13 原属 batch2，本 goal 提前交付核心件 = 判据件 + 指标定义 + 多判者协议；剩余部分 = claim 级独立重判执行，导出 queue） | agent | A7 | 条目格式与既有条目一致（含/不含清单 + 裁决登记） |
| A9 | APPROVALS.md 登记 U2（31 条 claim 措辞人工审定，runner 起草版可用但终审留成璐） | agent（写登记）→ user（审） | A2 | 登记项落盘；不阻塞收口 |
| A10 | 冻结数据零修改验证（git status：gold-tree/hit-matrix/prior-estimates/runs/stats 无 diff）+ 全量文件清单核对 | agent | A1-A8 | git status 输出仅含本 goal 预期文件 |
| A11 | 阶段 04.5 反方复核（≥3 攻击：claim 是否泄漏答案 / 指标是否被误读 / DRAFT diff 是否越界 / 三属性是否真满足）+ verdict | agent | A10 | verdict pass 方可收口 |
| A12 | 收口：commit + push `ralph/rv3g6-o3-claim-list` + ls-remote 验证 → merge main + push → goal-queue 标记 [x] + 结果注记 + 追加 ≥1 新候选（RV3G6-o3-claim-rejudge：claim 级独立重判执行，arena 通道，消费本 goal 的 31 条 claim + M1/M2 口径） | agent | A11 | main 上可见 merge commit；queue 队首变为下一 goal |

## 关键路径

A1→A2→(A3,A4,A5 并行)→A6→A7→A8→A9∥A10→A11→A12

## 不做的事（边界）

- 不改 gold-tree.md / hit-matrix.json / prior-estimates.json（只读）
- 不执行 claim 级独立重判（工具纪律禁 subagent；U1 导出 queue）
- 不动 DRAFT v2 除 L71 + R-13 状态行外的任何行（J4 最小 diff）
- 不代裁 claim 措辞终审（user 项，APPROVALS 登记）