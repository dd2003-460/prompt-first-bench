# N97: INT8 量化中激活值分布偏差的具体表现：ReLU/GELU 激活值的直方图峰值偏移导致量化步长不均匀，使得低概率 token 的概率被高估 5-10%，影响采

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

INT8 量化中激活值分布偏差的具体表现：ReLU/GELU 激活值的直方图峰值偏移导致量化步长不均匀，使得低概率 token 的概率被高估 5-10%，影响采样多样性（Perplexity 上升 2-4%）[待核验]

## Corrected Claim

INT8 量化中激活值分布偏差可能导致量化误差，进而影响采样多样性并引起 Perplexity 轻微上升，但具体幅度（如概率高估 5-10% 或 PPL 上升 2-4%）需视具体模型与场景而定。

## Evidence

[质询]具体数值（5-10%概率高估，2-4% PPL上升）缺乏通用性，高度依赖模型架构、数据集及量化实现细节，作为普遍事实陈述过于绝对且易受特定实验条件影响。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

INT8 activation distribution bias perplexity increase low probability token overestimation
