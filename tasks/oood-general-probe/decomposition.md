# OOD-GENERAL-PROBE — 状态机核的 general 性最小探针
> 起源: D 2026-11-27 20:20 质疑「prompt 不 general，没认真想过什么是 general / 怎么到 AGI」。
> 结论锚点（本轮已坐实，来源=代码直读）: ① SM 控制流核（State+run 主循环）结构上 domain-free（判据=max_nodes/max_depth/marginal_gain/contribution_threshold/contradiction_scan，无域字样）② 生产 prompt 声称通用（P1_L1_SKELETON L33 / P1H_INDEX L308,L320「对所有题目类型成立」）但嵌域味例子（P1_DECOMPOSE L66-67 写死 TCO/吞吐展开）③ questions/ 目录 Q1-Q5/Q9/T53 全属研究/硬件/AI 域族 → SM 从未在结构不同域测过 → "SM 有效"是域内胜任证据，不是 general 证据。
> 本探针 = 最短决定性路径: 同核（生产 prompt 一字不改）× 一个从未调过的域（气象物理·因果解释结构，非对比/优化结构）× 裸 27b 单发对照。

## 1. 分解树（正交子项）
**S1 不变核定义**（done，本轮 Lead 直读代码）: 核 = 控制流（State 枚举+run 循环+停止/剪枝/矛盾判据）+ 生产 prompt（P1_L1_SKELETON/P1H_INDEX/verify 系）+ 检索通道。域可变件 = 题面 + gold/judge 知识。conf 0.9
**S2 探针域选择**: 判据 = 结构不同（因果解释 vs 对比/优化）+ 域不同（气象物理 vs AI/硬件）+ 有可验证数值（衰减率 kt/hr）。选定: 热带气旋登陆后减弱机制。已知机制清单（gold，气象学教科书级稳定事实）: 地表摩擦 / 海气热湿通量(能量源)丧失 / 垂直风切变 / 流出阻塞。conf 0.85
**S3 双臂实验**: 臂 A = 生产 SM（max_nodes=40, max_depth=4，prompt 零改动）; 臂 B = 裸 27b 单发（同题，直接作答，无分解无核验）。conf 0.9
**S4 指标（机器可抽）**: L1 维度数 / 机制覆盖(4 选几) / 定量 claim 数(数值+单位 regex) / LLM 调用数 / wall time / L1 漂移（是否跑题到无关域）。conf 0.9
**S5 判决（预注册，见 §3）**: transfer / handcrafted / inconclusive 三态，跑前定死。conf 0.9

## 2. 正交性核对
| 对 | 重叠度 | 依据 |
|---|---|---|
| S1×S3 | <30% | S1 定义被测物，S3 只消费 |
| S2×S4 | 30-50% | gold 机制清单同时是题面(S2)和判分(S4)的输入，共享度量 |
| 其余 | <30% | S5 纯下游判决 |
结论: 无 >50%; S1/S2 done，S3+S4 一个 sub 串行干完（脚本落盘模式）。

## 3. 预注册判决判据（跑前定死，防事后合理化）
- **transfer（核是 general 的证据）**: SM 机制覆盖 ≥3/4 且（SM 机制覆盖 > 裸基线 或 SM 定量 claim 数 ≥2× 裸基线）且 L1 维度 3-7 无跑题
- **handcrafted（核不 general 的证据）**: SM 机制覆盖 ≤ 裸基线，或 L1 跑题到无关域（类比硬件域 34% drift），或树结构破（L1<3 或 >7）
- **inconclusive**: SM 结构健康但覆盖/定量与基线打平 → 需第二域（扩成迁移电池）再判
- 附加观测（不判决，只记录）: SM 在因果解释结构上是否自发产出"机制→量化→主导项"三层（对应 D 的机制级三要素判据）

## 4. 任务表
| 任务 | 依赖 | 读(行) | 写(行) | commits | 载体 |
|---|---|---|---|---|---|
| P1 双臂驱动脚本+跑（SM 后台+裸基线） | — | ~80（SM 入口+cfg+题面） | ~120（两脚本，write_file 落盘） | 1 | sub-27b（sa-0-dd003644 在跑） |
| P2 指标抽取+对照结论 | P1 | ~60（两臂产物 JSON/txt） | ~40（metrics.json+1 行结论） | 1 | sub-27b |
| P3 判决+登记 | P2 | ~30（metrics.json+本文件 §3） | ~20（decomposition 判决节） | 1 | 判断-Lead |
| P4 C/E 计算匹配对照臂（BoN N=SM调用数 / GenericMultiStep token 匹配） | P1（需 SM 实际调用数/token 定预算） | ~40（sm-arm.json rounds_log） | ~80（两臂脚本） | 1 | sub-27b |
| P5 电池 D2-D6 域跑（Q11-Q15 题面已备） | P3 判决=transfer 才跑满；=handcrafted 则先重设计核 | 每域~60 | 每域~40 | 2-3 | sub-27b 分批 |
| P6 迁移 gap 分布+四必要条件终判 | P4+P5 | ~80（全域 metrics） | ~30（终判节） | 1 | 判断-Lead |

## 5. 边界
- 生产 prompt / SM 源码零改动（改了就不是测生产核）
- 不碰在跑的 run_q9_gated.py（PID 95936）及其 checkpoints
- 8787 与 gated run 共享（max-num-seqs=8），直接跑不排队
- SM 预算硬顶 max_nodes=40；>40min 停报部分结果
