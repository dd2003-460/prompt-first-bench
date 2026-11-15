# T-soc-upperbound-thinking-20261116 — 0.813 上限估算的逻辑审查（thinking team）

**origin: ai** · 派发: zero (Hermes) · 2026-11-16 · 工作目录: /Users/a1-6/Desktop/workspace/pfb

## 背景（最小必要）
SOC 消融臂（S5 状态机跑中文社考题，逐条 claim 核验，cov = verified/total）gate 要求 cov ≥ 0.898。
当前 174/283=0.615。Lead 估算现实上限 ~230/283=0.813，依据：
- pending 77 中「约 46 个 knowledge/given 类可翻 verified」（拍的，未逐条核）
- degraded 31 中「约 10 个可救回」（拍的，未逐条核）
- 卡死原因：webllm 检索通道（Perplexity/ChatGPT）全挂，search 类节点拿不到来源

## 任务（纯逻辑审查，不需要联网，不需要逐条读节点）
1. **审估算方法**：「46/10 是拍的」这种拍法有什么系统性偏差？（提示：乐观偏差——人拍"可翻"数时倾向于把模糊的算进可翻）
2. **给一个更严谨的估算框架**：不逐条核的前提下，怎么用 checkpoint 里的字段分布（source/evidence 空否/search_query 空否）推出上限的区间（下界-上界）而不是点估计？把公式写出来，字段名写清楚。
3. **gate 可达性判断**：即使按你的上界，0.898 可达吗？如果不可达，gate 本身是不是设错了（比如该按"可核子集"算 cov 而不是全量）？给建议。
4. **和另外两路交叉**：core team 正在逐条分类 pending 77（`tasks/T-soc-pending77-team-20261116.md`），arena 正在调研外部来源可达性（`tasks/T-soc-arena-20261116.md`）。你的框架要设计成**能直接吃他们的产出**——写清楚"等他们的文件 X 出现后，把 Y 字段代入公式 Z"。

## 交付
`experiments/stage-ablation/loop-artifacts/stages/arena-outsource/soc-upperbound-review.md`
结构：四节对应四任务 + 末尾「核心发现 ≤10 行」。中文，每条结论标 conf(0-1)。
**文件不存在 = 未完成。** 完成后 commit 到 main（前缀 `soc:`），更新本文件末尾「## 完成报告」。