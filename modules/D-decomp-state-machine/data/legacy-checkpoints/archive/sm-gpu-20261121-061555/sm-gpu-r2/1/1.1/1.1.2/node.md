# N41: NVIDIA RTX 5080 (Blackwell) 的显存规格为 16GB GDDR7，带宽 960 GB/s，TDP 300W；其显存容量与 RTX 40

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

NVIDIA RTX 5080 (Blackwell) 的显存规格为 16GB GDDR7，带宽 960 GB/s，TDP 300W；其显存容量与 RTX 4080 Super 持平但带宽翻倍，需核实其是否支持 NVFP4 量化以决定其在 Qwen3-27B W4 推理中的可行性 [待核验]

## Corrected Claim

NVIDIA RTX 5080 (Blackwell) 的显存规格通常被报道为 16GB GDDR7，带宽约 960 GB/s，TDP 300W；其显存容量与 RTX 4080 Super 持平但带宽显著提升，需进一步核实其是否支持 NVFP4 量化以决定其在 Qwen3-27B W4 推理中的可行性。

## Evidence

[质询]参考来源[1]仅提供了产品营销页面链接和简短描述，未包含具体的显存容量、带宽、TDP等硬件规格参数，无法直接验证陈述中的具体数值（16GB, 960 GB/s, 300W）；此外，NVFP4支持情况也未在来源中体现。 | 经验事实，逻辑自洽但缺来源支持。来源[1]主题相关但内容过于简略，未提供具体规格数据以直接支持或反驳数值细节。

## Search Query

NVIDIA RTX 5080 specs GDDR7 bandwidth NVFP4 support

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/&rut=712d164b0ec1607ce20d30c2299b8c9947736df82aec018bd6019e067dede76c', 'type': 'ddg', 'title': 'GeForce RTX 5080 Graphics Cards | NVIDIA'}
