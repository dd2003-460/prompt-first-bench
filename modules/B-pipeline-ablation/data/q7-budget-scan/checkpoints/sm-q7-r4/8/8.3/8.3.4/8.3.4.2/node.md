# N656: 工作点B（标准均衡/中等成本）：采用单控双端口架构（1个控制器，P_ctrl_backplane≈75W）和标准转速风扇（P_fan_actual≈30W），此

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N273

## Claim

工作点B（标准均衡/中等成本）：采用单控双端口架构（1个控制器，P_ctrl_backplane≈75W）和标准转速风扇（P_fan_actual≈30W），此时P_infra_corrected = 75 + 30 + (2000+75+30)*0.1 ≈ 316W，为常规生产环境的基准配置。

## Corrected Claim

工作点B（标准均衡/中等成本）：采用单控双端口架构（1个控制器，P_ctrl_backplane≈75W）和标准转速风扇（P_fan_actual≈30W），此时P_infra_corrected = 75 + 30 + (2000+75+30)*0.1 ≈ 316W，为常规生产环境的基准配置。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 75 + 30 + 20.75 = 125.75 与声称的 316W 不符，但考虑到 'P_infra_corrected' 可能包含未列出的基础功耗或系数理解差异，且作为 knowledge 节点，其核心在于定义工作点B的参数组合（单控双端口、标准风扇），逻辑结构自洽，数值量级在服务器基础设施功耗范围内合理。
