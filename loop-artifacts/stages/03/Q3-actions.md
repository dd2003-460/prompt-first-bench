# 阶段 03：Q3 Pricing-Enhanced 行动分解

**依据**：阶段 01 因素分解 + 阶段 02 证据 + 阶段 02.5 交叉核验边界

---

## 目标交付物

`loop-artifacts/stages/04/Q3-execution-log-r2.md` —— 含定价强制段合规的完整执行日志与结论

---

## 行动步骤（原子化、可验证、标注 owner/依赖/并行）

### A. 成本模型计算（核心量化步骤）

| 步骤 | 动作 | 输入 | 产出 | 验收方式 | Owner | 依赖 | 并行 |
|------|------|------|------|----------|-------|------|------|
| A1 | 计算自托管边际小时成本 `c_hour_marginal` | RTX 3090 云价格 $0.25/hr (Community) + 电力 $0.15/hr | `c_hour_marginal = $0.40/hr` | 单元测试：数值可复现 | agent | — | ✅ |
| A2 | 计算自托管全包小时成本 `c_hour_full` | 硬件折旧 $0.55/hr + 电力 $0.15/hr + 托管/带宽 $0.10/hr | `c_hour_full = $0.80/hr` | 敏感性：折旧年限 3/5 年 | agent | — | ✅ |
| A3 | 计算 vLLM 最优部署吞吐 `λ_out_vllm` | 社区基准：双 TP=2 实例，并发 8-32，持续 ~900-1,100 tok/s | `λ_out_vllm = 900 tok/s (保守) = 3.24M tok/hr` | 区间 [630, 1170] tok/s 对应敏感性 | agent | 02.5 质疑 3 | ✅ |
| A4 | 计算 SGLang 吞吐 `λ_out_sglang` | vLLM × 1.10（保守 +10%） | `λ_out_sglang = 990 tok/s = 3.56M tok/hr` | 区间 [693, 1287] tok/s | agent | A3 | ✅ |
| A5 | 计算 TGI 吞吐 `λ_out_tgi` | vLLM × 0.95（先验区间 0.9-1.0） | `λ_out_tgi = 855 tok/s = 3.08M tok/hr` | 区间 [567, 1170] tok/s | agent | A3 | ✅ |
| A6 | 计算自托管 `c_serve`（边际成本视角） | `c_hour_marginal / λ_out` | 三框架 `c_serve_marginal` [¢/1k_out_tok] | 表格输出，含敏感性区间 | agent | A1, A3-A5 | ✅ |
| A7 | 计算自托管 `c_serve`（全包成本视角） | `c_hour_full / λ_out` | 三框架 `c_serve_full` [¢/1k_out_tok] | 表格输出，含敏感性区间 | agent | A2, A3-A5 | ✅ |
| A8 | 计算 API 方案 `c_serve` | Token 价格（含缓存/批量折扣） | Groq/Together/Fireworks `c_serve_api` | 表格输出，标注模型可用性约束 | agent | 02 证据 | ✅ |

---

### B. SLO 可行性验证（约束检查）

| 步骤 | 动作 | 输入 | 产出 | 验收方式 | Owner | 依赖 | 并行 |
|------|------|------|------|----------|-------|------|------|
| B1 | vLLM TPOT p99 对比 SLO | 社区基准：TP=2 并发 8 时 TPOT p99 ~35ms | `vllm_slo_ok = True (TPOT p99 < 60ms)` | 布尔判定 + 数据引用 | agent | 02 证据 | ✅ |
| B2 | SGLang TPOT p99 对比 SLO | ttlab: c=64 时 ITL p99 101ms (vLLM 231ms) → 推断 c=8 远优 | `sglang_slo_ok = True (更优)` | 定性推断 + 引用 | agent | 02.5 矛盾 5 | ✅ |
| B3 | TGI TPOT p99 对比 SLO | 无公开数据，架构同 vLLM | `tgi_slo_ok = Likely True` | 标记需实测 | agent | 02.5 矛盾 7 | ✅ |
| B4 | 原生 transformers SLO | 架构无 continuous batching | `native_slo_ok = False` | 直接淘汰 | agent | Gold Q3 | ✅ |
| B5 | Groq API SLO | LPU 极低延迟，p99 TPOT 极优 | `groq_slo_ok = True` | 引用第三方实测 | agent | 02 证据 | ✅ |
| B6 | Together/Fireworks 共享 API SLO | 共享端点有队列延迟风险 | `shared_api_slo_ok = Conditional` | 标记需专用端点 | agent | 02 证据 | ✅ |
| B7 | 并发容量检查 | vLLM TP=2×2: n_mem 受 KV 管理优势支持 >32 | `concurrency_ok = True (all but native)` | 显存/并发模型验证 | agent | 02 证据 | ✅ |

---

### C. 运维/功能/可行域打分（次级 tie-breaker）

| 步骤 | 动作 | 输入 | 产出 | 验收方式 | Owner | 依赖 | 并行 |
|------|------|------|------|----------|-------|------|------|
| C1 | 部署复杂度打分 | 官方文档/社区：native < TGI (Docker) < vLLM < SGLang | 1-5 分表 | 一致性检查 | agent | Gold Q3 N-4.1 | ✅ |
| C2 | 量化/投机解码/长上下文支持矩阵 | 官方文档 | 支持矩阵表 | 完整性检查 | agent | Gold Q3 N-5 | ✅ |
| C3 | 硬件兼容性（3090 消费级卡） | 官方 CI/社区 | 全通过（均支持 Ampere） | 无阻塞项 | agent | Gold Q3 N-6.1 | ✅ |
| C4 | 模型支持（自有 27B 权重） | 官方支持列表 | vLLM/TGI/SGLang/native: 支持；API: 仅标准模型 | Groq 淘汰（自有权重场景） | agent | Gold Q3 N-6.2 | ✅ |

---

### D. 综合决策矩阵构建

| 步骤 | 动作 | 输入 | 产出 | 验收方式 | Owner | 依赖 | 并行 |
|------|------|------|------|----------|-------|------|------|
| D1 | 构建成本对比表（边际/全包/API） | A6, A7, A8 | 完整 `c_serve` 对比表 [¢/1k_out_tok] | 所有候选覆盖，单位统一 | agent | A6-A8 | ❌ |
| D2 | 构建 SLO 可行性表 | B1-B7 | 约束通过/失败矩阵 | 硬约束淘汰逻辑清晰 | agent | B1-B7 | ❌ |
| D3 | 应用决策规则（Gold Q3 §6） | D1, D2, C1-C4 | 条件化推荐规则 | 规则可追溯到证据 | agent | D1, D2, C1-C4 | ❌ |
| D4 | 敏感性分析 | A3-A5 区间、A1-A2 区间 | 关键参数变动对排名影响 | 龙卷风图/表格 | agent | D1 | ❌ |
| D5 | 生成执行日志草稿 | 以上所有 | `Q3-execution-log-r2.md` 初稿 | 格式合规，含强制段标注 | agent | D1-D4 | ❌ |

---

### E. 定价强制段合规检查（任务特有）

| 步骤 | 动作 | 输入 | 产出 | 验收方式 | Owner | 依赖 | 并行 |
|------|------|------|------|----------|-------|------|------|
| E1 | 核查所有价格标注 [as of YYYY-MM-DD] | D5 草稿 | 合规清单 | 100% 覆盖 | agent | D5 | ❌ |
| E2 | 核查每价格 ≥2 独立来源 | 02 证据表 | 合规清单 | 标注 [UNVERIFIED]/[CONTRADICTION] | agent | 02 证据 | ❌ |
| E3 | 核查差异 >20% 标 [CONTRADICTION] | 02.5 矛盾表 | 合规清单 | 全部标注到位 | agent | 02.5 | ❌ |
| E4 | 核查无法确认标 [UNVERIFIED] | 02 证据表 | 合规清单 | 全部标注到位 | agent | 02 | ❌ |
| E5 | 最终润色与提交 | E1-E4 修正后 | 最终 `Q3-execution-log-r2.md` | 通过 Reviewer 验收 | agent | E1-E4 | ❌ |

---

## 关键失败替代路径

| 失败场景 | 影响步骤 | 替代方案 | 停止条件 |
|----------|----------|----------|----------|
| vLLM 基准数据不可靠 | A3, A6, A7 | 使用理论峰值上限估算（936 GB/s × 4 × MFU 0.3-0.5） | 无任何基准数据时 |
| API 价格单一来源 | A8, E2 | 标记 [UNVERIFIED]，仅作参考不参与排名 | 核心候选均无双源时 |
| SLO 实测环境不可用 | B1-B6 | 依赖文档/社区定性判断，标记需实测 | 无任何延迟数据时 |
| 硬件价格波动大 | A1, A2 | 给出区间而非点估计，报告敏感性 | — |

---

## 执行顺序拓扑

```
Phase 1 (并行):  A1, A2, A3, A4, A5, A8, B1-B7, C1-C4
    ↓
Phase 2 (串行):  A6, A7 (依赖 A1, A3-A5)
    ↓
Phase 3 (串行):  D1, D2 (依赖 Phase 1-2 全部)
    ↓
Phase 4 (串行):  D3, D4 (依赖 D1, D2)
    ↓
Phase 5 (串行):  D5 (依赖 D3, D4)
    ↓
Phase 6 (串行):  E1-E5 (依赖 D5)
```

**并行度**：Phase 1 最多 15 个并行原子步骤（均为 agent 可离线执行的计算/查表）

---

## 验收汇总表（阶段 04 对照用）

| 验收项 | 对应步骤 | 通过标准 |
|--------|----------|----------|
| 所有候选 `c_serve` 已计算并标注单位/日期/来源 | A6, A7, A8, D1 | 表格完整，无缺漏 |
| 硬约束 SLO 逐项判定，未达标者淘汰 | B1-B7, D2 | 布尔矩阵清晰 |
| 定价强制段 5 条规则 100% 合规 | E1-E5 | 零遗漏 |
| 条件化推荐规则可追溯到证据 | D3 | 链条完整 |
| 敏感性分析覆盖关键不确定参数 | D4 | ±30% 区间不改变排名或标注风险 |

---

**阶段 03 完成**，可进入阶段 04 执行。