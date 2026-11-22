# N200: 方案B可逆性成本 $C_{reverse}$ 的精确值：算法降权通过参数回滚恢复，$C_{reverse} = C_{rollback} + C_{verify

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

方案B可逆性成本 $C_{reverse}$ 的精确值：算法降权通过参数回滚恢复，$C_{reverse} = C_{rollback} + C_{verify}$。参数回滚（$C_{rollback}$）需0.5人日（配置变更+部署）；验证恢复（$C_{verify}$）需1人日（A/B测试确认CTR/成交率恢复至基线）。总 $C_{reverse} \approx 1.5$ 人日，原估算 $C_{reverse} \approx C_{train}$ 不准确，因回滚不涉及重训，成本更低。

## Corrected Claim

方案B可逆性成本 $C_{reverse}$ 的精确值：算法降权通过参数回滚恢复，$C_{reverse} = C_{rollback} + C_{verify}$。参数回滚（$C_{rollback}$）需0.5人日（配置变更+部署）；验证恢复（$C_{verify}$）需1人日（A/B测试确认CTR/成交率恢复至基线）。总 $C_{reverse} \approx 1.5$ 人日，原估算 $C_{reverse} \approx C_{train}$ 不准确，因回滚不涉及重训，成本更低。

## Evidence

先验知识/题面给定，逻辑校验通过：参数回滚不涉及模型重训，其成本（配置变更+部署+验证）通常远低于重新训练成本，1.5人日的估算在工程实践中量级合理且逻辑自洽。

## Search Query

algorithm rollback cost A/B test verification person-days
