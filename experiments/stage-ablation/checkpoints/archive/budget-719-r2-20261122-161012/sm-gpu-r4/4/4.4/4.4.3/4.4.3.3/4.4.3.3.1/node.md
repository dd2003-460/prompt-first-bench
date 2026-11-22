# N550: 1x H100 BF16 剩余 25GB 显存的 Batch Size 扩展量化：在 32K 上下文下，每增加 1 个 Batch 需额外 ~2GB 显存 (K

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N228

## Claim

1x H100 BF16 剩余 25GB 显存的 Batch Size 扩展量化：在 32K 上下文下，每增加 1 个 Batch 需额外 ~2GB 显存 (KV Cache + 激活值)，因此 25GB 剩余空间支持最大 Batch Size=10 (25GB/2.5GB per batch)；但 H100 的 BF16 峰值算力 (989 TFLOPS) 在 Batch Size>4 后受内存带宽 (3350 GB/s) 限制，实际吞吐增益递减，Batch Size=8 时吞吐从 60.9 tokens/s 降至 ~55 tokens/s (单用户口径不变，但并发能力增强)。

## Corrected Claim

在32K上下文下，1x H100 BF16剩余25GB显存，若每增加1个Batch需额外~2-2.5GB显存，理论上支持最大Batch Size约为10-12。随着Batch Size增加，单用户延迟可能增加，但总吞吐通常提升直至内存带宽成为瓶颈。具体吞吐数值需实测，不能简单断言Batch Size=8时总吞吐低于Batch Size=1。

## Evidence

[质询]数值量级与逻辑自洽性存在矛盾：1. 显存计算错误：25GB剩余空间除以每Batch 2GB（或2.5GB）应支持12-13个Batch，而非10个；2. 性能数据违背直觉：Batch Size从1增加到8，总吞吐（Total Throughput）通常应增加，而陈述称吞吐从60.9降至55 tokens/s，若指单用户延迟增加则表述为'吞吐降低'不准确，若指总吞吐降低则违背GPU并行计算基本规律（除非是极端内存带宽瓶颈下的异常，但H100在BS=8时通常未达此瓶颈）；3. 经验参数（如每Batch 2GB显存、具体吞吐值）属于经验事实，缺乏来源支持。 | 经验事实，逻辑校验发现显存计算与性能趋势描述存在内部矛盾或缺乏严谨性，且无外部来源支持，故降级。
