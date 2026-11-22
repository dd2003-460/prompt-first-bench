# N221: KV Cache 精度对显存占用的影响量化：若将 KV Cache 从 BF16 (2 bytes) 降至 INT8 (1 byte)，32K 上下文下的占用从

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N101

## Claim

KV Cache 精度对显存占用的影响量化：若将 KV Cache 从 BF16 (2 bytes) 降至 INT8 (1 byte)，32K 上下文下的占用从 5.2GB 降至 2.6GB，节省 2.6GB 显存；但注意力得分的量化误差会导致长上下文下的幻觉率上升，通常需配合 Q-Attention 或动态精度策略，否则在 >16K 上下文时质量损失超过 2%。

## Corrected Claim

KV Cache 精度降低（如 BF16 转 INT8）可线性减少显存占用（约 50%），但会引入量化误差，可能导致长上下文下的生成质量下降，具体损失幅度取决于模型架构、量化算法及上下文长度，通常需配合校准或混合精度策略以平衡精度与效率。

## Evidence

[质询]数值量级与具体硬件/模型配置强相关，缺乏通用性；且'质量损失超过2%'为经验性统计结论，非第一性原理可推导，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

KV cache quantization INT8 vs FP16 memory savings quality degradation long context
