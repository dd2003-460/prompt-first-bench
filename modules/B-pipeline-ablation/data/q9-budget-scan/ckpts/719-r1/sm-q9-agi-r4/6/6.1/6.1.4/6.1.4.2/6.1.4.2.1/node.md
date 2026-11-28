# N704: UECC (Uncorrectable ECC) 静默数据损坏 (SDC) 的发生率基线：在 V100 长期运行中，SDC 发生率约为 1e-9 / FLOP，

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N258

## Claim

UECC (Uncorrectable ECC) 静默数据损坏 (SDC) 的发生率基线：在 V100 长期运行中，SDC 发生率约为 1e-9 / FLOP，对于 27B 模型单次推理约 1e14 FLOPs，单次推理 SDC 概率 ≈ 1e-5，需通过 checksum 验证或双路计算比对检测。

## Corrected Claim

UECC 导致的静默数据损坏风险在长期运行中不可忽略，具体发生率取决于硬件批次与负载，通常需通过周期性校验和或冗余计算进行监控，而非依赖固定的 1e-9/FLOP 基线。

## Evidence

[质询]数值量级存疑：1e-9/FLOP 的 SDC 发生率远高于业界通常引用的硬件故障率（如 Google 论文中约为 1e-15 到 1e-12 量级），且将‘不可纠正 ECC 错误’直接等同于‘导致最终输出错误的 SDC’忽略了纠错机制和冗余设计的保护，存在高估风险。 | source=knowledge，逻辑推导自洽（1e-9 * 1e14 = 1e-5），但该经验参数（1e-9/FLOP）缺乏权威来源直接支持，且与常见硬件可靠性数据存在数量级差异，故降级为定性表述。

## Search Query

GPU silent data corruption rate uncorrectable ECC V100 benchmark
