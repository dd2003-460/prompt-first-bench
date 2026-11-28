# N252: GSM8K-CoT 长文变体的构造方法：将原始问题嵌入到 64k/128k/262k 长度的无关数学推导噪声文本中，保持关键实体不变；测量指标为 Exact M

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

GSM8K-CoT 长文变体的构造方法：将原始问题嵌入到 64k/128k/262k 长度的无关数学推导噪声文本中，保持关键实体不变；测量指标为 Exact Match (EM) 准确率；对照组为无噪声原始 GSM8K，ΔAcc 定义为 (Acc_noisy - Acc_clean) / Acc_clean，预期随长度增加 EM 下降 5%-15%

## Corrected Claim

GSM8K-CoT 长文变体的构造方法：将原始问题嵌入到 64k/128k/262k 长度的无关数学推导噪声文本中，保持关键实体不变；测量指标为 Exact Match (EM) 准确率；对照组为无噪声原始 GSM8K，ΔAcc 定义为 (Acc_noisy - Acc_clean) / Acc_clean，预期随长度增加 EM 下降 5%-15%

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GSM8K long context noise injection evaluation protocol exact match accuracy drop benchmark
