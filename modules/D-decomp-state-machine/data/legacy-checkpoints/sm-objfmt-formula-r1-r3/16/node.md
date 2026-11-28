# N123: 性价比综合评估模型定义：Cost-Effectiveness Score (CES) = (Inference_Throughput_TokensPerSec 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比综合评估模型定义：Cost-Effectiveness Score (CES) = (Inference_Throughput_TokensPerSec / Total_Cost_Per_Month) * Quality_Factor。其中 Total_Cost_Per_Month 包含硬件折旧（按3年直线折旧）、电力成本（Power_Watts * Hours * Electricity_Rate）、维护成本（固定月费）。Quality_Factor 定义为量化模型在 MMLU/GSM8K 上的相对得分（BF16 为 1.0，FP8 约为 0.98，INT8 约为 0.97，INT4 约为 0.90）。

## Corrected Claim

性价比综合评估模型定义：Cost-Effectiveness Score (CES) = (Inference_Throughput_TokensPerSec / Total_Cost_Per_Month) * Quality_Factor。其中 Total_Cost_Per_Month 包含硬件折旧（按3年直线折旧）、电力成本（Power_Watts * Hours * Electricity_Rate）、维护成本（固定月费）。Quality_Factor 定义为量化模型在 MMLU/GSM8K 上的相对得分（BF16 为 1.0，FP8 约为 0.98，INT8 约为 0.97，INT4 约为 0.90）。

## Evidence

检索失败: no sources from any channel (all 5 failed)
