# N213: 稀缺性阈值 N_thresh 的品类依赖性：N_thresh 并非固定为 5，而是随品类标准化程度 S_std 变化，公式为 N_thresh = 10 / S

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N68

## Claim

稀缺性阈值 N_thresh 的品类依赖性：N_thresh 并非固定为 5，而是随品类标准化程度 S_std 变化，公式为 N_thresh = 10 / S_std^0.5，对于非标品（S_std ≈ 0.2），N_thresh ≈ 22；对于标品（S_std ≈ 1.0），N_thresh ≈ 10，这意味着非标品的稀缺性感知阈值更高。

## Corrected Claim

N_thresh 随品类标准化程度 S_std 变化，通常非标品的稀缺性感知阈值高于标品。若采用模型 N_thresh = 10 / S_std^0.5，则非标品（S_std ≈ 0.2）阈值约为 22，标品（S_std ≈ 1.0）阈值约为 10。

## Evidence

[质询]该公式 N_thresh = 10 / S_std^0.5 及其具体参数（如 S_std 取值 0.2 和 1.0）属于特定的经验模型或假设，并非通用的第一性原理或数学公理。在缺乏具体文献或题面定义支持的情况下，无法确认该特定函数形式及系数 10 的准确性，存在口径混淆或来源不可靠的风险。 | 经验事实，逻辑自洽但缺来源支持。数学计算正确（10/sqrt(0.2)≈22.36, 10/sqrt(1.0)=10），且符合非标品需更多样本才能感知稀缺性的直觉，但具体公式形式无外部证据支持。

## Search Query

scarcity threshold standardization level click through rate second hand goods
