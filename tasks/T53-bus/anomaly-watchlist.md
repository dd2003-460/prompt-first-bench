# T53b 异常观察清单（04-verify 待核验）
> origin: ai | 2026-11-20 14:40 | 13/62 早期 run 分布核验

## 异常 run（62 跑完后统一判）
| run | 异常 | 04-verify 动作 |
|---|---|---|
| gpu_formula_r3 | depth=0.0 (cov 正常 0.133) | 查 depth 计算是否挂，决定是否重算 |
| gpu_formula_r6 | cov=0 + n_nodes 字段缺失 | 查是否早退/数据不全，决定作废或补跑 |
| gpu_formula_r8 | cov=0 (nodes=114 正常) | 查 coverage 计算是否挂 |

## 字段信号
- n_verified/n_degraded 仅 gpu r01-r05,r07 有值，r08 后全 0/0 → 疑似 pipeline 在 r07 后停止填充该字段（judge.overall 仍正常）。04-verify 确认该字段是否已废弃，废弃则从统计口径剔除。

## webllm 混淆变量（04-verify 必须处理，2026-11-20 14:48）
- **25/30 run 日志带 WEBLLM-BROKEN**（Perplexity/ChatGPT 未登录，webllm 交叉验证全跳过），只有 5 个 run webllm 正常：
  - webllm 正常（离群，与其余不可直接比）：gpu_formula_r08 / gpu_text_r01 / gpu_text_r04 / gpu_text_r05 / gpu_text_r06（11-19 02:42~11-20 02:26 窗口）
  - 其中 gpu_text_r04/r05 崩在 checkpoint FileNotFoundError，实际有效 webllm run 只有 3 个
- **臂间可比性**：nat/soc/gpu 三臂的 formula 臂几乎全降级（25 个里 20+ 个），降级在各臂间大致均匀 → 臂间对比仍有效（混淆变量同水平），但"测的是无 webllm 的 S5"，结论只能限定为"webllm 缺席条件下的消融"
- **webllm 效应不可识别（14:50 实测）**：OK 组 n=2（cov mean 0.034 / depth 0.351）vs BROKEN 组 n=14（cov 0.252 / depth 0.448），无配对、臂构成不同 → 现有数据分离不出 webllm 效应，之前"倾向 (a) 因降级均匀"的理由作废
- **推论**：登录窗口已超时 → 剩余 ~50 run 全部降级，5 个 webllm-OK run（11-19 早期窗口）是各臂离群点；nat_text/soc_text 臂尚未开跑，将与 gpu_text 同水平降级 → 臂间对比仍有效（混淆同水平）
- **处置选项（需 D 定，不阻塞当前 run）**：
  - (a) 接受降级数据：62 跑完后出"webllm 缺席"口径的消融结论，5 个 OK run 标离群剔除或单列；webllm 效应另立 goal 补
  - (b) 登录后重跑：当前 12/62 有数据作废，重跑 4-5h（需 D 重新发起登录）
  - 我倾向 (a)——新理由：webllm 效应从现有数据不可识别，(b) 重跑只能补测一个正交维度、代价 4-5h；(a) 的臂间结论不受影响，webllm 维度留待登录后小规模配对实验（同 qid+arm 同 round 跑 with/without 各 2-3 个，可识别效应）

## 补跑项（62 跑完后手动补，不碰在跑实验）
| run | 状态 | 原因 | 动作 |
|---|---|---|---|
| gpu_formula_r06 | 已回滚重跑（2026-11-20 14:58 Lead, commit 0e2716bf3） | 空 done 回滚为 done=False，自愈链自然重跑（新进程带 faulthandler） | 无需手动，跑完对账 |
| gpu_formula_r09/r10 | 未标 done（results 有 11-19 残留） | 自愈链会自然补 | 等自愈链，跑完对账 |

## 真实进度口径（§8 对账，2026-11-20 14:45）
- cc-state done=13，但有数据工件的只有 **12**（r06 空 done）
- 汇报用"有数据 12/62"，不用"done 13/62"

## 统计口径（04-verify 必须遵守）
- **cc-state.json 的 done 列表是权威账本**（13/62）；ablation-results.json 有 16 条，其中 gpu_formula_r09/r10 是 11-19 的作废残留（cc-state 未标 done），直接数 results 会多算 2 条。
- 聚合时：以 cc-state done 为准，逐条 join results 记录；results 有而 cc-state 无的 = 残留，剔除。
- gpu r01-r05 是今天回退重跑的新数据（11-20 05:25-11:32），旧作废数据已被覆盖，不用管。

## 臂对比初判（13/62，非结论）
- nat/soc 臂数值干净（cov 0.17-0.86, depth 0.46-0.74）
- gpu 臂早期有 3 异常，占比 3/10，若 62 跑完仍 >30% 异常则该臂数据可信度存疑
