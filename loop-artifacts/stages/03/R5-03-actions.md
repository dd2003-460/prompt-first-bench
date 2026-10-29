# 阶段 03：行动分解 — R5 独立 judge 盲测

> origin: ai · 2026-10-30 · 依据 `loop/prompt-first/03-action-decomposition.md` + 02.5 证据边界
> owner 标注：全部步骤 owner=agent（本任务无用户交互点；模型身份/权限已在 02 核验）。

## 步骤表

| # | 步骤 | 输入 | 动作 | 依赖 | 预期产出 | 验收方式 | 并行 |
|---|------|------|------|------|---------|---------|------|
| S1 | 构造盲估 prompt 包 | gold-tree.md 节点文本面、prompt-V0.txt、hit 频次表（02 §1 G1）、p̃ 定义+公式+root_policy、输出 JSON schema | 写自包含 prompt：含 31 节点清单（ID+名称+父 ID+公式行+gold 标记存在性+8run 命中数）、估计程序（01 F2b 四步）、禁读声明、schema。**不含** prior-estimates.json 任何数值 | 无 | /tmp/R5-blind-pkg.md | 人工核对：包内 grep 不到原 judge p̃ 数值（如 0.45/7.643856 等特征值） | 可先于 S2 |
| S2 | fresh-context subagent 盲估 | S1 prompt 包 | spawn Agent（general-purpose，全新上下文），执行 31 节点 p̃+w2+rationale 估计，返回 JSON | S1 | subagent 返回的 nodes 字典 | 31 键齐全；每键有 p_tilde∈(0,1]或 null + 非空 rationale；w2 与公式一致（S3 复算） | — |
| S3 | 计算链主会话执行 | S2 结果 + w1 规则派生列 + hit-matrix | python 脚本：① 复算全部 w2 校验 S2 算术 ② W3=w1×w2 全排序 ③ top-5 ④ 锚点计数（严格+窄口径，含 M2 敏感性：F-A 计入版）⑤ Spearman ρ（n=30 主口径 + 含 N-0 备查口径） | S2 | 计算结果集 | 脚本可重跑复现（命令落盘 04）；w2 复算与 S2 值差 <1e-6 | — |
| S4 | 落盘 judge-blindtest-r1.json | S2+S3 | 按任务书 §4 schema 写文件（judge/date/nodes/w3_top5/construct_validity_pass），date=2026-10-30 | S3 | bench/rubric-v3/ablation/judge-blindtest-r1.json | jq 可解析；字段齐全；pass 值 = S3 严格口径计数 ≥3 | — |
| S5 | 04 执行记录 + 锚点清单 D5 | 全部上游 | 写 04-execution-log.md：命令、输出、逐验收对照、完整 W3 排序表（R4 风险缓解）、锚点清单（gold 集 + 本 judge top-5 + 原 judge top-5 + F-A 不计入声明） | S4 | loop-artifacts/stages/04/R5-04-execution-log.md | 任务书验收 4 条逐条有结论 | — |
| S6 | commit + push + ls-remote | 全部工件 | git add（loop-artifacts/ + judge-blindtest-r1.json）→ commit → push origin r73-judge-blindtest-r1 → git ls-remote 记录 | S5 | 远端分支 + receipts 记录 | ls-remote 返回 hash = 本地 HEAD | — |
| S7 | 04.5 反方复核 + 最终回执 | 全链条 | 反方检查（泄漏抽查/口径攻击/结论边界）→ 写 04.5-review.md → 输出最终回执（W3 top-5 判定 + ρ + 锚点清单） | S6 | loop-artifacts/stages/04.5/R5-04.5-review.md + 会话回执 | 回执三要素齐全；薄弱点清单非空 | — |

## 失败路径与停止条件

| 故障 | 替代路径 | 停止条件 |
|------|---------|---------|
| S2 subagent 返回缺节点/格式坏 | 重试 1 次（同 prompt 包）；仍坏 → 主会话对缺失节点补估并标 "fallback:true" | 重试 2 次后仍 >10 节点 null → 回执 blocked 停（任务书降级条款） |
| S3 脚本错误 | 修脚本重跑（数据不动） | 同一错误 3 轮未解 → 手工计算 + 声明 conf 降级 |
| S6 push 拒绝 | 查权限（G5 已验可达）；token 问题 → 报告 Lead | 2 次失败 → 工件保留本地，回执标 push-failed |
| S2 估计出 p̃ 越界（≤0 或 >1） | 截断到 (0,1] 边界并在 rationale 注明 | — |

## 依赖图

S1 → S2 → S3 → S4 → S5 → S6 → S7（线性链，无环；S1 可与 03 之后的文档工作并行但无实际收益，保持线性）

## 阶段判定（agent 自检，conf-0.2）

- 步骤覆盖 D1–D6 全部交付物；每步有输入/产出/验收；owner 全标 agent；失败路径齐备。
- **pass**，进入阶段 04。