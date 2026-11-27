# N222: 4x RTX 4090 主板选型约束与价格验证：需支持 4 个 PCIe 4.0 x16 插槽且物理间距允许双槽位显卡安装。候选主板如 ASUS ProArt 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

4x RTX 4090 主板选型约束与价格验证：需支持 4 个 PCIe 4.0 x16 插槽且物理间距允许双槽位显卡安装。候选主板如 ASUS ProArt PA4090 (约 $1,500) 或 Supermicro H12SSL-i (约 $1,200)。关键约束：PCIe 通道分配需确保每卡获得 x16 带宽，若主板仅支持 x8/x8 分叉，带宽减半将导致多卡通信开销增加，影响 N92 中 4.7 tokens/s 的估算准确性。

## Corrected Claim

4x RTX 4090 主板选型需支持 4 个 PCIe 4.0 x16 插槽且物理间距允许双槽位显卡安装。候选主板如 ASUS ProArt PA3299CSWS 或 Supermicro 相应工作站主板（价格通常在 $2,000-$3,000+ 区间，具体需核实）。关键约束：PCIe 通道分配需确保每卡获得 x16 带宽，若主板仅支持 x8/x8 分叉，带宽减半将导致多卡通信开销增加，影响 N92 中 4.7 tokens/s 的估算准确性。

## Evidence

[质询]候选主板型号与规格严重不符：ASUS ProArt 系列通常无名为 'PA4090' 的型号（可能是混淆了显卡型号或虚构），且 Supermicro H12SSL-i 是双路服务器主板，其 PCIe 插槽布局和物理间距通常不支持标准双槽位消费级显卡（如 RTX 4090）的密集安装，更不可能以 $1,200 的价格作为 4 卡工作站主板的主要推荐（该价位通常对应入门级或二手服务器板，而支持 4 张 x16 4090 的专业主板如 ASUS ProArt PA3299CSWS 价格远高于此）。 | 经验事实，逻辑自洽但缺来源支持；且参考来源全部失败，无法验证具体型号、价格及物理兼容性，存在明显的型号虚构或规格错配风险。

## Search Query

ASUS ProArt PA4090 motherboard price PCIe 4.0 x16 slots 4 GPU support
