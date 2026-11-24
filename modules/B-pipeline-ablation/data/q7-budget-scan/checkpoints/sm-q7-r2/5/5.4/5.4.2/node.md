# N76: HDD分层过滤结果：温数据SSD层吞吐需求7GB/s，假设SSD层容量100TB，单盘顺序读~500MB/s，需盘数 = 7GB/s / 500MB/s = 1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

HDD分层过滤结果：温数据SSD层吞吐需求7GB/s，假设SSD层容量100TB，单盘顺序读~500MB/s，需盘数 = 7GB/s / 500MB/s = 14盘，总SSD容量 = 14 * 7.68TB = 107.5TB（满足100TB需求）；冷数据HDD层吞吐需求16.7TB/h（基于N40修正），单盘顺序读~200MB/s，需盘数 = 16.7TB/h / 3600s / 200MB/s = 23盘，总HDD容量 = 23 * 16TB = 368TB（接近400TB需求，需25盘）

## Corrected Claim

HDD分层过滤结果：温数据SSD层吞吐需求7GB/s，假设SSD层容量100TB，单盘顺序读~500MB/s，需盘数 = 7GB/s / 500MB/s = 14盘，总SSD容量 = 14 * 7.68TB = 107.5TB（满足100TB需求）；冷数据HDD层吞吐需求16.7TB/h（基于N40修正），单盘顺序读~200MB/s，需盘数 = 16.7TB/h / 3600s / 200MB/s = 23盘，总HDD容量 = 23 * 16TB = 368TB（接近400TB需求，需25盘）

## Evidence

先验知识/题面给定，逻辑校验通过：SSD层 7GB/s / 500MB/s = 14盘，14*7.68TB=107.52TB>100TB；HDD层 16.7TB/h ≈ 4.64GB/s，4.64GB/s / 200MB/s ≈ 23.2盘，取23盘容量368TB，取25盘容量400TB，计算与逻辑均自洽。
