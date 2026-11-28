# N62: 基准测试数据集的选择偏差控制：使用 ShareGPT 或 MT-Bench 等通用对话数据集测得的 tok/s 不能直接外推到科研长文本任务；需构建包含 32k

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

基准测试数据集的选择偏差控制：使用 ShareGPT 或 MT-Bench 等通用对话数据集测得的 tok/s 不能直接外推到科研长文本任务；需构建包含 32k-128k context 长度的合成科研数据集 (如 ArXiv 摘要拼接) 进行专项压测，以捕获长上下文下的 KV Cache 访问延迟。

## Corrected Claim

基准测试数据集的选择偏差控制：使用 ShareGPT 或 MT-Bench 等通用对话数据集测得的 tok/s 不能直接外推到科研长文本任务；需构建包含 32k-128k context 长度的合成科研数据集 (如 ArXiv 摘要拼接) 进行专项压测，以捕获长上下文下的 KV Cache 访问延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：通用短对话数据集无法反映长上下文KV Cache的内存带宽瓶颈，构建长文本专项数据集符合LLM推理性能测试的工程最佳实践。
