# N24: 下垫面粗糙度长度（Roughness Length, z0）敏感性：海洋表面 z0 ≈ 0.002-0.01 m，而典型陆地植被/城市 z0 ≈ 0.1-1.0

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

下垫面粗糙度长度（Roughness Length, z0）敏感性：海洋表面 z0 ≈ 0.002-0.01 m，而典型陆地植被/城市 z0 ≈ 0.1-1.0 m。z0 增加 10-100 倍会导致边界层高度 h 显著增加（h ∝ z0^(1/3) 至 z0^(1/4)），进而使摩擦耗散功率 P_fric = τV 增加约 30-50%，这是登陆后摩擦效应激增的直接物理参数。

## Corrected Claim

海洋表面 z0 ≈ 0.002-0.01 m，典型陆地植被/城市 z0 ≈ 0.1-1.0 m。z0 的增加会显著影响边界层结构和摩擦耗散，通常导致摩擦效应增强，但具体的边界层高度变化比例及功率增量需依赖特定气象模型参数化方案确定。

## Evidence

[质询]陈述中关于边界层高度 h 与 z0 的比例关系（h ∝ z0^(1/3) 至 z0^(1/4)）以及由此导致的摩擦耗散功率增加 30-50% 的具体数值范围缺乏通用物理定律的直接支持，属于特定模型或经验拟合结果，且不同气象模型中该敏感度系数差异较大，容易因口径混淆导致误差。 | 来源 [1] 和 [2] 确认了粗糙度长度 z0 的定义及其随下垫面（植被/城市 vs 海洋）变化的物理机制，支持 z0 量级差异（海洋远小于陆地）；但来源未提供 h 与 z0 的具体幂律关系及摩擦功率增量的定量数据，该部分为经验事实且缺乏多源一致支持。

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E7%B2%97%E7%B3%99%E5%BA%A6%E9%95%BF%E5%BA%A6/5008242&rut=cc0107bac66a74b2ec1974dbbe80e026c8583228f704e58986443d48ed927f07', 'type': 'ddg', 'title': '粗糙度长度 - 百度百科'}
- {'url': 'https://en.wikipedia.org/wiki/Roughness_length&rut=27f188fd2760e59db9a75726dd916d25abef903c1674fdd67ac9909664b57d26', 'type': 'ddg', 'title': 'Roughness length - Wikipedia'}
