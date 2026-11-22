# N215: LFU 在动态更新场景下的有效命中率 H_LFU_dynamic = H_LFU_static * e^(-r_update * T_window) * (1 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N78

## Claim

LFU 在动态更新场景下的有效命中率 H_LFU_dynamic = H_LFU_static * e^(-r_update * T_window) * (1 - P_stale)，其中 r_update=0.01/天，T_window 为统计窗口，P_stale 为缓存对象在窗口内被更新的概率，需根据对象更新分布独立计算。

## Corrected Claim

在特定动态更新场景下，LFU 的有效命中率可近似建模为 H_LFU_dynamic ≈ H_LFU_static * e^(-r_update * T_window) * (1 - P_stale)，其中参数需根据具体对象更新分布校准。

## Evidence

[质询]该公式为经验性启发式模型，缺乏严格的理论推导或通用标准支持，具体参数（如指数衰减形式）可能因场景而异，属于特定上下文下的假设而非普适事实。 | 先验知识/题面给定，逻辑校验通过（量纲一致，衰减因子合理），但作为经验公式缺乏通用来源直接支持，故降级。
