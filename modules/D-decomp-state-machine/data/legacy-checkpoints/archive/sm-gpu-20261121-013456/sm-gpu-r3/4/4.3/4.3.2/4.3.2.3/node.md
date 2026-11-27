# N200: 切换至 INT8 量化的可行性与代价量化：INT8 权重占用 27GB（相比 BF16 54GB 减半），双卡总显存需求 27GB + 4.3GB (KV) +

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

切换至 INT8 量化的可行性与代价量化：INT8 权重占用 27GB（相比 BF16 54GB 减半），双卡总显存需求 27GB + 4.3GB (KV) + 2GB (Buffer) = 33.3GB < 48GB，可行；但 INT8 量化通常需使用 GPTQ 或 AWQ 算法，校准数据集大小（如 128-512 样本）对最终准确率影响 < 0.5%，吞吐量相比 BF16 提升约 1.5-2x，单位 token 成本降低 33-50%。

## Corrected Claim

切换至 INT8 量化的可行性与代价量化：INT8 权重占用 27GB（相比 BF16 54GB 减半），双卡总显存需求 27GB + 4.3GB (KV) + 2GB (Buffer) = 33.3GB < 48GB，可行；INT8 量化通常需使用 GPTQ 或 AWQ 算法，校准数据集大小（如 128-512 样本）对最终准确率影响通常较小；吞吐量相比 BF16 通常有显著提升（具体倍数取决于硬件与推理引擎，常见范围约 1.5-2x），单位 token 成本相应降低。

## Evidence

[质询]吞吐量提升 1.5-2x 及单位 token 成本降低 33-50% 属于高度依赖具体硬件架构（如是否支持 INT8 Tensor Core）、推理引擎（vLLM/TensorRT-LLM）及模型结构的经验性数据，并非 INT8 量化的通用物理定律或第一性原理必然结果，且参考来源未提供具体数值支持。 | 来源 [1] 直接支持 INT8 权重存储减半（54GB->27GB）的逻辑，但缺乏对吞吐量提升倍数和成本降低幅度的具体数据支持，属于经验事实且仅有一个间接/部分相关来源，故降级。

## Search Query

Qwen3-27B INT8 GPTQ AWQ memory footprint throughput improvement

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2101062704052041724&rut=600fd92f86dd11b8172752cfc8f88a070a9c2addd03538149b791efd523dcf29', 'type': 'ddg', 'title': '从 Fp16 到 Int8：一文搞懂模型量化、伪量化、Ptq 与 Qat'}
