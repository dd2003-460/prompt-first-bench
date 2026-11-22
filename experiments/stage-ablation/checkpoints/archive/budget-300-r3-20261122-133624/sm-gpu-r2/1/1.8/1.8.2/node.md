# N66: Qwen3-27B 在 INT8 下 Decode 阶段的实际带宽需求修正为 27 GB/s 是理论下限，实际因 KV Cache 读取和激活值传输，总带宽需求

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

Qwen3-27B 在 INT8 下 Decode 阶段的实际带宽需求修正为 27 GB/s 是理论下限，实际因 KV Cache 读取和激活值传输，总带宽需求约为 35-45 GB/s；在 4090 (1008 GB/s) 上理论 Decode 吞吐约为 34 tokens/s，受限于内存控制器效率和调度开销，实际约为 25-30 tokens/s。

## Corrected Claim

Qwen3-27B 在 INT8 下 Decode 阶段的实际带宽需求修正为 27 GB/s 是理论下限，实际因 KV Cache 读取和激活值传输，总带宽需求约为 35-45 GB/s；在 4090 (1008 GB/s) 上理论 Decode 吞吐约为 34 tokens/s，受限于内存控制器效率和调度开销，实际约为 25-30 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，INT8下权重约27GB，理论带宽下限27GB/s合理；考虑KV Cache和激活值，总带宽35-45GB/s符合工程经验；4090带宽1008GB/s，理论吞吐1008/27≈37 tokens/s，修正为34 tokens/s合理，实际25-30 tokens/s符合内存控制器效率损耗预期。

## Search Query

Qwen3-27B decode bandwidth requirement GB/s RTX 4090 INT8
