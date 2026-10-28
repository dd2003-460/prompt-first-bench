# 27B 本地部署硬件选型 — Goal 文档（stage-gate: 27b-hw-costperf-decomp）

> 创建：2026-10-28
> 阶段：01-create-goal → 完成后推进 02-setup-repo
> 方法论：decomp 最终版 `loop/prompt-first/01-goal-decomposition.md`（因素分解）+ stage-gate research-task-template

---

## 【目标】
为本地部署 27B 级模型（以 Qwen3.8-27B 为基准）选出 2026 年 10 月中国大陆市场性价比最高的硬件系统，产出 1 个主推方案 + 分层替代方案，性价比排序可追溯。

## 【阶段】
27B 硬件选型项目，阶段 01（创建 Goal）。因素分解已完成（subagent sa-0-250a3c7f，3043s）。

## 【SOP 索引】
- `~/.hermes/.stage-gate/research-task-template.md`（调研任务模板）
- `agents/goal-template.md`（goal 五字段格式）
- `loop/prompt-first/01-goal-decomposition.md`（因素分解方法论，最终版）
- `projects/知识/D1-knowledge-base/notes/27b-hw-decomp/01-factor-decomposition.md`（阶段 01 工件）

## 【验收标准】
1. 因素分解：7 顶层因素正交覆盖 + 递归到叶子原子 + H/D/G 三分区（已完成，见 01 工件）
2. 阶段 02 证据：G1-G12 空缺全部有核验证据或明确标注无法核验，价格类带快照时间戳
3. 性价比排序：≥5 个候选的 元/(tok/s) 或综合打分排序，公式可复算
4. 推荐方案：1 主推 + ≥2 分层替代，每个有性能/成本/风险/软件可行性四维证据
5. 交叉检验：关键事实（价格/速度/架构参数）≥2 独立源

## 【失败降级】
- ego-browser 不可用 → 本地 web_search（本环境 web_search 实际可用）
- 某候选价格查不到 → 标注"无现货数据"并给区间估计 + 保守假设
- 用户不答澄清项（G7/G8/G10/G12）→ 按性价比优先默认假设并显式标注

---

## 1. 本地背景扫描

| 必查项 | 查了吗 | 搜索命令/路径 | 发现 |
|--------|--------|---------------|------|
| 相关项目目录 | ✅ | `search_files *gpu* projects/` + `find archive/gpu-to-decomp` | D1-gpu-research-2026（已归档，04.5 交叉验证）、D1-gpu-inference-hardware、D1-knowledge-base/notes/gpu-inference-hardware.md（KB 第5篇） |
| 已有调研/报告 | ✅ | `read_file projects/知识/D1-knowledge-base/notes/gpu-inference-hardware.md` + 本轮初版报告 | gpu-inference-hardware.md（Qwen3.8-27B 组合实测、PRO 5000/6000 数据、TCO 框架）；27b-local-hardware-costperf-2026-10.md（初版性价比报告，本轮产出，作为待核验线索） |
| 相关记忆 | ✅ | MEMORY.md 已在上下文 | D1-gpu 04.5 交叉验证 r1 完成 6 处修正 + 7 项降级；advance 门禁规则（attribute_matrix 全字段 + web-llm 门禁） |
| 用户过往讨论 | ✅ | `session_search "27B 本地部署 GPU 硬件 性价比"` | 2026-10-27 三个相关 session：decomp-research goal（T0 27B bench gold L0-L6）、gpu-27b-cost goal、本轮 mvqrea35o8drz6；D1-gpu-20260424 旧 goal 卡在 stage 05 web-llm 门禁 |

**小结**：本地已有 3 项可复用资产（KB 笔记、初版报告、bench gold 设计），需新增 = 阶段 02 的实时价格/性能核验。

## 2. 调研对象全集

| 候选 | 纳入/排除 | 理由 |
|------|-----------|------|
| C1 NVIDIA 消费级（RTX 5090/5080/5070Ti/5060Ti） | ✅ 纳入 | 主流选择，但受涨价/停产传闻影响，需核验（G2/G3） |
| C2 NVIDIA 专业/数据中心（RTX PRO 5000/6000、二手 A100/H100/A6000/L40S） | ✅ 纳入 | 大显存选项，价格高，作中高档对照 |
| C3 Apple Silicon（Mac Studio M5 Max/Ultra、Mac mini M5/M6） | ✅ 纳入 | 用户已有 Mac 跑 MLX，零迁移成本路径（D6） |
| C4 AMD（RX 7000/8000/9000） | ✅ 纳入 | 价格通常更低，ROCm 生态待核验（G6） |
| C5 二手/多卡（2-4 卡工作站、二手服务器） | ✅ 纳入 | 历史性价比之王（3090/4090），质量风险待核验（G99） |
| C6 国产/其他（昇腾/摩尔线程） | ✅ 纳入（待核验） | 候选完整性（G11），生态不成熟则记录排除理由 |
| C7 云/租赁 | ⏸ 边界参照 | 不作主选，仅用于性价比边界对照 |

## 3. 正交维度拆解

顶层 7 因素（F1 负载需求 / F2 候选供给 / F3 成本 / F4 性能 / F5 软件生态 / F6 风险 / F7 决策框架）正交且覆盖完整，递归到叶子的完整树见 `01-factor-decomposition.md` §2。

维度正交性自检：需求（F1）× 选项（F2）× 价格（F3) × 性能（F4）× 可行性（F5) × 风险（F6) × 裁决（F7）两两可同时取不同值 ✅
完备性自检：性价比 = F4/F3 受 F5 门禁、被 F6 修正、targeting F1、从 F2 选、由 F7 裁决，无落空 ✅
原子性自检：每叶子为 H/D 最小事实或指向 G# ✅

## 4. 量化定义

| 指标 | 公式 | 数据来源 | 单位 |
|------|------|---------|------|
| 显存需求 | 权重(B/param×quant) + KV(2×layers×kv_heads×head_dim×ctx×batch×bytes) + 激活 + 10%余量 | G1 config.json + D1/D2 | GB |
| decode 理论上限 | 显存带宽(GB/s) / 权重占用(GB) | G2 规格 | tok/s |
| 性价比（主指标） | 系统总价(元) / 实测 decode tok/s（同量化同上下文口径） | G2+G5 | 元/(tok/s) |
| 性价比（辅指标） | 综合打分 = w1×速度 + w2×容量余量 + w3×(1/价格) + w4×(1/风险)，权重待 G7 | G7 | 0-100 |
| 电力成本 | TDP(kW) × 24h × 365 × 电价(元/kWh) | G2 TDP | 元/年 |

## 5. 任务书（派发用）

见 03-dispatch 阶段生成。核心 = 01 工件 §7 第一批行动（G1 架构 → G3 市场核验 → G2 价格快照 → G5 实测搜集 → 用户澄清批）。

## 6. 验收标准（量化门禁）

- [x] 本地背景 4 项全查有证据
- [x] 候选全集 7 类含排除理由
- [x] 正交+完备+原子自检通过
- [x] 指标全有公式无模糊词
- [x] 任务书含失败降级
- [ ] get_goal 验证（create_goal 工具不在当前工具集，以 stage_init 落库为验证）

---

## Reviewer 门禁自检（阶段 01 工件）

按 01 prompt Reviewer 质检标准 8 项：覆盖因素✓ / H-D-G 分区✓ / 无关键未知假定✓ / 研究问题可追溯✓ / 02 可开工✓ / 未验证均标注✓ / 路径具体未伪装✓ / 预算未擅自设定✓。

**Verdict: PASS**（Lead 独立评审，非 subagent 自判）
