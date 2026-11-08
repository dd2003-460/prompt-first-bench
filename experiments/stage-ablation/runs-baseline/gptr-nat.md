Source: https://link.springer.com/chapter/10.1007/978-3-319-44615-8_14
Title: Analysis of LRU Cache Trees with a Power Law Reference Distribution | Springer Nature Link
Content: Analysis of LRU Cache Trees with a Power Law Reference Distribution | Springer Nature Link
Skip to main content
Advertisement
Analysis of LRU Cache Trees with a Power Law Reference Distribution
Conference paper
First Online: 28 August 2016
pp 162–167
Cite this conference paper
Access provided by SpringerLink China CAS eBook Consortium - STM Collection
Download book PDF
Download book EPUB
Save conference paper
View saved research
Information Technologies and Mathematical Modelling - Queueing Theory and Applications (ITMM 2016)
Analysis of LRU Cache Trees with a Power Law Reference Distribution
Download book PDF
Download book EPUB
Abstract
We investigate the performance of a LRU cache replacement policy. Regarding the hit and miss ratios of Zipf-distributed frequencies of object requests in a cascade of LRU caches, new explicit, computationally tractable formulae are derived.
Access provided by SpringerLink China CAS eBook Consortium - STM Collection. Download conference paper PDF

Source: https://link.springer.com/content/pdf/10.1007/978-3-319-44615-8_14.pdf
Title: 
Content: Analysis of LRU Cache Trees with a Power Law
Reference Distribution
Udo R. Krieger1(B) and Natalia M. Markovich2
1 Otto-Friedrich-Universit¨at, 96045 Bamberg, Germany
udo.krieger@ieee.org
2 Russian Academy of Sciences, 117997 Moscow, Russia
markovic@ipu.rssi.ru
Abstract. We investigate the performance of a LRU cache replacement
policy. Regarding the hit and miss ratios of Zipf-distributed frequencies of
object requests in a cascade of LRU caches, new explicit, computationally
tractable formulae are derived.
Keywords: LRU cache performance · Che’s approximation · Cache
trees
1
Modeling LRU Cache Trees
Following Che et al. [3] and Fricker et al. [4], we consider a hierarchical cascade
of LRU caches in an access and backbone infrastructure of a packet-switched
next generation network (see also [1]).
We assume that we have four layers in a tree-like hierarchy:
– Layer 3: The consumers consist of clients with a very small browser cache.

Source: https://novasolver.jp/en/tools/cache-hit-rate-lru.html
Title: Cache Hit Rate Lru Simulator - NovaSolver
Content: Cache Hit Rate Lru Simulator - NovaSolver
Interactive simulator
Cache Hit Rate Lru Simulator
Compare hit-rate curve, stack-distance sketch, and latency breakdown to see where adding cache stops helping.
Parameters
Cache capacity C 6 slots
Number of slots the cache can hold at once.
Working-set size W 16 keys
Total number of distinct keys that get accessed.
Locality α 0.90
How strongly access concentrates on a few keys (Zipf). 0 = uniform.
⏸ Pause animation
While paused, move the sliders to update the result instantly.
Real-time LRU cache animation
Green flash = HIT (move the key to the front); red flash = MISS (evict the least-recently-used slot at the tail, insert at the front). Left is MRU (most-recently used), right is LRU (least-recently used). The request stream has Zipf-like locality.
Live stats
—
Cache capacity C
—
Total accesses
—
Hits
—
Hit rate
Model and equations
$$H \approx 1-\exp\left[-\alpha\frac{C}{W}\right],\quad H=\frac{\text{hits}}{\text{accesses}}$$

Source: https://novasolver.jp/en/tools/cache-hit-rate-lru.html
Title: Cache Hit Rate Lru Simulator - NovaSolver
Content: How do I judge whether Working set W or Cache capacity C matters more?
Move Working set W alone, then move Cache capacity C by a comparable amount and compare the change in Hit rate. Latency and load shows combinations where margin or performance changes quickly.
How should this result be used in practice?
Use it for Early sizing of web or API caches. Instead of trusting a single point, widen the input range and check whether Hit rate keeps enough margin before moving to detailed analysis.
What are the limits of this simplified model?
Real LRU hit rate depends strongly on the access distribution. This model uses a locality factor to study capacity sensitivity before detailed traces. Final decisions still require standards, measured data, detailed analysis, and vendor limits.
How to Use
Enter working-set size W (item count) and cache capacity C (item count)
Set locality α (0.2–8, default 2.2): higher values concentrate access on a subset and raise hit rate for the same capacity

Source: https://novasolver.jp/en/tools/cache-hit-rate-lru.html
Title: Cache Hit Rate Lru Simulator - NovaSolver
Content: $$H \approx 1-\exp\left[-\alpha\frac{C}{W}\right],\quad H=\frac{\text{hits}}{\text{accesses}}$$
Real LRU hit rate depends strongly on the access distribution. This model uses a locality factor to study capacity sensitivity before detailed traces.
How to read it
The hit-rate curve shows where capacity improvements saturate.
The stack sketch explains why recent items remain in cache.
The latency view shows miss rate turning directly into backend load.
Learn Cache Hit Rate Lru by dialogue
🙋
When reading Cache Hit Rate Lru, where should I look first? Moving Working set W changes both the plots and the result cards.
🎓
Start with Hit rate, but do not treat the number as the whole answer. Use LRU hit-rate curve to confirm the assumed state, then read Stack-distance sketch for the distribution or trend. The hit-rate curve shows where capacity improvements saturate.
🙋
I can see why Working set W changes Hit rate. How should I judge the influence of Cache capacity C?
🎓

Source: https://novasolver.jp/en/tools/cache-hit-rate-lru.html
Title: Cache Hit Rate Lru Simulator - NovaSolver
Content: 🙋
So if Hit rate is within the target, can I accept the condition?
🎓
Treat this as a first-pass review. It helps with Estimating database or CDN miss load and Comparing cache cost against latency improvement, but final decisions still need standards, measured data, detailed analysis, and vendor limits. The latency view shows miss rate turning directly into backend load.
Practical use
Early sizing of web or API caches.
Estimating database or CDN miss load.
Comparing cache cost against latency improvement.
FAQ
What should I read first in Cache Hit Rate Lru?
Start with Hit rate and Miss rate. Then use LRU hit-rate curve to confirm the assumed state and Stack-distance sketch to read distribution or bias. The hit-rate curve shows where capacity improvements saturate
How do I judge whether Working set W or Cache capacity C matters more?

Source: https://link.springer.com/chapter/10.1007/978-3-319-44615-8_14
Title: Analysis of LRU Cache Trees with a Power Law Reference Distribution | Springer Nature Link
Content: Layer 2: This layer of leaf caches at level 1 consists of a network of N LRU caches with the capacities \(C(L_1) = (C_1, \ldots , C_N)\) in the access network of an ISP. Each cache m serves M Poisson flows \(f_{mj}\) of object requests with rates \(\lambda _{mj}\). They are arising from all M object types \(j \in \mathcal{C}\) stemming from the clients at layer 3. The superimposed Poisson stream of cache m has the rate \(\varLambda _m = \sum _{j=1}^M \lambda _{mj}\). It arises from the splitting \(\varLambda _m = \varLambda ^{(1)} \cdot l(1)_m\) of the overall Poisson traffic of the clients with the rate \(\varLambda ^{(1)}\) into the offered load \(\varLambda _m\) of each cache m with probabilities \(l(1)_m\).
The individual miss and hit ratios of each stream i are given by \(\eta _{mi}^{(1)}, H_{mi}^{(1)}= 1- \eta _{mi}^{(1)}\) and the corresponding overall variants of cache m at level 1 by \(\eta _{m}^{(1)}, H_{m}^{(1)}= 1- \eta _{m}^{(1)}\), respectively.

Source: https://link.springer.com/content/pdf/10.1007/978-3-319-44615-8_14.pdf
Title: 
Content: cache m with probabilities l(1)m.
The individual miss and hit ratios of each stream i are given by η(1)
mi, H(1)
mi = 1−
η(1)
mi and the corresponding overall variants of cache m at level 1 by η(1)
m , H(1)
m =
1 −η(1)
m , respectively.
c
⃝Springer International Publishing Switzerland 2016
A. Dudin et al. (Eds.): ITMM 2016, CCIS 638, pp. 162–167, 2016.
DOI: 10.1007/978-3-319-44615-8 14
Analysis of LRU Cache Trees with a Power Law Reference Distribution
163
– Layer 1: This layer comprises one level 0 backbone cache of capacity C0 with
an overall miss ratio η(0) and hit ratio H
(0) = 1 −η(0).
– Layer 0: It comprises a fully interconnected network of servers oﬀering all
requested objects, e.g. provided by a CDN-like set of data centers.
2
Performance Analysis of LRU Cache Cascades
In the following we formulate a computationally tractable, matrix-oriented
framework that can be used to determine all relevant quantities of our cache

Source: https://novasolver.jp/en/tools/cache-hit-rate-lru.html
Title: Cache Hit Rate Lru Simulator - NovaSolver
Content: 🎓
Move Cache capacity C in small steps and watch Miss rate. That reveals which term is controlling the result. Real LRU hit rate depends strongly on the access distribution. This model uses a locality factor to study capacity sensitivity before detailed traces. A single operating point is not enough; sweep the realistic scatter range.
🙋
What is Latency and load for? It feels like the ordinary curve already tells the story.
🎓
Latency and load is for finding boundaries where the condition becomes risky or margin collapses quickly. The stack sketch explains why recent items remain in cache. In Early sizing of web or API caches, the important question is often what happens after a small change, not only the nominal value.
🙋
So if Hit rate is within the target, can I accept the condition?
🎓 Source: https://github.com/0Kriti0/Smart-Caching-System
Title: GitHub - 0Kriti0/Smart-Caching-System: Implementation and comparison of LRU and LFU cache eviction policies · GitHub
Content: Uniform Access
All keys have equal probability of being accessed
Skewed Access (80–20 pattern)
Small set of keys receive majority of accesses
Common in real-world systems (hot items)
Sequential Access
Keys accessed in increasing order
Minimal repetition between accesses
Performance Metrics
The system measures:
Cache hits
Cache misses
Cache hit rate (%)
Execution time (for comparison purposes)
Observations
Under uniform access, both LRU and LFU show similar performance
Under skewed access, LFU achieves higher hit rates due to frequency awareness
Under sequential access, hit rate remains low because repeated accesses are minimal
As cache size increases, performance of both policies converges
These results highlight that no single caching policy is optimal for all workloads.
Learning Outcomes
Through this project, I gained understanding of:
Cache eviction strategies
Time–space trade-offs
Real-world access pattern behavior
Algorithm performance evaluation

Source: https://toolgeist.kilnwp.com/t/cache-eviction-simulator
Title: Cache Eviction Simulator — LRU vs LFU vs FIFO vs Belady Optimal | Toolgeist
Content: When does LFU beat LRU, and when does it fail?
LFU wins when popularity is genuinely stable, which is why it leads on the skewed workload. It fails on shifting popularity: an item that was hot once accumulates a large count and then squats in the cache long after anyone stopped wanting it. Production systems therefore use aged or windowed LFU variants rather than raw frequency counts.
What is Belady's OPT and why include something unimplementable?
It is the offline optimal policy — evict whatever will be used furthest in the future — and it is provably the minimum achievable number of misses. As a benchmark it answers the question that actually matters when tuning: if OPT is barely ahead of your policy, stop tuning and buy more cache; if the gap is wide, your policy is the bottleneck.
Why does FIFO do worse than LRU?

Source: https://toolgeist.kilnwp.com/t/cache-eviction-simulator
Title: Cache Eviction Simulator — LRU vs LFU vs FIFO vs Belady Optimal | Toolgeist
Content: Cache Eviction Simulator — LRU vs LFU vs FIFO vs Belady Optimal | Toolgeist
Toolgeist › Developer
Cache Eviction Simulator — LRU vs LFU vs FIFO vs Belady Optimal
Four eviction policies racing on one identical access trace, plus Belady's OPT — the policy that evicts whatever is needed furthest in the future — as the provable lower bound on misses. OPT cannot be implemented because it requires knowing the future, but that is exactly what makes it useful: the gap between it and your policy is the only honest measure of how much room is left for a smarter algorithm versus how many misses are simply unavoidable. The lower bound property was verified across 60 traces, 3 capacities and 4 policies, and no online policy ever beat it.
How to use Cache Eviction Policy Simulator — LRU vs LFU vs FIFO vs Belady
Pick a workload shape — skewed, cyclic scan, uniform random, or hot set plus noise.
Drag the capacity slider and watch the hit rates diverge.
Compare each policy against the Belady OPT bar.

Source: https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/
Title: LFU vs. LRU: How to choose the right cache eviction policy | Redis
Content: Try for free
Common LFU and LRU pitfalls and how to avoid them
Choosing between LFU and LRU, even including a hybrid strategy combining the two, is only half the battle. Even when you select the right caching policy, implementation mistakes or oversights can affect performance and limit potential. Fixing these issues in retrospect can be difficult, so if you recognize common pitfalls early and avoid them, you can prevent cache degradation, unnecessary troubleshooting, and performance bottlenecks.
Pitfall #1: Choosing the wrong policy for your workload
Teams often select LFU or LRU based on theoretical advantages, ignoring actual data access patterns and workloads. It’s easy to assume your workload depends more on recency or popularity, and end up picking the wrong one.

Source: https://toolgeist.kilnwp.com/t/cache-eviction-simulator
Title: Cache Eviction Simulator — LRU vs LFU vs FIFO vs Belady Optimal | Toolgeist
Content: Why does FIFO do worse than LRU?
FIFO evicts by insertion age and never accounts for use, so an item accessed on every single request is still evicted once it becomes the oldest. LRU refreshes an item on every hit. You can see the difference directly: on the trace A B C A D with capacity 3, FIFO evicts A despite A having just been used, while LRU keeps it and evicts B.
Which policy should I actually use?
On typical skewed traffic LRU is a sound default and is cheap to implement. Reach for a frequency-aware policy when popularity is stable and long-lived, and add scan resistance when large sequential reads pass through. The genuinely important step is measuring against your own trace, because the right answer changes completely with workload shape — which is what this tool is for.
Does a bigger cache always mean more hits?

Source: https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/
Title: LFU vs. LRU: How to choose the right cache eviction policy | Redis
Content: Systems with popularity rankings: In some cases, most often with recommendation systems, user activity determines the popularity of items and the frequency with which they’re recommended. LFU works well when the popularity of an evergreen item is more important than sheer item recency.
Either policy presents a tradeoff. The LFU tradeoff is right for you when evicting frequently-used items is worse than evicting recently-used but less popular items.
When to choose LRU
In general, opt for LRU when recent usage is the strongest signal of future usage. If your workload benefits from a cache that tracks the data being made available as it’s processed, LRU is likely the right choice. The most common scenarios where LRU makes sense include:

Source: https://toolgeist.kilnwp.com/t/cache-eviction-simulator
Title: Cache Eviction Simulator — LRU vs LFU vs FIFO vs Belady Optimal | Toolgeist
Content: Compare each policy against the Belady OPT bar.
Read the hit-rate-versus-capacity curve to decide between a better policy and more memory.
Frequently asked questions
Why does LRU sometimes get a 0% hit rate?
Because a cyclic scan over a working set one item larger than the cache defeats it perfectly: the key LRU evicts is always precisely the one needed next. Select the cyclic scan workload with capacity 8 and you will see 0%, not merely a poor number. MRU — normally a bad idea — wins outright there. This is why database buffer pools detect sequential scans and switch strategy rather than trusting LRU blindly.
When does LFU beat LRU, and when does it fail?

Source: https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/
Title: LFU vs. LRU: How to choose the right cache eviction policy | Redis
Content: Poor performance during cyclic workloads.
Memory overhead for large caches.
Neither policy presents a case for one being better than the other. Choosing requires understanding their impact and your use case.
Get started with Redis for high-performance caching
Reduce latency and offload your database with in-memory caching.
Try Redis
LFU vs. LRU: How to know which policy is right for you
The decision between LFU and LRU isn't always binary. To find the optimal approach, you need to understand your workload, map out its patterns, and use caching capabilities that allow you to dynamically adapt to changing usage patterns.
When to choose LFU
In general, opt for LFU when popularity is more important than trendiness for supporting data access. The most common scenarios where LFU makes sense include:

Source: https://github.com/0Kriti0/Smart-Caching-System
Title: GitHub - 0Kriti0/Smart-Caching-System: Implementation and comparison of LRU and LFU cache eviction policies · GitHub
Content: Time–space trade-offs
Real-world access pattern behavior
Algorithm performance evaluation
System-level thinking beyond application code
Why This Project Matters
Caching is a fundamental optimization technique used in:
Web servers
Databases
Operating systems
Distributed systems
E-commerce platforms
Understanding cache behavior helps in designing scalable and efficient systems.
Future Improvements
Add TTL (Time-To-Live) based eviction
Implement hybrid caching policies (e.g., ARC)
Simulate concurrent access patterns
Extend analysis to memory usage trade-offs
Author: Kriti B.Tech CSE (Data Science)
4th Semester
About
Implementation and comparison of LRU and LFU cache eviction policies
Resources
Readme
Activity
Stars
0 stars
Watchers
0 watching
Forks
0 forks
Report repository
Releases
Packages
Contributors
Languages
You can’t perform that action at this time.

Source: https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/
Title: LFU vs. LRU: How to choose the right cache eviction policy | Redis
Content: Tailor eviction policies to each workload, ensuring they don’t have to generalize a policy across too many workloads.
Maintain strong isolation under memory pressure, ensuring that a spike in one tenant won’t evict data from another tenant.
Fine-tune eviction behavior, ensuring different decay rates, sampling sizes, and maxmemory settings are configured for each tenant.
Operationalize for efficiency, ensuring, for example, lower memory and faster TTLs for certain use cases without those settings affecting other tenants.
This flexibility helps companies avoid a one-size-fits-all strategy because, when it comes to eviction strategies, one size typically fits none.
Real-time performance and low latency
In the nuances around caching strategies and eviction policies, it can be easy to lose sight of the key priorities: Reducing latency and maintaining consistently high performance. As a corollary, the goal is to do both even during periods when the workload is heavy.

Source: https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/
Title: LFU vs. LRU: How to choose the right cache eviction policy | Redis
Content: Pitfall #3: Ignoring cache size and infrastructure limits
The best caching strategy can only do so much if your cache is too small. Inadequate sizing or ignored infrastructure constraints can lead to unexpected cache evictions or performance degradation, even with what would have been the right strategy otherwise.
To avoid this pitfall, regularly monitor your cache hit ratio and adjust your cache size as your data set or traffic volume grows. If it all becomes too burdensome to monitor, consider finding a caching provider that offers auto-tiering or other infrastructure efficiency optimizations.
Pitfall #4: Overlooking the importance of flexibility
Rigid caching implementations can make sense in one moment but suffer in the next. Seasonal shifts or sudden spikes can lead to firefighting as important items are evicted right when you need them most, degrading performance during peak times.

Source: https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/
Title: LFU vs. LRU: How to choose the right cache eviction policy | Redis
Content: Skewed data access patterns: In workloads with an asymmetric data distribution, which often follow the 80/20 rule (or the Pareto principle), where a small subset of items accounts for the majority of access requests, historical access count (or "popularity") is a strong predictor of future access. In these cases, LFU caching tends to perform well. For example, an ecommerce site might prioritize caching popular category pages, like “best sellers” or “accessories," because users tend to access these in nearly every session and they tend to remain popular over time.
Static hot data: In some situations, the “hot” data doesn’t change often, and an LFU policy can ensure this data remains cached. Some applications offer a range of APIs, for example, but a select few are often executed much more frequently than others. In these cases, LFU is typically best.

Source: https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/
Title: LFU vs. LRU: How to choose the right cache eviction policy | Redis
Content: Sections
LRU vs. LFU at a glance
LFU vs. LRU: What's the difference?
What is least frequently used (LFU) caching?What is least recently used (LRU) caching?
LFU vs. LRU: How to know which policy is right for you
When to choose LFUWhen to choose LRUWhen to consider a hybrid or flexible approach
Common LFU and LRU pitfalls and how to avoid them
Pitfall #1: Choosing the wrong policy for your workloadPitfall #2: Underestimating complexity in LFU implementationPitfall #3: Ignoring cache size and infrastructure limitsPitfall #4: Overlooking the importance of flexibilityPitfall #5: Not accounting for regional or global scaling needsPitfall #6: Ignoring cost and operational efficiency
What to look for in a caching solution
Flexible eviction strategiesReal-time performance and low latencyProven scalability and reliabilityEase of implementation and managementCost efficiency and ROI
Level up your caching strategy with Redis
View as Markdown
Share
Get started with Redis today

Source: https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/
Title: LFU vs. LRU: How to choose the right cache eviction policy | Redis
Content: LRU vs. LFU at a glance
Policy
Prioritizes
Best for
Strengths
Tradeoffs
LFU
Frequency of access
Predictable or skewed workloads (e.g. best sellers)
Retains popular items
More complex to tune; slower to adapt to change
LRU
Recency of access
Dynamic workloads (e.g. user sessions, dashboards)
Simple to implement; adapts quickly
May evict frequently used but less recent data
Businesses operating in environments where speed can differentiate them from other competitors, such as ecommerce, real-time analytics, and AI, have especially high stakes here. With the right cache eviction policies, businesses can suffer from declining user retention, lost revenue, and weakened competitive advantage.
To avoid this risk, figure out the nuances that distinguish LFU and LRU, learn how to flexibly implement and configure these policies, and identify which setup is best for your scenario.
LFU vs. LRU: What's the difference?

Source: https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/
Title: LFU vs. LRU: How to choose the right cache eviction policy | Redis
Content: To avoid this pitfall, perform a careful analysis of your real-world access patterns before selecting a cache eviction policy. Look at your access patterns across a long period of time and consider how select events, such as holiday seasonality, might change those patterns. Often, you might assume one or the other, and the data reveals a mix, meaning a hybrid or adaptive caching approach is best.
Pitfall #2: Underestimating complexity in LFU implementation
LFU is complex, and teams often implement it incorrectly, leading to performance issues. The combination of complexity and the risk of poor performance leads many teams to avoid it altogether.
To avoid this pitfall, look for vendors that provide caching capabilities with simple, streamlined LFU implementation options. Some even offer algorithms that track frequency and adjustable decay counters.
Pitfall #3: Ignoring cache size and infrastructure limits

Source: https://github.com/0Kriti0/Smart-Caching-System
Title: GitHub - 0Kriti0/Smart-Caching-System: Implementation and comparison of LRU and LFU cache eviction policies · GitHub
Content: Hash Maps
Doubly Linked List
Ordered Dictionary
Matplotlib (for visualization)
Project Structure
smart-cache-system/ │ ├── lru_cache.py # LRU cache implementation ├── lfu_cache.py # LFU cache implementation ├── performance_analysis.py # Benchmarking and visualization ├── test_cache.py # Functional test cases ├── requirements.txt └── README.md
Cache Policies Implemented
LRU (Least Recently Used)
Evicts the item that has not been accessed for the longest time
Implemented using:
HashMap for O(1) lookup
Doubly Linked List to maintain access order
Commonly used in operating systems and web caches
LFU (Least Frequently Used)
Evicts the item with the lowest access frequency
In case of frequency tie, Least Recently Used is evicted
Implemented using:
Key–frequency mapping
Frequency buckets using OrderedDict
Useful when access patterns are heavily skewed
Access Patterns Simulated
Uniform Access
All keys have equal probability of being accessed
Skewed Access (80–20 pattern)