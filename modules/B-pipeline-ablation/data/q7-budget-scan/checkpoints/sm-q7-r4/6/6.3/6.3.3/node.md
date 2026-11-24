# N333: 年化成本的敏感性分析：C_idle_yearly 对 T_scan 和 Scan_Freq 的弹性系数 E = (∂C/∂X)*(X/C)；对 T_scan 弹

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

年化成本的敏感性分析：C_idle_yearly 对 T_scan 和 Scan_Freq 的弹性系数 E = (∂C/∂X)*(X/C)；对 T_scan 弹性为 1.0（线性），对 Scan_Freq 弹性为 1.0；若 T_scan 误差 ±10%，C_idle_yearly 波动 ±¥3.25M/年，需纳入风险评估 [knowledge]

## Corrected Claim

年化成本的敏感性分析：C_idle_yearly 对 T_scan 和 Scan_Freq 的弹性系数 E = (∂C/∂X)*(X/C)；对 T_scan 弹性为 1.0（线性），对 Scan_Freq 弹性为 1.0；若 T_scan 误差 ±10%，C_idle_yearly 波动 ±¥3.25M/年，需纳入风险评估 [knowledge]

## Evidence

先验知识/题面给定，逻辑校验通过：成本函数中若 C 与 X 呈线性关系，则弹性系数 E=1.0 符合数学定义；±10% 的输入误差导致 ±10% 的输出波动（即 ±¥3.25M 对应基准 ¥32.5M）在量级和逻辑上自洽。
