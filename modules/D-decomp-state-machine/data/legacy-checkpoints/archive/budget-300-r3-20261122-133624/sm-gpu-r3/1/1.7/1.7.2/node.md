# N64: Qwen3-27B 在 BF16 下 Decode 阶段的实际带宽需求修正为 54 GB/s 是理论下限，实际因 KV Cache 读取和激活值传输，总带宽需求

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

Qwen3-27B 在 BF16 下 Decode 阶段的实际带宽需求修正为 54 GB/s 是理论下限，实际因 KV Cache 读取和激活值传输，总带宽需求约为 60-70 GB/s；在 4090 (1008 GB/s) 上理论 Decode 吞吐约为 17 tokens/s，受限于内存控制器效率和调度开销，实际约为 12-15 tokens/s。

## Corrected Claim

Qwen3-27B 在 BF16 下 Decode 阶段的实际带宽需求修正为 54 GB/s 是理论下限，实际因 KV Cache 读取和激活值传输，总带宽需求约为 60-70 GB/s；在 4090 (1008 GB/s) 上理论 Decode 吞吐约为 17 tokens/s，受限于内存控制器效率和调度开销，实际约为 12-15 tokens/s。

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 冗余性：子节点2和3本质上是同一计算逻辑在不同硬件参数下的实例，属于可压缩的变量取值，而非独立的正交知识点。2. 完备性：父节点明确给出了4090的实际吞吐范围（12-15 tokens/s），但子节点2推导出的实际吞吐为10-12 tokens/s，存在数值不一致且未解释差异来源（如调度开销比例不同），导致对父节点关键结论的覆盖不准确。）

## Search Query

Qwen3-27B decode bandwidth requirement GB/s RTX 4090 BF16
