# N189: M/M/1 模型中服务时间 $L_{service}$ 的计算公式：$L_{service} = s_{avg} / B_{link}$，其中 $B_{link

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

M/M/1 模型中服务时间 $L_{service}$ 的计算公式：$L_{service} = s_{avg} / B_{link}$，其中 $B_{link}$ 为回源链路有效吞吐率（通常取预留带宽的 70%-80% 以留出协议开销余量），代入 $s_{avg}=1.5\text{MB}$ 和 $B_{link}=100\text{Mbps}$ 得 $L_{service} \approx 0.12\text{ms}$。

## Corrected Claim

M/M/1 模型中服务时间 $L_{service}$ 的计算公式：$L_{service} = s_{avg} / B_{link}$，其中 $B_{link}$ 为回源链路有效吞吐率，代入 $s_{avg}=1.5\text{MB}$ 和 $B_{link}=100\text{Mbps}$ 得 $L_{service} \approx 120\text{ms}$。

## Evidence

[质询]数值量级严重错误：1.5MB 数据在 100Mbps 链路下的传输时间约为 120ms，而非 0.12ms，相差 1000 倍。 | 逻辑校验失败：1.5MB = 12Mbit，12Mbit / 100Mbps = 0.12s = 120ms。陈述中 0.12ms 的结果存在明显的单位换算或数量级错误。
