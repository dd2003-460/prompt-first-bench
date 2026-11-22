# N35: AMD MI250X 显存带宽为 3276 GB/s (HBM2)，NVIDIA A100 80GB 为 2039 GB/s (HBM2e)，NVIDIA H1

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

AMD MI250X 显存带宽为 3276 GB/s (HBM2)，NVIDIA A100 80GB 为 2039 GB/s (HBM2e)，NVIDIA H100 80GB 为 3350 GB/s (HBM3)；对于 27B BF16 模型 (54GB)，MI250X 理论吞吐上限约为 3276/56 ≈ 58.5 tokens/s，显著高于消费级显卡。

## Corrected Claim

AMD MI250X 显存带宽约为 3276 GB/s (HBM2)，NVIDIA A100 80GB 为 2039 GB/s (HBM2e)，NVIDIA H100 80GB 为 3350 GB/s (HBM3)；对于 27B BF16 模型 (54GB)，基于显存带宽的粗略估算值约为 58.5 tokens/s，实际吞吐受计算和内存访问模式影响。

## Evidence

[质询]参考来源摘要中未包含具体的显存带宽数值（3276 GB/s, 2039 GB/s, 3350 GB/s），无法通过提供的来源直接验证这些具体参数；且将显存带宽直接除以模型大小得出的'理论吞吐上限'在工程上是一个极度简化的估算，忽略了计算瓶颈、内存访问模式及实际利用率，容易误导对实际性能的预期。 | 来源[1][2][3]确认了MI250X的存在及定位，但摘要未提供具体带宽数值；逻辑上3276/56≈58.5计算正确，但作为'理论吞吐上限'表述过于简化，且缺乏来源对具体数值的直接支持，属于经验事实缺来源支持。

## Retrieval Sources

- {'url': 'https://www.amd.com/en/products/accelerators/instinct/mi200/mi250x.html&rut=1943c9632f901a33b38d3269a930cc9e228b95e24eab454e6dfb305e0699d828', 'type': 'ddg', 'title': 'AMD Instinct™ MI250X Accelerators'}
- {'url': 'https://www.techpowerup.com/gpu-specs/instinct-mi250x.c3837&rut=e60f181fd70d3dc4e3408ab6858134b9ecaed6dce2c1610682e266a1a7f3515d', 'type': 'ddg', 'title': 'AMD Instinct MI250X Specs | TechPowerUp GPU Database'}
- {'url': 'https://www.amd.com/zh-cn/products/accelerators/instinct/mi200/mi250x.html&rut=b55e29b41abf03d6be47e4732824b711343059390d23d36e4cf220836d30896c', 'type': 'ddg', 'title': 'AMD Instinct MI250X 加速器'}
