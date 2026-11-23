# N321: 外包SRE成本对比：若采用外包模式，10个POP点年外包成本≈¥800k-1.2M（¥66k-100k/月），低于自建团队¥880k-3.16M（2-4人×¥4

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N101

## Claim

外包SRE成本对比：若采用外包模式，10个POP点年外包成本≈¥800k-1.2M（¥66k-100k/月），低于自建团队¥880k-3.16M（2-4人×¥440k-790k/人），但外包响应时间通常比自建团队慢15-30min，导致MTTR增加，P99延迟风险上升，需评估外包SLA是否满足P99≤T约束

## Corrected Claim

外包SRE成本通常低于自建团队，但响应时间可能较慢，需评估SLA是否满足业务约束（具体数值需根据实际市场报价和团队规模测算）

## Evidence

[质询]具体数值（如¥800k-1.2M、¥440k-790k/人、15-30min延迟）属于特定场景下的经验估算，缺乏通用性，且参考来源未提供具体金额数据，仅定性讨论招聘周期，无法验证具体成本量级和响应时间差异。 | 参考来源[1][2]仅定性讨论自建与外包的招聘周期差异，未提供具体成本数值或响应时间数据，属于间接相关但无直接数值支持；逻辑上外包成本低于自建符合一般市场规律，但具体数值无法从来源推导或验证。

## Search Query

SRE outsourcing cost China 10 edge nodes 2024

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/938574182_121963041&rut=a85cfed68e7d77dede08a12b42ed427c82d653f86483d3425e66c7321d308e44', 'type': 'ddg', 'title': '自建 It 团队 Vs 外包？算完这 3 笔账，90% 企业选了后者'}
- {'url': 'https://www.sohu.com/a/944087679_121963041&rut=a873dcac3ee735df47b367b3d5fbefcd58eb80ce528897c93db1ed55e52f51fd', 'type': 'ddg', 'title': '自建 It 团队 Vs 外包？算完这 3 笔账，90% 企业选了后者'}
