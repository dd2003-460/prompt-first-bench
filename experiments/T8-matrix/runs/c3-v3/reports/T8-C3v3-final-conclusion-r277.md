# T8-C3-v3 最终结论报告（收口版 · r277）

> origin: ai (r277 keepalive 立项 t8-c3v3-closeout-r277) · 2026-11-03
> 性质：**描述层收口**——合并 R4/R5/R6 + fullloop pilot 四轮证据，给出当前资源下可支撑的最终结论。
> conf 标注：同源 judge（qwen3.8-27b 既生成又裁判，G1b family_check PARTIAL-CLOSED）→ 全报告 conf-0.1；fullloop 部分另叠加降级通道 conf-0.2。

## 1. 实验对象与矩阵

测 3 个 prompt 组件（candidate-freeze / owner-tag / evidence-url）对 M8（核验真实性率：AI 裁判逐条判"主张是否真实可核验"的加权通过率）的因果贡献。9 配置（A-full 完整 / 单删×3 / 双删×3 / B-none 全删 / B-sham 等长中性填充对照）× 3 域（D1-meeting-room 开放选型 / D2-file-collab 开放选型 / D3-hardware-purchase 规格密集）× ≥2 seed。

| 轮次 | 范围 | 工件深度 | 状态 |
|------|------|---------|------|
| R4 | 9 cfg × D1/D2 × 2 seed = 36 run | 阶段 01+02 | receipt-r4-mainanalysis.json |
| R5 | 9 cfg × D3 × 2 seed = 18 run | 阶段 01+02 | receipt-r5-mainanalysis.json |
| R6 | G2 补全（R4+R5 合并主分析 54 run） | 阶段 01+02 | receipt-r6-mainanalysis.json + adjudication-final |
| fullloop | 3 cfg × D1/D2 × 完整四阶段到最终报告 | 阶段 01→03 | r265 pilot 6/6 + r268 同源重放 18 工件 |

## 2. 四轮读数汇总

### F1 · freeze 效应方向是任务类型依赖的（最稳健发现）
- R4（D1/D2 开放选型）：Δtruth(A-full − B-nofreeze) = **−0.35**（4 pair 中 3 负）——删 freeze 反而略高
- R5（D3 规格密集）：Δtruth = **+0.779**——删 freeze 显著降质
- R6 合并复算（J1 冻结口径，n=4 pair）：D1/D2 Δ = **+0.8175**（4 pair 全负差）；D3 方向引用 R5 +0.779
- 解读：freeze 在规格密集型任务上约束模型不跳步漏项（正效应），在开放选型任务上限制探索（负/零效应）。**不是 rubric 全局属性，是 task-type-dependent**。注意 R4 与 R6 对同一 D1/D2 数据读出方向相反——根因是 J1 口径换版本（原版 vs 冻结 v3）引入系统性重打分，跨版本数值不可直接比，只报"三轮各自内部方向稳定"这一弱声明。

### F2 · B-none 地板 + sham 分离（长度混淆已排除）
- R6：B-none J1 均分 0.0（4/4 run 全 fail），sham 组 0.875 ≈ A-full 0.929——等长中性填充不损害评分 → 评分差异来自 evidence/freeze 的**功能性内容**而非 token 长度。长度混淆排除成立。
- R5 补充：B-none cover=1.0 但 truth=0.125——模型自发覆盖全部核验点但主张质量全灭 → cover 与 truth 是两个独立维度，联合判读设计成立。

### F3 · cover 门槛经验激活
- R4 曾 vacuous（全 1.0）；R5 D3 首次 3/18 run cover<1.0，全部落在删 freeze 配置；R6 低 cover 集中在 B-nofreeze(0.742)/B-2del-fo(0.62)，未覆盖项全是交付物类核验点。freeze 同时管住结构完整性与规格覆盖。

### F4 · fullloop 完整链路：消融信号 < 测量噪声
- r265 pilot（9 cfg × 2 域完整四阶段到最终报告）：G2 区分力 1/12 PASS（唯一 PASS 还是 J2 边缘 spread 0.111）→ 决策不投 54-cell 全量。
- r268 同源重放（18 工件双判）：mean κ=0.441，10/17 cell κ<0.4，分歧集中在 S02 长工件的 J2-lenient（判分崩塌 0/45）→ **rubric v3 双判在 S02 长工件上不可靠**，该区域逐条判分不作决策依据。
- 结论：把链路从"阶段 01+02 中间工件"延长到"最终报告"后，消融信号依然没被量出来——瓶颈不在链路深度，在同源 judge 的测量噪声。

### F5 · 双判官分歧面（仲裁已闭合）
- R6：J1/J2 平均绝对差 0.248（n=35, max 1.0），分歧集中在 J1=0 的 run。人工仲裁队列 CLOSED（receipt-r6-adjudication-final）：fresh-context J1 重判 6/6 复现 0 分 + Lead 机械核对无一条误判 → 分歧来源 = J2 宽松版系统性偏松，非 J1 过严。

## 3. 最终结论（按置信度分层）

**可支撑（conf-0.1，同源偏差风险已标注）**：
1. 三个组件中只有 candidate-freeze 有可检测效应，且方向随任务类型翻转（规格密集正 / 开放选型负或零）。owner-tag 与 evidence-url 在所有轮次均无可检测效应（R6 Δ ∈ [−0.18, +0.29]，幅度 < 测量噪声）。
2. 长度混淆已排除（sham 分离成立）——效应归因于组件功能内容。
3. 完整四阶段链路上消融信号仍低于测量噪声 → 当前生成模型（qwen3.8-27b）+ 同源裁判条件下，C3 不能产出显著性级因果结论。

**不可支撑（明确不做）**：
- 任何 p 值级/效应量级推断（n≤6/cell，功效不足）
- 跨 rubric 版本的数值比较（J1 换版引入系统性重打分）
- S02 长工件区域的逐条判分结论（κ<0.4）

## 4. 解锁路径（升档条件，等待外部输入）

异源 judge 是唯一 conf 升档路径，三选一（均 blocked-on-human/external）：
- (a) 非 Qwen API key → 对同一批 18 工件（fullloop）+ 54 run 工件重打，与本表逐格对照；若 S02 J2 崩塌消失且 G2 仍弱 → 收口证据链闭合
- (b) LM Studio 装非 Qwen 模型（当前 :1234 端口 CLOSED）
- (c) arena 披露底层模型身份（family_check unknown 登记在案）

升级生成模型（>32B）为替代路径：换生成器后消融信号可能脱离噪声底，但成本另议。

## 5. 销账与状态位

- WORK_QUEUE P1「C3 v3 paired runs」：前置门禁 G1-G5 全闭合（G1 CONDITIONAL-PASS κ=0.6624 + CALM RR=0.983；G2 54-run 完成；G3 并入 R6 主分析；G4 hold-out=D3 已用；G5 本报告）→ 描述层 DONE
- goal-queue `T8-C3-v3-fullloop-execution`：[~] → 收口注记（pilot 完成 + 决策不投全量 + 本报告指针）
- 剩余卡人项不变：erratum-27 / G1b family_check / R121 / ORF arXiv 上传