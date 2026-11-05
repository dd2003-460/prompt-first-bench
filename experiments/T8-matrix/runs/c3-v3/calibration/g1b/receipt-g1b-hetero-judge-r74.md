# G1b 异源 judge 回执（C3 v3 · R5 家族隔离项）

- **日期**: 2026-10-31 · keepalive 轮
- **通道**: arena.ai/agent 会话 `01a19104-d30a-7cc0-a04e-5a5515bf59f2`，仓库 prompt-first-bench，arena 工作分支 `arena/15bf59f2-prompt-first-bench` → PR #36 → merge 入 `ralph/g1b-hetero-judge-dispatch`（远端 head eb2a9a7，本地已 ff 同步）
- **产物**: `experiments/T8-matrix/runs/c3-v3/calibration/g1b/hetero-judge-results.json`（commit b2e81d4）
- **协议**: J1-strict（sha256_16 = 15086eb4166b1884，与 G1a 冻结版一致，未改写）

## 结果

| 样本 | n | passed | fails | 备注 |
|---|---|---|---|---|
| blind-A1 | 27 | 27 | — | 与 G1a J1 逐条一致 |
| blind-A2 | 24 | 24 | — | 同上 |
| blind-B1 | 20 | 20 | — | 切分比 G1a 细（G1a 把 A1-A10 压成 1 条），交集 10 条全一致 |
| blind-B2 | 7 | 7 | — | 同上 |
| blind-P1 | 27 | 26 | **X5** | 阳性对照：异源 judge 抓到了植入退化 |

## κ 计算（条目级，G1a J1 vs G1b）

- 交集 95 条，po = pe = 0.9895 → **κ = 0.0（机械值）**。原因与 G1a 内部双判相同：**天花板效应**——校准集全是高质量全 pass 工件，pe→1 时 κ 无定义/归零，不是分歧多。
- 唯一翻转 = P1/X5（G1a J1、J2 均漏检；G1b 判 fail）。方向上这是**异源 judge 更敏感**，不是不一致噪声。
- 结论口径：κ≥0.6 的机械门槛在天花板数据上不可达（G1a 同病），R5 一致性项改按「唯一翻转方向 + 阳性对照敏感度」判读，见下。

## 关键发现

1. **F1 · 阳性对照交叉验证成立**：P1/X5 突变件，qwen J1/J2 双双漏检（G1a F1 已登记），异源 judge 独立抓到并点名「处置标已解释但证据称不可解释」。两个不同家族的评分器对同一植入退化的敏感度互补——J1 严格版（qwen）和异源 judge 各自独立通过阳性对照，评分器敏感度不再依赖单一模型。
2. **F2 · family_check = unknown（诚实登记，不粉饰）**：arena 平台未向会话披露底层模型全名，judge_model 字段如实写「arena.ai Agent Mode（底层模型标识未披露）」，family_check 标 unknown——只能确认非 ninfer qwen3.8-27b 同通道产物，无法自证非 Qwen 家族。**R5 家族隔离项状态：PARTIAL-CLOSED**（跨通道独立性已证，跨家族独立性未证）。若后续能拿到 arena 底层模型身份（或用户给一个明确非 Qwen 的 API key 重打一遍 5 份工件，成本 ~5 次调用），可升级为 CLOSED。
3. **F3 · B1 切分漂移登记**：G1b 按原始编号细分出 20 条（含攻击轮 1-5、U1），G1a J1 只有 11 条。κ 在交集上算不受影响，但 R4 阶段统一用 G1b 的细粒度 id 空间（信息量更大），G1a 粗粒度结果仅作历史参照。

## verdict

**PARTIAL-PASS**（与 G1a 同级）。解锁状态不变：R4 全因子 runs 开跑许可维持条件性授予（判读绑定 J1 严格版 + 双口径并报 + 分歧工件进人工仲裁）。R5 最终「judge 校准全过」口径仍缺 family_check 升级项（unknown → 确认非 Qwen），属低成本可补项而非硬阻塞。

## 教训

- arena 会话不能直接 push 到指定 ralph 分支（会话分支固定为 arena/<hash>-<repo>），任务书应直接要求「push 到自己分支 + 开 PR 到目标分支」，本轮靠 agent 自行走 PR #36 解决，下次任务书写明。
- 派发前确认远端分支 tip = 任务书 commit（断点 B 检查）：本轮 git ls-remote 核对通过后才发派。