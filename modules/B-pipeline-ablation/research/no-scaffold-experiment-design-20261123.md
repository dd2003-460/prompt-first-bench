# 去脚手架实验设计 — 测自发监控 (prompt-elicited vs spontaneous)

**时间**：2026-11-23 16:05
**状态**：设计完成 + runner 就绪（no_scaffold_runner.py, 输出隔离已修），**排队中**（D 2026-11-23 纪律：新 idea 记录 + 收敛，主线 workshop 投稿后再执行）
**触发**：补充40-45 揭示 (a)→(b) 触发链是 prompt-elicited 的，最干净的证据是补充45（knowledge 缺口内 `[待核验]` 标签是检索触发器，GPU 66% vs 14%）
**原始意图锚点**：USER.md "让模型'知道自己不知道'(标缺口→调研→更新记忆)" — 本实验直接测"知道自己不知道"是 prompt 脚手架撑的还是自发的

## 目的

回答 D 的核心问题：模型的自我认识（知道自己不知道）是 **prompt-elicited**（靠 prompt 指示标 `[待核验]`）还是 **spontaneous**（模型自发标不确定）？

现有证据（补充37/45）都指向 prompt-elicited，但都是**相关性**（有 tag 的节点更可能触发检索）。要**因果**证据，得做去脚手架实验：去掉 prompt 的 `[待核验]` 指示，看自发监控还在不在。

## 对照臂

| 臂 | prompt | 说明 |
|---|---|---|
| A (baseline) | 现有 prompt（含 `[待核验]` 指示） | 对照，复现补充37/45 的数字 |
| B (no-scaffold) | 剥掉 `[待核验]` 指示句，其余 byte-unchanged | 测自发监控 |

**剥离内容**（prompts.py，运行时 monkeypatch，不改文件）：
- line 78: `若某事实确实只有定性结论，claim 末尾标 [待核验] 并给出最接近的量化形式（变量/参数化公式）。`
- line 312: `确实只有定性结论的标 [待核验] 并给出最接近的量化形式`
- line 332: `(b) 其 claim 含待填参数（[待核验]、[时效待核]、符号变量未实例化）...`（这条是硬停门禁，剥离后模型不再被强制给待填参数建子节点）
- line 100/101: 示例里的 `[待核验]` 标签

**保留内容**：
- line 335: source 标记规则（given/knowledge/search）— 这是 (b) 的触发器，不能剥
- line 337: search_query 规则 — 同上
- 其余所有 decompose 规则

## 测量

每臂每域 3 reps，三域（gpu/nat/soc），共 18 runs：
1. **gap_rate**（自发缺口标记率）：Arm B 的 gap_rate vs Arm A
   - 预期：若 (a) 完全 prompt-elicited，Arm B gap_rate 掉到接近 0
   - 若 Arm B 还有 30-40%，说明有自发成分
2. **(a)→(b) 触发率**：缺口节点 → search_query 的比率
   - 预期：Arm B 的触发率应接近 baseline（无缺口节点的 query 率）
3. **knowledge 源缺口占比**：Arm B 是否还有 knowledge 源缺口节点

## 成本

18 runs × ~45min ≈ **13.5h GPU**（vLLM 8787 当前 idle）

## 风险

- **低**：独立输出目录（`data/no-scaffold/`），不碰现有 checkpoint/archive
- **prompts.py byte-unchanged**：运行时 monkeypatch，不改文件
- **可回滚**：实验脚本独立（`experiments/stage-ablation/no_scaffold_runner.py`），删了不影响现有 pipeline
- **GPU 占用**：13.5h，期间 vLLM 不可用于其他任务（当前 idle，无冲突）

## 实现要点

1. `no_scaffold_runner.py`：
   - import prompts，对 P1H_INDEX / P1_DECOMPOSE 做字符串替换（剥离 `[待核验]` 指示句）
   - 验证剥离后的 prompt 不含 `[待核验]`（assert）
   - 调 s5_state_machine 跑 run，输出到 `data/no-scaffold/`
2. 分析脚本：复用 `claim-evidence-separation.py` 的 gap_rate + 触发率计算
3. 对照：Arm A 用现有 prompt 复跑 3 reps/域（不是复用现有数据，因为现有数据是软上限时代）

## 待 D 确认

- 是否开跑（13.5h GPU）
- 三域都要还是只 gpu（省一半时间）
- 剥离范围：只剥 line 78/312（软指示）还是连 line 332（硬停门禁）一起剥
