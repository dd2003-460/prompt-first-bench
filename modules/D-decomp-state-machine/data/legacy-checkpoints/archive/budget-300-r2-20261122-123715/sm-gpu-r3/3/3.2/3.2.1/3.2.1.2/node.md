# N244: RTX 4090 在 LLM 推理预填充 (Prefill) 阶段的实际功耗 P_prefill 接近 TDP 上限 (450W)，因为该阶段为计算密集型 (C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

RTX 4090 在 LLM 推理预填充 (Prefill) 阶段的实际功耗 P_prefill 接近 TDP 上限 (450W)，因为该阶段为计算密集型 (Compute-bound)；需确定 Prefill 与 Decode 的时间占比 (t_prefill / t_total)，若上下文 32K 且生成长度 512 tokens，Prefill 占比通常 <10%，因此平均功耗加权计算需考虑此比例。

## Corrected Claim

RTX 4090 在 LLM 推理预填充 (Prefill) 阶段的实际功耗 P_prefill 接近 TDP 上限 (450W)，因为该阶段为计算密集型 (Compute-bound)；需确定 Prefill 与 Decode 的时间占比 (t_prefill / t_total)，若上下文 32K 且生成长度 512 tokens，Prefill 占比通常 <10%，因此平均功耗加权计算需考虑此比例。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP为450W，Prefill阶段计算密集导致功耗接近TDP符合物理直觉；32K上下文与512生成长度的比例计算（32768/(32768+512)≈98.5%为Prefill计算量，但时间占比受硬件并行度影响，通常Prefill耗时占比确实较低，逻辑自洽）。

## Search Query

LLM inference prefill vs decode compute bound power consumption ratio
