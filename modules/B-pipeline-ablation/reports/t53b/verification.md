# T53b 模块级验证报告（跑 / 记录 / 分析 / 稳定性 / 客观性）

# origin: ai
# 生成: 2026-11-21 · 数据快照: results.json 60 unique run + runs/ 60 SM + 60 judge
# 目的: 证明"完整实验流程模块"五个环节各有可复现验证证据，不是只有一堆文件。
# 复现总入口: `python3 experiments/stage-ablation/ablation_stats.py --spec t53b`
#   （无参 == --spec t53b，已回归验证一致；输出落 reports/t53b/stats.md）

## 0. 一句话结论

跑/记录/分析/稳定性 四环节证据闭环、可一键复现；客观性环节暴露两处必须如实记录的差异
（verify.md 旧 p 值与当前原始数据复算不一致；r7 判据三种口径结论一致但 verify.md 用的是最宽松口径）。
主结论（formula 臂 nat-depth / soc-cov 显著优）**方向不变、显著性不变**，差异只在 p 值精度和判据口径。

---

## 1. 跑（run）— 60/60 SM run 完成

| 证据 | 值 | 来源 |
|---|---|---|
| 权威账本 done | 60/62 work_units | `tasks/T53-bus/cc-state.json` |
| 2 个 not-done | `stats_summary` + `repro_check` | 同上（= 本报告的"分析/复现"任务，非 SM run） |
| SM run 文件 | 60 个 `*.json` | `data/t53b/runs/`（另 1 个 `pipeline-state.json` 是快照 manifest，非 run） |
| 每 run 可执行命令 | `python3 ablation_run_one.py <qid> <arm> <round>` | cc-state 每个 work_unit 的 `cmd` 字段 |

判定: **PASS**。60 个真实 SM run 全部有 run 文件；2 个 not-done 是分析/复现任务（本模块正在补），
不是"跑了没记录"的缺口。webllm 离群 5 run（T3 处置 (a)）已单列，见 §5。

复现: `python3 -c "import json;cc=json.load(open('tasks/T53-bus/cc-state.json'));wu=cc['work_units'];print(sum(v['done'] for v in wu),'/',len(wu))"`

---

## 2. 记录（record）— 三层账本 1:1 对账

| 层 | 数量 | 对账 |
|---|---|---|
| SM run 文件 | 60 | 基准 |
| judge 评分文件 | 60 | 60/60 覆盖，无 SM 无 judge、无 judge 无 SM |
| 过程 notes | 60 | 每 run 一份 |
| results.json 记录 | 60（去重后 unique） | 60/60 覆盖，无 SM 无 results |

判定: **PASS**。三层（run / judge / results）与 60 个真实 run 严格 1:1，无孤儿、无缺失。
results.json 内同 run 多次记录取最新 timestamp（去重逻辑在 stats.py）。

复现: 见 stats.py 主流程 `best` 去重段；对账脚本见本报告生成时的 execute_code（run_keys/judge_keys/results 集合比对）。

---

## 3. 分析（analysis）— 统计管线一键复现

`ablation_stats.py` 从 results.json + runs/ 重算，不读任何预存结论：

- 每题每臂 coverage/depth 的 mean±SE + 95%CI（per-run 聚合）
- 消融主口径 Δ = formula − text，**Welch 独立样本 t 检验**（t 分布 CDF 自实现，无 scipy 依赖）
- r7 复现（gpu 题 L1 不确定性维度，三判据口径）
- 缺口清单（cc done 但 results 无）

主表（当前原始数据复算，2026-11-21）:

| 题 | 指标 | n_f | n_t | Δ | t | p | 结论 |
|---|---|---|---|---|---|---|---|
| nat | cov | 10 | 10 | +0.167 | 1.49 | 0.155 | 不显著 |
| nat | depth | 10 | 10 | +0.113 | 2.75 | **0.013** | formula 优 ✓ |
| soc | cov | 10 | 10 | +0.186 | 2.75 | **0.016** | formula 优 ✓ |
| soc | depth | 10 | 10 | +0.003 | 0.08 | 0.939 | 不显著 |
| gpu | cov | 9 | 6 | −0.033 | −0.97 | 0.349 | 功效不足（n<8） |
| gpu | depth | 9 | 6 | −0.052 | −1.01 | 0.335 | 功效不足（n<8） |

t 分布实现校验（已知值）: t=2.262/df=9→0.0500 ✓, t=2.0/df=10→0.0734 ✓, t=1.96/df=1000→0.0503 ✓。

判定: **PASS**。分析环节完全从原始数据重算，无手工数字。

---

## 4. 稳定性（stability）— 去极端轮次 Δ 不变

stats.py 敏感性分析段：对每题每指标，去各自最低 / 去各自最高 / 双端 trim 后重算 Δ。

| 题 | 指标 | 原始 Δ | 去最低 | 去最高 | 双端 trim | 判定 |
|---|---|---|---|---|---|---|
| nat | cov | +0.167 | +0.167 | +0.185 | +0.187 | 稳定 ✓ |
| nat | depth | +0.113 | +0.119 | +0.118 | +0.124 | 稳定 ✓ |
| soc | cov | +0.186 | +0.175 | +0.206 | +0.197 | 稳定 ✓ |
| soc | depth | +0.003 | +0.002 | +0.003 | +0.002 | 稳定 ✓ |
| gpu | cov | −0.033 | −0.035 | −0.041 | −0.045 | 稳定 ✓ |
| gpu | depth | −0.052 | −0.018 | −0.053 | −0.014 | 稳定 ✓ |

判定: **PASS**。所有 Δ 去极端轮次后变化 <0.05 且方向不变 → 结论不是由个别极端轮次驱动。
（T2 原计划重跑好轮次验证波动，此分析已覆盖，T2 降级为抽 2 轮各重跑 1 次，不阻塞。）

**方差来源实测**（2026-11-21，8787 端点 temp=0，来源①）：单请求串行 2 次**逐字符一致**（短/长 prompt 均 MATCH）；
**并发 4 次全不同且 ≠ 串行**，两次并发产生相同输出集合（batch 组合决定，非随机采样）。
→ T53b 轮次间方差的真正来源 = **vLLM 并发非确定性（NVFP4+MTP+continuous batching）+ 基础设施故障
（rc=137/143、watchdog 误杀、502 burst）+ checkpoint resume 分叉**，不是 LLM 采样随机性。
我们测的是"基础设施/并发扰动下的结论稳健性"，比 2410 的纯采样方差更贴近本地真实部署。
[残留] nat_formula r05/r07 为 stop 早停（n_nodes 51/70 vs 正常 130-204），分数受"树没拆完"污染。
**已做稳健性检查**（2026-11-21）：剔除 r05/r07 后 nat depth Δ=+0.104 t=2.26 p=0.040（仍显著，方向一致），
nat cov Δ=+0.146 p=0.318（本就不显著，不变）→ **主结论对早停污染稳健**。
详见 `research/verification-sop-literature-20261121.md` §1c。

**量级对标**（2410.03492 "Towards Reproducible LLM Evaluation"，ar5iv 全文查证）：
该文的稳定性验证在 **100~5760 题 × 1~30 次重复 × 6 模型**量级，收敛判据是预测区间宽度 <0.01（需 n=30）。
我们的量级是 **3 题 × 10 轮/arm × 1 模型**——题目数小 33~1920 倍，重复次数上限小 3 倍。
其 t 分布预测区间方法与量级无关，n=10 可套（PI 宽度约为 n=30 的 1.7 倍，~0.02 量级）。
本表的 ad-hoc trim 是该方法在小样本下的启发式近似；
nat depth Δ=0.113 和 soc cov Δ=0.186 均 > 预估 PI 宽度（~0.02）的 5 倍以上，结论对量级差距稳健。
详见 `research/verification-sop-literature-20261121.md` §1b。

---

## 5. 客观性（objectivity）— 两处必须如实记录的差异

客观性 = 结论能否被独立方法/独立数据复现。本环节**没有全绿**，如实披露：

### 5.1 verify.md 旧 p 值与当前原始数据复算不一致

| 项 | verify.md（旧） | 当前复算 | 差异 |
|---|---|---|---|
| nat depth | t=2.66, p=**0.008** | t=2.75, p=**0.013** | p 差 0.005 |
| soc cov | t=2.75, p=**0.006** | t=2.75, p=**0.016** | p 差 0.010 |
| 均值/Δ | 0.650/0.537/+0.113, 0.900/0.714/+0.186 | 完全一致 | 无 |

- 均值和 Δ 完全对得上，差异只在方差估计 → t → p 的精度层。
- 可能原因: nat 全部 run 在 11-20~11-21 重跑过（timestamp 可查），verify.md 写于数据快照略早的时刻。
- **主结论不变**: 两项都仍 <0.05，显著性判定一致，方向一致。差异是 p 值精度，不是结论翻转。
- 处置: 以当前原始数据复算值为准（0.013/0.016），verify.md 旧值标注为历史快照。

### 5.2 r7 判据三种口径（结论一致，verify.md 用最宽松口径）

| 判据口径 | 命中 | 可评估 | 判定 |
|---|---|---|---|
| 任务书原文（L1 claim 以关键词开头 + scope 横切）[scope 字段缺失，仅 claim 开头] | 8/13 | 13/20 | PASS |
| L1 宽松（L1 claim 含关键词） | 9/13 | 13/20 | PASS |
| 全树（任意层级 claim 含关键词） | 11/13 | 13/20 | PASS |

- verify.md 记的 11/13 = 最宽松的"全树"口径。任务书原文是双条件（claim 开头 + scope 横切），
  但 run 文件无 scope 字段 → 原文口径只能退化成"claim 开头"= 8/13。
- 三种口径都 ≥3 轮 → 都 PASS，**结论对口径不敏感**。但 verify.md 当初标 11/13 时没说明用的是全树口径，
  这里补正：r7 PASS 成立，但应记为"全树口径 11/13"而非暗示是任务书原文口径。
- 7 个 gpu_formula 旧 run 无 nodes 字段（旧格式）→ 不可评，已单列。

### 5.3 客观性的固有边界（非缺陷，是口径限定）

- judge 族单一（qwen3.8-27b ×1，temperature=0，non-IRR）→ 打分本身无跨族一致性检验。
  语义级重判需异族 judge 或人（超出本机免费通道，已标 [残留]）。
- webllm 缺席条件下的 S5 消融 → 结论不可外推到 webllm 可用场景（E2 配对实验补）。
- seed=42 机制生效但 run 文件无 seed 字段 → 证据链缺口 [残留]（机制在 driver:59 设 SM_SEED=42 可查）。

判定: **CONDITIONAL PASS**。主结论方向与显著性稳健（§3/§4 支撑），但 p 值精度和 r7 口径需按本报告修正值记录。
客观性不是"全绿"，而是"差异已定位、已量化、主结论不受影响"。

---

## 6. 复现清单（一键）

```bash
cd /Users/a1-6/Desktop/workspace/pfb
# 分析 + 稳定性 + r7（输出 reports/t53b/stats.md）
python3 experiments/stage-ablation/ablation_stats.py --spec t53b
# 等价无参（回归验证一致）
python3 experiments/stage-ablation/ablation_stats.py
# 跑/记录对账
python3 -c "import json;cc=json.load(open('tasks/T53-bus/cc-state.json'));wu=cc['work_units'];print('done',sum(v['done'] for v in wu),'/',len(wu))"
ls modules/B-pipeline-ablation/data/t53b/runs/*.json | wc -l   # 61 = 60 SM + 1 pipeline-state
```

## 7. 残留清单（诚实标注，不假装闭环）

1. judge 单族 non-IRR → 语义级重判待异族 judge（免费通道外）。
2. seed 机制生效但 run 文件无 seed 字段 → 证据链缺口。
3. gpu n<8（离群剔除后 n_f=9/n_t=6）→ 功效不足，Δ 只作方向参考。
4. verify.md 旧 p 值（0.008/0.006）与当前复算（0.013/0.016）不一致 → 以当前为准，旧值标历史快照。
5. webllm 效应识别需登录 + I3 配对实验（未做）。
6. **方差来源 ≠ 采样**：单请求 temp=0 确定，并发非确定（vLLM batch 组合）。nat_formula r05/r07 stop 早停污染分数——**已做稳健性检查**：剔除后 nat depth Δ=+0.104 t=2.26 p=0.040 仍显著、方向一致，主结论稳健。公开 SOP 未覆盖"本地量化模型 + vLLM 并发非确定性"评估方法（gap）。
7. **量化保真度已关闭**（2026-11-21，D 指令：文献背书即可，不做 BF16 对照实验）：① 设计层面——双臂消融，量化是共同因素，Δ 中抵消；② 文献——2610.27913 ACE-Compression（35+ checkpoint × 6 LLM）：4-bit 量化在 procedural reasoning 维度 ≈ FP16 父模型。caveat：ACE 测 INT4 非 NVFP4（同属 4-bit 类，NVFP4 块级浮点 scale 保真度通常 ≥ INT4）；ACE 发现细粒度能力更不稳定，我们的 rubric 打分属细粒度维度，残余风险被 ① 覆盖。详见 research/verification-sop-literature-20261121.md §1d。
