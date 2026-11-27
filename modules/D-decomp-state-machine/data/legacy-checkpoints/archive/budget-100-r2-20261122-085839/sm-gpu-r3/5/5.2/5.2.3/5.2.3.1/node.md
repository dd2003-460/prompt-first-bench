# N248: Intel Gaudi 3 (BHS) 当前对 Qwen3 架构（特别是 GQA 和 RoPE 算子）的 PyTorch 支持状态：截至 2024 Q4，Gau

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

Intel Gaudi 3 (BHS) 当前对 Qwen3 架构（特别是 GQA 和 RoPE 算子）的 PyTorch 支持状态：截至 2024 Q4，Gaudi 3 官方支持列表未包含 Qwen3，需通过 ONNX 导出或手动实现算子，预计适配工时为 15-30 人天，且缺乏社区优化 kernel。

## Corrected Claim

Intel Gaudi 3 (BHS) 对 Qwen3 架构（特别是 GQA 和 RoPE 算子）的 PyTorch 原生支持可能不完整，通常需通过 ONNX 导出或手动实现算子进行适配，具体适配工时需根据实际工程情况评估，且社区优化 kernel 可能缺乏。

## Evidence

[质询]该陈述包含具体的经验性参数（如'15-30人天'的适配工时）和特定时间点（2024 Q4）的状态断言，属于经验事实而非第一性原理可推导内容。由于缺乏外部来源支持，无法验证具体工时估算的准确性及当时官方支持列表的确切状态，存在将推测性估算当作既定事实的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体工时及2024 Q4时的确切支持状态）

## Search Query

Intel Gaudi 3 Qwen3 support PyTorch kernel status 2024
