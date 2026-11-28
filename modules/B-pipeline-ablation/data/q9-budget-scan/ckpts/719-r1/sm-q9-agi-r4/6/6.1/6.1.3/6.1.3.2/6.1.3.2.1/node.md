# N696: 注意力分数 KL 散度 ΔKL_Attention 的一阶泰勒近似公式：ΔKL ≈ 0.5 * ||σ(q_fp16 * k_fp16) - σ(q_nvfp4

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N254

## Claim

注意力分数 KL 散度 ΔKL_Attention 的一阶泰勒近似公式：ΔKL ≈ 0.5 * ||σ(q_fp16 * k_fp16) - σ(q_nvfp4 * k_nvfp4)||^2 / T^2，其中 T 为 softmax 温度（通常为 1/sqrt(d_head)），需计算 Qwen3.8-27B 的 d_head 以确定温度系数。

## Corrected Claim

注意力分数 KL 散度的一阶泰勒近似通常基于 Logit 空间的差异计算，而非直接对概率分布向量使用简单的欧氏距离除以 T^2；具体系数需根据 Softmax 函数的导数严格推导。此外，需确认 'Qwen3.8-27B' 是否为真实存在的模型版本。

## Evidence

[质询]公式中分母 T^2 的量纲和系数推导存疑：标准 Softmax 的 KL 散度一阶近似通常涉及 logit 差值的平方和除以 T^2，但此处分子是概率向量（经过 sigmoid/softmax 后）的欧氏距离平方，其量纲与 logit 空间不同，直接套用 0.5/T^2 系数缺乏严格的数学推导支持，且 'Qwen3.8-27B' 这一具体型号名称可能存在虚构或混淆（常见为 Qwen2.5 或 Qwen3 系列，具体版本需核实）。 | 先验知识/题面给定，逻辑校验发现公式推导存在量纲/系数疑点，且具体模型版本号存疑，故降级。

## Search Query

kl divergence approximation softmax quantization error first order taylor
