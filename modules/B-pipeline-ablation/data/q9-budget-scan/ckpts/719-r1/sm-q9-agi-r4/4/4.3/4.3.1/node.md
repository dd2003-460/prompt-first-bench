# N63: MTTR < 30 分钟的分解：MTTR = Detection Time + Diagnosis Time + Recovery Time。Detection

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

MTTR < 30 分钟的分解：MTTR = Detection Time + Diagnosis Time + Recovery Time。Detection Time 依赖于监控粒度（建议 < 5 min，基于 Prometheus 抓取间隔 30s + 告警延迟），Diagnosis Time 依赖于日志聚合效率（建议 < 10 min），Recovery Time 依赖于容器重启与状态加载（建议 < 15 min）。

## Corrected Claim

MTTR < 30 分钟的分解：MTTR = Detection Time + Diagnosis Time + Recovery Time。Detection Time 依赖于监控粒度（建议 < 5 min，基于 Prometheus 抓取间隔 30s + 告警延迟），Diagnosis Time 依赖于日志聚合效率（建议 < 10 min），Recovery Time 依赖于容器重启与状态加载（建议 < 15 min）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点严格对应父节点公式中的三个组件（Detection, Diagnosis, Recovery）。其中 Recovery 被细分为‘容器启动’和‘状态加载’两个独立且互补的子任务，二者无重叠且共同构成完整的恢复过程。各子节点分别聚焦于不同的技术瓶颈（监控延迟、日志分析、镜像/进程启动、GPU上下文/KV Cache），逻辑上互斥且覆盖全面。）
