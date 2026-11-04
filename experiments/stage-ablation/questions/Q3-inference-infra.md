# Q3 · 推理基础设施（t17-generalization 域）

> 题面来源：`projects/decomp/bench/runs/t17-generalization/task-inference-infra.txt` 的任务段（原样）
> gold 锚点：`projects/decomp/bench/gold-inference-infra/tree.md`（25 节点 gold 树，根标量 ¢/1k_out_tok）

## 题面

我有一台固定的服务器（硬件已买好不能换），上面要跑一个 27B 规模的开源模型对外提供服务。我在纠结用 vLLM、TGI、原生 transformers 还是 SGLang 来部署。
请帮我拆解：决定「每千输出 token 的服务成本」的所有因素都有哪些，并判断哪个框架最划算。

## gold 要点（判分用，不进 prompt）

- 根标量：¢/1k_out_tok（每千输出 token 服务成本），硬件常数 → 重心全在吞吐
- 结构指纹：候选=服务软件框架，叶子=调度/KV cache/批量/运维属性
- SHARED 参数：n = min(n_mem, n_slo)（显存约束与 SLO 约束取小）
- 主导黑盒：调度效率（真实负载 vs benchmark 的差距）