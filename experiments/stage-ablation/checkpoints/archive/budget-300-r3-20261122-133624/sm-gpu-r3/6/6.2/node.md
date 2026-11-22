# N159: PagedAttention 在 RTX 4090 上的性能开销量化：启用 PagedAttention 后，由于内存分配碎片化和间接寻址，Decode 吞吐量

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

PagedAttention 在 RTX 4090 上的性能开销量化：启用 PagedAttention 后，由于内存分配碎片化和间接寻址，Decode 吞吐量通常下降 5-10%。对于 24GB 显存的 4090，若限制上下文至 16K，KV Cache 占用约 2.0GB，加上 27GB 权重和 2GB 框架，总占用 31GB，仍超出 24GB，故 4090 单卡在 32K 上下文下即使启用 PagedAttention 也无法运行 INT8 模型，必须使用 W4 量化（权重 13.5GB）或双卡方案。

## Corrected Claim

对于24GB显存的RTX 4090，若模型INT8权重为27GB，则单卡无法运行该模型，必须使用W4量化（权重约13.5GB）或双卡方案。PagedAttention主要用于优化KV Cache内存管理，其引入的额外计算开销通常较小，不会导致5-10%的显著吞吐量下降。

## Evidence

[质询]数值量级与逻辑矛盾：陈述中声称总占用31GB（2.0GB KV + 27GB权重 + 2GB框架），但27GB权重本身已远超24GB显存，无论是否启用PagedAttention或限制上下文，单卡4090根本无法加载27GB的INT8模型，因此‘限制上下文至16K’这一条件对解决显存溢出毫无意义，属于无效前提；此外，PagedAttention通常用于解决碎片化以提升吞吐或支持更大batch，而非导致5-10%的显著性能下降（通常开销极小或可忽略，甚至因减少碎片而提升效率），该性能开销数值缺乏普遍共识支持。 | 逻辑校验失败：27GB权重 > 24GB显存，单卡无法运行，与上下文长度无关；PagedAttention性能开销描述与主流认知（通常开销极低或有益）存在偏差。

## Search Query

PagedAttention overhead RTX 4090 24GB 27B model W4 quantization feasibility
