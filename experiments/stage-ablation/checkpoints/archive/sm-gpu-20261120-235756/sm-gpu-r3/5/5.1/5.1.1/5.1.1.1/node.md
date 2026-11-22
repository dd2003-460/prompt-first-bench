# N278: vLLM v0.6.x 对 Qwen3 架构的支持状态判定：检查 v0.6.0-v0.6.9 的 release notes 及代码库中 `qwen3` 模型注

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99, N100, N101

## Claim

vLLM v0.6.x 对 Qwen3 架构的支持状态判定：检查 v0.6.0-v0.6.9 的 release notes 及代码库中 `qwen3` 模型注册项；若仅支持 Qwen2 (Dense/部分MoE)，需评估 Qwen3 特有的 MoE 路由逻辑（如 Top-K 选择算法差异）导致的代码兼容性补丁复杂度，量化为预计需修改的文件数及核心逻辑行数。

## Corrected Claim

需评估 vLLM 当前版本对 Qwen3 架构的支持状态；若仅支持 Qwen2，需评估 Qwen3 特有的 MoE 路由逻辑导致的代码兼容性补丁复杂度，但具体修改文件数及核心逻辑行数需基于实际代码库分析确定，而非预设量化。

## Evidence

[质询]该陈述包含具体的版本范围（v0.6.0-v0.6.9）和特定的架构支持状态（Qwen3 vs Qwen2），属于经验事实。由于检索失败，无法验证 vLLM v0.6.x 是否真的不支持 Qwen3 或具体的兼容性补丁复杂度量化数据，存在版本信息过时或具体数值估算缺乏依据的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体版本支持状态及补丁复杂度量化数据）

## Search Query

vLLM v0.6 release notes Qwen3 MoE support github issues
