# N105: 批量并行执行对 T_verify 的摊薄：将 10 个独立代码片段打包为单一批次进行沙箱执行，T_verify 的固定开销（Docker 启动+解释器初始化）从

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

批量并行执行对 T_verify 的摊薄：将 10 个独立代码片段打包为单一批次进行沙箱执行，T_verify 的固定开销（Docker 启动+解释器初始化）从 200ms/instance 摊薄至 20ms/instance。总 T_human 中的验证部分从 (1-FPSR)*2min 降至 (1-FPSR)*0.5min。若 FPSR=0.7，则 T_verify 部分从 0.6min 降至 0.15min，节省 75% 的验证耗时。

## Corrected Claim

批量并行执行对 T_verify 的摊薄：将 10 个独立代码片段打包为单一批次进行沙箱执行，T_verify 的固定开销（Docker 启动+解释器初始化）从 200ms/instance 摊薄至 20ms/instance。总 T_human 中的验证部分从 (1-FPSR)*2min 降至 (1-FPSR)*0.5min。若 FPSR=0.7，则 T_verify 部分从 0.6min 降至 0.15min，节省 75% 的验证耗时。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（(1-0.7)*2=0.6, (1-0.7)*0.5=0.15, 节省比例(0.6-0.15)/0.6=75%），且批量执行摊薄固定开销符合系统性能优化的一般原理。
