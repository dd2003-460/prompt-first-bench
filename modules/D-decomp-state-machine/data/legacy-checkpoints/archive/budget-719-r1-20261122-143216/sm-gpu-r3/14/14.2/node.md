# N426: RTX 5090 (210 TFLOPS FP16) 与 A100 (312 TFLOPS FP16) 在 Prefill 阶段的理论速度比值为 210/312

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N153

## Claim

RTX 5090 (210 TFLOPS FP16) 与 A100 (312 TFLOPS FP16) 在 Prefill 阶段的理论速度比值为 210/312 ≈ 1:1.49，考虑到 MFU 差异 (RTX 5090 ~50%, A100 ~60%)，实际速度比值约为 1:1.8，表明在长 Prompt 场景下，算力差异比带宽差异更显著。

## Corrected Claim

RTX 5090 (210 TFLOPS FP16) 与 A100 (312 TFLOPS FP16) 在 Prefill 阶段的理论速度比值为 210/312 ≈ 1:1.49。若假设 MFU 差异 (RTX 5090 ~50%, A100 ~60%)，实际速度比值约为 1:1.8，表明在长 Prompt 场景下，算力差异比带宽差异更显著。

## Evidence

[质询]MFU（模型浮点利用率）的具体数值（RTX 5090 ~50%, A100 ~60%）属于高度依赖具体模型架构、序列长度及软件栈优化的经验参数，并非固定物理常数。不同场景下MFU波动极大，直接引用特定百分比作为通用事实缺乏严谨性，且RTX 5090作为消费级显卡，其FP16算力规格（210 TFLOPS）在不同来源中可能存在差异（如是否包含稀疏加速或特定精度模式），需核实具体口径。 | source=knowledge，逻辑推导自洽（210/312≈0.67，即1:1.49；考虑MFU后比值扩大符合逻辑），但MFU具体数值为经验事实，缺乏外部来源直接支持，依据经验事实排除条款降级。
