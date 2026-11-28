# N9: 显存碎片化率：在max_model_len=262144设置下，vLLM PagedAttention的显存碎片化率随并发数增加而上升，当碎片化率>20%时需启

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

显存碎片化率：在max_model_len=262144设置下，vLLM PagedAttention的显存碎片化率随并发数增加而上升，当碎片化率>20%时需启用--enable-chunked-prefill优化（预期碎片化率与max-num-seqs呈非线性关系）

## Corrected Claim

在max_model_len=262144设置下，vLLM PagedAttention的显存碎片化情况受并发数影响，高并发下可能出现显存分配效率下降，具体碎片化率及是否需要启用--enable-chunked-prefill需根据实际监控数据评估，而非固定阈值>20%。

## Evidence

[质询]该陈述包含具体的经验阈值（碎片化率>20%）和特定的优化建议（启用chunked-prefill），这属于经验事实而非第一性原理可推导内容。此外，PagedAttention的核心设计初衷正是解决显存碎片化问题，通常其碎片化率被控制在较低水平（如<5%），断言在特定配置下会随并发线性/非线性上升至>20%且需特定开关干预，缺乏通用理论支持，可能存在对机制的误解或特定极端场景的过度概括。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体阈值与因果关系无法从第一性原理严格推出）

## Search Query

vLLM PagedAttention memory fragmentation rate max_model_len concurrent requests chunked prefill optimization
