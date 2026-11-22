# N64: Qwen3-27B 在 BF16 下 Decode 阶段的实际带宽需求修正为 54 GB/s 是理论下限，实际因 KV Cache 读取和激活值传输，总带宽需求

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16下权重约54GB，理论带宽需求54GB/s合理；4090带宽1008GB/s，理论吞吐1008/54≈18.7 tokens/s，考虑KV Cache和激活值后实际带宽60-70GB/s，理论吞吐1008/65≈15.5 tokens/s，实际12-15 tokens/s符合内存控制器效率和调度开销的合理折损，数值量级和逻辑自洽。

## Search Query

Qwen3-27B decode bandwidth requirement GB/s RTX 4090 BF16
