# N52: INT4 (AWQ/GPTQ) 量化下的额外开销：Zero-point 和 Scale 通常以 FP16 存储，每 128 个元素一组，开销约为 (27 * 1

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

INT4 (AWQ/GPTQ) 量化下的额外开销：Zero-point 和 Scale 通常以 FP16 存储，每 128 个元素一组，开销约为 (27 * 10^9 / 128) * 4 bytes ≈ 850 MB；加上 Group Norm 等元数据，总占用约为 14.5-15.0 GB，而非简单的 13.5 GB

## Corrected Claim

INT4 (AWQ/GPTQ) 量化下的额外开销：Zero-point 和 Scale 通常以 FP16 存储，每 128 个元素一组，开销约为 (27 * 10^9 / 128) * 4 bytes ≈ 850 MB；加上 Group Norm 等元数据，总占用约为 14.5-15.0 GB，而非简单的 13.5 GB

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点2存在显著重叠和逻辑依赖：子节点2直接引用并复述了子节点1的计算结果（Scale/Zero-point开销），导致信息冗余。此外，子节点3关于KV Cache的内容与父节点标题“INT4量化下的额外开销”主题偏离，父节点主要讨论权重存储开销，而KV Cache通常独立于权重量化（除非特定场景），且子节点3并未体现为“额外开销”的一部分，而是澄清了非影响项，导致正交性受损（子节点3与1/2的主题维度不同，但子节点1和2内部高度耦合）。）

## Search Query

AWQ GPTQ INT4 quantization zero-point scale overhead memory usage 27B
