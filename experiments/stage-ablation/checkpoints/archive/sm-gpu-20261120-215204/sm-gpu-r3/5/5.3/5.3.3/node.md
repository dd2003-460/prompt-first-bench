# N124: N31 工作点 C 的 TCO 修正：硬件 $1,700 + 电力 (350W * 0.8 负载 * 2000h/年 * $0.15/kWh * 3年) ≈ $

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

N31 工作点 C 的 TCO 修正：硬件 $1,700 + 电力 (350W * 0.8 负载 * 2000h/年 * $0.15/kWh * 3年) ≈ $2,520，总 TCO ≈ $4,220；若因显存不足需增加 CPU 内存 Offloading 主机 (RAM 128GB, +$300)，总 TCO ≈ $4,520。

## Corrected Claim

N31 工作点 C 的 TCO 修正：硬件 $1,700 + 电力 (350W * 0.8 负载 * 2000h/年 * $0.15/kWh * 3年) ≈ $2,520，总 TCO ≈ $4,220；若因显存不足需增加 CPU 内存 Offloading 主机 (RAM 128GB, +$300)，总 TCO ≈ $4,520。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点N124聚焦于电力成本因负载因子修正导致的TCO变化（纯财务/能耗维度），而第二个子节点聚焦于CPU Offloading带来的性能瓶颈及额外硬件/机会成本（性能/架构维度）。两者关注点不同，无逻辑重叠或矛盾，且共同覆盖了父节点中TCO修正的两个主要变量（电力参数和显存溢出方案），因此正交且完备。）

## Search Query

RTX 4090 TCO 3 year electricity cost local inference
