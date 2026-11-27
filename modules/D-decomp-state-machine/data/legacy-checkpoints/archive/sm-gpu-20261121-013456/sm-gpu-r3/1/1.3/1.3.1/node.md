# N53: INT4/W4 精度下的 Group Quantization (如 GPTQ 或 AWQ) 通常以 Group Size=128 为单位存储 Scale 和 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

INT4/W4 精度下的 Group Quantization (如 GPTQ 或 AWQ) 通常以 Group Size=128 为单位存储 Scale 和 Zero Point (各 1 个 FP16 或 FP32 值)，额外显存开销计算公式为：Overhead_GB = (27B / 128) * (2 * 2 bytes) / 1e9 ≈ 0.84 GB (若使用 FP16 Scale/Zero)，总权重显存约为 13.5 + 0.84 = 14.34 GB。

## Corrected Claim

INT4/W4 精度下的 Group Quantization (如 GPTQ 或 AWQ) 通常以 Group Size=128 为单位存储 Scale 和 Zero Point (各 1 个 FP16 或 FP32 值)，额外显存开销计算公式为：Overhead_GB = (27B / 128) * (2 * 2 bytes) / 1e9 ≈ 0.84 GB (若使用 FP16 Scale/Zero)，总权重显存约为 13.5 + 0.84 = 14.34 GB。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了参数量定义、量化开销公式推导、基础显存计算以及不同精度（FP32）下的对比分析，逻辑层层递进且无重复，完整覆盖了父节点中关于显存计算的所有关键要素。）
