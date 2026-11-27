# N33: RTX 4060 Ti 16GB 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cach

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

RTX 4060 Ti 16GB 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cache) + 2GB(激活/框架) ≈ 20GB，大于 16GB 物理显存，必须启用 CPU Offload，吞吐量预计降至 15-25 tokens/s

## Corrected Claim

RTX 4060 Ti 16GB 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文，显存占用预计超过 16GB（权重约 13.5GB + KV Cache 及激活值），必须启用 CPU Offload，吞吐量将显著下降，具体数值取决于 CPU 内存带宽和 PCIe 版本。

## Evidence

[质询]KV Cache 4.5GB 的估算可能偏高或偏低，取决于具体的注意力头配置和精度（FP16 vs FP8），且 15-25 tokens/s 的吞吐量受 CPU 内存带宽和 PCIe 版本影响极大，缺乏具体硬件环境（如 DDR5 频率、PCIe 4.0/5.0）支持，数值精确度存疑。 | 先验知识/题面给定，逻辑校验通过：Qwen3-27B W4 量化权重约 13.5-14GB，加上 32K 上下文的 KV Cache 和激活值，总显存需求确实超过 16GB，必须启用 Offload；但具体 KV Cache 大小和吞吐量数值为经验估算，缺乏来源直接支持，故降级。
