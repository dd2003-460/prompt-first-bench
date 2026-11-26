# J3a 层级因素树 + 三性质检查
# origin: ai · 2026-11-26 · §1/§4/§2 线索=脚本机械生成，§2 判断/§3/§5=Lead 品味

## §1 层级因素树（转录自 S1 JSON，机械）

- **N-0** 每个通过任务的成本 `SHARE` [split] share=1.00
  - **N-1** 每小时持有成本 `h` [split] share=25
  - **N-2** 有效利用率 `u` [split] share=25
  - **N-3** 原始产出速率 `h` [split] share=25
  - **N-4** 任务通过率 `nuisance` [?] share=25 B1
  - **N-5** 可行域 `constraint` [split]
    - **N-1.1** 购置摊销 [split] share=42.8
    - **N-1.2** 电费 [split] share=49.3
    - **N-1.3** 故障损耗 [split] share=8.0
    - **N-2.1** 业务需求占空比 `duty_demand` [leaf] share=60 B6
    - **N-2.2** 调度效率 `sched_eff` [leaf] share=40 B6
    - **N-3.1** 时间 `prefill` [split] share=40.1
    - **N-3.2** 时间 `decode` [split] share=59.9
    - **N-5.1** 显存容量门槛 `n_cap` [leaf]
    - **N-5.2** 带宽准入下限 `s` [leaf] share=774
    - **N-5.3** 缓存命中率 `B8` [leaf] share=7.6 B8
      - **N-1.1.1** 卡价 `gpu_price` [leaf] share=55 B4 SHARED→N-1.3.2
      - **N-1.1.2** 主机价 `host_price` [leaf] share=15
      - **N-1.1.3** 残值率 `resid` [leaf] share=10 B8
      - **N-1.1.4** 摊销小时数 `H` [leaf] share=20 B8
      - **N-1.2.1** 整机功耗 `power_kw` [leaf] share=50
      - **N-1.2.2** 电价 `elec` [leaf] share=50 B5
      - **N-1.3.1** 三年故障概率 `p_fail` [leaf] share=50 B8
      - **N-1.3.2** 卡价 [?]
      - **N-3.1.1** 计算量 `prefill_flops` [leaf] share=30
      - **N-3.1.2** 峰值算力 `tf_peak` [leaf] share=25
      - **N-3.1.3**  `mfu` [split] share=45 B2
      - **N-3.2.1** 权重字节 `w_bytes` [leaf] share=25
      - **N-3.2.2** 每流 `kv_per_stream` [leaf] share=20 B7
      - **N-3.2.3** 峰值带宽 `bw_peak` [leaf] share=25
      - **N-3.2.4** 有效带宽系数 `eta_bw` [split] share=30 B3
        - **N-3.1.3.1** 占用率 `sm_occupancy` [leaf]
        - **N-3.1.3.2** 利用率 `tensor_util` [leaf]
        - **N-3.1.3.3** 命中率 `l2_hit` [leaf] SHARED→N-3.2.4.2
        - **N-3.2.4.1** 带宽利用率 `hbm_sol` [leaf]
        - **N-3.2.4.2** 命中率 `l2_hit` [leaf] SHARED→N-3.1.3.3
        - **N-3.2.4.3**  `launch_gap` [leaf]

> 顶层 5 节点 = 3 性能(u/λ_raw/G_pass) + 1 成本(c_hour) + 1 约束(feasible_set)。

## §4 完备检查：c_pass 公式参数 → 叶子覆盖（机械映射）

| 公式参数 | 应覆盖叶子 param | 命中 | 缺口 |
|---|---|---|---|
| c_hour/摊销 | gpu_price, host_price, resid, H | gpu_price(N-1.1.1), host_price(N-1.1.2), resid(N-1.1.3), H(N-1.1.4) | ✓ 无缺口 |
| c_hour/电费 | power_kw, elec | power_kw(N-1.2.1), elec(N-1.2.2) | ✓ 无缺口 |
| c_hour/故障 | p_fail, gpu_price | p_fail(N-1.3.1), gpu_price(N-1.1.1) | ✓ 无缺口 |
| u | duty_demand, sched_eff | duty_demand(N-2.1), sched_eff(N-2.2) | ✓ 无缺口 |
| λ_raw/prefill | prefill_flops, tf_peak, mfu | prefill_flops(N-3.1.1), tf_peak(N-3.1.2), mfu(N-3.1.3) | ✓ 无缺口 |
| λ_raw/decode | w_bytes, kv_per_stream, bw_peak, eta_bw | w_bytes(N-3.2.1), kv_per_stream(N-3.2.2), bw_peak(N-3.2.3), eta_bw(N-3.2.4) | ✓ 无缺口 |
| G_pass | — | — | ✓ 无缺口 |

**树外标定常数（覆盖检查单列，不算缺口）**：['tp_eff', 'out_tok']（在 calc.py，非 gold 树叶子）

**反向（冗余候选）**：叶子 param 未被 c_pass 公式直接引用 = ['B8', 'SHARE', 'constraint', 'decode', 'h', 'hbm_sol', 'l2_hit', 'launch_gap', 'n_cap', 'nuisance', 'prefill', 's', 'sm_occupancy', 'tensor_util', 'u']

## §2 正交检查：线索（机械列出，判断见下）

**SHARED 节点（正交性破绽候选，shared_ref 非空）**：

| 节点 | param | 共享自 | 含义 |
|---|---|---|---|
| N-1.1.1 卡价 | gpu_price | N-1.3.2 | 同一底层因素进两层 |
| N-3.1.3.3 命中率 | l2_hit | N-3.2.4.2 | 同一底层因素进两层 |
| N-3.2.4.2 命中率 | l2_hit | N-3.1.3.3 | 同一底层因素进两层 |

**同层因素 + share（正交判断的输入）**：

- L1: N-1 每小时持有成本(share=25) | N-2 有效利用率(share=25) | N-3 原始产出速率(share=25) | N-4 任务通过率(share=25) | N-5 可行域(share=?)
- L2: N-1.1 购置摊销(share=42.8) | N-1.2 电费(share=49.3) | N-1.3 故障损耗(share=8.0) | N-2.1 业务需求占空比(share=60) | N-2.2 调度效率(share=40) | N-3.1 时间(share=40.1) | N-3.2 时间(share=59.9) | N-5.1 显存容量门槛(share=?) | N-5.2 带宽准入下限(share=774) | N-5.3 缓存命中率(share=7.6)
- L3: N-1.1.1 卡价(share=55) | N-1.1.2 主机价(share=15) | N-1.1.3 残值率(share=10) | N-1.1.4 摊销小时数(share=20) | N-1.2.1 整机功耗(share=50) | N-1.2.2 电价(share=50) | N-1.3.1 三年故障概率(share=50) | N-1.3.2 卡价(share=?) | N-3.1.1 计算量(share=30) | N-3.1.2 峰值算力(share=25) | N-3.1.3 (share=45) | N-3.2.1 权重字节(share=25) | N-3.2.2 每流(share=20) | N-3.2.3 峰值带宽(share=25) | N-3.2.4 有效带宽系数(share=30)
- L4: N-3.1.3.1 占用率(share=?) | N-3.1.3.2 利用率(share=?) | N-3.1.3.3 命中率(share=?) | N-3.2.4.1 带宽利用率(share=?) | N-3.2.4.2 命中率(share=?) | N-3.2.4.3 (share=?)

**判断（Lead，2026-11-26）**：

- **SHARED 节点 ≠ 正交性违反**。正交性判据 = 解释维度不重叠（一个因素的敏感度不被算两次），不是"参数唯一"。两组 SHARED 都是**同一物理量经多条机制路径进入成本**：
  - `gpu_price`：购置摊销（资本路径 N-1.1）+ 故障更换（运营路径 N-1.3）——gold-tree §2 原文：真实弹性 0.275 = 两条路径叠加，比只看摊销高 17%。删任一路径 = 低估卡价敏感度，**共享是结构必需**。
  - `l2_hit`：MFU（N-3.1.3，命中率→计算效率）+ η_bw（N-3.2.4，命中率→HBM 流量）——gold-tree §2 原文：同一 L2 命中率同时作用于两条路径。同上，共享是物理现实。
  - **结论：3 个 SHARED 均判"共享底层因素"，非正交性不成立**（conf 0.8，依据 = gold-tree §2 弹性表 + 机制路径独立性）。
  - **真缺口**：SHARED 节点 share 在源里 = `.?`（未标定），两条路径的敏感度分配无法从树内读出 → 标 [开放]：缺 l2_hit 的 per-path 弹性标定实验。
- **同层同时变动检查**：N-1.1 摊销 vs N-1.2 电费 = 资本支出 vs 运营支出，采购决策与用电决策独立 → 正交（conf 0.7）。N-3.1 prefill vs N-3.2 decode = 同一 t_task 的两段，**share 40.1/59.9 随负载长度共变**（长 prompt → prefill 占比升）→ 非独立分解，是**条件分解**，判"可接受但需注明"：share 只对特定负载分布成立 [开放：缺 share 的负载分布标定]。
- **异常值**：N-5.2 share=774、N-5.3 share=7.6 —— 约束域节点带 share 不合"份额"语义，疑为标定常数误入 share 字段 → [待核验：gold-tree 源语义]，不影响 §4 完备结论。

## §3 最小检查（Lead 判断，2026-11-26）

判据：删该层后，c_pass 公式结构是否失去解释（下层参数无处安放或敏感度被合并丢失）。

- **N-1 成本 / N-2 利用率 / N-3 速率 / N-4 通过率**：c_pass = c_hour/(u·λ_raw·G_pass) 的四因子分子分母结构，删任一 → 公式退化为一团参数，敏感度分解消失。**必要**（conf 0.9，公式结构直接可读）。
- **N-5 可行域**：不进 c_pass 闭式（§4 反向清单证实），作用是**剪枝**（N-5.1 显存门 / N-5.2 带宽门 淘汰 5 配置，J3b 实证与价格无关）。删之 → 枚举空间爆炸 + 无淘汰判据。必要但性质不同：是约束层不是成本层（conf 0.8）。
- **N-1.x 三兄弟（摊销/电费/故障）**：删 N-1.3 → gpu_price 只剩资本路径，卡价弹性从 0.275 退回 ~0.235（gold-tree §2：17% 低估）。**必要**（conf 0.8）。
- **N-3.1/N-3.2（prefill/decode）**：删之 → t_task 变黑箱单参数，tf_peak 与 bw_peak 的敏感度无法分离（J3b 实证：tf_peak×0.5~×2 排名鲁棒性依赖这条分解）。**必要**（conf 0.9）。
- **N-3.1.3（MFU）/ N-3.2.4（η_bw）二层**：删 N-3.1.3 → mfu 变单常数，sm_occupancy/tensor_util/l2_hit 三条杠杆失去入口；删 N-3.2.4 → η_bw 变单常数，hbm_sol/l2_hit/launch_gap 失去入口。**必要**（conf 0.85）。
- **结论：5 层全部必要，无冗余层**。树的最小性 = c_pass 公式的因子结构 + 可行域剪枝，一一对应（conf 0.85）。~~N-5.3 与 l2_hit 语义重叠~~ **已排除（11-26 grep 核验）**：N-5.3 param=`cache_hit_rate`（前缀缓存命中率，nuisance）≠ N-3.2.4.2 param=`l2_hit`（L2 命中率），是两个不同参数，名称相近造成误判。

## §5 作用域（Lead 判断，2026-11-26，引 J3b 4 判据）

树的作用域 = c_pass 公式的作用域，四条边界（引 `j3b_generalization.py` L134-138 原文判据）：

1. **候选集依赖**：树的排名结论仅在给定候选集内成立（J3b：gold winner 3090×4 在候选集含 4090 时已被 T8b 证翻转；本表纳入 L40S/A100/H100 后 3090×4 仍成本最优，但对 tf_peak×0.5~×2 鲁棒）。**树本身是候选集无关的（参数分解结构），排名结论是候选集相关的**——claim 只到"分解结构"，不到"winner"（conf 0.9）。
2. **tf_peak 作用域**：t_prefill 占比 <30% 的负载下，排名对 tf_peak 不确定度不敏感 → 树中 N-3.1.2 的敏感度结论**只在该负载 regime 内有效**，长 prompt 负载需重标定（conf 0.8）。
3. **价格口径**：c_pass 随价格线性、排名对价格比稳健（J3b 判据 3）→ 树的价格敏感度结论对 ①/②/③ 类价格源**口径稳健**，但绝对 c_pass 值随口径变（T8c S1 实证：①类价 $975 下 winner 翻转，正是此判据的实例化）（conf 0.9）。
4. **芯片命名作用域**：gold 树 M2Ultra(bw560) ≠ KB m5-ultra(bw1200) ≠ doc M3/M5 Ultra → 树中消费级芯片节点**绑定特定 KB 口径**，跨源引用需先对齐命名（conf 0.7，命名混乱是已知坑）。

**明确不做**：质量提升 claim（树只分解成本，G_pass 是 nuisance 参数 N-4，不在树内建模）。
**综合**：树在"给定候选集 + 给定负载 regime + ①类价格 + KB 芯片口径"四重限定内完备（§4 无缺口）且最小（§3 无冗余层）；越出任一限定需重标定对应分支，不需重建整树（conf 0.8）。
