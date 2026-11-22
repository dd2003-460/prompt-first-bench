# N446: 单卡 RTX 4090 运行 W4+FP8 KV 配置的显存余量风险量化：总占用估算为 14.5 GB (权重) + 4 GB (KV) + 1.5 GB (开

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N185

## Claim

单卡 RTX 4090 运行 W4+FP8 KV 配置的显存余量风险量化：总占用估算为 14.5 GB (权重) + 4 GB (KV) + 1.5 GB (开销) = 19.5 GB。剩余显存 = 24 GB - 19.5 GB = 4.5 GB。该余量需覆盖动态激活值 (Activations) 峰值。若 Batch Size=1 且 Seq Len=32K，激活值峰值可能达到 1-2 GB，导致总占用逼近 21.5-22.5 GB，存在 OOM (Out Of Memory) 风险，需设置 Max Batch Size=1 并监控显存峰值。

## Corrected Claim

单卡 RTX 4090 运行 W4+FP8 KV 配置的显存余量风险量化：总占用估算为 14.5 GB (权重) + 4 GB (KV) + 1.5 GB (开销) = 19.5 GB。剩余显存 = 24 GB - 19.5 GB = 4.5 GB。该余量需覆盖动态激活值 (Activations) 峰值。若 Batch Size=1 且 Seq Len=32K，激活值峰值可能达到 1-2 GB，导致总占用逼近 21.5-22.5 GB，存在 OOM (Out Of Memory) 风险，需设置 Max Batch Size=1 并监控显存峰值。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存为 24GB，W4 量化权重约 14.5GB（对应约 30B 参数模型），FP8 KV Cache 在 32K 序列下约 4GB，激活值估算 1-2GB，总占用 19.5-22.5GB，余量 1.5-4.5GB，存在 OOM 风险符合工程直觉。
