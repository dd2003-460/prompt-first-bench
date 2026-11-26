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
    - **N-5.2** 带宽准入下限 `s` [leaf] share=4
    - **N-5.3** 缓存命中率 `B8` [leaf] share=8 B8
      - **N-1.1.1** 卡价 `gpu_price` [leaf] share=55 B4 SHARED→N-1.3.2
      - **N-1.1.2** 主机价 `host_price` [leaf] share=15
      - **N-1.1.3** 残值率 `resid` [leaf] share=10 B8
      - **N-1.1.4** 摊销小时数 `H` [leaf] share=20 B8
      - **N-1.2.1** 整机功耗 `power_kw` [leaf] share=50
      - **N-1.2.2** 电价 `elec` [leaf] share=50 B5
      - **N-1.3.1** 三年故障概率 `p_fail` [leaf] share=50 B8
      - **N-1.3.2** 卡价 [?] share=1.1
      - **N-3.1.1** 计算量 `prefill_flops` [leaf] share=30
      - **N-3.1.2** 峰值算力 `tf_peak` [leaf] share=25
      - **N-3.1.3**  `mfu` [split] share=45 B2
      - **N-3.2.1** 权重字节 `w_bytes` [leaf] share=25
      - **N-3.2.2** 每流 `kv_per_stream` [leaf] share=20 B7
      - **N-3.2.3** 峰值带宽 `bw_peak` [leaf] share=25
      - **N-3.2.4** 有效带宽系数 `eta_bw` [split] share=30 B3
        - **N-3.1.3.1** 占用率 `sm_occupancy` [leaf]
        - **N-3.1.3.2** 利用率 `tensor_util` [leaf]
        - **N-3.1.3.3** 命中率 `l2_hit` [leaf] share=2 SHARED→N-3.2.4.2
        - **N-3.2.4.1** 带宽利用率 `hbm_sol` [leaf]
        - **N-3.2.4.2** 命中率 `l2_hit` [leaf] share=2 SHARED→N-3.1.3.3
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
- L2: N-1.1 购置摊销(share=42.8) | N-1.2 电费(share=49.3) | N-1.3 故障损耗(share=8.0) | N-2.1 业务需求占空比(share=60) | N-2.2 调度效率(share=40) | N-3.1 时间(share=40.1) | N-3.2 时间(share=59.9) | N-5.1 显存容量门槛(share=?) | N-5.2 带宽准入下限(share=4) | N-5.3 缓存命中率(share=8)
- L3: N-1.1.1 卡价(share=55) | N-1.1.2 主机价(share=15) | N-1.1.3 残值率(share=10) | N-1.1.4 摊销小时数(share=20) | N-1.2.1 整机功耗(share=50) | N-1.2.2 电价(share=50) | N-1.3.1 三年故障概率(share=50) | N-1.3.2 卡价(share=1.1) | N-3.1.1 计算量(share=30) | N-3.1.2 峰值算力(share=25) | N-3.1.3 (share=45) | N-3.2.1 权重字节(share=25) | N-3.2.2 每流(share=20) | N-3.2.3 峰值带宽(share=25) | N-3.2.4 有效带宽系数(share=30)
- L4: N-3.1.3.1 占用率(share=?) | N-3.1.3.2 利用率(share=?) | N-3.1.3.3 命中率(share=2) | N-3.2.4.1 带宽利用率(share=?) | N-3.2.4.2 命中率(share=2) | N-3.2.4.3 (share=?)

**判断（Lead 填）**：
- [ ] 每个 SHARED 节点是否构成真正的非正交？（共享底层因素 vs 独立分解）
- [ ] 同层两因素是否会同时变动？（如 N-1.1 摊销 vs N-1.2 电费：资本 vs 运营，独立？）
- 证不出 = 标 [开放] + 缺什么

## §3 最小检查（Lead 判断）

- [ ] 逐层：删该层后下层是否失去压缩（用 c_pass 公式结构论证）
- 示例：删 N-3(λ_raw) → t_task 失去 prefill/decode 分解 → decode 时间项失去解释

## §5 作用域（Lead 判断，引 J3b 4 判据）

- [ ] 候选集依赖 / tf_peak 作用域 / 价格口径 / 芯片命名（引 j3b_generalization.py 4 判据段）
- 不做质量提升 claim
