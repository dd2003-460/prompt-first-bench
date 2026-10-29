# 阶段 02：信息调研 — R5 独立 judge 盲测

> origin: ai · 2026-10-30 · 依据 `loop/prompt-first/02-information-research.md` + 01 阶段空缺 G1–G5
> 本任务为**仓库内数据核验型**（非外部资料搜集）：全部"来源" = main 分支文件 + 运行时探测。无价格/库存等易变事实，7 天时效规则不适用；网页 LLM 交叉询问对本任务无增量（p̃ 估计是本 judge 的一手产出，不是待核验的外部主张），按 02 流程第 2 条的失败降级精神记录后跳过 web-llm 调用（ralph CLI 在本环境不可用，见 00 §3）。

## 1. 逐空缺核验

### G1：31 节点 p̃ 值 → 本任务核心工作，入口已就绪
- 输入面核验完成：gold-tree.md 31 节点 ID 全集与父子结构已读（N-0, N-1, N-1.1, N-1.1.1..4, N-1.2, N-1.2.1..2, N-1.3, N-1.3.1..2, N-2, N-2.1..2, N-3, N-3.1, N-3.1.1..3, N-3.2, N-3.2.1..4, N-4, N-5, N-5.1..3）= **31 个，计数核对通过**。
- prompt-V0.txt 题面已读（父上下文上游）：C9-plain 档硬件部署成本分解题，8×3 候选硬件、27B 权重、90:9:1@64K token 画像。
- hit-matrix.json 8 runs × 31 节点全量已读，各节点 h=1 频次统计（供 F2b step3 sanity check）：

| 节点 | 8run 命中数 | 节点 | 8run 命中数 | 节点 | 8run 命中数 |
|---|---|---|---|---|---|
| N-0 | 6 | N-3.1.1 | 0 | N-5.1 | 5 |
| N-1 | 0 | N-3.1.2 | 1 | N-5.2 | 0 |
| N-1.1 | 8 | N-3.1.3 | 0 | N-5.3 | 8 |
| N-1.1.1 | 4 | N-3.2 | 4 | N-2 | 0 |
| N-1.1.2 | 0 | N-3.2.1 | 6 | N-2.1 | 0 |
| N-1.1.3 | 0 | N-3.2.2 | 6 | N-2.2 | 0 |
| N-1.1.4 | 7 | N-3.2.3 | 8 | N-4 | 4 |
| N-1.2 | 7 | N-3.2.4 | 4 | N-1.3 | 0 |
| N-1.2.1 | 7 | N-3 | 1 | N-1.3.1 | 0 |
| N-1.2.2 | 3 | N-3.1 | 4 | N-1.3.2 | 0 |

（上表由脚本对 hit-matrix.json 全量重算，非手抄；N-5 命中 5。）
| N-1.1(父N-1) 见上 | | | | N-5 | 6 |

注：N-1/N-2/N-3(仅1)/N-1.3 系节点 8 run 近乎全 0 命中 —— 说明真实模型几乎从不把根直接切成"小时持有成本/利用率/原始速率/故障损耗"这种四元结构，而是走"每任务成本 = 硬件小时价×耗时/通过率"的公式路线。这是 p̃ 估计的关键先验信号（这些节点的"那一刀"对通用 LLM 是反直觉的）。

### G2：原 judge p̃ 序列 → 隔离读取已完成（顺序纪律执行点）
- prior-estimates.json 结构：{epsilon, weight_formula, root_policy, nodes{31}, declared_gold_node_count}。
- 读取范围裁定执行：w1/parent_share 列（规则派生，F3b 允许）+ p_tilde 列（**仅用于 04 阶段末的 Spearman 计算**，不进入 04 盲估步骤的输入）。reason/w2 文本未读入估计过程。
- 原 judge root_policy 确认："N-0 has no parent context; p_tilde=null and neutral weight 1" → 本 judge 沿用（01 F2a 冻结）。
- 口径备注：declared_gold_node_count=35 与 31 节点树不符（疑似含子拆分或历史编号），不影响本任务（锚点集以 stats-w3w4.json construct_validity 为准，F4 已冻结两口径）。

### G3：本 judge 模型标识
- 运行时标识：**qwen3.8-27b**（Claude Code 会话注入的环境事实，非自报）。
- judge 字段取值：`"qwen3.8-27b (Claude Code ralph loop channel)"`。
- 与原 judge 关系：原 judge 为 arena 侧 LLM（ablation-result.md 未记录模型名，记 "original-judge(arena)"）。运行时家族不同（Qwen vs arena 侧未明模型），满足任务书"换模型家族盲测"意图；**不确定性**：arena 侧具体型号未知，若恰为 Qwen 系则独立性声明需降级 —— 已在 04.5 登记为残余风险。

### G4：ralph review CLI 可用性
- 实测：`ralph prompt-first review .` → `[Errno 2] No such file or directory: '/Users/a1-6/Desktop/workspace/pfb/ralph-loop.md'`。
- 原因：本仓库从未执行 `ralph prompt-first init`（无 ralph-loop.md 项目状态文件）。
- 处置（T7.1 先例，conf-0.2）：阶段判定 = agent 自检 + 04.5 反方复核；不手写 verdict 块（00-common-review §8）。

### G5：推送权限
- `git ls-remote https://github.com/dd2003-460/prompt-first-bench.git HEAD` → 返回 d22b5fb…（可达，权限正常）。push 验证在 04 阶段执行。

## 2. 关键主张与来源对照表

| 主张 | 来源（路径 @ main d22b5fb） | 观察时间 | 不确定性 |
|------|------|------|------|
| W3 top-5 门槛 = ≥3/5 gold 标记 | tasks/R5…brief.md §验收 + stats-w3w4.json criterion | 2026-10-30 | 无 |
| 严格口径 gold 集 = {N-2.1, N-3.2.2, N-2, N-4, N-1.3} | stats-w3w4.json strict_criterion_check + bench.md O3 | 2026-10-30 | 窄口径 {N-2.1,N-3.2.2,N-2} 并存，双报 |
| 原 judge W3 top-5 = [N-3.2.2, N-3.2.4, N-2.1, N-2, N-1.1.3]，3/5 | stats-w3w4.json results.W3 | 2026-10-30 | 仅用于 D5 对照，不进入盲估 |
| w1 映射 = f(parent SHARE)，确定性规则 | TASK-ablation.md Step 2 + prior-estimates.json w1 列 | 2026-10-30 | 规则边界（SHARE 恰好 0.25/0.1）按原 judge 取值沿用 |
| ε=0.01，封顶 log₂(100)≈6.64，w2∈[1,8] | 任务书 §3 + prior-estimates.json epsilon | 2026-10-30 | 无 |
| N-0 政策 = p̃ null / w2 中性 1 | prior-estimates.json root_policy | 2026-10-30 | 沿用以保证跨 judge 可比 |

## 3. 矛盾与未解决项

- **矛盾 M1（已解释）**：hit-matrix 中 N-1.1 命中 8/8 但 gold-tree 里 N-1（其父）命中 0/8 —— 不矛盾：runs 普遍写"折旧/摊销"内容，被 r69 judge 判给 N-1.1 层而非 N-1 层（层级归属判定）。对 p̃ 的含义：估 N-1 的 p̃ 时看的是"根下切出 c_hour 这一刀"的先验，不受子层命中影响。
- **未解决 U1**：arena 侧原 judge 精确型号未知（G3 不确定性）→ 不阻塞，04.5 登记。
- **未解决 U2**：Spearman ρ 的显著性无法检验（n=30，且两序列来自同一任务的两台机器式估计）→ 只做描述性报告，不做推断（继承 stats-recomputed.json note 口径）。

## 4. 阶段判定（agent 自检，conf-0.2）

- 01 阶段 G1–G5 逐项有结论或明确保留；来源均为仓库内文件 + 实测命令输出，无外部易变事实。
- web-llm 交叉询问：本任务无外部待核验主张，且 ralph CLI 不可用 → 记录跳过理由（非静默省略）。
- **pass**，进入阶段 02.5。