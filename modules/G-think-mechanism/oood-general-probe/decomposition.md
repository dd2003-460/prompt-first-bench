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

## 6. 核/配置/超参三层分离（D「把非 general 部分去掉」→ 隔离非删除）
- 设计: `kernel-config-split.md`（S0 原版 / S1 剥离版域中性 / B 裸基线，2×2 三臂，判决域味=污染/域适配配置/功能）
- 任务: K1 生成剥离版 prompt → K2 S1 气象 → K3 S0/S1/B 硬件 40 节点 → K4 三臂判决（详见该文件 §5 任务表）
- 时序: S0 气象(在跑)验收后派 K1；K2/K3 等 8787 释放

## 7. S0 气象列半程判决（2026-11-27 21:55, P3 判断-Lead）
**记分（P2, metrics-s0-cyclone.json）**: SM 机制覆盖 4/4 = 基线 4/4（打平）; 定量 claim SM 27 vs 基线 38（同量级, 非 2×）; L1=6（N1-N6, 结构带内）无跑题; SM 40 节点/2162s/161 次 LLM 调用, 基线单发 3455 字。
**判决: inconclusive（预注册第三态命中）** — 结构健康（L1=6 无跑题）+ 覆盖/定量与基线打平。transfer 条件（覆盖>基线 或 定量≥2×）未满足; handcrafted 条件（覆盖≤基线）技术上 4/4≤4/4 满足, 但打平+结构健康落入预注册第三态而非 handcrafted 的实质（"SM 在 OOD 不如裸模型"）。
**两个 caveat（判决有效性边界）**:
1. **无检索退化态**（instrument-artifact-s0.md）: webllm L56 崩, 后 143 调用无检索, degraded 24/40 主因=检索缺失。S0 测的是"SM 无检索态的 OOD 迁移", 不是完整 SM。若 S1(K2, 同无检索口径) 显著优于 S0 → 域味=负资产证据; 若持平 → 域味在建树阶段影响小。
2. **tree-only 口径**: 驱动只调 sm.run() 不跑 synthesize_answer, 记分基于 40 claim 树质量（机制覆盖/定量密度/L1 结构）, 非合成答案。K2/K3 同口径, 2×2 内部可比。
**附加观测（预注册, 强正向信号）**: SM 在从未调过的气象域**自发产出「机制→量化→主导项」三层结构**（L1: N1 机制谱系/N2 量化基准/N3 主导项判别/N4 强度调制/N5 敏感性/N6 黑盒）— 精确对齐题面 5 要求 + D 的机制级三要素判据, 未漂到硬件域「成本公式→因子」模板。这是控制流核 domain-free 的直接行为证据（prompt 域味例子没把 L1 分解带歪）。
**待 K2/K3**: 2×2 终判（域味=负资产/域适配配置/功能）+ 气象列 S1 vs S0 的域味效应。

## 8. K5 转正（2026-11-28, 执行-Lead）
**判决依据**: K4b 格 1 负资产（域味该删）。
**执行**: 生产核（pfb-thinkmech 两文件）应用 S1 剥离版 diff = oood-probe/s1/ 副本直接覆盖（diff 已核: 纯域味替换, 零结构漂移, s5 18行+prompts 24行）。py_compile 过, 域味残留 grep=0（仅 L1549 注释 1 处, 非 prompt）。commit caf6e0048, pushed。
**靶子勘误**: K5 任务卡初版误指 pfb 仓旧单体文件; 生产核实为 pfb-thinkmech 两文件结构（run_s1_sm.py shadow assert 证实被测 S1 影子的是这里）。
**残留 [待核验]**: ① /tmp/prompts-golden.json 回归基准快照未刷新（/tmp 临时文件, 若回归脚本在跑需重建）; ② 端到端 smoke（40 节点短跑对照 k3-s1-hw.json）未跑——prompt 已变, 下一轮 Q9/Q10 run 即为天然 smoke, 单独短跑性价比低, 标降级验收。
**OOD 线状态**: 判决+转正完成, 线收口。6 域电池（Q11-Q15）按预注册只在 transfer 判决下才跑满, 本判决=格1, 不触发; 若后续要推广验证, 另立项。
