# N79: 工作点B（INT4量化/24GB显存）：1×RTX 4090运行Qwen3-27B INT4(AWQ)，权重13.5GB+KV Cache 4.3GB+Buff

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

工作点B（INT4量化/24GB显存）：1×RTX 4090运行Qwen3-27B INT4(AWQ)，权重13.5GB+KV Cache 4.3GB+Buffer 2GB≈19.8GB<24GB，可行；吞吐量提升至~30-40 tokens/s（相比BF16的15 tokens/s提升2-2.5倍），TCO_3y保持不变但单位token成本降低50-60%。

## Corrected Claim

工作点B（INT4量化/24GB显存）：1×RTX 4090运行Qwen3-27B INT4(AWQ)在24GB显存下可行（来源证实）；吞吐量预计提升至BF16的2-2.5倍（具体数值需实测确认），单位token成本显著降低。

## Evidence

[质询]吞吐量数值（30-40 tokens/s）及具体显存占用细分（KV Cache 4.3GB）属于特定硬件与配置下的经验事实，参考来源仅确认了可行性（能跑），未提供具体的吞吐量实测数据或精确的显存占用分解，存在数值偏差风险。 | 来源[1]和[2]直接支持RTX 4090 24GB可运行Qwen3-27B INT4量化模型（可行性验证），但缺乏对吞吐量具体数值（30-40 tokens/s）及显存细分构成的直接数据支持，属于经验事实缺来源直接支持。

## Search Query

Qwen3 27B INT4 AWQ RTX 4090 inference speed tokens/s

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2083555506732512359&rut=3500097cb3ed29c7b1bd2fc0071f208d076cac111c37de4fb03e30bdc07669c3', 'type': 'ddg', 'title': '24GB 显存榨干指南：RTX 4090D 部署 Qwen3.8-27B 全流程实测'}
- {'url': 'https://zhuanlan.zhihu.com/p/2078119870546309718&rut=8d72ed3413306adcf30f1029d570ab43e36b0d8f8d054dd81d24aae5200c9272', 'type': 'ddg', 'title': 'RTX 4090 24GB 能跑 Qwen3.8-27B 吗？该选什么量化和云GPU？'}
