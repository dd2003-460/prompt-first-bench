# N193: 在 TP=2 张量并行下，Qwen3-27B 每层 Transformer 需跨卡同步的激活数据量 V_sync 约为 4 MB（基于 Batch=1, Seq

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

在 TP=2 张量并行下，Qwen3-27B 每层 Transformer 需跨卡同步的激活数据量 V_sync 约为 4 MB（基于 Batch=1, Seq=32K, Hidden=4096, BF16 精度计算：2 * 32768 * 4096 * 2 bytes / 1024^2），而非 N52 中声称的 ~1 GB；若采用更高 Batch 或全精度 KV 同步，该数值需按 Batch_Size * Seq_Len * Hidden * Dtype_Size 重新计算。

## Corrected Claim

在 TP=2 张量并行下，Qwen3-27B 每层 Transformer 需跨卡同步的激活数据量 V_sync 约为 512 MB（基于 Batch=1, Seq=32K, Hidden=4096, BF16 精度计算：2 * 32768 * 4096 * 2 bytes / 1024^2 = 512 MB），而非 N52 中声称的 ~1 GB；若采用更高 Batch 或全精度 KV 同步，该数值需按 Batch_Size * Seq_Len * Hidden * Dtype_Size 重新计算。

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2 * 32768 * 4096 * 2 bytes = 536,870,912 bytes ≈ 512 MB，与陈述中的 4 MB 存在数量级差异，但陈述核心在于指出 N52 的 ~1 GB 错误并给出基于特定公式的修正逻辑。然而，仔细检查计算：2 * 32768 * 4096 * 2 = 536,870,912 Bytes = 512 MB。陈述中声称计算结果为 4 MB，这是明显的算术错误（512 MB vs 4 MB）。等等，让我重新计算：32768 * 4096 = 134,217,728。乘以 2 (BF16) = 268,435,456 Bytes = 256 MB。再乘以 2 (可能是双向或两个张量?) = 512 MB。陈述说结果是 4 MB，这显然是错的。但是，题目要求核验的是“关键事实节点”的陈述。陈述说“V_sync 约为 4 MB... (基于...计算：2 * 32768 * 4096 * 2 bytes / 1024^2)”。让我们算一下括号里的值：(2 * 32768 * 4096 * 2) / (1024 * 1024) = 536870912 / 1048576 = 512。所以计算结果应该是 512 MB，而不是 4 MB。陈述中的数值结论（4 MB）与其提供的计算公式（得出 512 MB）矛盾。这是一个硬逻辑错误/内部矛盾。因此，该陈述在逻辑上不自洽。
