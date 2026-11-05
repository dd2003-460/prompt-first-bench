# Q2 · 模型选型（t17-generalization 域）

> 题面来源：`projects/decomp/bench/runs/t17-generalization/task-model-selection.txt` 的任务段（原样）
> gold 锚点：`projects/decomp/bench/gold-model-selection/tree.md`（24 节点 gold 树，根标量 ¢/1k_acc）

## 题面

我要为一个内部代码助手选一个开源大模型，主要任务是函数级代码补全（Python/JS）和通用指令跟随，预算是单台双卡 24GB 或等效 API 额度。候选有 Qwen3-32B、Qwen2.5-Coder-32B-Instruct、Mistral-Small-2501-24B、GLM-4-32B-0414、DeepSeek-Coder-V2-33B、Llama-3.3-70B-Instruct(W4) 这几个。
请帮我拆解：决定「每千次合格回答的总成本」的所有因素都有哪些，并判断哪个模型最划算。

## gold 要点（判分用，不进 prompt）

- 根标量：¢/1k_acc（每千次合格回答成本），合格 = 代码补全通过测试 + 指令跟随达标
- 结构指纹：候选=模型权重，叶子=基准分/单价/许可/生态；约束=许可证一票否决
- SHARED 参数：params（三路径耦合）
- 主导黑盒：基准→真实任务的 transfer 率