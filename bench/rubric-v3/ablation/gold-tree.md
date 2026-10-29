# 全树一页

31 个节点，主干深度 4，叶子 13 个。所有数字来自 [`../tasks/T0-local-27b/reference/calc.py`](../tasks/T0-local-27b/reference/calc.py)，赢家配置 3090×4 / W4 / n=2。

长出这棵树的过程见 [`L0`](L0-root.md) → [`L1`](L1.md) → [`L2`](L2.md) → [`L3`](L3.md) → [`L4`](L4.md) → [`L5`](L5-blackbox.md)。

---

```
N-0  每个通过任务的成本  c_pass [¢/task]                        SHARE 1.00   split
│    c_pass = c_hour / ( u × λ_raw × G_pass )
│
├─ N-1  每小时持有成本  c_hour [$/h]                            .25   split
│  │    c_hour = 摊销 + 电费 + 故障
│  ├─ N-1.1  购置摊销            42.8%                                split
│  │  │    = (卡价 + 主机价 − 卡价×残值率) / H
│  │  ├─ N-1.1.1  卡价          gpu_price    .55  B4  2.2x   leaf S-b  SHARED→N-1.3.2
│  │  ├─ N-1.1.2  主机价        host_price   .15            leaf S-a
│  │  ├─ N-1.1.3  残值率        resid        .10  B8        leaf S-b
│  │  └─ N-1.1.4  摊销小时数    H            .20  B8  2.02x leaf S-b
│  ├─ N-1.2  电费                49.3%                                split
│  │  │    = 整机功耗 × 电价
│  │  ├─ N-1.2.1  整机功耗      power_kw     .50            leaf S-a
│  │  └─ N-1.2.2  电价          elec         .50  B5  1.88x leaf S-b
│  └─ N-1.3  故障损耗             8.0%                       ★F-C    split
│     │    = 三年故障概率 × 卡价 / H
│     ├─ N-1.3.1  三年故障概率  p_fail       .50  B8        leaf S-b
│     └─ N-1.3.2  卡价          → N-1.1.1              SHARED
│
├─ N-2  有效利用率  u [—]                                      .25   split   ★F-B
│  │    u = 业务需求占空比 × 调度效率
│  ├─ N-2.1  业务需求占空比     duty_demand  .60  B6  8.00x leaf S-b  ■瓶颈#1
│  └─ N-2.2  调度效率           sched_eff    .40  B6        leaf S-b
│
├─ N-3  原始产出速率  λ_raw [task/h]                            .25   split
│  │    λ_raw = 3600 / t_task ;  t_task = t_prefill + t_decode/n
│  ├─ N-3.1  prefill 时间        40.1%                       ★F-A    split
│  │  │    = prefill_FLOPs / (卡数 × 峰值TFLOPS × MFU × tp_eff)
│  │  ├─ N-3.1.1  prefill 计算量 prefill_flops .30           leaf S-a  594 TFLOP
│  │  ├─ N-3.1.2  峰值算力       tf_peak       .25           leaf S-a
│  │  └─ N-3.1.3  MFU            mfu           .45  B2 1.20x leaf S-b
│  └─ N-3.2  decode 时间         59.9%                       ★F-A    split
│     │    = 输出tok × (W + n×KV) / (卡数 × 峰值BW × η_bw × tp_eff)
│     ├─ N-3.2.1  权重字节       w_bytes       .25           leaf S-a  14/27/54 GB
│     ├─ N-3.2.2  每流 KV 字节   kv_per_stream .20  B7 2.0x  leaf S-b  ★ 2倍分歧
│     ├─ N-3.2.3  峰值带宽       bw_peak       .25           leaf S-a
│     └─ N-3.2.4  有效带宽系数   eta_bw        .30  B3 1.43x leaf S-b
│     └─ (并发数 n  → 由 N-5 决定, S-c, SHARED)
│
├─ N-4  任务通过率  G_pass [—]        nuisance              .25  B1 1.57x  stopped S-b  ■瓶颈#2
│
└─ N-5  可行域  feasible_set          constraint            —          split
   ├─ N-5.1  显存容量门槛   n×KV + W ≤ 可用显存   → n_cap            leaf S-a
   ├─ N-5.2  带宽准入下限   W4 774 / W8 1034 / W16 1574 GB/s         leaf S-a
   │         → 划掉 M2Ultra(560) · L40S×1 · A100×1-W16 · 3090×2-W8/W16
   └─ N-5.3  缓存命中率     cache_hit_rate  nuisance  B8  7.6x       leaf S-b
```

**图例**　`.25` SHARE（对父节点的弹性份额）｜`2.2x` BOUND｜`B4` 黑盒编号（见 [`L5`](L5-blackbox.md)）｜`S-a/b/c` 停止依据（见 [`README`](README.md)）｜`★` 本次分解订正的地方

> **补充**：混合负载下效率大幅下降的发现见 [`L6-mixed-load.md`](L6-mixed-load.md)——并发扩展不是线性的，混合负载使实际吞吐远低于理论值，可能改变赢家排名。

---

## 三处 `SHARED`

| 参数 | 出现在 | 符号 | 后果 |
|---|---|---|---|
| `gpu_price` | `N-1.1.1`、`N-1.3.2` | 同号 | 真实弹性 0.275，比只看摊销高 17% |
| `quant` | `N-3.2.1`、`N-5.1`、`N-4` | **前两条降成本，第三条升成本** | W4 不是无条件最优；`ΔG > 0.08` 时输给 W8 |
| `n` 并发数 | `N-3.2`、`N-5.1`、`N-5.2` | — | 不是自由量，`n = min(n_speed, n_cap)`，S-c |

---

## OC-1 卡片格式（三个样例）

每个节点的完整 12 字段形式。字段定义见 [`../rubric/output-contract.md`](../rubric/output-contract.md)。

```
### N-0  每个通过任务的成本
PARENT:  -
NOW:     未知
GOAL:    ¢/task，前三名的区间不重叠
GAP:     缺「每小时多少钱」「几成小时在干活」「干活时每小时出几个」「出的里面几个算数」
IN:      候选硬件 8×3；27B 权重规格；token 画像 90:9:1 @64K
OUT:     c_pass
KIND:    signal
RES:     -
SHARE:   1.00
BOUND:   -
TEST:    跑 calc.py，对每个可行配置输出一个 ¢/task
STATUS:  split
```

```
### N-2.1  业务需求占空比
PARENT:  N-2
NOW:     未知，区间 [0.10, 0.80]
GOAL:    一个标量，±0.05
GAP:     没有任务日志
IN:      三个月的 GPU 任务排队记录
OUT:     duty_demand
KIND:    nuisance
RES:     时间
SHARE:   0.60
BOUND:   8.00x
TEST:    统计日志里 GPU 忙时 / 总时。1 小时
STATUS:  stopped:S-b   → 黑盒 B6   ■ 全题瓶颈第 1
```

```
### N-5.2  带宽准入下限
PARENT:  N-5
NOW:     W4 774 / W8 1034 / W16 1574 GB/s
GOAL:    对每个候选判 pass/fail
GAP:     -
IN:      候选的峰值带宽 × 卡数 × η_bw × tp_eff
OUT:     bw_ok
KIND:    constraint
RES:     显存带宽
SHARE:   -
BOUND:   -
TEST:    BW_eff ≥ 下限？M2Ultra 560 < 774 → fail
STATUS:  leaf:S-a
```

---

## 和旧版 `reference/tree-v0.md` 的关系

`../tasks/T0-local-27b/reference/tree-v0.md` 是这棵树的**上一版**，有三处已订正的错误
（prefill:decode 25:75、利用率埋在第三层、缺故障损耗节点），
并且用的是 19 个节点的旧编号。

**评分以本目录为准。** 旧文件保留，因为 `KIND-KEY` 和 `gold-numbers` 两节仍在被 rubric 的 S5 / C1 引用，
而且它是 F-A/F-B/F-C 这三处订正的「订正前」证据。
