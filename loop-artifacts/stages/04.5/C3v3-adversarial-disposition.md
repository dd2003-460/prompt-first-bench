# C3 v3 对抗核验回执 · 处置表（04.5 工件 · r59）

**goal**: T8-C3-v3-paired-runs 链 · **日期**: 2026-10-31 · **执行**: Hermes keepalive r59
**输入**: `receipts/c3-v3-adversarial-check.json`（arena 分支 5a525c7 检出，sha256=8001189a… 对账 byte-exact）
**总判定（arena）**: PASS-with-fixes —— 无根本缺陷；确认性开跑前 3 条 blocking fixes：① R4 样本量/分析单元/任务块模型 + 4 角点 estimand + G3 sham 门禁重写 ② R5 judge 身份/量尺/阈值/校准抽样冻结 ③ 机会集盲标仲裁冻结 + 空分母 + truth-cover 联合门槛 + 新旧 M8 口径版本化。

## 逐条处置（对照 R4 已执行事实 + r54 G1a backfill）

### R1 · C1 三道地板有效性（部分成立 / 中）→ 已覆盖
- arena 要求：C1 不恢复时不得称「R1 已校正 top-k」；n=4 Spearman 只作探索性警报。
- 现状核对：T8-prompt-ablation.md §R1 已写「双证据链独立收敛表述正式删除，C1 提供探索性候选」；r47 结论未做任何「R1 已校正」宣称；Spearman 结果（r=0.104, n=36）在 receipt-r4-execution.json 里定位为「不触发否决」而非「通过长度混淆检验」。
- 残余动作：零——现有文档措辞与 arena 要求一致，无需改动。若未来恢复 C1，按 required_fixes 三条执行（多 sham 文本 + d-d0 降为敏感性分析 + 预注册稳健性标准）。

### R4 · 功效/estimand/sham 门禁（成立 / 高）→ 部分覆盖
- arena 四条 required_fixes 逐项核：
  1. **F-sham 排除出 factorial 拟合** → ✓ 已达成。r47 主分析报的是 cell 级均值对比（B-nofreeze -0.35 配对差），未做 2³ 系数拟合，sham 单独作为阴性对照报告。
  2. **任务块聚类模型 + MDE 反推题数预注册** → ✗ 未覆盖。R4 实际 = 2 域 × 2 seed = 4 run/cell，从未预注册任务块固定/随机效应或 cluster-robust SE。等效缓解：r47 verdict 明确「描述层结论，推断层上限=方向性证据」——即 arena 说的「限为探索性/方向性」已被遵守，但缺书面预注册件。
  3. **4 角点 estimand 误称** → ✓ 已规避。r47 没有把 B-nofreeze−A-full 称为「freeze 平均主效应」，表述为「唯一稳定低于 A-full 的配置」+「与 freeze 贡献最大假设方向一致」（假设层面，非估计层面）。
  4. **G3 sham 等效性门禁重写** → N/A 于已执行轮。R4 未设 F-sham≈F111 的等效性门槛（这正是 arena 批评的原始设计）；v11 特异性指纹测试替代了原 G3 职能（sham 0.517 跌至第 2 低组即验收），逻辑上等价于「用 sham 检测评分器对空转的敏感度」而非「sham 必须等效 full」。
- 净缺口：**MDE/任务块模型预注册件缺失**。影响面：R4 全部数字只能作方向性证据（r47 已如此声明，故结论未被污染，只是「合规性文书」欠一份）。

### R5 · judge 校准可操作性（成立 / 高）→ 部分覆盖
- arena 四条 required_fixes 逐项核：
  1. **κ 分类对象 = 逐条核验机会 pass/fail（非 run 分数切 0.5）** → ✓ 已解决。G1 设计件 §3 二值化方案 = 条目级三测 pass/fail 聚合，G1a 实跑（d8c6eb2）按此执行；r54 backfill 的 n_items/pass 均为条目粒度。
  2. **CALM 阈值单位统一 + 长度相关统计量预注册** → ◐ 部分。CALM 扰动有实测记录（J1-CALM 零翻转）；长度相关 R4 补算了 pearson r=0.104（n=36）并预注册了「|r|≥0.7 否决」线（G1a receipt F4）。阈值是事后写入 receipt 而非事前冻结——登记为边界，不改历史。
  3. **异源 judge 身份开跑前实测冻结，不可用则停在 G2** → ✗ 未覆盖 = **G1b blocked-on-human**（queue L25 既有登记）。这是 arena 回执与当前状态的唯一硬阻塞重合点，非新发现。
  4. **校准集配置覆盖依据** → ◐ 部分。G1a 校准集 = A-full 双域 + X5 阳性 + sham 阴性（3 类工件），未覆盖 B-noowner/B-noevidence 等格式变体。G1a receipt 已声明「留 R4 B 组工件扩集重算」，R4 后 36 工件全量重打 J1/J2 事实上完成了扩集——但 κ 因天花板效应（po=1.0）仍不可计算，登记为数据局限非协议违规。
- 净缺口：同 G1b（异源 judge）。

### M8-truth/M8-cover · 机会集完整性（成立 / 高）→ **未覆盖（真缺口）**
- arena 要求四子项：① 机会集由谁定义 ② 何时冻结 ③ truth 空分母处理 ④ 新旧 M8 口径版本化。
- 现状核对：**四子项均无成文落盘**。修正 4（r50）写了「以任务输入预定义的核验机会集为分母」的原则，但从未落地为可执行协议。
- **对已执行 R4 的实际影响（本轮关键发现）**：R4 的 M8 分母 = 各 run 自身产出的核验条目数——正是修正 4 要消灭的可变分母。后果：B-noevidence 0.954 > A-full 0.781 的比较混淆了两个东西——(a) 每条核验的质量 (b) 核验条目的产出数量。删 evidence-url 组件后模型可能少产出核验条目（难项退出分母），truth 率被动抬高。r47「evidence 对 M8 判分无正向贡献」的表述因此需要限定语：**在未固定机会集前提下，该比较无法区分质量效应与分母收缩效应**。
- 受影响程度评估：freeze 负效应（B-nofreeze 0.400/-0.35）受此混淆影响较小——candidate-freeze 删除主要改变行为模式（是否冻结候选集）而非条目产出数量，且 B-nofreeze 是全场最低组（分母收缩只会抬高分，它仍最低说明质量效应真实存在的可能性高）。evidence/owner 方向的结论置信度相应下调。
- 处置：导出候选 goal `T8-C3-v3-opportunity-set-freeze`（见 receipts/c3v3-adversarial-receipt-r59.md 末节）。

### selection_validation_isolation · 选择-验证隔离（部分成立 / 中）→ 已覆盖
- arena 判定：两域限定内的探索/因果估计不被阻塞；第三域 hold-out 外推被阻塞。
- 现状核对：r47 结论上限声明 =「同族方向性证据 conf 降档」+「G1b 异源仍是升档唯一路径」；hold-out 域缺失已在 G1 设计件与 CONTINUE_MSG 阻塞项登记；无任何文档宣称跨域外推。✓

### C2_compensation_proxy · 补偿代理指标（低）→ 已覆盖
- arena 判定：保持描述性定位 + 完善编码文档即可，非 blocker。
- 现状核对：C2 指标（候选集漂移次数/URL 比例/owner 标注比例）在 runs-r4 receipt 中仅作描述性记录，未参与任何判读分支。✓

## 04.5 自检（反方视角）
1. **「已覆盖」判定是否过宽？** R4 第 2 条我判「等效达成但缺书面件」——arena 原文是「run_blocker: 是」，严格读法下 R4 数字不应被引用为任何结论基础。但 r47 引用时已带「描述层/方向性」限定，实质风险已控。保守处置：本次处置表不修改 r47 任何数字与结论，仅新增限定语候选（待 opportunity-set-freeze goal 落地后回填）。
2. **回执时效性**：arena 核验时 reviewed_head = 82ad8b6（r62 之前），当时 R4 尚未执行、G1a 未跑。本处置表是「事后对齐」——arena 的 required_fixes 针对的是当时的方案稿，部分 fix 已被后续执行自然满足。这个时间差本身登记为边界：若 arena 看到 R4 实际执行方式，可能对「cell 均值对比代替 factorial 拟合」给出不同评价（更宽松或更严均可能）。
3. **最弱环节**：机会集缺口是唯一「已执行数据受未落地协议影响」的项，其余五项要么已覆盖要么是外部阻塞（G1b）。优先级排序据此定。

## verdict
**pass-with-gap** —— 回执消费完毕，3 条 blocking fixes 中 2 条已被后续执行自然覆盖大半（残留 = 文书性预注册件），1 条是真缺口（机会集协议）且影响已量化定位到具体结论（evidence/owner 方向）。导出 1 个纯仓库内可执行候选 goal，不代裁、不动冻结件。