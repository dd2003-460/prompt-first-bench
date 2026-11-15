# T39: Gold 分解树复现 — 方法调研

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

## 任务

调研"如何让 LLM 生成定量分解树"的业界最佳实践。目标：找到让 27B 模型在纯推理（无外部工具）条件下，输出接近 gold 级分解树的 prompt 策略。

## 调研对象（≥5 个）

1. Tree-of-Thoughts (Yao et al. 2023) — 结构化探索
2. Self-Consistency (Wang et al. 2022) — 多路径投票
3. AutoGPT / BabyAGI — 任务分解+执行循环
4. OpenHands (ex-OpenDevin) — SWE-agent 式分解
5. LangGraph / CrewAI — 多 agent 分工
6. (bonus) Decomposition-based reasoning in math (PaLM, Chinchilla papers)

## 关键问题

- 哪些系统要求"每个叶子节点必须带具体数值"？怎么强制的？
- 迭代式分解（粗→细→补数据）vs 一次性全树，哪个效果好？
- 交叉验证在分解流程中的位置：事前约束 vs 事后检查？
- 对 27B 级别模型（非 frontier），什么分解策略最 realistic？

## 产出

`loop-artifacts/stages/02/research-gold-replication.md`：
- ≥5 系统对比表（分解策略/叶子粒度/验证机制/适用模型规模）
- ≥3 条可迁移 insight（每条带：来源 + 预期收益 + 实施成本）
- 推荐方案：NEW-A prompt 的具体文本草稿

## 约束

- 不编造引用，所有来源给 URL
- 区分"论文声称"和"实际开源实现"
- 如果某系统没有公开 prompt，标注 [不可见] 并推测其策略
