# N107: P99超标赔付量化：C_penalty = N_affected_users * P_compensation * T_outage，其中N_affected_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

P99超标赔付量化：C_penalty = N_affected_users * P_compensation * T_outage，其中N_affected_users为受影响用户数（按故障POP覆盖比例估算），P_compensation=¥1-5/用户/次（行业典型赔付标准），T_outage=MTTR/60小时，单次故障赔付¥5k-50k

## Corrected Claim

P99超标赔付量化模型：C_penalty = N_affected_users * P_compensation * T_outage，其中N_affected_users为受影响用户数，P_compensation为单用户单次赔付标准（需根据具体SLA协议确定），T_outage为故障持续时间（小时）。

## Evidence

[质询]该陈述包含具体的行业经验参数（如赔付标准¥1-5/用户/次、单次故障赔付范围¥5k-50k），这些属于经验事实而非第一性原理可推导内容，且参考来源仅涉及P99统计定义，完全未覆盖赔付量化逻辑，缺乏外部证据支持。 | 逻辑自洽（公式量纲正确，数值量级在合理范围内），但参考来源[1][2]仅解释P99统计概念，与赔付量化无关，属于经验事实且缺来源支持。

## Search Query

CDN SLA compensation per user per incident China 2024 2025

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1907850060240257948&rut=f8568459f53c969be6c08e9ce6f128269cd34bc1378fc3538a037e0cd1594e62', 'type': 'ddg', 'title': '运维必懂：监控指标中的 P90、P95、P99，到底是个啥？'}
- {'url': 'https://zhuanlan.zhihu.com/p/2090470641262770092&rut=83ea332e6b1a4987e790ff625ef4e44a48269e51effd7e1b8ec080686b090be2', 'type': 'ddg', 'title': '分位数（p50/p95/p99） 到底在讲什么? - 知乎'}
