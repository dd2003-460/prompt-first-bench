# N267: AWQ 量化 Qwen3-27B 在 RTX 4090 (24GB) 上的具体耗时：基于校准集大小 128 样本，实测耗时约 1.5-2.5 小时（AWQ 算法

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

AWQ 量化 Qwen3-27B 在 RTX 4090 (24GB) 上的具体耗时：基于校准集大小 128 样本，实测耗时约 1.5-2.5 小时（AWQ 算法复杂度低于 GPTQ，通常快 30-50%，需引用 AWQ 官方 GitHub 性能测试数据）

## Corrected Claim

AWQ 量化 Qwen3-27B 在 RTX 4090 (24GB) 上的耗时取决于校准集大小与实现细节，通常比 GPTQ 更快，但具体数值需实测确认。

## Evidence

[质询]具体耗时数值（1.5-2.5小时）及加速比例（30-50%）属于高度依赖硬件环境、软件版本及校准集具体内容的经验事实，且缺乏来源支持，无法通过第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

AWQ quantization time RTX 4090 Qwen3-27B calibration duration
