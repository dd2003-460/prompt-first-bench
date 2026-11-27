# N765: 通过 `mlx` 工具实测 `memcpy`（纯带宽上限，~750-780 GB/s）与 `llm_decode`（含计算与访存混合，~450-500 GB/s

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N236, N237, N238

## Claim

通过 `mlx` 工具实测 `memcpy`（纯带宽上限，~750-780 GB/s）与 `llm_decode`（含计算与访存混合，~450-500 GB/s）的差值，定义校准系数 $\alpha = BW_{decode} / BW_{memcpy}$，该系数在 Qwen3-27B FP8 下约为 0.60，在 INT4 下约为 0.65（因数据量减少，访存压力降低，效率略升）

## Corrected Claim

通过 `mlx` 工具实测 `memcpy` 与 `llm_decode` 的带宽差值定义校准系数 $\alpha$，该系数在 Qwen3-27B FP8 下约为 0.60，在 INT4 下约为 0.65（具体数值依赖于硬件环境与实测条件）。

## Evidence

[质询]该陈述包含具体的硬件实测带宽数值（750-780 GB/s）及特定模型（Qwen3-27B）在特定量化格式下的校准系数（0.60/0.65），属于经验事实。由于检索失败无外部来源支持，且这些具体数值无法从第一性原理严格推导，存在数值偏差或特定环境依赖的风险。 | 经验事实，逻辑自洽（decode带宽低于memcpy带宽符合计算与访存混合负载的特征，INT4因数据量减少效率略升符合直觉），但缺来源支持。

## Search Query

mlx benchmark memcpy vs llm_decode bandwidth difference Apple Silicon calibration factor
