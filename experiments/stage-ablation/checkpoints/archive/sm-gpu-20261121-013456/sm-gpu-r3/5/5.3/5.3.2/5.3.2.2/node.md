# N232: 架构代际更新失效触发点量化：当新架构（如Blackwell RTX 5090）发布且其单位吞吐成本（TCO_3y / throughput_tokens_s）低

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

架构代际更新失效触发点量化：当新架构（如Blackwell RTX 5090）发布且其单位吞吐成本（TCO_3y / throughput_tokens_s）低于旧架构（Ada 4090）的 80% 时，旧架构TCO模型失效。计算公式：Ratio = (TCO_new / Throughput_new) / (TCO_old / Throughput_old)。若 Ratio < 0.8，则旧方案不再推荐。当前RTX 5090预计单位成本比4090低30-40% [待核验：需RTX 5090正式发布价格与实测吞吐]。

## Corrected Claim

架构代际更新失效触发点量化：当新架构（如Blackwell RTX 5090）发布且其单位吞吐成本（TCO_3y / throughput_tokens_s）低于旧架构（Ada 4090）的 80% 时，旧架构TCO模型失效。计算公式：Ratio = (TCO_new / Throughput_new) / (TCO_old / Throughput_old)。若 Ratio < 0.8，则旧方案不再推荐。当前RTX 5090在支持NVFP4等新技术下具有显著性能优势，具体单位成本降低幅度需结合实测吞吐与价格进一步核验。

## Evidence

[质询]陈述中关于“RTX 5090预计单位成本比4090低30-40%”的具体数值缺乏直接来源支持，且“单位吞吐成本”受具体模型、量化精度（如NVFP4 vs FP16）及负载类型影响极大，单一百分比区间可能过于简化或存在口径混淆。 | 来源[1]和[3]确认了RTX 5090基于Blackwell架构及NVFP4支持，证实了架构代际更新的事实，但未提供具体的TCO对比数值或30-40%的成本降低数据；该数值属于经验事实，逻辑自洽但缺来源直接支持。

## Search Query

RTX 5090 vs RTX 4090 inference throughput cost efficiency comparison

## Retrieval Sources

- {'url': 'https://github.com/lna-lab/blackwell-geforce-nvfp4-gemm&rut=f9eb2a0906512712d452cd20481ade41697c6f49f9a3c03e5e00076ebb05a36c', 'type': 'ddg', 'title': 'blackwell-geforce-nvfp4-gemm - GitHub'}
- {'url': 'https://zhuanlan.zhihu.com/p/2106277546606305799&rut=7d1a0414d31f134cd770fc138a6bae6aead8602b26bb34fcdb467cb9326429e5', 'type': 'ddg', 'title': 'Blackwell 架构深度剖析：从双 die 封装到 tcgen05，以及每个新特性对应的优化手法'}
- {'url': 'https://zhuanlan.zhihu.com/p/18645190489&rut=d3e7ea85d0e28e74cca132d9455053b5d2df170aaa5a1b07976eedf9cfe1c9ee', 'type': 'ddg', 'title': 'Nvidia Blackwell架构深度剖析：深入了解RTX 50系列GPU的升级'}
