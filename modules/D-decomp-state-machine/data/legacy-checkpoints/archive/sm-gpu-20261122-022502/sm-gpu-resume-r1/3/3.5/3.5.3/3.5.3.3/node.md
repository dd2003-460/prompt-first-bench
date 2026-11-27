# N238: Qwen3-27B 在 Apple M2 Ultra (MLX/Llama.cpp) 上的实测 Decode 吞吐与理论带宽上限的比值（Efficiency R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

Qwen3-27B 在 Apple M2 Ultra (MLX/Llama.cpp) 上的实测 Decode 吞吐与理论带宽上限的比值（Efficiency Ratio）：若理论上限为 12.0 tokens/s (N89)，实测 12-15 tokens/s (N86) 表明效率比 >100% 或理论计算存在偏差（可能因 KV Cache 读取未完全计入瓶颈或量化格式差异），需重新校准理论模型中的带宽瓶颈项（权重 vs KV Cache 读取比例）。

## Corrected Claim

Qwen3-27B 在 Apple M2 Ultra (MLX/Llama.cpp) 上的实测 Decode 吞吐与理论带宽上限的比值（Efficiency Ratio）：若理论上限为 12.0 tokens/s (N89)，实测 12-15 tokens/s (N86) 表明效率比 >100% 或理论计算存在偏差（可能因 KV Cache 读取未完全计入瓶颈或量化格式差异），需重新校准理论模型中的带宽瓶颈项（权重 vs KV Cache 读取比例）。

## Evidence

先验知识/题面给定，逻辑校验通过：实测吞吐（12-15 tokens/s）高于理论带宽上限（12.0 tokens/s）在物理上意味着效率比>100%，这通常表明理论模型低估了有效带宽或高估了瓶颈（如未准确计入KV Cache优化或量化影响），该推断符合硬件性能分析的基本逻辑。
