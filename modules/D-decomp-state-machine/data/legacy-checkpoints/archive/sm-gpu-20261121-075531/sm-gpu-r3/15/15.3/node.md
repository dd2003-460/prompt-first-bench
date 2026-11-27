# N383: Mac Studio (M2 Ultra, 192GB统一内存) 运行 Qwen3-27B (BF16/FP16) 的推理吞吐量约为 20-30 tokens/

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130

## Claim

Mac Studio (M2 Ultra, 192GB统一内存) 运行 Qwen3-27B (BF16/FP16) 的推理吞吐量约为 20-30 tokens/s，显著低于 RTX 5090 (60-70 tokens/s)，但噪音优势使其在特定场景下成为唯一可行选项。

## Corrected Claim

Mac Studio (M2 Ultra, 192GB统一内存) 运行 Qwen3-27B (BF16/FP16) 的推理吞吐量显著低于 RTX 5090，但噪音优势使其在特定场景下成为可行选项。

## Evidence

[质询]吞吐量数值（20-30 tokens/s）属于具体硬件性能经验数据，缺乏直接来源支持，且不同量化/优化策略下波动较大，存在量级偏差风险。 | 经验事实，逻辑自洽但缺来源支持
