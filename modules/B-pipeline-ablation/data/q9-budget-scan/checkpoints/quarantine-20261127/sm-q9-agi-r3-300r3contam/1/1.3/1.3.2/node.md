# N37: 代码执行环节的总人工介入时间 T_human = (1-FPSR) * T_debug_avg + (1-FPSR_2nd) * T_verify，其中T_de

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

代码执行环节的总人工介入时间 T_human = (1-FPSR) * T_debug_avg + (1-FPSR_2nd) * T_verify，其中T_debug_avg平均为5分钟/次，T_verify为2分钟/次，用于计算沙箱可靠性对整体科研循环耗时的贡献。

## Corrected Claim

代码执行环节的总人工介入时间 T_human = (1-FPSR) * T_debug_avg + (1-FPSR_2nd) * T_verify，其中T_debug_avg平均为5分钟/次，T_verify为2分钟/次，用于计算沙箱可靠性对整体科研循环耗时的贡献。

## Evidence

先验知识/题面给定，逻辑校验通过
