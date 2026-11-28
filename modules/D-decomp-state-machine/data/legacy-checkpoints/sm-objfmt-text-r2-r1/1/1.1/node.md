# N7: Qwen3-27B 模型总参数量 P_total 为 27.8B，其中激活参数 P_active 约为 3.3B（基于 MoE 架构公开数据或官方技术报告），该

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1

## Claim

Qwen3-27B 模型总参数量 P_total 为 27.8B，其中激活参数 P_active 约为 3.3B（基于 MoE 架构公开数据或官方技术报告），该参数决定了 KV Cache 计算的基准规模

## Corrected Claim

Qwen3系列27B规模模型总参数量约为27.8B，其MoE架构下的激活参数规模通常在数B级别（如3.3B左右），具体数值需以官方对应版本技术报告为准。

## Evidence

[质询]来源标题及摘要中提到的模型版本为 'Qwen3.8-27B' 和 'Qwen3.6-27B'，与待核验事实中的 'Qwen3-27B' 版本号不一致，存在版本混淆风险；且来源仅提及总参数量约270亿，未提供激活参数3.3B的具体数据支持。 | 来源[1][2]证实了27B级别模型的总参数量量级（~270亿），但未直接覆盖'Qwen3-27B'特定版本的激活参数细节，且版本号存在差异，故降级为定性表述。

## Search Query

Qwen3-27B total parameters active parameters MoE architecture

## Retrieval Sources

- {'url': 'https://blog.csdn.net/2401_85375151/article/details/164094490&rut=95f41eb6bfe4cd728450013434f73285e95b049081e0cbd764d0f34782bbe596', 'type': 'ddg', 'title': 'Qwen3.8-27B本地部署教程（全网最详细版）-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_00208/article/details/157234872&rut=4a49a2eb9bb3f9305a60a1d1618f251cb86a252aa98581be6eeed2fa8da333ff', 'type': 'ddg', 'title': 'Qwen3.6-27B最佳实践：3大采样参数组合+8万token输出设置，解锁模型全部潜力-CSDN博客'}
