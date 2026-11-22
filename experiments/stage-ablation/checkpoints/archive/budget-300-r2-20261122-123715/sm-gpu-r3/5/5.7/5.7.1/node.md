# N340: AMD MI300X 的 TDP 并非固定 750W，而是随负载波动；在 LLM 推理（Decode 阶段）中，由于 HBM 访问密集但计算单元利用率低，实际功

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N103

## Claim

AMD MI300X 的 TDP 并非固定 750W，而是随负载波动；在 LLM 推理（Decode 阶段）中，由于 HBM 访问密集但计算单元利用率低，实际功耗通常低于峰值 TDP，平均功耗 P_avg_decode 需基于实测数据或负载模型估算，通常约为峰值的 60-80%。

## Corrected Claim

AMD MI300X 的 TDP 并非固定 750W，而是随负载波动；在 LLM 推理（Decode 阶段）中，由于 HBM 访问密集但计算单元利用率低，实际功耗通常低于峰值 TDP，具体平均功耗需基于实测数据估算，通常显著低于峰值（具体比例视负载模型而定）。

## Evidence

[质询]具体数值范围（60-80%）属于经验性工程数据，缺乏通用物理定律或第一性原理支持，且不同模型、序列长度及硬件批次下波动较大，该具体区间可能因特定测试条件而具有局限性。 | 逻辑自洽：LLM Decode阶段受限于内存带宽（Memory-bound），计算单元（FLOPS）利用率低，导致功耗低于计算密集型负载（如Prefill或训练）的峰值TDP，符合硬件功耗与负载类型的物理直觉。但source为search且无可用来源，具体百分比数值属于经验事实，无法通过第一性原理严格推导，故降级。

## Search Query

AMD MI300X power consumption LLM inference decode phase average watts
