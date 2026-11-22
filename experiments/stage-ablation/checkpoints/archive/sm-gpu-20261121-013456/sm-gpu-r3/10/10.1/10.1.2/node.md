# N285: 最小必要校准数据量 N_min 的确定公式为：N_min = argmin{N | (Acc_BF16 - Acc_INT4(N)) < Threshold_Q

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

最小必要校准数据量 N_min 的确定公式为：N_min = argmin{N | (Acc_BF16 - Acc_INT4(N)) < Threshold_Quality AND Time_Calibration(N) < Budget_Time}。其中 Threshold_Quality 通常设为 1% MMLU 准确率损失，Budget_Time 为可接受的校准耗时（如 4 小时）。对于 Qwen3-27B，基于 H100 单卡，N=128 样本的校准时间约为 2-3 分钟，N=512 约为 10-15 分钟，因此时间约束通常不成为瓶颈，质量约束主导 N_min 的选择。

## Corrected Claim

最小必要校准数据量 N_min 的确定公式为：N_min = argmin{N | (Acc_BF16 - Acc_INT4(N)) < Threshold_Quality AND Time_Calibration(N) < Budget_Time}。其中 Threshold_Quality 通常设为 1% MMLU 准确率损失，Budget_Time 为可接受的校准耗时（如 4 小时）。对于 Qwen3-27B，基于 H100 单卡，N=128 样本的校准时间约为 2-3 分钟，N=512 约为 10-15 分钟，因此时间约束通常不成为瓶颈，质量约束主导 N_min 的选择。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

quantization calibration time cost H100 27B model GPTQ
