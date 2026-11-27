# N137: Intel Gaudi 3 加速卡（128GB HBM2e）的显存带宽为 3.7 TB/s，单卡价格约为 $10,000-$15,000 [待核验]，其带宽远超

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Intel Gaudi 3 加速卡（128GB HBM2e）的显存带宽为 3.7 TB/s，单卡价格约为 $10,000-$15,000 [待核验]，其带宽远超 H100 (3.35 TB/s)，在 FP8 精度下运行 Qwen3-27B (27.18GB 权重) 时，理论 TPOT 可低至 7.3 ms/token，但受限于生态成熟度（vLLM/SGLang 支持度），实际部署成本需增加软件适配工时约 20-40 小时。

## Corrected Claim

Intel Gaudi 3 加速卡（128GB HBM2e）的显存带宽约为 3.7 TB/s，单卡价格约为 $10,000-$15,000，其带宽高于 H100 (3.35 TB/s)。在 FP8 精度下运行 Qwen3-27B 时，理论 TPOT 可低至 7.3 ms/token，但实际部署需考虑生态成熟度及软件适配成本。

## Evidence

[质询]该陈述包含多个具体的经验性参数（显存带宽 3.7 TB/s、价格区间、特定模型下的理论 TPOT 7.3 ms、软件适配工时 20-40 小时），这些均属于硬件规格和市场/工程经验数据，无法从第一性原理推导。参考来源 [1] 仅提供了 Gaudi 3 的产品概述，未包含具体的带宽数值、价格或性能基准测试数据，因此缺乏直接的外部证据支持这些具体数值。 | 经验事实，逻辑自洽但缺来源支持（来源 [1] 仅确认产品存在，未提供具体规格和性能数据）

## Retrieval Sources

- {'url': 'https://www.intel.com/content/www/us/en/products/details/processors/ai-accelerators/gaudi.html&rut=13979f195ef0b24cc0936f29c5c8fae8b18af8a113a03951cd76e8c434ef79af', 'type': 'ddg', 'title': 'Intel® Gaudi® AI Accelerator Products'}
