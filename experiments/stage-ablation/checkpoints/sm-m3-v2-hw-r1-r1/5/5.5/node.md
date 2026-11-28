# N35: 置信度校准方法：使用温度缩放（Temperature Scaling）调整模型输出概率，最小化 ECE (Expected Calibration Error)

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

置信度校准方法：使用温度缩放（Temperature Scaling）调整模型输出概率，最小化 ECE (Expected Calibration Error)，ECE = (1/N) Σ |Confidence - Accuracy|；训练集大小 N_calib ≥ 1000 样本，目标 ECE ≤ 0.05；校准后置信度区间 [p_low, p_high] 覆盖真实概率的频率 ≥ 95%

## Corrected Claim

置信度校准方法：使用温度缩放（Temperature Scaling）调整模型输出概率，最小化 ECE (Expected Calibration Error)，ECE = (1/N) Σ |Confidence - Accuracy|；训练集大小 N_calib ≥ 1000 样本，目标 ECE ≤ 0.05；校准后置信度区间 [p_low, p_high] 覆盖真实概率的频率 ≥ 95%

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

confidence calibration temperature scaling ECE expected calibration error LLM
