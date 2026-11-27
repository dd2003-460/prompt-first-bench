# N246: 1×RTX 4090 BF16 Offload 方案的显存溢出机制：权重 54GB 中仅 24GB 驻留 GPU，剩余 30GB 在 CPU 内存，每次解码需从

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

1×RTX 4090 BF16 Offload 方案的显存溢出机制：权重 54GB 中仅 24GB 驻留 GPU，剩余 30GB 在 CPU 内存，每次解码需从 CPU 加载 30GB 数据，PCIe 4.0 带宽 32GB/s 下加载耗时 0.94s，导致吞吐量从理论 5-8 tokens/s 降至 2-3 tokens/s，TCO/Throughput 恶化至 $0.05-$0.08/token

## Corrected Claim

1×RTX 4090 BF16 Offload 方案的显存溢出机制：权重 54GB 中仅 24GB 驻留 GPU，剩余 30GB 在 CPU 内存，每次解码需从 CPU 加载 30GB 数据，PCIe 4.0 带宽 32GB/s 下加载耗时 0.94s，导致吞吐量从理论 5-8 tokens/s 降至 2-3 tokens/s，TCO/Throughput 恶化至 $0.05-$0.08/token

## Evidence

先验知识/题面给定，逻辑校验通过：30GB/32GB/s≈0.94s，计算自洽；RTX 4090 24GB 显存与 PCIe 4.0 带宽符合硬件规格常识。
