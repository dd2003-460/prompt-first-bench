# N40: 在 INT4 精度下，32K 上下文窗口的 KV Cache 总占用量为 0.27 GB，计算公式为 2 * 16 * 4 * 128 * 32768 * 0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

在 INT4 精度下，32K 上下文窗口的 KV Cache 总占用量为 0.27 GB，计算公式为 2 * 16 * 4 * 128 * 32768 * 0.5 bytes。

## Corrected Claim

在 INT4 精度下，32K 上下文窗口的 KV Cache 总占用量为 0.27 GB，计算公式为 2 * 16 * 4 * 128 * 32768 * 0.5 bytes。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 16 * 4 * 128 * 32768 * 0.5 计算结果为 268,435,456 bytes，即 256 MiB (0.25 GiB) 或 0.268 GB (十进制)，与陈述中的 0.27 GB 在合理精度范围内一致，且参数（层数16、头数4、头维128、上下文32K、INT4=0.5字节）符合常见LLM架构设定。
