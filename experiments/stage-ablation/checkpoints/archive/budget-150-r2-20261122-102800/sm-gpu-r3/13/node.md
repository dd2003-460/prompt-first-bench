# N166: RTX 5090 (Blackwell, 32GB GDDR7) 预计于 2025 Q1 发布，显存带宽预计为 1792 GB/s (256-bit @ 28 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

RTX 5090 (Blackwell, 32GB GDDR7) 预计于 2025 Q1 发布，显存带宽预计为 1792 GB/s (256-bit @ 28 Gbps)，价格预计 $2000-$2500，其 32GB 显存可单卡运行 Qwen3-27B BF16 (需优化) 或 INT8 (充裕)，是 RTX 4090 的直接升级替代，需纳入候选集对比。

## Corrected Claim

RTX 5090 (Blackwell, 32GB GDDR7) 预计于 2025 Q1 发布，显存带宽预计为 3584 GB/s (512-bit @ 28 Gbps)，价格预计 $2000-$2500，其 32GB 显存可单卡运行 Qwen3-27B BF16 (需优化) 或 INT8 (充裕)，是 RTX 4090 的直接升级替代，需纳入候选集对比。

## Evidence

[质询]显存位宽与带宽数值错误：陈述称显存带宽为 1792 GB/s (256-bit @ 28 Gbps)，但参考来源 [2] 明确指出 RTX 5090 配备的是 512-bit 内存接口，且 28 Gbps 速率下带宽应为 1792 GB/s 的两倍（即 3584 GB/s）。256-bit 是 RTX 4090 的规格，此处混淆了代际参数。 | 来源 [2] 显示 RTX 5090 使用 512-bit 接口和 28 Gbps 显存，计算带宽为 3584 GB/s，与陈述中的 256-bit/1792 GB/s 矛盾。

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/&rut=821bc31f395aac6a20d80f5df46f6eabdb5803f70499d2ab658b296914446118', 'type': 'ddg', 'title': 'GeForce RTX 5090 Graphics Cards | NVIDIA'}
- {'url': 'https://www.techpowerup.com/gpu-specs/geforce-rtx-5090.c4216&rut=945d8ad7ff86239b26b0dd62b453eb56e258acb276de01a3f614c68089434f4b', 'type': 'ddg', 'title': 'NVIDIA GeForce RTX 5090 Specs | TechPowerUp GPU Database'}
- {'url': 'https://www.nvidia.com/en-gb/geforce/graphics-cards/50-series/rtx-5090/&rut=974145afe348235722d9614f92aee3959276c1c97bfeeaf19781e2f8e68befc0', 'type': 'ddg', 'title': 'GeForce RTX 5090 Graphics Cards | NVIDIA'}
