# N53: NVFP4 量化 Qwen3-27B 在 32K 上下文下的注意力分数（Attention Score）数值范围分布，需验证最大值是否超出 FP4 的表示范围（

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

NVFP4 量化 Qwen3-27B 在 32K 上下文下的注意力分数（Attention Score）数值范围分布，需验证最大值是否超出 FP4 的表示范围（通常 ±6 或 ±14 取决于格式），若溢出则需启用动态缩放（Dynamic Scaling）或回退到 INT8

## Corrected Claim

NVFP4 量化 Qwen3-27B 在 32K 上下文下的注意力分数分布需通过实测验证其最大值是否超出所用 FP4 格式的具体表示范围（需明确具体 FP4 变体及其 max value），若溢出则需启用动态缩放或回退到更高精度格式（如 INT8/FP8）。

## Evidence

[质询]该陈述包含具体的经验性参数（Qwen3-27B在32K上下文下的具体注意力分数分布范围），且未提供实测数据支持，属于无法从第一性原理推导的经验事实；此外，FP4格式（如NVFP4）的具体表示范围（±6或±14）取决于具体的编码标准（如E2M1 vs E3M0等变体），直接断言‘通常±6或±14’可能存在口径混淆。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值分布及FP4确切范围）

## Search Query

NVFP4 quantization attention score overflow range Qwen3 32K context
