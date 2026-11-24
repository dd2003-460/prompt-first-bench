# N332: 空闲成本的替代计算口径：若集群在扫描期间可执行其他后台任务（如日志压缩、备份），则净空闲成本 C_net_idle = C_idle_gross * (1 - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

空闲成本的替代计算口径：若集群在扫描期间可执行其他后台任务（如日志压缩、备份），则净空闲成本 C_net_idle = C_idle_gross * (1 - Utilization_Background)，假设后台任务填充 30% 空闲时间，C_net_idle = ¥89,000 * 0.7 = ¥62,300/天 [knowledge]

## Corrected Claim

空闲成本的替代计算口径：若集群在扫描期间可执行其他后台任务（如日志压缩、备份），则净空闲成本 C_net_idle = C_idle_gross * (1 - Utilization_Background)，假设后台任务填充 30% 空闲时间，C_net_idle = ¥89,000 * 0.7 = ¥62,300/天 [knowledge]

## Evidence

先验知识/题面给定，逻辑校验通过：公式 C_net = C_gross * (1 - U) 符合成本抵扣的基本逻辑，数值计算 89000 * 0.7 = 62300 准确无误。
