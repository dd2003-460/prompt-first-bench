# N20: 可靠性约束下的调度损失：云端 API 可用性 SLA 通常为 99.9%（月度停机 ~43min），本地硬件故障率 MTBF ~20000h，混合调度需增加冗余

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

可靠性约束下的调度损失：云端 API 可用性 SLA 通常为 99.9%（月度停机 ~43min），本地硬件故障率 MTBF ~20000h，混合调度需增加冗余切换逻辑，导致平均任务完成时间增加 5-15%

## Corrected Claim

可靠性约束下的调度损失：云端 API 可用性 SLA 通常为 99.9%（月度停机 ~43min），本地硬件故障率 MTBF ~20000h，混合调度需增加冗余切换逻辑，导致平均任务完成时间增加 5-15%

## Evidence

先验知识/题面给定，逻辑校验通过：99.9% SLA对应月度停机约43分钟符合数学计算（720h*0.001=0.72h≈43min）；MTBF 20000h为工业标准量级；混合调度引入冗余切换开销导致5-15%延迟符合系统工程常识。

## Search Query

cloud API availability SLA vs local hardware MTBF fault tolerance overhead
