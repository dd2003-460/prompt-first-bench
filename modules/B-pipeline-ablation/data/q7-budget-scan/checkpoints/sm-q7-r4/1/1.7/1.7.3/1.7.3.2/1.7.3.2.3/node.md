# N420: QD>64 后的功耗平台期原因：当 QD 超过 64 时，NVMe 控制器的内部仲裁器 (Arbiter) 成为瓶颈，无法进一步并行化 NAND 操作，功耗不再

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N184

## Claim

QD>64 后的功耗平台期原因：当 QD 超过 64 时，NVMe 控制器的内部仲裁器 (Arbiter) 成为瓶颈，无法进一步并行化 NAND 操作，功耗不再随 QD 线性增长，而是趋于饱和值 20-21W，增加 QD 仅带来 < 2% 的额外能耗

## Corrected Claim

QD>64 后的功耗平台期原因：当 QD 超过 64 时，NVMe 控制器的内部仲裁器 (Arbiter) 成为瓶颈，无法进一步并行化 NAND 操作，功耗不再随 QD 线性增长，而是趋于饱和值 20-21W，增加 QD 仅带来 < 2% 的额外能耗

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe controller arbiter bottleneck power saturation high queue depth
