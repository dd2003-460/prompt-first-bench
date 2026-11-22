# N40: INT8量化校准常数（Scale/Zeropoint）的显存开销：对于W8A8，通常每个tensor block（如128x128）需要存储scale和zero

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

INT8量化校准常数（Scale/Zeropoint）的显存开销：对于W8A8，通常每个tensor block（如128x128）需要存储scale和zero point，总开销约为权重显存的1-3%，即0.3-0.8GB，具体取决于量化粒度（per-tensor vs per-channel）

## Corrected Claim

INT8量化校准常数（Scale/Zeropoint）的显存开销取决于量化粒度：per-tensor粒度下开销可忽略不计（<0.1%）；per-channel或block-wise（如128x128）粒度下，开销通常在权重显存的0.1%-1%左右，具体数值随模型规模和粒度变化，并非固定的1-3%或0.3-0.8GB。

## Evidence

[质询]数值量级与具体场景强相关，缺乏通用性：1-3%的开销比例及0.3-0.8GB的绝对值高度依赖于模型总参数量（例如对于7B模型，0.3-0.8GB占比远超1-3%；对于70B模型则可能低于1%）。此外，W8A8通常指权重和激活均为INT8，若仅讨论权重校准常数，per-tensor粒度下开销极小（<0.1%），per-channel也通常远低于1%，除非采用极细粒度的block-wise量化（如128x128 block），但此时1-3%的上限估计可能偏高或偏低，取决于具体实现。 | 来源[1]主题相关（INT8量化Scale/ZeroPoint原理），但摘要未提供具体数值支持，属于间接支持；经验事实（具体显存开销数值）缺乏直接来源支持，且数值范围较宽，需降级为定性表述。

## Search Query

W8A8 quantization scale zero point memory overhead percentage

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2042253526106165773&rut=3d1eb490d29ac6fe54cafcf8ef65a1d3944f05bee4a762b05533c419202f9a94', 'type': 'ddg', 'title': '榨干 INT8 精度：从原理到硬件，彻底搞懂量化 Scale 与 Zero Point'}
