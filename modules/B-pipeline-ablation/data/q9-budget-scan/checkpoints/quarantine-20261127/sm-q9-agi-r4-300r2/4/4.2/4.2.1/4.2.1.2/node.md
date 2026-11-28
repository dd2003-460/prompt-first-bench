# N169: MTP 接受率 η_avg 的实测校准方法：在 vLLM 日志中记录 draft_tokens_accepted / draft_tokens_proposed

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

MTP 接受率 η_avg 的实测校准方法：在 vLLM 日志中记录 draft_tokens_accepted / draft_tokens_proposed 的比率，滑动窗口平均；若连续 100 步 η_avg < 0.25，触发降级逻辑：将 num_speculative_tokens 从 4 降至 2，并重新测量 S_new = 1 + 2 * η_avg_new；若 S_new > S_old * 0.9，则保持降级状态直至 η_avg 回升至 >0.3

## Corrected Claim

MTP 接受率 η_avg 的实测校准方法：在 vLLM 日志中记录 draft_tokens_accepted / draft_tokens_proposed 的比率，滑动窗口平均；若连续 100 步 η_avg < 0.25，触发降级逻辑：将 num_speculative_tokens 从 4 降至 2，并重新测量 S_new = 1 + 2 * η_avg_new；若 S_new > S_old * 0.9，则保持降级状态直至 η_avg 回升至 >0.3

## Evidence

先验知识/题面给定，逻辑校验通过
