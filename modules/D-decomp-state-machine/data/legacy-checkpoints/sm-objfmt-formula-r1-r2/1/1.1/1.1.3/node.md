# N47: AMD RX 7900 XTX 24GB 当前市场均价约为 $900-$1000 USD，单GB显存成本约为 $38-$42/GB，但因缺乏成熟的 FP8/NV

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N7, N8, N9

## Claim

AMD RX 7900 XTX 24GB 当前市场均价约为 $900-$1000 USD，单GB显存成本约为 $38-$42/GB，但因缺乏成熟的 FP8/NVFP4 推理框架支持（ROCm 生态滞后），其有效性价比在 LLM 推理场景中低于 NVIDIA 同级产品

## Corrected Claim

AMD RX 7900 XTX 24GB 的市场价格通常在 $900-$1000 USD 区间波动，单GB显存成本约为 $38-$42/GB；由于 ROCm 生态在 FP8/NVFP4 推理框架支持上相对滞后，其在特定 LLM 推理场景下的软件优化程度和易用性可能低于 NVIDIA 同级产品，从而影响综合性价比。

## Evidence

[质询]价格波动性高且随时间变化，$900-$1000 的均价可能偏离当前实时市场价；此外，'有效性价比低于 NVIDIA' 是一个主观且依赖具体工作负载的结论，缺乏量化基准测试支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

RX 7900 XTX price ROCm LLM inference support FP8 compatibility
