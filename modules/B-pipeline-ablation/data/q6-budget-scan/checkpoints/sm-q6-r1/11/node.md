# N35: P99 延迟目标值 $T$ 的估算方法：基于用户地理分布 $G(x)$ 的加权平均 RTT，若 90% 用户位于核心 3 区域（华东/华南/华北），且自建 PO

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

P99 延迟目标值 $T$ 的估算方法：基于用户地理分布 $G(x)$ 的加权平均 RTT，若 90% 用户位于核心 3 区域（华东/华南/华北），且自建 POP 覆盖这 3 区域，则 $T_{target} \approx 1.5 \times RTT_{core} + 5\text{ms}$，其中 $RTT_{core}$ 典型值为 20-30ms，故 $T_{target}$ 约为 35-50ms。

## Corrected Claim

P99 延迟目标值 $T$ 的估算方法：基于用户地理分布 $G(x)$ 的加权平均 RTT，若 90% 用户位于核心 3 区域（华东/华南/华北），且自建 POP 覆盖这 3 区域，则 $T_{target}$ 可近似估算为 $1.5 \times RTT_{core} + 5\text{ms}$（注：系数与常数项为经验值，需根据实际网络环境校准），其中 $RTT_{core}$ 典型值约为 20-30ms，故 $T_{target}$ 估算范围约为 35-50ms。

## Evidence

[质询]该陈述包含具体的工程经验参数（如1.5倍系数、5ms固定开销、20-30ms核心RTT典型值），这些属于经验事实而非第一性原理可推导的数学或物理定律，且参考来源仅解释P99定义，未提供任何关于地理分布加权RTT估算方法或具体数值的支持。 | 逻辑自洽（1.5*20+5=35, 1.5*30+5=50），但参考来源[1]仅涉及P99定义，与具体估算公式及数值无关，属于经验事实且缺来源支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/608621390&rut=9fd29817021b056703c82108e143ee7bea18c9f317d69b9cd4ff0f8df2e0db6c', 'type': 'ddg', 'title': 'Prometheus 中是如何计算 P99 的？ - 知乎'}
