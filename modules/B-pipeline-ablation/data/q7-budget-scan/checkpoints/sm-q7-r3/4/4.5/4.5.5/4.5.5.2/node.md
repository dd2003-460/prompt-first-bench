# N316: HDD+SSD 分层方案中 SSD 层与 HDD 层故障的相关性修正：若电源或背板故障同时导致多块盘失效，故障率需乘以相关性系数 ρ；典型服务器电源 MTBF 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114

## Claim

HDD+SSD 分层方案中 SSD 层与 HDD 层故障的相关性修正：若电源或背板故障同时导致多块盘失效，故障率需乘以相关性系数 ρ；典型服务器电源 MTBF 1,000,000h，λ_power = 0.0088 次/年，若电源故障导致所有盘离线，则 λ_correlated = λ_power + λ_disks * (1-ρ)，ρ 通常取 0.1-0.3，需计入总故障率 λ_Mixed 的修正项。

## Corrected Claim

HDD+SSD 分层方案中，若存在电源或背板等共因故障导致多块盘同时失效，故障率需引入相关性系数 ρ 进行修正。具体修正公式及典型参数（如电源 MTBF、ρ 取值范围）需依据具体硬件规格及可靠性工程数据确定，通用逻辑为 λ_correlated 需反映共因故障的影响。

## Evidence

[质询]该陈述包含具体的工程经验参数（如服务器电源MTBF 1,000,000h、相关性系数ρ取值0.1-0.3）及特定的故障率修正公式，属于经验事实而非第一性原理可推导的数学/物理定律。参考来源仅讨论Windows 10分层存储的功能原理，完全未涉及可靠性工程、故障相关性或MTBF计算，无法提供外部支持。 | 逻辑上故障相关性修正公式符合可靠性工程基本直觉（共因故障需修正），但具体数值（MTBF、ρ）为经验参数，参考来源[1]与可靠性计算无关，无法验证具体数值，故降级。

## Search Query

server power supply failure correlation disk array common cause failure

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/456602263&rut=aa39c68306d31f8974a601511f68b280a971b0c38886adc456d8782d9a7e9967', 'type': 'ddg', 'title': 'Windows10使用分层存储，自制混合硬盘 - 知乎'}
