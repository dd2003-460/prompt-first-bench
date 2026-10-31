# C3 v3 全链收口汇总回执（r76 · Lead 视角）

日期：2026-11-01。对象：T8-C3-v3-paired-runs 全链条（G1 盲标 → G1a/G1b 校准 → R4 全因子 runs → rubric v11 修订 → M8 联合判读 → r74 双口径仲裁）。
性质：**汇总型回执，零新实验、零数据改动**——把散落在 15+ 份 receipt 里的结论收敛成一份可引用的终态陈述，供后续报告与决策引用。全部数值均引自既有冻结回执，未重算。

## 1. 证据链状态（逐环）

| 环 | 回执 | 状态 |
|---|---|---|
| G1 盲标协议 + X5 阳性对照 + 8 配置 MANIFEST sha 冻结 | loop-artifacts/stages/01/C3v3-G1-blind-label-design.md @ 2a2bb63 | 完成 |
| G1a ninfer 内部一致性校准（J1/J2 ×3 工件 + CALM 扰动） | receipts/c3v3-g1a-judge-calibration.json @ d8c6eb2 | PARTIAL-PASS（通道修正 :8000→:8787；κ 天花板效应登记） |
| G1b 异源 judge（arena 01a19104 盲评 5 工件） | calibration/g1b/receipt-g1b-hetero-judge-r74.md @ eb2a9a7 | PARTIAL-PASS（F1 阳性对照交叉验证成立；family_check=unknown） |
| R4 全因子 36 runs + 双判 72/72 | runs-r4/receipt-r4-execution.json @ dd612b4 | PASS-with-caveat（执行完整；R1 地板首跑失效） |
| rubric v11 特异性指纹测试（sham 地板修复） | runs-r4/rubric-v11-validation.json @ 4a2ec01 | PASS（v2→v11 十轮迭代收口） |
| R1 三道地板复验 + R4 主分析重启 | runs-r4/receipt-r4-mainanalysis.json | UNBLOCKED（描述层；推断上限受限） |
| M8-frozen-v1 机会集冻结 + Lead 盲法联合判读 | runs-r4/receipt-r4-lead-blind-joint-readout.json @ r73 | PASS（机制层收口；cover 恒 1.0 vacuous 已登记） |
| r74 双口径分歧仲裁（7 cell/30 flip） | runs-r4/receipt-r4-adjudication-r74.json | 队列清空（25 ID_SPACE_DRIFT + 5 UPHOLD_J1，0 条推翻 J1v11） |

## 2. 最终科学结论（含限定语）

**主结论（方向性证据，conf 降档）**：在 D1-meeting-room / D2-file-collab 两域、J1v11 严格版口径、n=4/cell 下——
1. **freeze 组件负效应最稳健**：B-nofreeze Δtruth = −0.350（全场最低），七 judge sweep（v2/v4/v6/v7/v9/v10/v11）下 rank 1/9 均成立；删 freeze 后核验真实性率显著下降。
2. **evidence 组件正向**：B-noevidence Δtruth = +0.156（删 evidence 反而得分高——该组件对 M8 判分无正向贡献，可能是任务书回声载体）。
3. **owner 组件中性**：B-noowner Δtruth = +0.017（边际）。
4. **sham 分离**：v11 特异性指纹测试使 B-sham 跌至第 2 低组（0.517），空转工件可被 fail；四 judge（v3/v7/v11/v6）sham 分离成功。
5. **cover 维度 vacuous**：36/36 run cover = 1.000（含语义等价层），当前任务难度不足以让任何配置漏项——协议机制层跑通，但需 harder task 激活区分力。

**硬限定语（引用时必须带）**：
- 同族 judge（qwen3.8-27b 既产工件又当判官）+ n=4/cell → 结论上限 = 描述层方向性证据，非因果定论。
- family_check = unknown（arena 未披露底层模型全名）→ R5 家族隔离项 PARTIAL-CLOSED，跨通道独立性已证、跨家族独立性未证。
- 盲法强度降级：Lead 非严格事前盲（见过 r60 回执结论），价值在「规则先行 + 全量重算 + 逐条留痕」而非信息隔离；严格盲法需第二人。
- 外推性声明收窄：第三 hold-out 域资产不存在（G1 设计 §2 盘点），结论仅限既定两域。

## 3. 剩余未决（按解锁条件分类）

| # | 项 | 解锁条件 | 成本 |
|---|---|---|---|
| 1 | G1b family_check unknown→CLOSED（queue T8-C3-v3-g1b-family-upgrade） | 用户给明确非 Qwen API key 或 arena 平台披露模型身份 | ~5 次 judge 调用或一次会话查询；blocked-on-human |
| 2 | κ 门禁阈值标定（RV3G6-kappa-u1k1-execution） | 成璐对 kappa-u1k1 材料 §4 勾选裁定 | 裁定后 ~6 步机械落地；blocked-on-human |
| 3 | 严格盲法复核（第二人执行 M8 联合判读） | 第二人类标注者参与 | 外部依赖 |
| 4 | harder domain 激活 cover 区分力 | 第三域任务资产建设 | 新 goal |

## 4. 判定

C3 v3 paired runs 链条**机制层收口**：所有可自主执行的环节全部闭环，回执链完整可追溯，r74 仲裁后无双口径残留分歧。剩余四项全部 blocked-on-human/external，agent 侧无可推进空间——本 goal 进入等待态，等 #1/#2 任一解锁后升档或扩展。
