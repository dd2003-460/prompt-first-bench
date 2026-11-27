# N43: 归一化容量 $c$ 在考虑大小-热度负相关时，需从 $C/E[S]$ 修正为 $C/E[S|H_{top-c}]$，其中 $E[S|H_{top-c}]$ 是驻

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

归一化容量 $c$ 在考虑大小-热度负相关时，需从 $C/E[S]$ 修正为 $C/E[S|H_{top-c}]$，其中 $E[S|H_{top-c}]$ 是驻留集合对象的平均大小，该值低于全局 $E[S]$，导致有效容量 $c_{eff} > c_{indep}$。

## Corrected Claim

归一化容量 $c$ 在考虑大小-热度负相关时，需从 $C/E[S]$ 修正为 $C/E[S|H_{top-c}]$，其中 $E[S|H_{top-c}]$ 是驻留集合对象的平均大小，该值低于全局 $E[S]$，导致有效容量 $c_{eff} > c_{indep}$。

## Evidence

先验知识/题面给定，逻辑校验通过：在大小-热度负相关（大对象冷，小对象热）的假设下，驻留集合（Top-c 热度）的平均大小确实小于全局平均大小，因此分母减小，有效容量 c_eff 增大，推导自洽。
