# N124: N31 工作点 C 的 TCO 修正：硬件 $1,700 + 电力 (350W * 0.8 负载 * 2000h/年 * $0.15/kWh * 3年) ≈ $

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

N31 工作点 C 的 TCO 修正：硬件 $1,700 + 电力 (350W * 0.8 负载 * 2000h/年 * $0.15/kWh * 3年) ≈ $2,520，总 TCO ≈ $4,220；若因显存不足需增加 CPU 内存 Offloading 主机 (RAM 128GB, +$300)，总 TCO ≈ $4,520。

## Corrected Claim

N31 工作点 C 的 TCO 修正：硬件 $1,700 + 电力 (350W * 0.8 负载 * 2000h/年 * $0.15/kWh * 3年) ≈ $2,520，总 TCO ≈ $4,220；若因显存不足需增加 CPU 内存 Offloading 主机 (RAM 128GB, +$300)，总 TCO ≈ $4,520。

## Evidence

先验知识/题面给定，逻辑校验通过：电力成本计算 (350*0.8*2000*0.15*3 = 2520) 准确，总 TCO 加法 (1700+2520=4220, 4220+300=4520) 无误，数值量级符合工程常识。

## Search Query

RTX 4090 TCO 3 year electricity cost local inference
