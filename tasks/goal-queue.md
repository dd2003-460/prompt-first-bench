# origin: ai — Goal 队列（ralph loop 消费）

> 格式：`- [ ] <goal 短名> | <一句话目标> | <产投比依据>`。完成改 `[x]` + 日期。新导出的候选追加到底部。

## 待办

- [ ] RUBRIC-V3-FULL-AUDIT | rubric-v3 完整消融推进+矛盾/漏洞/优化审计（G1-G6 六子goal，研究级长任务）| 任务书 tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md；队首优先——决定 rubric-v3 能否定稿，含真正的方法论判断（构念效度根因），非 trivial 修补。runner 按 G1→G6 顺序拆子 goal 逐个走 1-loop，每个子 goal 独立收口 merge main 后取下一个。**进度：G1 完成 (2026-10-30, ralph/rubric-v3-audit-g1) — loop 工件补齐 + 矛盾清单 C1-C4 落盘 bench/rubric-v3/ablation/G1-contradiction-audit.md（C1 ρ_orig=0.456 弱相关 / C2 三二项式红旗 N-1,N-1.1,N-5.3 / C3 零命中高p̃清单 / C4 W3结论对p̃来源敏感 3/5↔1/5）；形式一致率 35/35=100%（h=1方向），语义级独立重判 unverified（禁subagent，arena 通道可复用已落盘 75 样本清单补数）。G2 完成 (2026-10-30, ralph/rubric-v3-audit-g2) — 根因=双源 p̃ 偏差(共同零命中高估+新 judge 保守下界)+判据极严(P≥3 基线 1.99%)；公式层排除；三选项 O1/O2/O3 落盘 bench/rubric-v3/ablation/g2-rootcause.md。G3 完成 (2026-10-30, ralph/rubric-v3-audit-g3) — stats-w3w4.json JSON 层验证链闭合复验（W3/W4 分数 8/8+8/8、ρ 7/7、tie 4/4、top-5 strict 计数全通过；修正任务书「未走完验证链」表述，真实缺口=独立 judge 维度）；敏感性分级 W3 高（gold 3/5↔1/5 翻转）/ W4 排序中·构念效度高（gold 平均排名 6.4→8.6 与 W3 同幅）→ W3/W4 都不单独值得救；决策矩阵：O1 推荐子选项=gold 平均排名口径（唯一全部 7 方案×judge 组合方向一致），O2 外部阻塞本轮不可执行，O3 可行（代价重估=校准损失为主）；推荐路径供 G6 定稿非决策，交付物 bench/rubric-v3/ablation/g3-w3w4-completion.md。G4 完成 (2026-10-30, ralph/rubric-v3-audit-g4) — gap-analysis Q2 五条结构性解释逐条判定：S1 构念错配=部分规避（未到期，第二格/T17 本仓缺席；02.5 Q1 从「已规避」降级）/ S2 唯一 gold 路径偏置=**未规避**（单源 gold + §4 补丁与 gold 答案同构 + O2 条款砍掉抗同源出口 → 系统性偏置来源，前序全部 top-5 分析均为「相对 Lead-gold」）/ S3 可靠性成本=部分规避（降档：DRAFT ≥3 LLM 盲生成 p̃ 协议 vs 实际单 judge 自评，κ 门禁无回执）/ S4 可比性=部分规避（子项分裂：版本依赖已管控、跨域无机制）/ S5 surprisal=部分规避（强度不足：三重事前防护被实证穿透 ρ=0.688 / |Δw2|≥2 共 7 节点 / top-5 翻转）；负面结果三条（「S1 已规避」「paper 协议=受控」「blindtest=独立校验」均推翻或限定）；三种「部分」结构对应 G5 三类优化动作（强制机械化/补覆盖/加固阈值）；G6 硬约束=S2 未闭环前 O3 数字必须声明「相对 Lead-gold」+ adversarial-check 28 findings（9 blocker）需处置表；交付物 bench/rubric-v3/ablation/g4-vulnerability-crosscheck.md。下一步 G5（机械化/并行化机会清单 + 成本估算）**
- [ ] R5.2-third-scorer | 第三打分器（不同模型家族）用 packet v2 盲打 r4 三 run，κ 从 2-rater 升到 Fleiss'κ | R5.2 已交付 packet v2（输入对称断言通过），本 goal 直接消费；需 arena 通道或第三个本地模型，产投比中但依赖外部
- [x] T8-matrix-run-r1 (2026-10-30, r101: M8=1.00 团队文件协作/网盘选型域) | 按 tasks/T8-matrix-run-r1.md 任务书执行矩阵 run | 任务书已 push，产投比中

## 已完成

- [x] R5.2-evidence-packet (2026-10-30, r102: baff4b3) — 模板 v2 + packet v2（run1 M2=24/run2 M2=25/run3 null~45；M5 轮数 1/1/2 全带 basis）+ 对称性断言 67/0 exit 0；X2 错配登记（原 packet "run3 任务书25行"张冠李戴）
- [x] R5.2-packet-audit (2026-10-30, r103) — 原 v1 packet 单行摘要 12+1 原子断言全字段审计：8 confirmed / 3 mismatch / 1 unverified；新登记 X4(run1"无降级"vs degraded[3])/X5(14m27s unverified)/X6(step2"49/25/25"双错配，分值结论不变仅理由文本错→APPROVALS 条目 3)/X7("M1-M6定义+"空承诺)；机判脚本 assert-packet-audit.py 16/0/2 exit 0；未改任何冻结分
- [x] R5.2-sourcepath-hardening (2026-10-30, r104) — W1 收口：assert-packet-symmetry.py 删 basename glob 兜底（严格模式：全部 token base join 命中才 PASS + EXEMPT 显式豁免预留）；packet v2 十条 source_path 规范化为完整相对路径（字段值零改动）；重跑 67/0 exit 0 基线维持；模板 v2 补填写规则
- [x] R5.2audit-C12-mechanize (2026-10-30, r105) — C12 "M1-M6 定义+" 形式性检查由 SKIP(manual) 改机判信号输出（声称子串 + 正文正则，只扫 evidence_packet 字段；signal-only、verdict 归类留人工）；重跑 16 PASS / 0 FAIL / 1 SKIP + 1 SIGNAL exit 0；审计表 C12 行补机判引用；未改任何 verdict 与冻结分

## 新导出候选

- [x] R5.2hard-EXEMPT-sentinel (2026-10-30, r106: 6fbd47b) — EXEMPT 非空哨兵警告落地, SELF-TEST 假豁免验证触发, 67/0 exit 0 基线维持
- [ ] R5.2audit-C4-timing-reconstruct | C4 "14m27s" 数值化机判：解析 $WS/run2/loop-state.json channel 时间戳做差值重建耗时区间，与 14m27s 比对输出 SIGNAL（若转录件无逐事件时间戳则降级为"不可重建"信号并登记 X5 状态更新） | R5.2-audit 02.5 A4 导出：C4 属数值计算而非字符串比对，超出 C12 goal 边界；工作量小
- [ ] R5.2audit-signal-counter | assert-packet-audit.py 汇总行 "+ 1 SIGNAL(C12)" 硬编码改为 signal 计数变量（防未来加第二个 signal 时汇总行撒谎） | R5.2c12 04.5 R6/W1 登记，工作量极小
- [ ] RV3G1-semantic-rejudge | G1 语义级独立重判补数：用 arena 通道对已落盘 75 样本 cell（bench/rubric-v3/ablation/scripts/g1-sample-cells.json）做 fresh-context 盲重判 h，报语义一致率（覆盖 S1 未覆盖的 h=0 漏判方向），回填 G1-contradiction-audit.md §1 | G1 04.5 W1/R4 导出：工具纪律禁 subagent 导致降级交付，样本清单已就绪可直接复用；需 arena 会话通道
- [ ] RV3G3-goldrank-threshold-proof | G3 遗留：gold 平均排名口径的过线阈值正式论证（超几何 n=31,k=5 参考值 E[X]≈1.61 / P(≥4)≈2.7% 只是锚点）+ top-10 口径同级备选地位的终裁材料，供 G6 定稿 O1 时消费 | G3 04.5 W6 导出：本 goal 只给参考值不定稿论证；工作量小，纯仓库内推导
- [ ] RV3G4-prior-source-assert | G4 强制机械化候选落地：assert 脚本校验 prior-estimates.json 必须记录 ≥N 个独立 p̃ 生成源（source 字段缺失/单源 = FAIL），参考 R5.2 系列 assert-* 模式（signal-only 或 verdict 二选一在 01 定）| G4 交付物「给 G5 的导出」第一类 + S3 降档教训（纸面协议零防护力直到被执行）；工作量小，纯仓库内
- [ ] RV3G4-kappa-receipt-assert | G4 强制机械化候选落地：评分文件缺 κ 门禁执行回执 = FAIL 的断言脚本（回执格式定义 + 存在性检查），消除 R3「κ 门禁 unverified」状态 | G4 交付物「给 G5 的导出」第一类；工作量小，纯仓库内
