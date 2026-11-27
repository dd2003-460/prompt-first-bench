# TASK-D2 — Q9-agi gold 骨架升级（arena 外包）

> origin: ai · 2026-11-24 · research-agi-budget goal 子项⑤ D2 原子
> 前置：decomposition-research-agi-budget.md §7 任务书（本文件是其执行实例）
> 现状：gold/Q9.md v0 = 本地 conf 0.2 骨架（深度 3，12 叶子，12 判定点），arena 登录过期未交叉核验
> 目标：升级到深度 5 + 每叶子量化公式 + ≥2 agent 交叉核验，conf 0.2 → 0.8

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

[任务] 在 4×V100 + 27b 本地模型 + 不改权重约束下，把 Q9-agi gold 骨架从深度 3 扩到深度 5，每叶子带量化公式，≥2 agent 交叉核验，产出升级版 gold/Q9-v1.md + 回执。

[背景]（最小必要，≤10 行）
- 题面：experiments/stage-ablation/questions/Q9-agi-research.md（目标定义，合法题面，可含 AGI 操作化 + D 硬件）
- 现状骨架：experiments/stage-ablation/gold/Q9.md（v0，深度 3，12 叶子，12 判定点 J1-J12，权重和=1.00）
- 硬件事实锚（实测 2026-11-22）：4×V100-SXM2-16GB（cap 7.0, TP=4）+ qwen3.8-27b NVFP4 + MTP 投机解码 + KV fp8 offload 24GB + max_model_len=262144 + max-num-seqs=8 + 开发机 M1 Max
- 约束：不改权重（prompt+hook+记忆+工具）；预算=max_nodes（节点=贡献因子）；质量=judge depth+coverage
- 分解维度（已定）：能力上限/总成本/可靠性/时间/路径（N-1..N-5）
- 量化口径：decomposition-research-agi-budget.md §6 公式（预算 B=max_nodes，质量 Q=depth_score，覆盖 C=判定点命中/总数，Pareto 拐点=ΔQ/ΔB<0.01/节点）
- 对标格式：gpu gold 37 节点/深度 5（experiments/stage-ablation/gold/gpu-gold-units.json 或 gold-gpu-units.json）
- 已知证据（T53b）：SM 臂 +0.182 depth 优势（注意力维持）；27b 微架构层可达/NCU 层不可达；并发非确定性已量化
- 不泄露边界：gold 骨架 = 答案，绝不进 prompt；prompt 只含题面

[约束] 中文回答；每条结论标 conf(0-1)；给来源 URL（arXiv/GitHub/官方文档）；不确定的标"未验证"；≥2 agent 交叉核验（同一 arena 会话内不同对战轮次各答一遍，或 arena + 另一站点）

[交付]
1. `experiments/stage-ablation/gold/Q9-v1.md`：深度 5 树（对标 gpu 37 节点格式）+ 每叶子 S-a/S-b/S-c 判分档 + 量化公式 + 来源 URL + conf
2. `experiments/stage-ablation/gold/Q9-v1-receipt.md`：回执，含
   - repo URL + branch + commit_sha（指纹，Lead 用 git ls-remote 核验）
   - ≥2 agent 交叉核验记录（responses[] + successful_provider_ids[] ≥2 + observed_at ISO 8601 带时区）
   - 与 v0 的 diff 摘要（新增/修改/删除的节点 + 判定点）
   - 不泄露审计（gold 维度名/节点 ID/判据关键词/公式 零命中 prompt）
3. 判定点扩展：J1-J12 → J1-J??（深度 5 叶子数），权重和=1.00

[长度] ≤50 行（核心发现+关键数字+决策，过程论证放附录）

[正交性自检] 本子领域与④预算扫描（K7）输入/输出/时间轴重叠 <30%（④消费 gold 判分，⑤生产 gold 骨架；④在跑 vLLM，⑤不占 vLLM）

[落盘约束] 文件不存在=任务未完成，Lead 不验收

[失败降级] arena 登录过期/通道故障 → 记录具体报错（链路标识+403/沙箱/tiptap/超时），Lead 本地 conf-0.2 兜底（v0 已存在），下一周期重试
