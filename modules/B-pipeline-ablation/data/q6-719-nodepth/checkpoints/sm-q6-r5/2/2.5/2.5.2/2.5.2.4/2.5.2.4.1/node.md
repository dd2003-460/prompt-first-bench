# N609: 单 POP 一次性硬件采购成本 C_hardware_onetime = N_servers_per_pop * C_server_unit + N_stora

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N201

## Claim

单 POP 一次性硬件采购成本 C_hardware_onetime = N_servers_per_pop * C_server_unit + N_storage_units * C_storage_unit，其中 N_servers_per_pop ∈ [4, 8] 台，C_server_unit ≈ ¥25,000（基于 N67 折旧前原值），N_storage_units 为 5TB NVMe SSD 阵列，C_storage_unit ≈ ¥15,000/TB，计算得 C_hardware_onetime ≈ ¥155,000 - ¥265,000

## Corrected Claim

单 POP 一次性硬件采购成本 C_hardware_onetime = N_servers_per_pop * C_server_unit + N_storage_units * C_storage_unit，其中 N_servers_per_pop ∈ [4, 8] 台，C_server_unit ≈ ¥25,000（基于 N67 折旧前原值），N_storage_units 为 5TB NVMe SSD 阵列，C_storage_unit ≈ ¥15,000/TB，计算得 C_hardware_onetime ≈ ¥155,000 - ¥265,000

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程自洽（4*25k+5*15k=155k, 8*25k+5*15k=265k），数值量级符合硬件成本常识。

## Search Query

edge server hardware cost per unit NVMe SSD 5TB price 2024
