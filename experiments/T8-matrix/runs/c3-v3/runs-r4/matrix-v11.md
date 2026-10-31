# R4 全因子 × J1-strict-v11 判官矩阵

> origin: ai · 2026-10-31 · runner r45 后解析 runs-r4/*-J1v11.json (36/36)
> 判官: J1-strict-v11 (design/rubric-v2-density-test.json) · 模型: qwen3.8-27b @ :8787

| config | mean_pass_rate | D1/a | D1/b | D2/a | D2/b | floors触发 |
|---|---|---|---|---|---|---|
| A-full | 0.750 | 10/10 | 3/10 | 9/10 | 8/10 | — |
| B-nofreeze | 0.494 | 3/8|low_specificity | 8/10 | 4/8 | 3/10 | low_specificity |
| B-noevidence | 0.906 | 7/8 | 6/8 | 10/10 | 8/8 | — |
| B-noowner | 0.767 | 7/8 | 4/6 | 5/8 | 9/10 | — |
| B-2del-fe | 0.627 | 6/10 | 6/8 | 4/17|low_specificity | 12/13 | low_specificity |
| B-2del-fo | 0.523 | 5/10 | 3/10 | 4/6 | 5/8 | — |
| B-2del-eo | 0.606 | 6/8 | 14/16 | 3/10 | 3/6 | — |
| B-none | 0.678 | 4/8 | 7/9 | 18/30 | 10/12 | — |
| B-sham | 0.542 | 2/20|floor,evidence_floor,low_specificity | 4/10 | 14/14 | 4/6 | evidence_floor,floor,low_specificity |

## 观察

1. **B-noevidence=0.906 异常 — 已定位机制（2026-10-31 二次分析 + recheck 三轮验证）**：人工过 4 个原始输出确认证据并未缺失（具体数值/厂商/正交分解都在，模型自发写出）。对比 density/echo 字段后发现真正原因：A-full 的 D1/seedb 单点塌方（pass 3/10, echo_ratio=0.3, method_echo=0.19, density=0.28 均为四 cell 最差），把 A-full 均值从 ~0.9 拖到 0.75；B-noevidence 四 cell echo 全部 ≤0.16 无塌方。**recheck 升级结论（r49）**：对 A-full/D1/seeda 同 prompt 复跑 3 次（seeda-recheck-{1,2,3}，判官 J1v11 同口径 temperature=0），echo_ratio = 0.35 / 0.18 / 0.27，pass = 2/8 / 14/19 / 4/7 —— 非系统性塌方也非单次噪声，是**cell 级高方差**（同一 prompt 输出质量在 11%~74% pass 间摆动）。推论：n=2/cell 的矩阵均值受方差主导，配置间差异（如 B-noevidence vs A-full 的 15pt）部分可能是采样噪声而非组件效应；置信度从"中"降为"低-中"，升档需 n≥4/cell 重跑或固定种子复现。
2. **B-none(0.678) > B-sham(0.542)**：v11 能区分真空组件与假消融；sham 触发 floor+evidence_floor（识别出引用不存在的冻结记录）。完整矩阵复现 v11 关键改进。
3. **B-noowner≈A-full**（0.767 vs 0.750）：owner 组件在两个任务域无可测贡献，或 rubric 10 项无直接考 owner 行为的题项。
4. B-nofreeze=0.494 最低：冻结件仍是最大单组件贡献（-35%），与 v11 部分验证一致。

## 04.5 反方复核（r49）

- prompt sha 三源一致（recheck×3 = 原 seeda = 37297a537f9c9022），复跑口径无漂移。
- 判官 3/3 输出成功解析为合法 JSON，temperature=0 格式稳定。
- **登记边界**：判官 items 总数跨 run 不稳定（8/19/7），pass_rate 分母漂移 → 本矩阵跨配置比较应以 echo_ratio / floor 触发为主指标，pass_rate 仅参考；此弱点影响全部 36 cell 而非 recheck 独有，升档前需判官条目数锚定（rubric 显式列 10 题项编号）。

## n=4 方差控制复核（r51，见 matrix-v11-n4.md）

- 4 关键配置 × n=4 重采样：**配置间排序单调保持**（A-full > B-noevidence > B-none > B-sham，echo 与 pass 双口径同序），r49 "方差主导一切"修正为"方差大但均值差仍可测"。
- **B-noevidence 反超 A-full 坐实为 n=2 采样噪声**（n=4 下 0.744 < 0.795）。观察 1 的置信度从"低-中"回升至"中"，结论方向不变（非组件效应）。

## r57 机会集冻结协议消费（T8-C3-v3-opportunity-set-freeze）

- arena 对抗回执 blocking fix #3 落地为草案：`design/opportunity-set-freeze-protocol-draft-r57.md`（定义主体=Lead 盲法前置 / 空分母保守口径默认 / truth-cover 联合门槛 / 新旧 M8 口径版本化）。
- **R4 限定语回填（r57 生效 → r60 部分收回）**：~~evidence/owner 方向的 M8 比较在分母收缩 -25.5% 下无法分离质量效应与数量效应，降档为"未分离的方向性证据"~~ → **r60 cover 分析否定分母收缩假设**（B-noevidence cover=1.000 与 A-full 持平，冻结集口径下分母固定不存在收缩）。evidence/owner 方向 M8 比较恢复为「方向性证据」（同族 judge + n=4/cell 的上限不变），不再带「未分离」限定语。freeze 负效应（B-nofreeze 0.469 全场最低）**三 judge 下均 rank 1/9，结论最稳健**。
- 三层口径不一致坐实：judge 条目（6-30/run）≠ 题面机械可提取机会（5-8/seed）≠ 成文冻结集（无）。事后重建只能给下界 → R4 不复算，新口径从下一 run 起生效。
- 待裁定：空分母保守/激进口径 + cover 门槛 -0.05 数值（草案 §四，不代裁）。

## r55 数据完整性修订

- **发现**：一个旧 rerun 进程（runner v1 bug：首次 pass 丢失 output 字段）覆盖了 A-full/D1 的 seeda/seedb 原始 run，且覆盖后未重新判官——旧判官分（seeda 10/10 echo 0.125 / seedb 3/10 echo 0.30）对应的是已不存在的旧 output。
- **处置**：用完整 v11 rubric 对两个新 output 重判（seeda 9/10 echo 0.13 / seedb 4/8 echo 0.35），matrix-v11-n4.md 全部 n=4 均值重算。
- **影响评估**：4 关键配置排序与 r51 版完全一致（A-full 0.807 > B-noevidence 0.744 > B-none 0.608 > B-sham 0.543），核心结论不受影响；仅 A-full/D1 内部数值不可与 r44 纵向比较（新采样 + 1 天时间跨度）。
- **教训登记**：runner 的 SKIP/覆盖逻辑必须校验 output 字段存在性 + SHA，不能只查 key 是否存在；任何 output 覆盖操作必须触发下游判官重跑。
