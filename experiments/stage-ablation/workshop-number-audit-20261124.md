# Workshop Draft 数字口径审计（workshop-number-audit）

> 日期 2026-11-24 01:30 · 对象 `workshop-draft-metacog-20261122.md`（投稿前 verify 的另一半：守"承重数字对不对"）
> 方法：提取 draft 承重数字 → 找数据源脚本 → 重跑复算 → 过 16 条检查。

## 核验表（数字 / 数据源 / 结果）

| 数字 | 声明口径 | 数据源（脚本实算） | 结果 |
|---|---|---|---|
| 52.5% (5,630/10,730) | GPU 域非 verified 占比 | `gpu-unverified-52pct.py` 重跑 = 5630/10730 | ✓ |
| 45.5% (9,984/21,945) | 全语料非 verified 占比 | 同上脚本 = 9984/21945 | ✓ |
| 60.6% (1,330/2,196) | 19 树 search 节点无 URL | `url-retention-gap.py` 重跑 = 1330/2196，80% 有引用痕迹 | ✓ |
| 3.7% (331/8,870) | rework fix rate 节点级 | `repair-closure-dryrun.py` 重跑 = 331/8870（80 run json） | ✓ |
| 3.1% (331/10,702) | rework fix rate 事件级 | 同上 = 331/10702；docstring 与实算一致（无静默过期） | ✓ |
| 71.0% vs 27.7%, z=+16.24/+8.13/+11.73 | 清洗后 search-source 防御标记耦合，三域 | `T-JUDGE-1-depth-axis-provenance-20261123.md` L722-724 逐值一致 | ✓ |
| 93.5% | unv/(unv+con) 不含 ambiguous | provenance doc L479 两口径核验 | ✓ |
| 5.2% (32/621) | Q6 15 run rework fix rate | 本轮从 15 个 run 文件（5 budget × 3 rep）逐文件重算 = 32/621 = 5.15%；同口径同代码（GPU 3.7%） | ✓ |
| 21.5% / 11.0% | 功效分析（large/medium effect） | 本轮脚本实算（非中心 F 蒙特卡洛，n=15, df 2/12） | ✓ |
| 45.6% / 2.8% | 文献数字（arXiv:2611.10787） | 非本项目数据，引用文献值 | N/A |
| F(2,12)=0.036 | monitoring 轴 ANOVA | 本轮复算 = 0.0360（每档 0.099/0.100/0.108） | ✓ |

## 16 条检查过审记录

- **红旗 #4（同一数字改 2 次）**：z 值出现 15.55（脚本未清洗）vs 16.24（draft 清洗后）——溯源确认是两个口径（清洗前/后），draft 明确写 "survives the cleaning" 用清洗后值，口径自洽，**非错误**。
- **scope #1**：52.5% 限定 "GPU domain"（分母 10,730 = GPU 域节点），45.5% 限定 "full corpus"（21,945）——限定词与分母人群一致 ✓。
- **口径 #15（参考工件钉死）**：coverage 声明均标 gold 工件（36 units enriched / 46 units Q6），judge 默认 gold 已显式确认 ✓。
- **era #7**：metacog 不变发现 era-scoped 到 rep-scan（n=5/tier），abstract 措辞已对齐（本轮功效分析进一步限定）✓。
- **abstract 强度 #8**：headline 已降级 "suggestion with stated power limits"，≤ 正文支持强度 ✓。
- **统计 #10**：flat 声明带层内 sd + ANOVA + 功效（本轮补）✓。
- **加法 #2**：104 = 83+6+15、83 = 34+49 均自洽 ✓。

## 结论

**11 个承重数字全部溯源通过，0 个口径错、0 个双计、0 个 docstring 静默过期。** 唯一值得留意的点（z 值双口径）已确认自洽。数字审计 = verify 完成；结合红队审视（claim 可防御性），workshop draft 的投稿前 verify 两项都过。
