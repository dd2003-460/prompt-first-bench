# N155: AMD Instinct MI300X 在 ROCm 栈下对 Qwen3-27B 的兼容性风险：ROCm 对混合注意力架构（Gated DeltaNet）的支持

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

AMD Instinct MI300X 在 ROCm 栈下对 Qwen3-27B 的兼容性风险：ROCm 对混合注意力架构（Gated DeltaNet）的支持程度未知，需确认 vLLM 或 TensorRT-LLM 的 AMD 分支是否已适配该模型结构；若需手动适配，开发成本（人时）需计入 TCO，估算为 20-40 小时 * $100/h = $2,000-$4,000 [待核验]。

## Corrected Claim

AMD Instinct MI300X 在 ROCm 栈下对 Qwen3-27B 的兼容性风险：ROCm 对混合注意力架构（Gated DeltaNet）的支持程度未知，需确认 vLLM 或 TensorRT-LLM 的 AMD 分支是否已适配该模型结构；若需手动适配，开发成本需计入 TCO，具体人时与费用需根据实际适配工作量评估（原估算 20-40 小时 * $100/h = $2,000-$4,000 仅供参考，未经来源验证）。

## Evidence

[质询]该陈述包含具体的工程估算数值（20-40小时）和成本（$2,000-$4,000），属于经验事实。由于缺乏任何外部来源支持，且“Gated DeltaNet”在Qwen3-27B中的具体实现细节及ROCm适配难度属于高度依赖具体版本和实现的工程经验，无法从第一性原理推导，存在数值量级和前提假设（如是否真的需要手动适配）的不确定性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

ROCm vLLM Qwen3-27B support OR Gated DeltaNet AMD compatibility
