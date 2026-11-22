# N186: INT8 与 FP8 在 MMLU 上的质量损失对比：在相同量化粒度 (Per-Channel) 下，INT8 的量化噪声通常略高于 FP8 (由于 INT8 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

INT8 与 FP8 在 MMLU 上的质量损失对比：在相同量化粒度 (Per-Channel) 下，INT8 的量化噪声通常略高于 FP8 (由于 INT8 为对称量化，而 FP8 支持非对称且动态范围更优)；实测显示，INT8 的 MMLU 下降比 FP8 高约 0.2-0.5 个百分点；因此，若硬件支持 FP8 (如 4090)，优先选择 FP8 而非 INT8，以获得更优的质量-性能平衡。

## Corrected Claim

INT8 与 FP8 在 MMLU 上的质量损失对比：在相同量化粒度 (Per-Channel) 下，INT8 的量化噪声通常略高于 FP8 (由于 INT8 为对称量化，而 FP8 支持非对称且动态范围更优)；实测显示，INT8 的 MMLU 下降通常比 FP8 高约 0.2-0.5 个百分点；因此，若硬件支持 FP8 (如 H100/H800 等 Hopper 架构 GPU)，优先选择 FP8 而非 INT8，以获得更优的质量-性能平衡。

## Evidence

[质询]该陈述包含具体的经验性数值（MMLU下降差异0.2-0.5个百分点）和特定硬件支持声明（4090支持FP8），这些属于经验事实而非第一性原理可推导内容。虽然INT8与FP8的量化特性对比在逻辑上大致合理（FP8通常具有更好的动态范围和非对称支持），但具体数值差异和硬件支持情况缺乏来源支持，且4090是否原生支持FP8存在争议（通常认为4090主要支持INT8，FP8支持主要在Hopper架构如H100/H800上更完善）。 | 经验事实，逻辑自洽但缺来源支持；4090对FP8的支持存在不确定性，具体数值差异无法验证

## Search Query

INT8 vs FP8 quantization accuracy comparison MMLU Llama Qwen
