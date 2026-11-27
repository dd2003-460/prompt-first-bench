# N308: 在 Linux 系统下，ACS (Access Control Services) 关闭的具体操作是通过内核参数 `pci=noaer` 或 `pcie_acs

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N100

## Claim

在 Linux 系统下，ACS (Access Control Services) 关闭的具体操作是通过内核参数 `pci=noaer` 或 `pcie_acs_override=downstream,multifunction` 启动，或在 BIOS 中关闭 'PCIe ACS' 选项；若未关闭，`lspci -vv` 显示 ACS Capability 为 Enabled，此时 P2P DMA 被拦截，有效带宽从 PCIe 5.0 的 64 GB/s 降至 CPU 内存控制器带宽（Intel 12代/13代/14代 ~100 GB/s，AMD 5000/7000 ~120 GB/s [时效待核]），导致 TP=2 通信延迟增加约 3-5 倍（基于 N100 的 3-5 倍延迟增量估算，实际需 `nvidia-smi topo -m` 验证 P2P 状态为 OK 或 SYS）

## Corrected Claim

在 Linux 系统下，ACS 关闭可通过内核参数 `pci=noaer` 或 `pcie_acs_override=downstream,multifunction` 实现，或在 BIOS 中关闭 'PCIe ACS'。若未关闭，`lspci -vv` 显示 ACS Enabled，P2P DMA 被拦截，数据需经 CPU 内存中转，有效带宽受限于 PCIe 链路带宽（如 PCIe 5.0 x16 单向约 64 GB/s）及内存带宽，通常低于直接 P2P 带宽，导致通信延迟显著增加（具体倍数取决于平台内存带宽与 PCIe 版本，需实测验证）。

## Evidence

[质询]数值量级与逻辑矛盾：陈述称未关闭ACS时带宽从PCIe 5.0的64 GB/s降至CPU内存控制器带宽（Intel ~100 GB/s，AMD ~120 GB/s），这在逻辑上自相矛盾。如果P2P被拦截并经由CPU内存中转（PCIe-to-PCIe via CPU），有效带宽受限于PCIe链路带宽（64 GB/s）或内存带宽，但通常PCIe 5.0 x16单向64 GB/s是上限，而现代CPU内存带宽（如DDR5双通道）往往高于或接近此值，但陈述暗示‘降至’内存带宽且该值高于PCIe带宽，这在P2P被阻断的场景下表述混乱。更关键的是，若P2P被阻断，数据必须经过CPU内存，此时瓶颈通常是PCIe链路（64 GB/s）而非内存控制器（100+ GB/s），因此‘降至100 GB/s’的说法在PCIe 5.0语境下不成立（因为PCIe 5.0本身只有64 GB/s单向，双向128 GB/s，但P2P阻断后通常受限于单向链路或内存拷贝效率，不会‘降至’一个比PCIe链路还高的数值作为瓶颈描述，除非指双向聚合，但语境模糊）。此外，TP=2延迟增加3-5倍是基于N100（低功耗CPU，PCIe 3.0/4.0）的估算，直接套用到PCIe 5.0的高性能平台缺乏依据，属于经验事实且缺乏来源支持。 | 逻辑校验发现内部矛盾：PCIe 5.0单向带宽为64 GB/s，若P2P被阻断经由CPU内存中转，瓶颈通常为PCIe链路或内存带宽，但陈述称带宽‘降至’100-120 GB/s（高于PCIe 5.0单向带宽），这在单方向P2P通信语境下逻辑不通；且延迟倍数估算基于N100平台，外推至PCIe 5.0平台缺乏逻辑必然性。来源不可用，无法外部核验。

## Search Query

Linux disable PCIe ACS P2P DMA nvidia-smi topo -m bandwidth degradation
