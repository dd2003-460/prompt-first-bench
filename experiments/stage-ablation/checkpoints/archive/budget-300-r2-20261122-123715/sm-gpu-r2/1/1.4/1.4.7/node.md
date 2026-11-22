# N52: PCIe 4.0 x16 实际有效带宽：理论峰值 32GB/s，但受协议开销和驱动影响，实际有效带宽通常为 25-28GB/s；在 2×RTX 4090 TP=

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8, N9, N10

## Claim

PCIe 4.0 x16 实际有效带宽：理论峰值 32GB/s，但受协议开销和驱动影响，实际有效带宽通常为 25-28GB/s；在 2×RTX 4090 TP=2 场景下，每层需传输 ~1GB 数据，总通信延迟对吞吐量的影响系数 k_bandwidth 需通过实测或模拟确定。

## Corrected Claim

PCIe 4.0 x16 理论峰值约 31.5GB/s，实际有效带宽通常低于理论值（具体数值需实测，一般认为在 25-28GB/s 区间）；在 2×RTX 4090 TP=2 场景下，每层需传输 ~1GB 数据，总通信延迟对吞吐量的影响系数 k_bandwidth 需通过实测或模拟确定。

## Evidence

[质询]参考来源主要讨论PCIe 3.0及通用带宽计算原理，未提供PCIe 4.0 x16具体实测有效带宽（25-28GB/s）的直接数据支持，且该数值属于经验事实，无法仅凭逻辑推导得出。 | 逻辑自洽：PCIe 4.0 x16理论带宽为64GT/s * 16 lanes * 128b/130b编码 ≈ 31.5GB/s，实际受开销影响降至25-28GB/s符合工程常识；但来源[1]仅提及PCIe 3.0实测，来源[2]仅给出计算公式，均无PCIe 4.0具体实测数据直接支持，属经验事实缺来源支持。

## Search Query

PCIe 4.0 x16 effective bandwidth LLM tensor parallelism bottleneck

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_42561476/article/details/160360021&rut=494f120e7dd937bb396b358475eed2da5bba4a15a797b8d649f2f5114b69f1cc', 'type': 'ddg', 'title': '别再只看理论值了!实测告诉你PCIe 3.0 x16的真实有效带宽到底有多少-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_42229404/article/details/84069859&rut=c9820ca2f5aa396236f132dc6edea3a3d73e8f123586fea723b59d2955c56eca', 'type': 'ddg', 'title': 'PCIE2.0/PCIE3.0/PCIE4.0/PCIE5.0接口的带宽、速率计算_pcie2.0 x1速度-CSDN博客'}
