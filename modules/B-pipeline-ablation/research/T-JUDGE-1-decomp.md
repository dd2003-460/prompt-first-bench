# T-JUDGE-1 — 客观 judge：embedding 匹配 + LLM 兜底（decomp）

**发起**: 2026-11-22 D 拍板："embedding 处理，LLM 只负责处理 gold 上没有近似的情况；embedding MacPro 本身可以跑"
**动机**: D 洞察——领域知识有客观完整结构（gold 树），压缩率/损失/Pareto 边界可计算，judge 不该依赖 LLM 主观打分。当前 judge（27b 自评）绝对值不可信、方差 ~0.1，是 K7 Pareto 分析和 T-PR-17 因果归因的上游瓶颈。
**定位**: 离线后处理打分脚本（读 checkpoint 树 + gold 树 → 匹配 → 计算指标），不碰 SM 生成循环，符合固化约束。所有历史 run 免费重打。

**编号约定**: J1-J6 = 本任务分解树子项（前缀 = 任务首字母，各 decomp 独立编号，非全局）。文中出现的 K7 = research-agi-budget goal 的预算扫描（design 文档 item 标签），跨任务引用时带全名。

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
├── J6. 重打历史数据 + dual-track 对照
    ├── 范围: budget scan 13 run（✅ 已打，K7 719_r2/r3 完成后补 2）
    │   + matched 批 30 run（树体不在盘上，只有 2/30 节点数命中归档 → 跳过）
    │   + 9 棵 checkpoint 树（gpu 3 棵 = K7 719_r2 活中间状态 ❌ 无效; nat/soc 6 棵 = 旧树 ✅）
    ├── 旧 judge 分数位置: runs_budget_scan/*.json 内嵌 judge.scores（15 点 0/1）+ depth_score
    ├── 树体位置: checkpoints/archive/budget-*/runs-s5-sm-gpu.json（错位一格映射已验证）
    ├── 判据: 新覆盖率 vs 旧 depth_score 相关性（Spearman ρ）
    │   ρ > 0.7 → 新 judge 可信且更客观；ρ < 0.5 → 测的不是同一构念，回查匹配质量
    │   ✅ 首跑结果（n=13, 2026-11-22, 旧 gold 16 单元, 已作废备份 tjudge1-dualtrack-wronggold.json）:
    │   - 旧 cov15 vs 新 cov16: Spearman = -0.122（零相关）
    │   - depth vs 旧 cov15: Spearman = 0.785（强相关）
    │   - depth vs 新 cov16: Spearman = 0.036（零）
    │   → 旧 judge "coverage" 实际测答案长度/深度（长答案覆盖更多 rubric 点）
    │   → 新 embedding judge 测特定 gold 单元是否文本存在
    │   → 两者测不同构念，互补不冗余
    │   → 新 judge confirmed 精度差（抽查: 0.65-0.79 sim 大量"主题相关但没真覆盖"）
    │   → 结论: 0.65 阈值对 confirmed 口径太松; embedding judge 召回高、精度低
    │   → 修正方向: confirmed 需 LLM 二次确认（不只磁体），或阈值提到 0.75+
    │   ✅ 重打（n=13, 2026-11-22, J7 修正后 36 单元 gold）:
    │   - 新 cov36 (confirmed): 0.111-0.306, 含 pending 0.333-0.611
    │   - 旧 cov15 vs 新 cov36: Spearman = -0.336（仍零/负相关）
    │   - depth vs 新 cov36: Spearman = -0.221（零）; depth vs 旧 cov15: 0.785（不变）
    │   → 构念结论不变: 旧 judge = 长度代理, 新 judge = gold 单元存在性
    │   → 新发现: 719_r1 (665 节点) 新 cov = 0.167 与 150_r1 (392 节点) 持平
    │     → 预算从 150→719 没有提升 gold 覆盖（与 K7 预算-质量弱相关一致）
    │   → 磁体单元 6-16/run（enriched text 后更严重）→ LLM 兜底量会大,
    │     J4 跑前需重新生成 fallback 清单（旧 102 条作废）
├── J8. 公式 judge（第三轨，机械验证，2026-11-22 D 提出"公式当节点结果判定"）
    │   动机: 旧 LLM judge=长度代理, embedding judge=文本存在性(精度低)。
    │   公式 judge 把判定降到计算层: 结构对不对(sympy 化简差为0) + 系数在不在区间
    │   + 排序对不对。三层全机械, 不依赖 LLM/embedding。
    ├── 设计（D 2026-11-22 两问确认）:
    │   ① 公式验证器只验结构, 不纠结系数值 —— 恒等式/定义式(N-0/N-1/N-3.1)结构唯一,
    │      经验系数(MFU/η_bw/duty/p_fail)验区间+弹性加权(BOUND); 终极验证=选卡排序
    │      (系数分歧不改变赢家 3090×4/W4/n=2 就不影响结论)
    │   ② 深度评判=结构对齐度, 不是节点数 —— gold 深度 5 由停止准则定义
    │      (S-a 信息充足停/S-b 黑盒停/S-c SHARED 停); 显卡种类在 N-5 列候选不逐个展开,
    │      MFU 展开到 NCU 层(可测量影响排序), duty 停 N-2.1(业务数据不可推导)。
    │      "深度"= 模型树在 gold 该展开处展开/该停处停, 机械可算, 比长度代理客观。
    ├── 防 hack: tricky 代数独立点输入(√2,√3,1/√5,√7,√6)。标准输入(3090×4/W4)
    │   模型可能背过, tricky 输入必须真算; 两公式在足够多代数独立点输出相同=同一公式。
    ├── 落地（6d568d293）:
    │   gold-gpu-formulas.json: 36 单元 × {kind: formula/param/ncu/constraint/set,
    │       expand: split/leaf, sympy 公式, ref 区间, share/bound 弹性}
    │   tjudge1_formula.py: sympy 结构等价 + tricky 数值验证 + 不等式布尔化
    │   自检: 12/13 数值通过(N-3.1.3 Σ 恒等式走结构验证, 预期)
    │   150_r1 冒烟: 29/122 节点含可提取公式, 19 sympy 可解析;
    │   结构匹配 0 命中 = 模型公式符号体系与 gold 不对齐(模型用 Total_Mem/Weights_MB,
    │   gold 用 c_pass/c_hour) → 需 LLM 补写对齐符号(微信在做, 预算无所谓)
    ├── 与现有 judge 关系: 第三轨, 最客观(机械)。三轨互补:
    │   embedding=提到没有(文本存在性), 公式=算对没有(计算正确性), 旧 LLM=废弃
    │   两者都过=强确认; 只过 embedding 没过公式=提到但算错; 只过公式没过 embedding=
    │   算对但换说法
    └── 缺口: calc.py 不在仓库(gold-tree.md 引用但缺失), 参考值散在 gold-tree.md 文本
        (594 TFLOP/14-27-54 GB/774-1034-1574 GB/s/42.8-49.3-8.0%), 已提取进 sidecar ref 字段
        ✅ 已解决(2026-11-22, 963206281): calc.py 从 L3/L4/L5 文档无损重建
        (bench/rubric-v3/tasks/T0-local-27b/reference/calc.py), 4锚验证全过
        ✅ L0 自洽性通过(2026-11-22): sidecar 5/5 份额 + 1/1 带宽门槛重算命中
        (T-JUDGE-1-L0-20261122.md); 关键口径: t_decode 除以 n, bw_ok=(W+KV)×20 tok/s
└── J7. gpu 题目统一 + bench 完善（2026-11-22 D 指令"统一题目，只跑 gpu"）
    ├── J7-1 关键发现: gpu qid 下混着两道题 ——
    │   │   QUESTIONS['gpu']（K7 实际跑）= 本地工作站推理 Qwen3-27B 选卡方案
    │   │   gold/Q1.md（tjudge1 旧映射）= H100 SXM vs PCIe 吞吐差异（另一道题）
    │   │   真正的 gpu 题 gold = bench/rubric-v3/ablation/gold-tree.md
    │   │   （37 节点/深度 5/17 叶子, frozen ed552c4, c_pass 成本分解树）
    │   │   → 之前所有 gpu 新 judge 结果（J3 阈值标定/J5 首跑/J6 dual-track 的 cov16）
    │   │     都是拿错题的 gold 算的，数值作废，需重打
    │   └── 修复（3f5c713f7）: load_gold('gpu') → 37 节点树; enriched sidecar
    │       gold-gpu-units.json（36 单元, text 与 SM claim 同语言风格, 原树冻结不修改）
    │       冒烟（150_r1, 392 节点）: 0.65 阈值覆盖 6/36 → 20/36
    ├── J7-2 未覆盖 16 单元的结构: 6 个 = NCU 微架构层（N-3.1.3.x/N-3.2.4.x, 27b 能力上限外,
    │   已证不可达）; 其余 = 摊销/利用率/带宽系数等中间层（best sim 0.55-0.69, 差一点过线）
    └── J7-3 bench 完善候选（待 D 圈选）:
        ① NCU 层 6 节点从匹配分母剔除或单列"超纲层"（coverage 只算可达层 30 单元）
        ② enriched 后 0.65 阈值 confirmed 精度需重抽检
        ③ 权威题面裁定: rubric-v3 V0-baseline 题面 vs QUESTIONS['gpu'] 措辞不同
        ④ nat/soc 正式弃用（flat 6/7 点太粗）, 历史数据保留
        ⑤ 双 gold（第三方/异族独立建同域 gold）= 发表线构念效度硬需求
```

## 缺口清单

| 子项 | 缺什么 | 补法 |
|---|---|---|
| J1 gold 解析 | Q1-Q5 的 markdown 格式未逐一核（Q9 已核: 代码块包裹 + N-x 编号） | 解析前逐文件 head 核格式 |
| J3 模型选型 | ✅ 已定 bge-m3（dim 1024，MPS 跑通，缓存已落） | — |
| J3 阈值 | ✅ 首跑标定 0.65 + 磁体降级（0.60 假匹配多 / 0.70 覆盖塌） | 后续: 人工标定集（20 正例 + 20 负例对）验证 ROC 拐点 |
| J4 触发率 | ✅ 首跑 29 条（r2 磁体 5 单元）；脚本就绪，**等 K7 释放 vLLM 后跑** | 跑完重算 confirmed 覆盖率 |
| J4 数据失效 | 首跑后扩 3-qid 生成的 102 条 fallback 清单（tjudge1-llm-fallback-all.json）基于旧 gold（错题）→ 作废 | K7 释放后基于 36 单元 gold 重新生成 fallback 清单再跑 J4 |
| J5 信息量定义 | token 数代理的局限（长 ≠ 信息多） | 报告中声明局限；备选: embedding 向量模长（无意义）→ 维持 token 数 |
| J6 覆盖范围 | budget scan 结果无树，需回 checkpoints/ 取 | ✅ 已解决: 归档错位一格映射（目录名=新 run 时间戳, 内容=上一 run）, 13/15 run 树体在盘 |
| J6 构念差异 | 旧 cov15 与 depth 强相关(0.785)但与新 cov16 零相关(-0.122) | 报告必须分开报告两个构念; 旧 judge 的"coverage"≈长度代理, 新 judge 测单元存在性 |
| J3 阈值精度 | 0.65 对 confirmed 口径太松（抽查大量主题相关假匹配） | 方向: ①confirmed 全送 LLM 二次确认 ②阈值 0.75+ ③人工标定集 ROC（待 K7 后做） |
| matched 批树体 | 30 棵中 28 棵不在盘上（archive 66 棵按 n_nodes 只命中 2） | 不重跑（vLLM 在跑 K7）; matched 批 dual-track 放弃, 用 budget scan 15 run 替代 |

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
