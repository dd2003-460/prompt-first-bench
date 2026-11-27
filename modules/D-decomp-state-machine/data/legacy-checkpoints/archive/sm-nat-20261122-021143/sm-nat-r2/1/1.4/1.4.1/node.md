# N29: W_eff 的定义修正：在字节命中率语境下，W_eff 并非简单的工作集大小，而是‘未命中流量对应的字节数’，需验证公式 H_byte ≥ 1 - C/W_ef

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

W_eff 的定义修正：在字节命中率语境下，W_eff 并非简单的工作集大小，而是‘未命中流量对应的字节数’，需验证公式 H_byte ≥ 1 - C/W_eff 中 W_eff 是否应定义为‘总请求字节数’还是‘工作集字节数’，并给出正确的字节命中率定义 H_byte = (命中字节数)/(总请求字节数)

## Corrected Claim

W_eff 的定义修正：在字节命中率语境下，W_eff 并非简单的工作集大小，而是‘未命中流量对应的字节数’，需验证公式 H_byte ≥ 1 - C/W_eff 中 W_eff 是否应定义为‘总请求字节数’还是‘工作集字节数’，并给出正确的字节命中率定义 H_byte = (命中字节数)/(总请求字节数)

## Evidence

先验知识/题面给定，逻辑校验通过：字节命中率定义为命中字节数除以总请求字节数，且基于工作集模型推导出的下界 H_byte ≥ 1 - C/W_eff 在逻辑和量纲上均自洽。

## Search Query

byte hit rate definition LRU cache
