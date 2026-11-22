# N78: RTX 4090 (Ada Lovelace) 硬件单元不支持原生 FP8 计算，执行 FP8 推理需通过软件层（如 vLLM 或 TensorRT）将 FP8

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12, N13, N14

## Claim

RTX 4090 (Ada Lovelace) 硬件单元不支持原生 FP8 计算，执行 FP8 推理需通过软件层（如 vLLM 或 TensorRT）将 FP8 数据 upcast 至 BF16/FP16 或在 CUDA 核中模拟，导致有效吞吐量约为原生 BF16 吞吐量的 85-90% [待核验：需引用具体框架在 4090 上的 FP8 vs BF16 基准测试日志]。

## Corrected Claim

RTX 4090 (Ada Lovelace) 硬件单元不支持原生 FP8 计算，执行 FP8 推理需通过软件层（如 vLLM 或 TensorRT）进行模拟或精度转换（如 upcast 至 BF16/FP16），导致有效吞吐量低于原生 BF16 吞吐量（具体损耗比例需依据特定框架和基准测试确定）。

## Evidence

[质询]该陈述包含具体的性能损耗数值（85-90%）和特定的软件行为描述（upcast至BF16/FP16），属于经验事实。虽然RTX 4090确实不支持原生FP8硬件加速（这是已知的硬件规格事实），但具体的吞吐量比例和软件实现细节（如是否一定upcast到BF16而非FP16，或是否有其他优化路径）缺乏来源支持，且不同框架（vLLM vs TensorRT）的实现差异可能导致数值波动，无法仅凭逻辑推导确定具体百分比。 | 经验事实，逻辑自洽但缺来源支持。RTX 4090不支持原生FP8是已知硬件限制，但具体性能损耗比例（85-90%）及软件层具体处理方式（upcast目标精度）属于需实测验证的经验数据，当前无可用来源佐证具体数值。

## Search Query

RTX 4090 FP8 inference performance penalty vs BF16 vLLM benchmark
