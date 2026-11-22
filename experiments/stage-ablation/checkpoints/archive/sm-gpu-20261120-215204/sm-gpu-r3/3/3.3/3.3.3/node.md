# N90: 2x RTX 4090 通过 PCIe 4.0 互联运行 Qwen3-27B 时，每 Token 生成的跨卡 All-Reduce 通信数据量约为 2 * 隐藏

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

2x RTX 4090 通过 PCIe 4.0 互联运行 Qwen3-27B 时，每 Token 生成的跨卡 All-Reduce 通信数据量约为 2 * 隐藏层维度 * 序列长度 * 字节数，对于 32K 序列，单次通信量约 2 * 4096 * 32768 * 2 bytes = 512MB，PCIe 4.0 带宽 32GB/s 下通信延迟约 16ms，占总 Token 生成时间 (假设 20ms/token) 的 80%，严重瓶颈吞吐。

## Corrected Claim

2x RTX 4090 通过 PCIe 4.0 互联运行 Qwen3-27B 时，若采用张量并行且 batch size 为 1，每 Token 生成的跨卡 All-Reduce 通信数据量约为 2 * 隐藏层维度 * 序列长度 * 字节数。对于 32K 序列，假设隐藏层维度为 4096，单次通信量约 512MB。PCIe 4.0 带宽 32GB/s 下通信延迟约 16ms。若总 Token 生成时间为 20ms，则通信占比约 80%，构成严重瓶颈。但实际总生成时间取决于模型架构、并行策略及硬件优化，需具体测量确认。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 正交性失败：子节点1、2、3、4、5、7、8均围绕'显存容量与KV Cache量化'展开，存在大量逻辑重叠和相互依赖，并非独立正交维度。2. 完备性失败：父节点核心论点是'All-Reduce通信延迟导致吞吐瓶颈'，但子节点几乎全部在讨论'显存是否够用'及'量化策略'，完全缺失了对通信带宽、延迟计算、并行策略（如TP vs PP）对通信量影响的分析。3. 冗余严重：子节点2、3、5、7、8本质上是在不同量化假设（BF16 vs INT8）下重复计算显存占用，属于同一逻辑分支的参数变体，应合并为一个'显存可行性分析'节点，或作为参数化处理，而非拆分为多个独立事实节点。）

## Search Query

PCIe 4.0 bandwidth bottleneck LLM inference all-reduce latency 32k context
