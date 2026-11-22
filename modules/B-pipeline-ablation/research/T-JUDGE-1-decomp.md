# T-JUDGE-1 — 客观 judge：embedding 匹配 + LLM 兜底（decomp）

**发起**: 2026-11-22 D 拍板："embedding 处理，LLM 只负责处理 gold 上没有近似的情况；embedding MacPro 本身可以跑"
**动机**: D 洞察——领域知识有客观完整结构（gold 树），压缩率/损失/Pareto 边界可计算，judge 不该依赖 LLM 主观打分。当前 judge（27b 自评）绝对值不可信、方差 ~0.1，是 K7 Pareto 分析和 T-PR-17 因果归因的上游瓶颈。
**定位**: 离线后处理打分脚本（读 checkpoint 树 + gold 树 → 匹配 → 计算指标），不碰 SM 生成循环，符合固化约束。所有历史 run 免费重打。

## 架构（D 拍板的分工）

```
输出树节点 ──┐
             ├─→ embedding 相似度匹配 ─→ 匹配上 → 客观指标（覆盖率/深度/压缩率/Pareto）
gold 树节点 ─┘        │
                      └─ 无近似（sim < 阈值）→ LLM 二元裁决（"是否表达了 gold 语义？"是/否）
```

- **embedding 主匹配**：本地 Mac（M1 Max，MPS 可用），不占 vLLM 4×V100
- **LLM 只兜底**：仅对 embedding 判"gold 上无近似"的节点调 27b 做二元判断（是/否，不是 0-1 连续分）
- **与旧 judge 并跑（dual-track）**：新 judge 出客观指标，旧 judge 保留语义质量维度；两者相关性本身是可报告指标

## 数据结构（2026-11-22 实测确认，非凭记忆）

| 数据 | 位置 | 格式 |
|---|---|---|
| SM checkpoint 树 | `experiments/stage-ablation/checkpoints/sm-{qid}-r{N}/` | 树形目录（1/, 1.1/, 1.1.3/），每节点 `node.json` 含 `id`/`claim` 字段 |
| 旧格式 | `checkpoints/sm-{qid}-r{N}.json` 单文件 / `nodes/` 子目录 | SM 代码已兼容读取（s5_state_machine.py:1044-1046） |
| gold 树 | `experiments/stage-ablation/gold/Q{1-5,9}.md` | **markdown 树文本**（非 JSON），需解析器提取节点（N-x 编号 + 缩进层级） |
| budget scan 结果 | `modules/B-pipeline-ablation/data/t53b/runs_budget_scan/*.json` | 只有分数（depth_score/coverage），**无树**（final_state="rework" 是状态标记）→ 重打需回 checkpoints/ 取树 |
| 环境 | sentence_transformers 5.1.2 + torch 2.8.0 MPS ✅（本机已装，刚验证） | 无现成 embedding 模型缓存（HF hub 只有生成模型）→ 需下载 |

## 分解树

```
T-JUDGE-1 客观 judge
├── J1. gold 树解析器
│   ├── 输入: gold/Q*.md —— **格式实测不统一**（2026-11-22 逐文件核）:
│   │   Q1(gpu): 事实清单（表格行+编号误读+bullet 结论/缺口，非树）→ 匹配单元=事实条目
│   │   Q2-Q5: N-0 根节点树（**nat/soc 无 gold，暂不用**）
│   │   Q9: 代码块包裹树（conf 0.2 待 arena 扩）
│   ├── 首跑范围 = gpu only → 解析器只需支持 Q1 事实清单格式（表格行/编号项/bullet 各=1 单元）
│   ├── 输出: [(unit_id, depth, text, parent_id)] 列表（事实清单 depth=1, parent=N-0 虚拟根）
│   └── 验证: 解析单元数 == 手工清点（Q1: 表格 5 行 + 误读 4 条 + 结论 3 条 + 缺口 4 条 ≈ 16）
├── J2. checkpoint 树读取器
│   ├── 输入: checkpoints/sm-{qid}-r{N}/ 树形目录（node.json 的 claim 字段）
│   ├── 输出: 同 J1 schema（兼容旧格式 nodes/ 目录）
│   └── 验证: 节点数 == n_nodes 字段（sm-gpu-r1 已知 37 节点）
├── J3. embedding 匹配核心
│   ├── 模型: bge-m3（dim 1024，已下载缓存，MPS 本地跑，不占 vLLM）✅
│   ├── 匹配算法: 每输出节点 vs 全部 gold 单元余弦，取 top-1
│   ├── 阈值标定（首跑结果 2026-11-22）:
│   │   阈值敏感性（覆盖率/精确率，gold=16）:
│   │     r1(n=30):  0.55→8/16,0.87 | 0.60→6/16,0.50 | 0.65→5/16,0.20 | 0.70→1/16
│   │     r2(n=113): 0.55→12/16,0.90 | 0.60→11/16,0.70 | 0.65→8/16,0.30 | 0.70→5/16
│   │   → **选定 0.65**（0.60 段假匹配多，0.70 覆盖塌）
│   │   → **磁体效应（新发现）**: SPEC-2（HBM 带宽，短且泛）在 r2 吸 ~20 节点，
│   │     0.60-0.65 段大量假匹配（GPU 候选集/价格/内存需求 → HBM 带宽 ✗）
│   │     → 解法: 吸 N 个节点的 gold 单元标 magnet，其匹配全部降级送 LLM 兜底复核
│   └── 验证: top 匹配肉眼核验通过（N21 多卡并行→MIS-4 ✓ / N46 A100 算力→SPEC-1 ✓ /
              N56 RX TDP→SPEC-5 ✓）；边界段 0.60-0.65 混入率 ~50%（阈值 0.65 后大幅减少）
├── J4. LLM 兜底（二元裁决）✅ 脚本就绪（tjudge1_llm_fallback.py，等 K7 释放 vLLM）
│   ├── 触发（首跑后修正）: 磁体匹配的节点（gold 单元吸 >=3 节点 → 全部降级），
│   │   不是低 sim 节点——低 sim 直接判 unmatched 更稳（0.60-0.65 段混入率 ~50%）
│   ├── prompt: 二元 yes/no（节点是否实质覆盖该 gold 单元）+ 一句话理由；temp=0
│   ├── 成本: 27b 本地，每节点 1 次调用；首跑触发 29 条（r1 0 + r2 29，磁体 5 单元）
│   └── 验证: 兜底裁决与 embedding 判断的一致率（应高，否则阈值标定有问题）
├── J5. 指标计算（从匹配结果导出，纯计算）✅ 首跑已出
│   ├── 覆盖率 = 匹配上的 gold 单元数 / 16（按 spec/misread/conclusion/gap 分类报告）
│   │   首跑（confirmed 口径）: r1 5/16=0.312 | r2 3/16=0.188（+磁体 pending 5 → LLM 裁决后上限 8/16）
│   ├── 压缩率 = confirmed 节点 claim 总长 / 对应 gold 单元总长（token 数代理，局限已声明）
│   │   首跑: r1 1.30x | r2 4.37x（r2 节点多 4 倍但覆盖少 → 每覆盖单元花更多文本 = 更"稀释"）
│   ├── 精确率 = confirmed 节点 / 输出节点总数（**粒度比，不是质量比**——输出树比 gold 细 7 倍，
│   │   多节点覆盖同一 gold 单元是正常分解；主指标是覆盖率+压缩率，precision 只作参考）
│   └── Pareto 点 = (cost=节点数, 覆盖率) → 跨 run 画前沿（K7 全量数据出来后重打）
└── J6. 重打历史数据 + dual-track 对照
    ├── 范围: sm-gpu-r1/r2（✅ 已打）+ matched 批 30 run（gpu/nat/soc，judge_file 已有旧分）
    │   + synth-l5-719nodes + budget scan 15 run（K7 完成后）
    ├── 旧 judge 分数位置: data/t53b/runs_sm_matched/*_judge.json（scores 0/1 列表 + reasons）
    └── 判据: 新覆盖率 vs 旧 depth_score 相关性（Spearman ρ）；
              ρ > 0.7 → 新 judge 可信且更客观；ρ < 0.5 → 测的不是同一构念，回查匹配质量
```

## 缺口清单

| 子项 | 缺什么 | 补法 |
|---|---|---|
| J1 gold 解析 | Q1-Q5 的 markdown 格式未逐一核（Q9 已核: 代码块包裹 + N-x 编号） | 解析前逐文件 head 核格式 |
| J3 模型选型 | ✅ 已定 bge-m3（dim 1024，MPS 跑通，缓存已落） | — |
| J3 阈值 | ✅ 首跑标定 0.65 + 磁体降级（0.60 假匹配多 / 0.70 覆盖塌） | 后续: 人工标定集（20 正例 + 20 负例对）验证 ROC 拐点 |
| J4 触发率 | ✅ 首跑 29 条（r2 磁体 5 单元）；脚本就绪，**等 K7 释放 vLLM 后跑** | 跑完重算 confirmed 覆盖率 |
| J5 信息量定义 | token 数代理的局限（长 ≠ 信息多） | 报告中声明局限；备选: embedding 向量模长（无意义）→ 维持 token 数 |
| J6 覆盖范围 | budget scan 结果无树，需回 checkpoints/ 取 | 核对 checkpoints/ 里哪些 run 的树还在（archive 已核验 11 个） |

## 正交性自检

- J1/J2（读取）vs J3/J4（匹配）vs J5（计算）vs J6（应用）：读→配→算→用，不重叠 ✓
- 与 T-PR-17：T-PR-17 用旧 judge 先跑（不阻塞）；新 judge 出来后重打 T-PR-17 数据做 dual-track ✓
- 与 K7：K7 在跑（719_r2），本任务纯本地 CPU/MPS，不占 vLLM ✓
- 与旧 judge（score.py 系列）：并存不替换，dual-track 对照 ✓

## 完备性自检

D 拍板三要素 = ①embedding 处理（J3）②LLM 只兜底 gold 无近似（J4）③Mac 本地跑（J3 环境已验证 MPS ✅）。全覆盖。
D 洞察三指标 = ①压缩率（J5）②损失程度（J5 覆盖率）③Pareto 边界（J5）。全覆盖。

## 执行顺序

1. J1+J2 解析器（先跑通"能读到树"）
2. 下载 embedding 模型（后台，~2.3GB）
3. J3 匹配 + 标定集（人工造对，~30min）
4. J4 兜底 prompt + 首跑
5. J5 指标 + J6 重打历史 + 相关性报告
