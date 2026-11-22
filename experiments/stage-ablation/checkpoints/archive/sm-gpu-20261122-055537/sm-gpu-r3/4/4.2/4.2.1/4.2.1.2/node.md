# N221: RTX 4090 在推理负载下的实际功耗波动范围：在 Decode 阶段（带宽受限，计算单元空闲）功耗降至 300-350W，在 Prefill 阶段（计算受限

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

RTX 4090 在推理负载下的实际功耗波动范围：在 Decode 阶段（带宽受限，计算单元空闲）功耗降至 300-350W，在 Prefill 阶段（计算受限）功耗升至 450W，因此 24/7 运行的平均功耗 P_avg 约为 380-420W，而非峰值 550W，这会导致年度电力成本估算需乘以负载因子 0.7-0.8。

## Corrected Claim

RTX 4090 在推理负载下的实际功耗随阶段波动：Decode 阶段（带宽受限）功耗通常低于 Prefill 阶段（计算受限），平均功耗显著低于峰值 TDP（450W），导致年度电力成本估算需应用负载因子（通常小于1，具体数值依工作负载而定）。

## Evidence

[质询]具体数值（300-350W, 450W, 380-420W）缺乏统一基准，不同模型规模、序列长度及驱动版本下功耗波动极大，且RTX 4090 TDP为450W，Prefill阶段达到450W意味着持续满载，而Decode阶段300-350W也偏高（通常纯带宽受限且计算空闲时功耗可能更低，取决于具体实现和内存访问模式），这些精确区间属于经验事实，无法从第一性原理推导，且无来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 inference power consumption decode vs prefill phase
