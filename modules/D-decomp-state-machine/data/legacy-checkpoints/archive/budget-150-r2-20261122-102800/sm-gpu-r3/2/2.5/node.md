# N17: 多卡方案显存分布与通信开销：2×RTX 4090 (48GB total) 运行BF16时，权重分片每卡27GB，KV Cache分片每卡2.15GB，总显存每

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

多卡方案显存分布与通信开销：2×RTX 4090 (48GB total) 运行BF16时，权重分片每卡27GB，KV Cache分片每卡2.15GB，总显存每卡~30.5GB < 24GB? 否，30.5 > 24，故2×4090无法运行BF16 Qwen3-27B 32K上下文；2×RTX 3090 (48GB total) 同理；2×A6000 (96GB total) 运行BF16时每卡~30.9GB < 48GB，可行

## Corrected Claim

2×RTX 4090 (48GB total) 运行BF16时，权重分片每卡27GB，KV Cache分片每卡2.15GB，总显存每卡~29.15GB > 24GB，故2×4090无法运行BF16 Qwen3-27B 32K上下文；2×RTX 3090 (48GB total) 同理；2×A6000 (96GB total) 运行BF16时每卡~29.15GB < 48GB，可行

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 矛盾/非正交：父节点结论称 2×4090 总显存需求~30.5GB，而子节点1计算为32.65GB（含激活开销），子节点2计算为18.075GB，数据不一致且子节点间未区分清楚条件（如是否包含激活开销）。2. 冗余：子节点1和子节点3本质上是同一计算逻辑（BF16权重+KV+开销）在不同硬件显存上限下的应用，属于同一公式的不同参数代入，应合并为一个“BF16显存需求模型”节点，通过变量区分硬件。3. 不完备：父节点明确提到“2×RTX 3090 (48GB total) 同理”，但子节点完全缺失对 3090 的分析，遗漏了父节点的关键对比对象。）

## Search Query

multi-GPU tensor parallelism 27B LLM VRAM per GPU BF16 KV cache sharding
