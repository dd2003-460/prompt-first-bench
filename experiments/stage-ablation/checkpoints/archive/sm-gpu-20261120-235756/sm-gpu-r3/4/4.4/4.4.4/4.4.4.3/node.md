# N268: 校准数据集大小对量化精度的边际收益曲线：从 128 样本增加到 512 样本，MMLU 准确率下降幅度的改善量（通常边际收益递减，512 样本相比 128 样本

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

校准数据集大小对量化精度的边际收益曲线：从 128 样本增加到 512 样本，MMLU 准确率下降幅度的改善量（通常边际收益递减，512 样本相比 128 样本仅额外改善 0.1-0.2% 准确率，但耗时增加 4 倍），据此确定最优校准样本数（通常 128-256 为性价比拐点）

## Corrected Claim

校准数据集大小对量化精度通常呈现边际收益递减规律，增加样本数带来的准确率提升有限，而计算耗时线性或超线性增加，因此存在性价比拐点（常见于 128-256 样本区间），但具体数值需视量化算法和数据分布而定。

## Evidence

[质询]具体数值（0.1-0.2% 改善、4 倍耗时）属于特定实验条件下的经验数据，缺乏通用性，且不同量化方法（如 GPTQ, AWQ, SmoothQuant）对校准集大小的敏感度差异巨大，直接断言固定数值范围存在以偏概全的风险。 | 经验事实，逻辑自洽（边际收益递减符合一般规律）但缺来源支持，且具体数值缺乏普适性证据。

## Search Query

LLM quantization calibration dataset size 128 vs 512 accuracy improvement diminishing returns
