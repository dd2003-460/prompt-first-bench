# N240: NVFP4 (4-bit) 量化在 27B 规模模型上的 Perplexity 增加量 ΔPPL 实测值，需引用 Qwen 官方报告或社区评测

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

NVFP4 (4-bit) 量化在 27B 规模模型上的 Perplexity 增加量 ΔPPL 实测值，需引用 Qwen 官方报告或社区评测

## Corrected Claim

NVFP4 (4-bit) 量化在 27B 规模模型上会导致 Perplexity 增加，具体 ΔPPL 数值需参考 Qwen 官方报告或特定社区评测基准（如 WikiText-103）的实测数据。

## Evidence

[质询]该陈述要求引用具体的实测数值（ΔPPL），属于经验事实。由于检索失败，无法验证具体数值是否准确，且不同评测基准（如WikiText vs C4）会导致数值差异，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法提供直接证据或独立多源验证）

## Search Query

Qwen3-27B NVFP4 4-bit perplexity increase benchmark
