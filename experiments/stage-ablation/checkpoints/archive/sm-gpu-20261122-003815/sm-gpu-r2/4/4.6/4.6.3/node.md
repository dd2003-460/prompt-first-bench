# N137: 通信开销对Decode吞吐的影响量化：Decode阶段每层需一次All-Reduce。若单卡计算时间 t_comp = 1/R_decode，通信时间 t_co

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

通信开销对Decode吞吐的影响量化：Decode阶段每层需一次All-Reduce。若单卡计算时间 t_comp = 1/R_decode，通信时间 t_comm = L_layers * t_allreduce。2x4090 (PCIe) 总时间 = t_comp + 64*16ms ≈ t_comp + 1.024s。若单卡t_comp≈70ms (14 tok/s)，总时间≈1.094s，吞吐降至 ~0.91 tokens/s (严重瓶颈)。2xA100 (NVLink) 总时间 = t_comp + 64*0.85ms ≈ t_comp + 0.054s，吞吐损失 <5%。

## Corrected Claim

通信开销对Decode吞吐的影响量化：Decode阶段每层需一次All-Reduce。若单卡计算时间 t_comp = 1/R_decode，通信时间 t_comm = L_layers * t_allreduce。2x4090 (PCIe) 总时间 = t_comp + 64*16ms ≈ t_comp + 1.024s。若单卡t_comp≈70ms (14 tok/s)，总时间≈1.094s，吞吐降至 ~0.91 tokens/s (严重瓶颈)。2xA100 (NVLink) 总时间 = t_comp + 64*0.85ms ≈ t_comp + 0.054s，吞吐损失 <5%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（64*16ms=1.024s, 64*0.85ms=0.0544s），吞吐推导符合逻辑（1/1.094s≈0.91 tok/s），硬件通信延迟量级（PCIe vs NVLink）符合工程常识。
