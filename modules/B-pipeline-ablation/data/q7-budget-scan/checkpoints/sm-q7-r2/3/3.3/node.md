# N22: 500TB总量约束：三种方案均可支持500TB存储，无方案被排除

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

500TB总量约束：三种方案均可支持500TB存储，无方案被排除

## Corrected Claim

500TB总量约束：三种方案均可支持500TB存储，无方案被排除

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别从物理资源需求（硬件规格）、系统扩展性边界（控制器/架构限制）以及可靠性/故障域（RAID策略与恢复）三个不同维度对500TB约束进行分解。各维度关注点独立，无逻辑重叠或矛盾，且共同覆盖了存储方案在容量层面的关键工程约束。）
