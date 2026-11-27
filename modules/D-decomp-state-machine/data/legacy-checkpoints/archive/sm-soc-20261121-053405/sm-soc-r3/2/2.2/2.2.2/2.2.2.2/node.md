# N120: 下游投影1：最小样本量 $N_{sample}$ 的精确计算：要求 $H_{null} = 1/\sqrt{N_{sample}} < 0.1$，解得 $N_{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N39

## Claim

下游投影1：最小样本量 $N_{sample}$ 的精确计算：要求 $H_{null} = 1/\sqrt{N_{sample}} < 0.1$，解得 $N_{sample} > 100$。但需考虑统计功效：在 $\alpha=0.05$ 且效应量 $d = (H_{obs} - H_{null})/\sigma_{H}$ 下，若 $H_{obs}=0.15, H_{null}=0.1$，且 $\sigma_{H} \approx H_{null}/\sqrt{N_{sample}}$（近似），则 $d \approx 0.05/0.01 = 5$，功效接近 1.0。因此 $N_{sample} = 100$ 是理论下限，实际建议 $N_{sample} \geq 150$ 以应对数据缺失和异常值剔除。

## Corrected Claim

下游投影1：最小样本量 $N_{sample}$ 的精确计算：要求 $H_{null} = 1/\sqrt{N_{sample}} < 0.1$，解得 $N_{sample} > 100$。但需考虑统计功效：在 $\alpha=0.05$ 且效应量 $d = (H_{obs} - H_{null})/\sigma_{H}$ 下，若 $H_{obs}=0.15, H_{null}=0.1$，且 $\sigma_{H} \approx H_{null}/\sqrt{N_{sample}}$（近似），则 $d \approx 0.05/0.01 = 5$，功效接近 1.0。因此 $N_{sample} = 100$ 是理论下限，实际建议 $N_{sample} \geq 150$ 以应对数据缺失和异常值剔除。

## Evidence

先验知识/题面给定，逻辑校验通过：不等式求解正确，效应量计算符合统计学定义，建议值合理。

## Search Query

minimum sample size homogeneity index threshold 0.1 statistical power calculation
