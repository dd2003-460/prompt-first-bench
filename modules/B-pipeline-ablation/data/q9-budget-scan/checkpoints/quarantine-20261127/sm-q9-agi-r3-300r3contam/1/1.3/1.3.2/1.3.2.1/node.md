# N104: 自动调试代理（Auto-Debugger）对 T_human 的替代效应：部署基于 LLM 的自动调试代理后，人工介入率从 (1-FPSR)=35% 降至 10

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N37

## Claim

自动调试代理（Auto-Debugger）对 T_human 的替代效应：部署基于 LLM 的自动调试代理后，人工介入率从 (1-FPSR)=35% 降至 10%。剩余 10% 为复杂逻辑错误，平均 T_debug_avg 从 5 分钟降至 15 分钟（因需更深层审查）。新 T_human = 0.10 * 15min + 0.05 * 2min = 1.6 min/instance，相比原 2.0 min 仅降低 20%，但释放了 75% 的人力带宽用于高价值审核。

## Corrected Claim

部署自动调试代理后，人工介入率从35%降至10%。假设原平均调试时间为5分钟，原T_human约为1.75 min/instance；新场景下若10%介入中50%为复杂错误（15min）其余为简单错误（2min），新T_human为1.6 min/instance，降幅约8.6%。人力带宽释放比例需基于总工作量重新评估，不能直接由耗时降幅推导。

## Evidence

[质询]数值计算存在内部矛盾：若人工介入率从35%降至10%，且剩余10%中复杂错误占比隐含为50%（0.05/0.10），则原T_human应为0.35*5=1.75min，而非陈述中的2.0min；此外，'释放75%人力带宽'与'耗时仅降低20%'在逻辑上缺乏直接推导关系，属于主观推断。 | 先验知识/题面给定，但逻辑校验发现数值不自洽（原T_human计算不符）及因果推断跳跃，故降级。
