# 阶段 02：信息调研 — RV3G6-o3-claim-list

> goal: O3 gold 节点转原子 claim 清单 · 分支 ralph/rv3g6-o3-claim-list · 2026-10-30
> 任务：为 31 个 gold 节点收集「该节点声称的实质内容」的三源证据（gold-tree 本体 / judge reason / run evidence），校准 claim 措辞；机算映射一致性基线候选值

## 0. web-llm 交叉询问回执（强制步骤）

`ralph prompt-first web-llm . "..." --context "阶段 02"` 已执行，回执 `loop-artifacts/prompt-first/02-web-llm-cross-check.md`（2026-10-30T00:29Z）：**三 provider 全失败**（perplexity-review: login or UI changed / chatgpt-review: sign in manually / gemini-review: 同）。与 AUDIT-report 附录 B、batch1 记录一致（登录过期状态延续）。外部文献线索 unverified——本 goal 为纯仓库内工作，不阻塞。

## 1. 三源证据盘点（31 节点全覆盖）

### 1.1 源 A：gold-tree.md 本体（ablation/gold-tree.md L10-57）

每节点的「实质内容」= 该行的量名 + 公式行 + SHARE/BOUND/KIND 标注。关键结构性事实：
- **SHARED 参数 ×3**（L65-71 表）：`gpu_price`（N-1.1.1 ≡ N-1.3.2）、`quant`（N-3.2.1/N-5.1/N-4 三处符号相反后果）、`n` 并发数（N-3.2/N-5.1/N-5.2，非自由量 n=min(n_speed,n_cap)）
- **★订正 ×3**：F-A（N-3.1/N-3.2 prefill-decode 占比订正）、F-B（N-2 利用率位置订正）、F-C（N-1.3 故障损耗补入）
- **■瓶颈 ×2**：N-2.1（占空比，8x BOUND）、N-4（通过率，1.57x）
- 叶子 13 个 / split 18 个；主干深度 4

### 1.2 源 B：prior-estimates.json nodes.*.reason（judge 视角「这一刀是什么」）

31 条 reason 全部提取（见 §1.4 对照表）。用途：(a) 验证 claim 草案与 judge 对节点的理解一致；(b) reason 中的「冷门/直观」判断是 p̃ 依据，**不得**写入 claim（claim 只写可判内容，不写稀有度评价——防 R1 泄漏）。

### 1.3 源 C：hit-matrix.json h=1 evidence（run 实际怎么写）

聚合结果（h=1 cell 共 98/248 = 39.5%；逐节点分布见 §1.4）：
- 高频命中（≥5 hit）：N-1.1(8) / N-1.2(7) / N-1.2.1(7) / N-1.1.4(7) / N-3.2.1(6) / N-3.2.2(6) / N-3.2.3(8) / N-5.3(8) / N-0(6) / N-5(5) / N-5.1(5)
- 零命中节点（8 run 全 h=0，共 13 个）：N-1 / N-1.1.2 / N-1.1.3 / N-1.3 / N-1.3.1 / N-1.3.2 / N-2 / N-2.1 / N-2.2 / N-3.1.1 / N-3.1.3 / N-5.2 —— 其中 gold strict 5 节点中 N-2.1/N-2/N-1.3 三个零命中
- **evidence 措辞规律**（claim 校准核心输入）：
  - 同一节点跨 run 表述差异大但语义稳定（N-3.2.2：「粗估 1.5–6 GB」/「KV cache 64K≈8GB」/「~200-400MB/流」→ 共同实质 = 「给出每流 KV 字节数的估算/区间」，无 run 用节点 ID 表述）
  - 数值从不逐字匹配 gold（gold 说 14/27/54 GB，run 写 13.5/14/18 GB）→ **claim 若写死数值则 8/8 run 全 miss，重演 #13**
  - 方向错误实例：run1/run6/run7 把自家树的 N-1.3 写成「通过率倒数 1/P」（实为 gold N-4 的内容），gold N-1.3（故障损耗）被漏 → 证明「ID 对得上」判据在 run 自带编号体系下会系统性错配（run 的 N-x.y 编号 ≠ gold 编号，只是巧合相似）

### 1.4 逐节点三源对照表（claim 起草底稿）

格式：node | gold-tree 实质内容 | reason 要点 | h=1 evidence 模式 | claim 草稿方向

| node | gold 实质 | reason 要点 | evidence 模式 | claim 方向 |
|------|-----------|-------------|---------------|------------|
| N-0 | c_pass=c_hour/(u·λ_raw·G_pass)，¢/task | 根节点中性 | 6 hit：「每任务总成本/花多少钱」+ 乘除结构 | 产出以每（通过）任务成本为目标量并给出含成本率×耗时÷通过率的分解结构 |
| N-1 | c_hour=摊销+电费+故障 | 少见拆法 | 0 hit | 小时持有成本被拆为购置摊销+电费+故障损耗三项之和 |
| N-1.1 | 购置摊销=(卡价+主机价−残值)/H，42.8% | 常见但常被省略 | 8 hit：折旧/摊销 $/hr | 硬件购置成本按寿命摊销进小时成本（一次性支出折成每小时） |
| N-1.1.1 | gpu_price，B4 黑盒 2.2x | 直观易提 | 4 hit：具体卡价 | 给出候选卡的购置价格（或明确标为待取数的黑盒+获取路径） |
| N-1.1.2 | host_price 单独拆出 | 少见，常合并整机 | 0 hit | 主机/机箱价格从卡价中单独列出（而非合并为整机价） |
| N-1.1.3 | resid 残值率，B8 | 需生命周期视角 | 0 hit | 显式引入残值率（卡报废时的剩余价值）修正摊销基数 |
| N-1.1.4 | H 摊销小时数，B8 2.02x | 较专业 | 7 hit：3 年/8000hr | 给出摊销年限或等效小时数（而非只写「折旧」一词） |
| N-1.2 | 电费=功耗×电价，49.3% | 常见 TCO 项 | 7 hit：功耗×时长×电价 | 电费作为独立成本支建模（功耗×电价的乘积结构） |
| N-1.2.1 | power_kw 整机功耗 | 显著规格 | 7 hit：350W 等 | 给出整机/满载功耗数值或区间 |
| N-1.2.2 | elec 电价，B5 1.88x | 常被假设固定 | 3 hit：$0.1/kWh | 显式设定电价取值（含单位），而非隐含在数字里 |
| N-1.3 | 故障损耗=三年故障概率×卡价/H，8.0%，★F-C | 冷门首层拆分 | 0 hit | 硬件故障导致的损失被纳入小时成本（可靠性/故障率项） |
| N-1.3.1 | p_fail 三年故障概率，B8 | 极冷门 | 0 hit | 给出（或标为待测的）多周期硬件故障概率估计 |
| N-1.3.2 | 卡价 SHARED→N-1.1.1 | 共享参数建模 | 0 hit | 故障损耗项引用的卡价与摊销项为同一参数（显式复用，非重复取数） |
| N-2 | u=占空比×调度效率，★F-B | 常被忽略 | 0 hit | 有效利用率作为吞吐的独立因子进入成本公式（而非隐含在实测吞吐里） |
| N-2.1 | duty_demand，B6 8x，■瓶颈#1 | 极不直观 | 0 hit | 利用率进一步拆出业务需求占空比（需求侧，需日志测量）并识别其高敏感度 |
| N-2.2 | sched_eff 调度效率 | 较少出现 | 0 hit | 利用率拆出调度效率子因子（供给侧，区别于需求占空比） |
| N-3 | λ_raw=3600/t_task，t=t_prefill+t_decode/n | 常见主支 | 1 hit | 原始产出速率按单任务耗时倒数建模，且耗时拆 prefill+decode 两段 |
| N-3.1 | prefill 时间，40.1%，★F-A | 常被略过 | 4 hit | prefill 阶段时间被单独建模（计算量/算力结构，非与 decode 混为一谈） |
| N-3.1.1 | prefill_flops 精确 FLOPs | 不如 token 数直观 | 0 hit | prefill 计算量以 FLOPs 形式量化（而非只给时间或 token 数） |
| N-3.1.2 | tf_peak 峰值算力 | 易从规格表引入 | 1 hit：35.6 TFLOPS | 引入候选卡的峰值算力规格参与 prefill 时间估算 |
| N-3.1.3 | mfu，B2 1.20x | 专业指标 | 0 hit | 引入 MFU（模型算力利用率）折扣峰值算力，而非直接用峰值 |
| N-3.2 | decode 时间，59.9%，★F-A | 很容易想到 | 4 hit | decode 阶段时间被单独建模为带宽受限过程（输出字节/有效带宽结构） |
| N-3.2.1 | w_bytes 14/27/54GB，quant SHARED | 明显因素 | 6 hit：13.5/14/18GB | 按精度位宽给出权重字节数（量化位数→GB 的换算关系） |
| N-3.2.2 | kv_per_stream，B7 2x，★2倍分歧 | 细粒度不直观 | 6 hit：8GB vs 200-500MB/流 | 给出每并发流的 KV cache 字节数估算（区分总量口径与每流口径） |
| N-3.2.3 | bw_peak 峰值带宽 | 显眼规格 | 8 hit：936/1555/7.2TB/s | 引入候选卡峰值显存带宽规格参与 decode 时间估算 |
| N-3.2.4 | eta_bw 有效带宽系数，B3 1.43x | 通常不自发 | 4 hit：3-5 折/0.6-0.9× | 区分峰值带宽与有效带宽（引入 TP/实现损耗系数打折） |
| N-4 | G_pass nuisance，B1 1.57x，■瓶颈#2 | 常被漏掉 | 4 hit：p 0.5-0.95 ÷p | 任务通过率作为成本放大因子进入公式（有效成本÷通过率，而非假设全通过） |
| N-5 | feasible_set constraint | 常见约束结构 | 5 hit：淘汰/不进 OBJ | 存在可行性过滤层：不满足硬约束的候选被淘汰、不进入成本优化 |
| N-5.1 | n×KV+W≤可用显存→n_cap | 直观容量约束 | 5 hit：权重+KV≤显存 | 显存容量门槛被用作并发数上限（权重+KV 总和 ≤ 可用显存的判定） |
| N-5.2 | 带宽准入下限 W4 774/W8 1034/W16 1574 GB/s | 较专门 | 0 hit | 按精度推导最低带宽准入阈值并据此显式淘汰候选（如低带宽单机出局） |
| N-5.3 | cache_hit_rate nuisance，B8 7.6x | 很少见 | 8 hit：90:9:1/57.6K | 前缀缓存命中率被单列为影响速率的参数（含敏感性/nuisance 标注） |

**NA 档检查结果（J3）**：31 节点全部能写出可二值 claim，**零 NA**。最接近 NA 的是 N-1.3.2（SHARED 引用节点）——按 R4 缓解展开为完整陈述（「故障项与摊销项引用同一卡价参数」）后仍可二值判。

## 2. 映射一致性指标——冻结数据基线候选值（机算）

脚本：`bench/rubric-v3/ablation/scripts/assert-o3-claim-list.py`（本 goal 新增，§04 执行时落盘）

**口径 M1（主口径，降级代理）**：claim 级重判 unverified（无 fresh-context judge），用 hit-matrix h 值做**节点级一致率**作为下界代理：
- 定义：consistency_M1 = |{ (run, node) : h_claim(run,node) == h_id(run,node) }| / |{(run,node)}|
- 当前唯一可算实例：h_claim := h_id（claim 判据尚未被执行）→ consistency_M1 = 248/248 = 1.000（**恒等基线，非有效性证据**——它只说明两判据在同一份数据上同义，任何后续独立 claim 重判与此 1.000 的偏离量才是指标的实际读数）
- 口径声明（强制随指标一起报出）：M1 在 claim 判据首次独立执行前恒等于 1.0；其价值在于为未来重判提供锚点与分母定义

**口径 M2（辅助口径，run 级聚合）**：per-run hit 向量完全一致的 run 比例。同样在当前数据上 = 8/8（恒等），作用同上。

**gold strict 子集切片**（5 节点 × 8 run = 40 cell）：h=1 共 10 cell（N-3.2.2×6 + N-4×4 + N-2.1×0 + N-2×0 + N-1.3×0）——零命中的 3 个 gold 节点正是 claim 判据最需要检验的方向（漏判是否因「没出现 ID 字样」造成），导出 queue 补数。

## 3. DRAFT v2 修订对象定位

- 修订行：DRAFT-rubric-v3-v2.md **L71**「命中判据不变：judge 拿产出逐节点对照 gold tree.md，节点 ID 对得上且通过正确性/相关性/必要关系核验才算 h_v=1」
- 替换为：引用 o3-claim-list.md 的 claim 级判据（judge 判产出是否包含各节点 claim 的实质内容，≥2/3 独立判者一致，h_v=1）
- 不动：L66 权重公式（h_v 符号保留）/ L73 状态声明（gmr 相关）/ L75-77 宣称前置条件（R-06 已落地）
- revision-log-batch1.md 追加条目：R-13 提前落地登记（原属 batch2，范围切割理由 = 本 goal 只交付判据件，DRAFT 仅改一行判据引用）

## 4. 未解决空缺

| # | 空缺 | 影响 | 处置 |
|---|------|------|------|
| U1 | claim 级独立重判（fresh-context judge 盲读 run 原文按 claim 判 h） | M1/M2 基线只能是恒等值，指标无实际读数 | unverified，导出 queue（与 RV3G1-semantic-rejudge 同通道，样本可扩到 31×8 全 cell） |
| U2 | claim 措辞人工审定 | 31 条 claim 为 runner 起草，最终措辞属人工决策 | APPROVALS.md 登记，不阻塞落盘 |
| U3 | web-llm 外部文献线索 | 业界 practice 命名（CheckEval/claim-grounding 类）unverified | 不阻塞（AUDIT §4 差异表已有 CheckEval 引用，本 goal 不新增外部主张） |

## verdict

**pass** — 31 节点三源证据齐全（§1.4 全覆盖，零 NA）；evidence 措辞规律直接支撑 claim 设计原则（不写死数值/写机制不写 ID/方向内嵌）；映射一致性双口径定义 + 恒等基线 + 强制口径声明齐备；DRAFT 修订对象精确定位到行。web-llm 三 provider 失败如实记录（§0），U1-U3 空缺全部登记不伪装。进入 02.5。