# LeetCode Google Interview Discussions

_Updated: 2026-05-24 · 124 posts_


## [Google L3 Onsite Delayed Interview Once 592Ok](https://leetcode.com/discuss/post/7544550/google-l3-onsite-delayed-interview-once-592ok/)

_Crawled: 2026-05-24 · 211 words_


I was feeling not well and under prepared during the original interview day, so I emailed the recruiter and delayed the interview once.

Still nervious for this interview, and I got a time-series / interpolation style question (GPS-ish coordinates).

Here's what was asked:

```sql
There were two sorted streams by timestamp:
- a small set of “ground truth” checkpoints
- a set of noisy measured samples

Goal was to compute an overall error metric by, for each sample:
- locating the surrounding checkpoints in time
- interpolating the expected position at that timestamp
- computing distance error and summing across samples

What helped:
Two pointers scanning both arrays in one pass (O(n+m)) instead of doing a binary search per sample.

Edge cases I discussed:
- samples exactly on a checkpoint time
- multiple samples between the same two checkpoints
- zero time delta between checkpoints (avoid divide-by-zero)
- samples outside the checkpoint range (clarify expected behavior)
```

Pretty similar to a problem I practiced [here](https://leetcode.com/link/?target=https%3A%2F%2Fofferretriever.com%2Fquestions%2F18)

I think the interview went pretty well since I had seen a similar problem. So glad that I pushed it and just happen to worked out and got the question that I've practiced before.

Best of luck to everyone else with their Google interviews.

16

11

---

## [Career Suggestion Appreciated](https://leetcode.com/discuss/post/7638768/career-suggestion-appreciated-by-anonymo-bjg3/)

_Crawled: 2026-05-24 · 118 words_


Hello reader, I would be providing my current situation considering so I will appreciate it if you would give some genuine advice.

Experience: Currently in a service based company with 9 months of exp in java backend.

Current salary: 4LPA.

Tech knowledge: Java, Spring, Springboot, MERN, microsoft AI 900 certified.

DSA: Just started preping fron last week.

Aspiration: SWE in GCC companies. Paying more than 12LPA.

Question:

1. Can I crack it in next 9 months? Provided I will continue with my dsa.

2. Is it possible to be hired in such less experience ? cause i barely see any opening for 1-2 yoe.

3. Any tips to be noticed or approached by companies over linkedin.


2

1

---

## [Interview Experience Sharing First In Pe Oyg1](https://leetcode.com/discuss/post/7567827/interview-experience-sharing-first-in-pe-oyg1/)

_Crawled: 2026-05-24 · 400 words_


Hi everyone,

I recently did a Google onsite that was in-person with whiteboard (first time doing a real onsite after a long time of virtual interviews). Just sharing my experince with it since it's quite different. I was honestly nervous walking in, but the day ended up feeling surprisingly smooth and nice.

The onsite day itself felt pretty well organized. The coordinator will give you clear schedule, travel/commute details, and no confusion on where to be next. I felt like the interviewer was being really collaborative, and you don't have to run any tests or write bug-free code like many virtual ones required.

* * *

## Round 1 — DSA (Coding): Permutation Sequence

**Problem set:**

I was asked a problem similiar to this permutation sequence problem: [https://leetcode.com/problems/permutation-sequence/description/](https://leetcode.com/problems/permutation-sequence/description/)

It's not the exact same but if you know how to solve this one, you can solve the one I got asked during the onsite too.

**What we discussed**

For this round, I feel like my interviewer was really focused on communication and explaining the solution and walk through examples before writing anything on the white board. I didn't fully finish writing everything, but interviewer said it's okay and it feel like the feedback would be positive.

* * *

## Round 2 — DSA String processing problem

**Problem**

String processing problem on sorted strings.

Given a sorted string, find characters that appear more than twice and return their first and last positions.

**What we discussed**

- discussed a follow-up where you are not only given the sorted strings but also a Dictionary, see if you can remove some repeated characters so the string could match a dictionary word


This one is similiar to the Dictionary of sorted letters I practiced from this list: [https://offerretriever.com/companies/85cd771e-d78d-434d-b2b1-53af58aada31](https://leetcode.com/link/?target=https%3A%2F%2Fofferretriever.com%2Fcompanies%2F85cd771e-d78d-434d-b2b1-53af58aada31)

* * *

## Takeaways

Overall, the problems were not extremely difficult, I honestly prepared many questions and even practiced DP a lot. I mostly did my interview prepping with leetcode + [offerretriever](https://leetcode.com/link/?target=https%3A%2F%2Fofferretriever.com%2F) \+ [hellointerview](https://leetcode.com/link/?target=https%3A%2F%2Fwww.hellointerview.com%2Fdashboard) (system design).

The white board experience feels more collabortive, but honestly my hand-writing is super horrible. If you also haven't written anything for a while like me lol, I'd recommend some small amount of practice writing so your hand-writing won't be a problem during interview.

Going back to whiteboard interviews actually felt refreshing. Does anyone know if more companies are going back to real-person onsite? I'd actually love this trend.

15

8

---

## [System Design For Google L4 India](https://leetcode.com/discuss/post/7576666/system-design-for-google-l4-india-by-ano-kx61/)

_Crawled: 2026-05-24 · 64 words_


Hi all,

For Google L4 (India) interviews, are system design questions asked in the coding/DSA rounds?

If yes:

What type of design is expected (LLD or HLD) and how deep should we prepare?

Could you share a sample question?

How much time is typically spent on design?

If it’s asked along with a coding problem, is there enough time for both?

Thanks!

1

1

---

## [Ai Engineer 2 At Microsoft Vs Swe Iii At Fzdx](https://leetcode.com/discuss/post/7576201/ai-engineer-2-at-microsoft-vs-swe-iii-at-fzdx/)

_Crawled: 2026-05-24 · 30 words_


Can someone please highlight the pros and cons of AI Engineer II at Microsoft v/s SWE III at Google ?

Which is better choice to go for ?

0

5

---

## [Google L4 Infinite Loop](https://leetcode.com/discuss/post/7572765/google-l4-infinite-loop-by-anonymous_use-3dgh/)

_Crawled: 2026-05-24 · 211 words_


Hi,

I had my phone screen round in June '25 and onsite rounds wrapped up in Aug '25.

Got a confirmation from recruiter that I am moving to HM round in early Septemeber.

Got my HM calls scheduled in Nov-Dec '25 and then moved to HC in Jan '26 and then they come up with saying that I need to go for an additional round.

Meanhile I joined another great company and already spent 3-4 months there for which I interviewed for after Google.

First of all, it's quite frustrating since I am not into that prep mode anymore and secondly I am really liking the work at my current firm (which is comparable to Google in terms of comp and reputation). The recruiter even mentioned that the total comp for Google L4 has been reduced to max 70LPA which sounds like a lowball and lower than my current comp.

Just a few queries:

1. What is the level/bar of additional interviews if someone has given recently ? Is it same as onsites ?
2. Is it worth moving to Google now considering the recent layoffs and not only the brand value ?
3. What's the max comp expectation that I can ask for if I go through?

Thanks.

0

5

---

## [Stuck In Google L3 Hiring Process](https://leetcode.com/discuss/post/7619379/stuck-in-google-l3-hiring-process-by-ano-ewqq/)

_Crawled: 2026-05-24 · 98 words_


**2 weeks ago I got a call from HR that the manager likes my profile and wants to proceed with me further(after team matching call L3). He also told me that he will send me mail regarding what are the documents I need to upload for BGV. But since then I didn't get any further update or google career portal update or any mail. What does this mean? Is it mean I got an offer or does it mean that I am stuck in internal procedure and can be rejected from here also? Please help me!**

1

3

---

## [Need To Figure Out Where I Stand In The Ohstw](https://leetcode.com/discuss/post/7626962/need-to-figure-out-where-i-stand-in-the-ohstw/)

_Crawled: 2026-05-24 · 136 words_


_Current stats_

YOE : **3Y 8M (As of 5/3/26)**

Current Company: **Robert Bosch (3rd party payroll)**

CTC: **15.5 LPA (All fixed)** \| **No bonus or anything**

Tenure in current company: **1Y 6M**

* * *

So, here are the question to community.

- Is this good, bad or worse CTC at this level?
- Should I consider switching now or wait for current tenure to complete 2 years? (PS. I stayed 2 years in previous company also).
- Also going forward, at 10YOE will frequent switches matter?
- Although I'm not sure for switch, I have been active on job portals, but am not getting any good calls like good PBC. (Since I'm targeting good PBC, I'm entertaining SBCs anymore).
- And if someone like me has jumped to good PBC, tell me how?

1

2

---

## [Google Interview Experience L3 Onsite Ba 6Eig](https://leetcode.com/discuss/post/7570658/google-interview-experience-l3-onsite-ba-6eig/)

_Crawled: 2026-05-24 · 115 words_


Hi Community,

I recently gone thorugh Google interview loop for L3 role and I will share my personal verdicts for the rounds and will really appreciate your inputs that if I will get success or not.

R1 - Googlyness ( virtual ) - LH/H

R2 - Coding round ( virtual ) - SH/H

\-\-\- after clearing the virtual rounds got selected for 2 onsite rounds----

R3 - Coding round ( onsite ) - LH

R4 - Coding round ( onsite ) - SH/H

My interview loop compeleted on 10th Feb, and how much time it takes to get the result and feedback.

And what do u guys think if I will get selected.

1

16

---

## [Google Dream Ruined L 3](https://leetcode.com/discuss/post/7577253/google-dream-ruined-l-3-by-anonymous_use-isia/)

_Crawled: 2026-05-24 · 174 words_


Hi everyone,

I’m looking for some guidance regarding my Google team match situation.

I cleared all interview rounds at Google in May 2025 with strong positive feedback. My recruiter initially told me that I should expect a team match within 3–4 weeks.

However, after some time my recruiter changed, and the new recruiter wasn’t very responsive. Later, my original recruiter returned and in January she mentioned that she would continue sharing my profile with Hiring Managers. Since then, there has been no update.

It’s been several months now, and I’m still stuck in the team match phase. Meanwhile, I’ve seen some of my friends receive multiple team match calls—even when they didn’t perform perfectly in every round.

I’m feeling quite frustrated and discouraged. It’s hard not to feel like all the effort and preparation went to waste.I guess my recruiter is not making any effort regarding team match.

Has anyone else been in a similar situation?

What would you suggest I do at this stage?

Any advice would really help. Thank you.

9

12

---

## [Google London L3 Team Matching](https://leetcode.com/discuss/post/7693767/google-london-l3-team-matching-by-anonym-g0te/)

_Crawled: 2026-05-24 · 54 words_


Can anyone say how long they waited until finding a team for SWE II (L3) in London? Looks like it's going to take several months.

According to my recruiter, all my feedback was positive and I have 1 YOE at another Big Tech, also in London. Does that help with team matching?

1

0

---

## [Google L3 Interview 2026](https://leetcode.com/discuss/post/7595211/google-l3-interview-2026-by-anonymous_us-cxtr/)

_Crawled: 2026-05-24 · 322 words_


Hi everyone,

I recently completed my interview process with Google and had a feedback call with my recruiter yesterday. I wanted to share my situation and get some insight from people who may have gone through something similar.

Here’s a summary of what happened:

- My screening interview feedback was **very strong**.
- My first onsite interview went **very well**, and the interviewer even mentioned that I demonstrated **seniority level**.
- However, my second onsite interview received **negative feedback**. During that interview, I solved the main problem optimally, but the follow-up was challenging. I initially suggested a solution that wasn’t optimal, then proposed another one that the interviewer agreed was optimal. Also, the interviewer joined late, which made me more nervous.
- My Googliness interview feedback was **positive, but not exceptionally strong**.

My recruiter told me that overall my positive results will remain valid for **18 months**, and that I am now officially in the **team matching phase**. She also mentioned that there’s **no guarantee of placement**, but she will try to match me with suitable teams in London or Dublin. The next step would be a **fit call**, which she described as a conversation with a hiring manager, not an interview.

She also mentioned that I could potentially do another interview to balance the negative feedback, but she believes it may not be necessary since my other interviews were strong.

My questions:

- How common is it to enter team matching with one negative onsite interview?
- What are my realistic chances of getting matched with a team in this situation?
- Does being in team matching mean I’ve effectively passed the hiring committee?
- Is there anything I can do to improve my chances during the team matching phase?
- How long does team matching typically take?

I’d really appreciate hearing from anyone who has been in a similar position or has experience with Google’s hiring process.

Thanks!

6

11

---

## [Google London L3 Team Match](https://leetcode.com/discuss/post/7574654/google-london-l3-team-match-by-anonymous-0qsq/)

_Crawled: 2026-05-24 · 39 words_


Hi, I had team match call for Google London team on 10th Feb. The conversation went well with the HM.

I want to know how much time will it take to get feedback for team call?

Thanks.

4

5

---

## [Understanding Time Complexity For Backtr Rn7U](https://leetcode.com/discuss/post/7614127/understanding-time-complexity-for-backtr-rn7u/)

_Crawled: 2026-05-24 · 198 words_


I have an upcoming interview for SDE3 postion (YOE-4.5)

I’m having difficulty analysing the time complexity of backtracking solutions.

From my understanding, the general approach is:

Time Complexity = (number of choices) ^ (depth of the recursion tree)

However, I get confused when pruning is involved, because many branches are cut early and the full tree is not explored.

For example:

[https://leetcode.com/problems/generate-parentheses/description/](https://leetcode.com/problems/generate-parentheses/description/)

[https://leetcode.com/problems/restore-ip-addresses/description/](https://leetcode.com/problems/restore-ip-addresses/description/)

In problems like Restore IP Addresses, the maximum length is constant, so the overall complexity should technically be constant. But why is O(3⁴).

Also, in some backtracking problems, the time complexity is written as O(n!). I’m confused about when and why the complexity becomes factorial. Is factorial complexity only associated with recursion, or does it specifically occur when we are generating all permutations or arrangements?

My questions:

How do we correctly estimate time complexity when pruning reduces the search space?

When the input size is bounded (constant constraints), should the complexity be considered constant?

How do we derive expressions like 3⁴ in such cases?

When does backtracking lead to O(n!) complexity, and how can we identify such cases?

Any intuition or general method for analyzing backtracking complexity with pruning would be very helpful.

2

2

---

## [Google L5 Interview Experience Onsite Ba Mk1Z](https://leetcode.com/discuss/post/7610148/google-l5-interview-experience-onsite-ba-mk1z/)

_Crawled: 2026-05-24 · 148 words_


I didn't have a phone screen cause this is my second onsite. Round 1 dsa and Googleyness were online and the other 3 were onsite at their bangalore office.

Round 1

Graph problem - Given network of routers where some are defective, a source and a destination, check if a broadcast and shut down msg will reach destination.

Round 2

1. Binary search - first bad commit


Follow up - what if the size is too large and the l,r pointers cause integer overflow
2. Dp - given a mapping of digits to alphabets (1:a, 26:z) and a string of digits, return the number of possible interpretations.

Round 3

1. Logger rate limiter
2. Dont log the msg if repeated more than once in a 10s window.

System Design

1. Design Inshort


Follow up - how to avoid duplicate summaries of same article from different sources?

16

6

---

## [Google Interview Process Changed Need He Oaqx](https://leetcode.com/discuss/post/7581438/google-interview-process-changed-need-he-oaqx/)

_Crawled: 2026-05-24 · 151 words_


Hi everyone,

I’m currently preparing for Google L5 interviews and wanted to check with folks who have interviewed recently about the current interview structure.

Earlier, the commonly known process was:

Recruiter call

1 phone screen (DSA)

Onsite loop with:

3 DSA rounds

1 System Design + Googliness

However, I’ve recently come across different experiences shared online, such as:

Split loops (e.g., 2 virtual/offsite + 2 onsite rounds)

Googliness happening before DSA

System design appearing earlier in the process

“Onsite” loops being partially virtual

I understand that the evaluation areas remain the same (DSA, system design, googliness, leadership), but it seems the ordering and format might vary or has changed.

If you’ve interviewed for Google L5 in the past 6–12 months, could you please share:

Your round breakdown

Virtual vs onsite format

When Googliness and system design were scheduled

Thanks in advance and hoping this helps others preparing as well.

14

11

---

## [Google L3 Vs Adobe Mts 2 India 3 Yoe See P84Q](https://leetcode.com/discuss/post/7605427/google-l3-vs-adobe-mts-2-india-3-yoe-see-p84q/)

_Crawled: 2026-05-24 · 71 words_


Hi everyone,

I’m evaluating two offers and would appreciate input from the community.

Experience: ~3 years (Backend – Java/Spring Boot/Microservices)

Google – L3 (Bangalore)

Base: ₹24.1 LPA

Target Bonus: 15%

Equity: ~$30K (4-year vest)

Location: Bangalore

Adobe – MTS-2 (Noida)

Base: ₹24 LPA

Annual Bonus: 10%

RSUs: ~$60K (4-year vest)

Joining Bonus: ₹2L

Location: Noida

Would appreciate insights from the community or those familiar with either org.

Thank you.

2

9

---

## [Microsoft Engineer This Market Is Beyond 5Fm9](https://leetcode.com/discuss/post/7571641/microsoft-engineer-this-market-is-beyond-5fm9/)

_Crawled: 2026-05-24 · 351 words_


I work at Microsoft.

3.5 YOE. L60. Core portal team. Full-stack dev. Good review, good visibility, zero hope of promotion. Everyone knows the ladder here moves slower than a Windows update.

I’ve applied to 300+ jobs at this point. google, uber, atlassian, random startups, whatever.

got a few calls, then nothing. just straight up ghosted. no feedback, no rejection, nothing.

google recruiters hit me up like 4 times in the last 3 months. sounds good right?

Nope.

every time it’s android role, android domain round, in person. I’m full-stack, I don’t do android.

I told them clearly: I’m not an Android dev. I’m full-stack. I don’t touch android. I can’t become Google-level Android engineer in 4 weeks preperation to pass a domain round face-to-face. That’s just unrealistic.

Then a friend gave me a referral. Applied to FullStack and backend roles, Soon enough I recieved a mail:

“we will contact you soon for a FULLSTACK role!”

I was genuinely happy for like 5 minutes.

Call happens.

Guess what? Android role again. Domain round again.

At this point I’m convinced my resume auto-routes to Android hiring pipeline no matter what I apply for.

lets take about uber now,

applied via refferal, recruiter calls, hypes up the team, says they’re looking for strong backend/full-stack.

Says they’ll schedule rounds next week.

Next week comes, recruiter says “headcount on hold, but we’ll keep you updated.”

Two weeks later I get an auto-rejection email. No interviews. No explanation. just vibes-based hiring.

stripe was another joke. same as uber. recruiter said they’ll schedule interviews for some AI platform team. I was like okay lessgooo.

that was 3 weeks ago. no scheduling, no replies to follow-up mails. just vanished. hell nah.

salesforce at least gave an offer.

28 base + stocks, lower than my overall current comp. tried to negotiate politely, that rude ass HR said take it or leave it and cut the call in 4-5 minutes. May his soul rot in hell, completly unprofessional.

what is this market.

Anyway, back to solving LC hard and pretending everything is fine.

maybe DP will fix my life.

42

14

---

## [Dsa Mock Interview Partner Google](https://leetcode.com/discuss/post/7639416/dsa-mock-interview-partner-google-by-ano-oqyi/)

_Crawled: 2026-05-24 · 145 words_


Hi everyone,

I’m currently preparing for Google and looking for a serious interview buddy to practice consistently.

About me:

• 2.8 years of experience in C# Backend at a FinTech

• LeetCode Knight, used to do competitive programming (Expert at Codeforces)

• Got rejected by google last year

• Currently on notice period

I’m planning to form a small group of 3 serious candidates so we can conduct structured mock interviews and genuinely improve together.

What I’m looking for:

• Someone Good in DSA

• Serious about cracking Google

How I’m thinking we can practice:

• Timed mock interviews

• Discuss approach, optimizations, trade-offs, and edge cases

• Cross-questioning similar to real interviews

• 1 sessions daily or a few sessions per week (we can decide mutually)

If you’re genuinely serious and ready to commit, please fill the form below:

Form Link:

[https://forms.gle/Niy9p7u5iSzSHuNx7](https://leetcode.com/link/?target=https%3A%2F%2Fforms.gle%2FNiy9p7u5iSzSHuNx7)

0

8

---

## [Google Team Match L3](https://leetcode.com/discuss/post/7589707/google-team-match-l3-by-anonymous_user-bg7i/)

_Crawled: 2026-05-24 · 44 words_


Hi,

I had my Google team match round 10 days ago, and I haven't received an update yet.

If anyone knows how long it typically takes to receive team match feedback (accepted or rejected), it would be very helpful.

Interview Exp:

[https://leetcode.com/discuss/post/7406634/google-europe-l3-interview-experience-by-tk0f/](https://leetcode.com/discuss/post/7406634/google-europe-l3-interview-experience-by-tk0f/)

2

4

---

## [Google Web Solutions Engineer L3](https://leetcode.com/discuss/post/7611418/google-web-solutions-engineer-l3-by-anon-fo7v/)

_Crawled: 2026-05-24 · 339 words_


I recently interviewed with Google for WSE role. Sharing my interview experience to help others.

# Round 1

I was asked to code a CSV Parser from scratch. Method signature looked like this - `parse_csv(const string &input)`. We were supposed to return the contents of this CSV in an approprate data strcuture of our choice. Focus was on code readability, and edge cases - quotes within quotes, nested commas, etc.

# Round 2

There are `N` aliens in a galaxy far away. These aliens are living on some number of planets. We are also given an array `friends`, that contains list of pairs of friends living on the same planet. We are asked to find the number of ways two aliens can be sent to Earth such that both of them belong to different planets.

He then asked me about some web tech questions and CS fundamentals like virtual memory and how CPU handles multiple tasks at a time.

# Round 3

You are given an integer array `nums`, such that each index `i` has a parent `nums[i]` in a tree. We are supposed to figure out if this array represents a valid tree or not.

This was followed by some questions on Web Tech - HTTP status codes, How to debug an API, how to optimize a slow website.

# Round 4

This was an unsual round specific to this role. It was taken by the HM in which for the first 40 minutes, he asked me some SQL problems based on joins, aggregation, etc. He also expected me to know ranking functions which I wasn't aware of.

He then asked me to come up with a new feature for Google Maps in which we will show businesses the user would find interesting. I was supposed to come up with the Google platforms which could be used to do this and/or what features would be useful to make this recmommendation.

He then asked me some behavioural questions on multiple deadlines and how I would manage them.

17

6

---

## [Google Team Matching L3 Doubt](https://leetcode.com/discuss/post/7615069/google-team-matching-l3-doubt-by-anonymo-fe5h/)

_Crawled: 2026-05-24 · 66 words_


Hi Leetcode Community,

I gave google L3 interveiw around april 2025 and till now i am in team matching phase (overall verdict of interview is positive) and it is only 2 month left till my candidature expire and my recruiter is saying she is waiting for hiring team

I don't know what should i do

If anyone is from Google please suggest something

Thankyou

2

5

---

## [Google L4 Dsa Round Difficulty Convertin Cy0N](https://leetcode.com/discuss/post/7605894/google-l4-dsa-round-difficulty-convertin-cy0n/)

_Crawled: 2026-05-24 · 113 words_


I’m currently finding it difficult to write bottom-up (tabulation) solutions directly.

In interviews, is it acceptable to first implement a top-down (memoized) approach? Also, after writing a top-down solution, is it okay to convert it into a bottom-up one if time permits?

Could someone share tips or a structured way to think so that I can write bottom-up solutions directly and efficiently?

I have an interview in a few days and I’m feeling quite nervous, so any practical advice would really help.

Like for example:

This questions- [https://leetcode.com/problems/maximum-number-of-points-with-cost/description/](https://leetcode.com/problems/maximum-number-of-points-with-cost/description/)

I was able to solve it using top-down (recursive approach)

But inspite of seeing bottom-up solution, I am not able to code it.

1

8

---

## [Google Virtual Onsite Deny](https://leetcode.com/discuss/post/7643272/google-virtual-onsite-deny-by-anonymous_-6vgl/)

_Crawled: 2026-05-24 · 96 words_


Hi,

i would like to know that i know google understand employees, interviwee conditions better. but when i demand oniste virtual having situation then after many mails she constantly denies , i think she is no mood of doing it. they are mentioning it in their mails "Should a conflict or emergency arise, contact me right away."

now let see what she last mail i do her was to shift atleast inperson to gurgaon as job location is gurgaon ?

any suugesstions is i am asking too much , she frustated or anthing else?

3

1

---

## [Compensation At Google](https://leetcode.com/discuss/post/7602545/compensation-at-google-by-anonymous_user-019s/)

_Crawled: 2026-05-24 · 164 words_


I have close to 5 yrs of experience. I have worked in two big tech companies - both among MAANG.

I have cleared phone screen interview of Google. I am appearing for L4 position. And while discussing compensation range before interviews they are saying the range is 60LPA to 70LPA. But I already have compensation in this range. What shocked me the most is the split - 32-36LPA base and equity 45k-60k. I am already earning 46LPA base and 50-60k equity. Should I proceed with Google onsite?

Even with compete offer they are saying there would strictly be no room for negotiation. I have compete offer from Meta. And the recruiter also wants in written that I accept to take onsite interview for the compensation range of 60LPA to 70LPA. I am not even entry level L4 - I have experience close to Senior.

Is this the range for Google L4 these days or am I being lowballed?

Why confirmation in written?

1

9

---

## [Interview Experience Google L3 Web Solut Ger7](https://leetcode.com/discuss/post/7624355/interview-experience-google-l3-web-solut-ger7/)

_Crawled: 2026-05-24 · 255 words_


## Overview

- **Role:** Web Solutions Engineer (L3)
- **Organization:** GTech
- **Duration:** ~60 Minutes
- **Focus:** Data Structures, Algorithms, and Web Internals

* * *

## Data Structures & Algorithms

### The Visibility Problem

Given an array representing the heights of people, determine how many people are visible to the **last person** in the array.

**Rule:** Person A is visible to Person B if there is no one between them who is taller than both Person A and Person B.

**Example:**

- **Input:**`[1, 10, 5, 7, 6, 3, 2, 4]`
- **Output:**`5` (The people with heights 2, 3, 6, 7, and 10 are visible to 4)

**Follow-up:**

Find the number of visible people for **every** person in the list (not just the last one).

**Goal:** Implement an optimized solution with O(n) time complexity for both cases.

### **Web Technology**

How would you optimize a website across the following three layers(Frontend, Backend, Database)?

Explain the process of what happens from the moment a user types a **URL** into the browser until the **page** is fully rendered.

Compare and contrast **Server-Side Rendering (SSR)** vs. **Client-Side Rendering (CSR)**.

### **Section 3: Bonus / Quickfire Question**

#### **Problem: Transition Peak Finding**

You are given an array that is a mixture of `True` and `False` values.

- The array always starts with `True`.

##### \\* The array always ends with `False`.

- **Task:** Find any index i such that `arr[i] == True` and `arr[i+1] == False`.

**Goal:** Implement an optimized solution (Binary Search) with O(logn) time complexity.

6

6

---

## [Google L4 Chances](https://leetcode.com/discuss/post/7641721/google-l4-chances-by-anonymous_user-m7h3/)

_Crawled: 2026-05-24 · 38 words_


DSA rount 1: SH/H

Googlyness: SH/H

* * *

Onsite Round 1: H/SH

Onsite Round 2: LH/H

70 % chnaces of 1st rating and 30% of the other one.

What are my chances for being Accepted?

4

5

---

## [Google Team Match Swe L3](https://leetcode.com/discuss/post/7617480/google-team-match-swe-l3-by-anonymous_us-b7jn/)

_Crawled: 2026-05-24 · 42 words_


Hi,

I have heard that passing the interviews at Google does not always guarantee an offer.

I believe I have at least three strong hires. What are my chances of getting on the team and receiving an offer from Google?

0

1

---

## [Google L3 Interview Process Recruiter As 5E6T](https://leetcode.com/discuss/post/7641112/google-l3-interview-process-recruiter-as-5e6t/)

_Crawled: 2026-05-24 · 217 words_


Hi everyone, I’m hoping someone familiar with the Google hiring pipeline can help me understand where I currently stand.

Location: India

Exp: +1.5 YOE

Timeline:

- **Last March 2025**: Completed onsite interviews for an L3 role at Google
- **Mid April 2025**: Recruiter told me feedback was “overall positive” and that I’d move to team matching. There were delays because my recruiter changed twice.
- **Feb 23 2026**: Right after my second team-fit call, the recruiter asked me for additional details such as: _transcripts, updated resume, expected salary, internal references, career trajectory / background info_

However, there was no explicit mention of whether my packet is going to Hiring Committee (HC) or if it already has.

So I’m trying to understand:

- Does this usually mean I’m pre-HC and they’re preparing the packet? Or could I already be post-HC and in team matching / approval stages?
- Once a candidate goes to HC, how long does it usually take to hear back?
- I pinged my recruiter asking about my status, but I haven’t received a reply yet. At what point does it make sense to email the candidate support email instead if the recruiter isn’t responding? Or is that generally discouraged?

Would really appreciate insights from anyone who’s been through the process recently.

Thanks!

1

3

---

## [Extremely Sad Google L5 Interview Experi Jm8B](https://leetcode.com/discuss/post/7631077/extremely-sad-google-l5-interview-experi-jm8b/)

_Crawled: 2026-05-24 · 514 words_


Hi Everyone,

I wanted to share an extremely disappointing experience that happened in my Google L5 onsites. In 2025 beginning I interviewed for SWE, ML role at Google. My initial rounds were two domain based ML system design rounds where I got H and LNH/NH respectively. After getting LNH review my recruiter made me close the loop as she thought with LNH it wont make it past the HC. This was despite the fact that the interviewer who gave LNH also had some positive feedbacks mentioned. My friends suggested not to close the loop as good performance in further rounds could have made up for it. But she forced me to withdraw. It was an extremely sad moment for me.

Fast forward Oct 2025, she reached out to me again over linkedin. I had not given up my LC prep and despite being sick with some health complications I decided to interview again. Post that in November I ended up clearing Sr SWE ML interviews at Linkedin but the role got closed by the time my onsites completed. In Feb I cleared Atlassian p50 MLE(got go through from HC) but couldn't be team matched due to company wide hiring freeze. My first Google onsite interview was in Feb which got rescheduled thrice due to interviewer unavailability and moved to March.

During all this time my recruiter never answered my calls or responded to my messages. She did reply once or twice to my emails. My interview didn't go quite well as I was asked a tricky variation of the meeting room 3 problem. I ended up explaining the optimal approach for the problem, wrote the pseudo code but couldn't write the code and dry run. The interviewer before ending told me that I did arrive at the optimal solution and may be with a bit more time could have put up everything together. I was disappointed but still hopeful that may be further rounds can make up for it. This was on Thursday.

I was absolutely shocked when yesterday, I received a rejection mail from my recruiter without any call or discussion of feedback. I tried reaching out to her over phone, linkedin, email but she is not responding. I requested her to atleast let me complete my DSA rounds and then decide but she is not responding. **She rejected me based on just one round of interview.**

At this point I feel crushed as I worked really hard this time. My LC count was 500+ and I could solve leetcode hard graph and DP questions conveniently. I worked extremely hard despite serious health complications and 3 days in office thing.

**I want to ask the leetcode community if there is anything I can do at this point so that she atleast gives me a chance at other rounds before rejecting me.**

The market is crazy and despite all my efforts things somehow seem to go out of hand. Companies are reaching out for interviews but either they don't go ahead and schedule them or end up ghosting while interviews are underway.

12

8

---

## [Google Interview Query](https://leetcode.com/discuss/post/7632037/google-interview-query-by-anonymous_user-0xnw/)

_Crawled: 2026-05-24 · 115 words_


Hi everyone,

I recently completed the Coding Round and Googliness Round for a Software Engineer role and received positive feedback from the recruiter. The next step would be the onsite rounds.

However, the recruiter mentioned that the interviews are typically conducted onsite in Bangalore. Due to a family medical situation, traveling right now is a bit difficult for me, so I have politely asked if it might be possible to conduct the interviews virtually.

I wanted to ask the community if anyone has been in a similar situation. Do companies sometimes allow virtual onsite interviews in special cases? Any advice on how to handle this situation would be really helpful.

Thanks in advance!

1

7

---

## [Google L5 Interview Screening](https://leetcode.com/discuss/post/7617354/google-l5-interview-screening-by-anonymo-ld26/)

_Crawled: 2026-05-24 · 128 words_


I gave screening rounds of Google for L5 position. There were 2 rounds: DSA and Googleyness. Can someone help for the next stes:

1. DSA: It was a question on Dijkstra. While I could correctly identify and explain the solution, I was not able to implement it well. My code has bugs. I am not sure how this round will impact my overall candidature.
2. Googleyness: It was rather 30 minutes round, went really well. Preprating using STAR and creating some commmon scenrios using chatgpt helped a lot.

Please help me understand, will my candidature be considered after bad DSA round? Or this will be treated more like a screening and the onsites are the only ones which will be considered for final verdict.

Thank you!

7

9

---

## [Google L4 Team Match 6 Months](https://leetcode.com/discuss/post/7623227/google-l4-team-match-6-months-by-anonymo-a2vl/)

_Crawled: 2026-05-24 · 156 words_


It's been six months, one team match only and rejcted there as they needed more database exprerienced.

How do I change the recruiter as recruiter did not update me about the rejection at that team match till 20 days, I had to reach out to them via call to get the feedback as reply didn't come in mail.

Should I ask google candidate help desk to change the recruiter as I don't have any transparancy what's going on google team match, which team they share with or what? No communication now, and packet will be expired soon, don't know when?

My tech stack is java?

Interview Feedback: All rounds positive, a bit lag in 1 round but got the correct answer at the end. Went ahead with team match.

Received this feedback in September first week.

College: tier-3

Please help. Let me know if any senior employee wants to connect to me to discuss.

1

4

---

## [Looking For Lldhld Practice Partner](https://leetcode.com/discuss/post/7626143/looking-for-lldhld-practice-partner-by-a-junj/)

_Crawled: 2026-05-24 · 68 words_


Hi everyone,

I have 2.5 years of experience and I'm preparing for System Design interviews (LLD + HLD). I'm looking for a serious practice partner to do regular mock discussions.

Plan

- Practice 3-4 times per week

- Cover LLD + HLD problems

- Do mock interview style discussions


If you're interested, please fill this quick form so we can coordinate:

👉 Google Form: [https://forms.gle/1GhNe8cnbEsp5VWF7](https://leetcode.com/link/?target=https%3A%2F%2Fforms.gle%2F1GhNe8cnbEsp5VWF7)

Thanks!

8

5

---

## [Google L3 Interview Experience Hc Approv Akpm](https://leetcode.com/discuss/post/7629725/google-l3-interview-experience-hc-approv-akpm/)

_Crawled: 2026-05-24 · 420 words_


YOE: 1.5 (at the time of interview)

Phone interview:

1. Some verbal question on BST
2. Define a tree DS in C++; couldn’t remember deconstructor syntax
3. **MEDIUM** problem on tree + hashMap, solved it optimally but got stuck on a syntax bug (wrote just return instead of return null :P)
4. Got asked a **MEDIUM-HARD** design-type problem on Stack + BST. Discussed a lot of solutions, finally after a lot of clarifications was able to figure out the solution which interviewer wanted using stack and explained the flow. Interviewer agreed, but didn’t have enough time to code.

Feedback: "Positive with scope of improvement". LH most likely, or H at most.

Onsites:

1. **HARD** range-based design-type problem. I was able to solve first problem optimally without any help but had some 2 edge cases missing. Interviewer gave failing edge case, for which I ran through the code ignorantly and couldn’t find the bug. Interviewer insisted to go line by line, which I did and was able to find both the bugs and fixed it.


Follow-up: I only explained since time wasn't left, which they agreed upon was optimal.

_**Learned to go through each line after coding to find edge cases, specially before interviewer does.**_

**Personal Rating: H likely or LH.** Let me know if H will be a push here..

2. **MEDIUM** Graph based problem. Was able to explain and code 1st one smoothly, no bugs.


Follow-up: **HARD** Graph based problem. Was able to explain without any bugs.


Follow-up 2: **HARD** Graph + DP based problem. Interviewer only wanted a recurrence formula, which I was able to write down. In the end the interviewer was satisfied.

**Personal Rating: SH**

3. **HARD** Graph based problem. Solved using binary search + BFS, also could be solved using djikstra etc. Explained solution, coded, clean, no bugs. Interviewer was satisfied, even praised my code neatness.

**Personal Rating: SH**

4. Behavorial. There were like 5 or 6 problems which we discussed upon. All of them were from [this post](https://leetcode.com/discuss/post/5963463/Googlyness-Frequently-Asked-Questions/)

**Personal Rating: H/SH**


Recruiter reached out to me saying the feedback is “overall positive” and I will be moving to the team match phase.

Had 2 team fit calls, and after 2nd team fit call was asked for more details like grade transcripts, salary expectations, internal references etc. I believe it’s for HC packet.

I am interested in knowing what are my chances of passing HC from the Leetcode community! Also If you believe my ratings are too optimistic/pessimistic please let me know..

Thanks!

7

5

---

## [Is Net A Bad Tech Stack For Switching To 2Umg](https://leetcode.com/discuss/post/7725096/is-net-a-bad-tech-stack-for-switching-to-2umg/)

_Crawled: 2026-05-24 · 173 words_


I’m currently working in an MNC with ~1 year of experience, mainly on .NET and Azure.

Lately, I’ve been preparing to switch to a product-based company, but I keep hearing things like:

“Tech stack matters a lot” or “.NET isn’t preferred in top product companies.”

This has honestly made me a bit confused.

So I wanted to ask directly:

- Do product-based companies actually shortlist based on tech stack?
- Does working in .NET put me at a disadvantage compared to Java/Node/Python folks?
- How relevant is .NET in today’s product ecosystem?
- If I’m open to learning any tech stack, will companies still judge me based on my current experience?

I don’t want to limit myself to just one stack, but at the same time, my experience is tied to .NET right now — and I’m unsure how much that impacts my chances.

Would love honest opinions from people who’ve made similar switches or are already in product-based companies.

Is this a real problem… or just overthinking?

Thanks in advance!

3

1

---

## [Honest Poll For People Preparing For Goo Djwn](https://leetcode.com/discuss/post/7632214/honest-poll-for-people-preparing-for-goo-djwn/)

_Crawled: 2026-05-24 · 79 words_


Every week people grind the “Top / Most Tagged Google Questions” list on LeetCode.

But the list keeps changing constantly.

So I’m genuinely curious:

How useful are these questions actually in real Google interviews?

📊 Poll:

Very useful — I’ve seen the same questions

Somewhat — helps recognize patterns

Not really — interviews are different

Waste of time — better to study fundamentals

💬 If you’ve interviewed at Google recently, did any question come directly from LeetCode?

7

6

---

## [Google L5 Interview Experience](https://leetcode.com/discuss/post/7624444/google-l5-interview-experience-by-anonym-o9ja/)

_Crawled: 2026-05-24 · 65 words_


Helping the community -

Gave interview for L5 Role

```sql
You are given:
 - Array arr of size n
 - q queries
    - Each query: (l, r, k)

For each query:
 - Update all elements from index l to r to value k

n -> 10^5
queries -> 10^5

Two variations :
1) if k remains same
2) if k is different
```

10

11

---

## [What Are The Chances To Pass To The Team 5Sog](https://leetcode.com/discuss/post/7641689/what-are-the-chances-to-pass-to-the-team-5sog/)

_Crawled: 2026-05-24 · 146 words_


I just completed my Google loop.

I passed the phone screen with a brute-force approach and by mentioning the optimal solution, i was convinced performed horribly but the recruiter told me I received excellent feedback for both coding and Googliness.

My two onsite interviews went in opposite directions: one went really well with an optimal solution (I would rate myself as 'Hire' or 'Strong Hire'), while the other involved a hard mathematical question that made me panic. I struggled for 40 minutes with a brute-force approach (I’d rate myself a 'No Hire' maybe even 'Strong No Hire,' though that feels harsh).

I know Google can request an additional round, but from what I’ve read, that mostly happens for L4 and above. What do you think will happen? Will I be rejected directly, or will the recruiter try to move me to team matching nontheless?

5

5

---

## [Need Advice Google Onsite Round Offline Q7Ewb](https://leetcode.com/discuss/post/7619877/need-advice-google-onsite-round-offline-q7ewb/)

_Crawled: 2026-05-24 · 84 words_


Hello,

I am having my Google onsite round for SWE-II role and it will be held offline at their Bengaluru office in next 7 days. I have already cleared Preliminary rounds (1 technical + 1 googlyness). Can you suggest me how can i prepare for the onsite rounds for the next 7 days?

As per the recruiter, there will be two rounds that will be held on the same day. Please help (especially those who have given onsite rounds recently please help)

7

9

---

## [Google Interview Stuck In Approval Pendi 8P0J](https://leetcode.com/discuss/post/7644812/google-interview-stuck-in-approval-pendi-8p0j/)

_Crawled: 2026-05-24 · 149 words_


I received a call from a recruiter at Google via LinkedIn in the last week of January. During the call, I mentioned that I would need about **3–4 weeks to prepare**, and she said that was fine and that she would **reach out again in the last week of February to schedule the interview**.

However, I didn’t receive any update from the recruiter around that time, so I followed up myself to schedule the interview. She replied saying that **the process is still ongoing and that she hasn’t received approval yet**, and that the status remains the same even now.

I’m not entirely sure what this means. Has anyone else experienced something similar during the Google hiring process (this is for **Bangalore, India**)?

At this point, I’m starting to wonder whether the interview will actually get scheduled or not. **Is this normal, or should I be concerned?**

3

2

---

## [Sharing Regular Off Campus Job Opportuni 8F9U](https://leetcode.com/discuss/post/7643229/sharing-regular-off-campus-job-opportuni-8f9u/)

_Crawled: 2026-05-24 · 118 words_


Hey everyone,

While preparing for interviews and solving problems on LeetCode, I realized many good off-campus opportunities never reach most students or early-career engineers.

So I started sharing verified job openings daily in a WhatsApp channel.

I usually post roles like:

- SDE / SWE roles (0–3 YOE)
- AI / ML / Data Science roles
- Internships from companies like Microsoft, Uber, Qualcomm, Myntra, Apple, etc.

The goal is simple: help people discover opportunities early so they can apply quickly.

If you’re actively preparing for tech interviews or looking for roles, you might find it useful.

Join here:

[https://whatsapp.com/channel/0029Vb7E3WB9xVJW3qfYOE1N](https://leetcode.com/link/?target=https%3A%2F%2Fwhatsapp.com%2Fchannel%2F0029Vb7E3WB9xVJW3qfYOE1N)

Also you can follow me on intagram for AI/ML, DSA, System Design resources and content.

[https://www.instagram.com/thegrowthrepo/](https://leetcode.com/link/?target=https%3A%2F%2Fwww.instagram.com%2Fthegrowthrepo%2F)

1

2

---

## [Google Team Matching Hell](https://leetcode.com/discuss/post/7642901/google-team-matching-hell-by-sachinbhola-dt1h/)

_Crawled: 2026-05-24 · 71 words_


Hi Googlers,

I Interviewed at Google for Android L4 position(India) and completed my last round in mid January. I got a positive feedback in a week.

It's been two months since then and still not a single Team Matching call is scheduled. It is quite frustating. If anyone has gone through the same process can you please share your experience and tips to improve changes for team matching.

Thanks

2

8

---

## [Google L3 Team Matching Process Info](https://leetcode.com/discuss/post/7646569/google-l3-team-matching-process-info-by-aohqg/)

_Crawled: 2026-05-24 · 90 words_


Recently, I got the call from the recruiter that I have cleared all the interview rounds and I am being moved to Team Matching phase. I want to know the further process like what happens next, what happens in TM phase, when will the recruiter ask for documents for BGV, when will the offer discussion be done ?

It will be really helpful if someone can explain it

Edit: I have shared the onsite interview question (not exactly as they were asked) on the following in comments

[https://leetcode.com/discuss/post/7619877/need-advice-google-onsite-round-offline-q7ewb/](https://leetcode.com/discuss/post/7619877/need-advice-google-onsite-round-offline-q7ewb/)

6

7

---

## [Google Europe L3 Rejected My Experience 44O6K](https://leetcode.com/discuss/post/7691552/google-europe-l3-rejected-my-experience-44o6k/)

_Crawled: 2026-05-24 · 395 words_


I recently completed my L3 loop for Google. I may sound cliche but working in Google was my dream when I started leetcode 6 months ago so you can imagine how I felt when I received the call from the recruiter at the start of January that I was selected for interviews.

I did my phone screen and googlyness at the start of February and (quoting the recruiter) I got "the maximum score possible, excellent feedback".

I can't find the exact question online but was like "you get an array, find if the array can be divided in two equals part" and followup "what if you can change at most k numbers"

Then the onsite arrived. The first one went SO bad, I got a rude indian interviewer that asked a medium-hard problem (similar to [this](https://leetcode.com/link/?target=https%3A%2F%2Fwww.reddit.com%2Fr%2Fleetcode%2Fcomments%2F1b22k2q%2Fgoogle_onsite_round_1_monotonic_stack_problem%2F)) that required a math intuition, I didn't get it so I struggled and panicked with a brute force for 40 minutes with him doing sarcastic remarks. As expected I was rated 0/4 on this round.

The second onsite I thought it went great, immediately recognized the optimal solution and code it up (and she agreed that my code would work) it was a string matching problem that required two queue. But then the recruiter told me I got a score of just 2/4 and I was penalized on code understanding because I slightly misjudged the time complexity and on debugging because I didn't do a dry run (but the recruiter never asked, all the other explicitly asked me to do a dry run, and again: she agreed the code was correct).

So I can't help but feel like I let myself down and I wasted my great chance to leave the job I hate, improve my life and move geographically to a better place.

Even the recruiter when she called with the feedback she said "I'm not sure what happened during the onsite, you had such good feedback on the phone screen" which didn't helped me even though she meant well.

I guess I should be prouder of completing the loop and getting a great feedback on the phone screen but right now I can see only the failures, especially after 6 months of grind on LC and the 12 months cooldown is brutal.

Also, is doing a dry run a musto do? even if not asked?

6

2

---

## [Amazon Logical And Maintainability Round Kx6E](https://leetcode.com/discuss/post/7697546/amazon-logical-and-maintainability-round-kx6e/)

_Crawled: 2026-05-24 · 80 words_


Hi everyone,

Has anyone recently gone through Amazon’s Logical & Maintainability interview round for SDE-2?

If yes, could you please share:

What kind of questions were asked?

What exactly was expected from candidates?

I’m particularly trying to understand whether this round is closer to:

Low-Level Design (UML, class diagrams, etc.), or

More of a DSA-based coding round with emphasis on OOP principles and clean, maintainable code.

Any recent insights or experiences would be really helpful. Thanks in advance!

0

2

---

## [Urjent Help Needed Google L3](https://leetcode.com/discuss/post/7685204/urjent-help-needed-google-l3-by-rakesh_r-wado/)

_Crawled: 2026-05-24 · 73 words_


I joined Adobe as MTS 2 (CTC ~43 LPA). Recently Got an offer from Google for L3, but the comp they’re offering is ~40 LPA.

I did try negotiating, but they said this is the final offer and can’t go higher.

Also, is there any way to push negotiation further at this stage?

Would really appreciate hearing from folks who’ve been in a similar situation

Edit:

Tier 1 college

2.7 YOE

4

8

---

## [Google Team Matching Stuck 1 Year Is Thi Q4Kx](https://leetcode.com/discuss/post/7659329/google-team-matching-stuck-1-year-is-thi-q4kx/)

_Crawled: 2026-05-24 · 165 words_


Need some candid advice from folks familiar with Google hiring.

I cleared interviews for SWE ~1 year ago and have been in team matching since then with zero calls.

Recruiter feedback so far:

1. One coding round was borderline/negative

2. Current stack might not align with most teams

3. The role I originally applied for is now closed, but my profile is still “active”


I even asked if I can do another interview to improve my packet, but recruiter said process doesn’t allow additional rounds.

At this point, it feels like I’m just sitting in the system without real movement.

Questions:

1. Is a 1-year team match wait basically a soft reject?

2. Do profiles like this ever actually get matched?

3. Any way to revive this, or is reapplying after cooldown the only realistic option?


Would appreciate blunt, honest answers from them who have been to hiring process of google.

And one more thing recruiter said my profile is valid till september

3

3

---

## [Offer Comparison Google Vs Nvidia](https://leetcode.com/discuss/post/7654767/offer-comparison-google-vs-nvidia-by-ano-rar5/)

_Crawled: 2026-05-24 · 66 words_


Hello

I want to ask the community about its suggestions for which offer to choose.

Google: SWE-2 (Location: Google Ananta, Bengaluru)

NVIDIA: SDE-1 (Location: NVIDIA Graphics, Pune)

YOE: 1.5 years

Compensation : Around 50 lpa

Both companies are offering similar compensation

In both the companies, I am getting teams with tech stack of C++

Please suggest me which offer you guys would have chosen

2

9

---

## [Need Guidance Sap Consultant Sde At Faan 26L8](https://leetcode.com/discuss/post/7676880/need-guidance-sap-consultant-sde-at-faan-26l8/)

_Crawled: 2026-05-24 · 85 words_


Hi everyone ,

I have 1.6+ Year of Experience in SAP BASIS(DevOps) + SAP ABAP

Currently learning Java+Spring Boot , Docker and Kubernetes and Redis

with learning DSA in C++ as well.

College - (Tier 3)

I m confused that will they accept my application I dont have prior SDE experience

please help me and guide me what should i do and also what about this tech stack .

Any help or guide will truely helps me , \*\*please dont ignore this \*\*

2

2

---

## [Google L5 Interview Phone Screening](https://leetcode.com/discuss/post/7706368/google-l5-interview-phone-screening-by-a-4tjw/)

_Crawled: 2026-05-24 · 253 words_


I am starting with my interviews for Google L5, had one few days back last week. It was supposed to be a DSA round, Interviewer asked me a pretty simple coding question, which is a standard leetcode easy on arrays. I was a bit shocked that why was it easy, asked all the clarifying questions and finished code maybe in 15 mins.He said code looks good and he liked my code style and design choice.

I expected a followup, but he said he has another question more on internal implementation of data structure Hash. I wasnt prepared for it, missed a few things here and there. I feel I was unable to answer it in an acceptable way. Interviewer at 30 mins point (out of 45 mins) asked if I had some questions to him. Asked a few questions about the work and AI in general, he answered patiently and went on to say lets close the call if no further questions. I asked him not sure to be happy or sad about closing the call early(as i nailed the Algo question but on Data structure question it was bad). He mentioned we knowingly keep more time for screening interview for diverse set of applicants.

Havent been reached out by recruitor yet. Not sure if asking non=coding DS questions are also normal in Google. Anybody faced the same? What should I expect, not expeciting more than Lean hire honestly. Given I solved coding question correctly, can it be no-hire as well?

1

5

---

## [Google Sde 3 Phone Screen Behavioral Got Pao9](https://leetcode.com/discuss/post/7827768/google-sde-3-phone-screen-behavioral-got-pao9/)

_Crawled: 2026-05-24 · 260 words_


Hi Leetcoders,

I recently had a phone screen interview at Google (based in Warsaw).

It consisted of 45 mins of coding round + 45 mins behavioral (Googliness) round, all in one day.

The behavioral round went smoothly and I got a positive feedback from it.

The coding round started with a warmup question (the interviewer did not explicitly mention its a warmup, but he made it clear we will have some follow ups after it).

Unfortunately, it took me a lot of time to understand the problem and I got hung up on some implementation details more than I should have. I won't share the exact problem, but the optimal solution involved implementing subsets (backtracking). I was able to code it up, answer follow-up questions, discuss time and space complexity, but it took me whole 45 minutes, so we did not have any time left for another question (which apparently was supposed to be the main one).

It was confirmed in the feedback, that they cannot pass me because I spent all the time on the warmup question, however since I solved it correctly and communicated it properly, they are willing to give me a second chance for a coding round.

I don't know how it will go, but I am already really happy to get this chance, it is my 4th attempt and in all previous attempts I was not even able to come up with a brute force solution.

So, if you are or were in such a situation, keep it up, we will get there!

5

0

---

## [Google L4 Dsa Round Question](https://leetcode.com/discuss/post/7705895/google-l4-dsa-round-question-by-anonymou-nh2t/)

_Crawled: 2026-05-24 · 115 words_


L4 DSA Rond question:

You are given a list of packages to compile, along with two APIs: `getDependencies` and `compile` (you can treat both as simple method calls).

The goal is to compile all the packages in a **multithreaded environment**. A package can only be compiled after all of its dependencies have been successfully compiled.

This problem is similar to [https://leetcode.com/problems/course-schedule-ii/description/](https://leetcode.com/problems/course-schedule-ii/description/), but with the added complexity of multithreading.

Points to consider:

1. getDependencies may return packages that are not in the original list. These must also be handled and compiled.
2. Your solution should detect and handle circular dependencies.
3. Thread count should be configurable

What is the best way to solve this?

3

4

---

## [Google](https://leetcode.com/discuss/post/7714230/google-by-anonymous_user-qmbu/)

_Crawled: 2026-05-24 · 128 words_


Hey community! 👋

I recently cleared my virtual rounds for a Software Engineer II role at Google and have been scheduled for an onsite interview in Bangalore.

I completed the travel form via Graebel a couple of days ago but haven't received any travel booking confirmation or update yet.

For those who have recently gone through Google's onsite interview process:

🔹 How long did it take to hear back from Graebel after submitting the travel form?

🔹 Did you receive travel confirmations close to the interview date?

🔹 Any tips or things to expect during the onsite rounds?

Would love to hear from anyone who has recently been through this process! Any insights would be really helpful. 🙏

#Google #GoogleInterview #SoftwareEngineer #Hiring #InterviewPrep #LeetCode #TechInterview #SWE

3

3

---

## [Google Partner Engineer Device Ops Youtu H7T2](https://leetcode.com/discuss/post/7684068/google-partner-engineer-device-ops-youtu-h7t2/)

_Crawled: 2026-05-24 · 62 words_


I got a connect and interview scheduling request for this role ( [https://www.google.com/about/careers/applications/jobs/results/115249433850847942-partner-engineer-device-ops-youtube](https://www.google.com/about/careers/applications/jobs/results/115249433850847942-partner-engineer-device-ops-youtube)) from a google recurtier on linkedin. I just want to understand how it is different from software engineer roles , if anybody have knowledge from same domain.

I am core backend engineer with 4 yrs of experience should i go for it or not?

thanks in advance

0

1

---

## [Google Wse First Round What To Expect](https://leetcode.com/discuss/post/7753715/google-wse-first-round-what-to-expect-by-ire9/)

_Crawled: 2026-05-24 · 53 words_


Hey everyone,

I have my first technical round coming up

for Google Web Solutions Engineer (WSE) role.

Recruiter said: backend focused DSA, 60 mins coding.

For people who went through this:

1. What kind of problems were asked?
2. One problem or two?
3. Easy-Medium or Medium-Hard?
4. Any tips?

Thanks!

2

1

---

## [Google L3 Application Engineer Role](https://leetcode.com/discuss/post/7727298/google-l3-application-engineer-role-by-a-hexq/)

_Crawled: 2026-05-24 · 134 words_


Hey everyone,

Need some honest advice from folks here.

I have ~3.7 YOE as an SDE (Java backend) and recently got an offer from Google for an Application Engineer (L3) role.

### Offer details:

- Base: ₹24 L
- Bonus: 15%
- RSU: $32.5K (4 years, ~38% first year) (~₹11 L)
- Joining Bonus: ~₹3 L

### Current situation:

- Current base: ₹27 L (WFH)

* * *

### My concerns:

1. AE vs SDE
   - Is moving from SDE → Application Engineer a downgrade in long term?
   - Does it affect switching later to product/backend roles?
2. Internal tools
   - Work is on internal systems (not user-facing products)
   - Does this reduce learning / resume value?

Need Advice on taking the decision, that I should accept or decline?

Thanks in advance!

2

7

---

## [L3 Google Onsite Arithmetic Sequence Que 85X3](https://leetcode.com/discuss/post/7708808/l3-google-onsite-arithmetic-sequence-que-85x3/)

_Crawled: 2026-05-24 · 271 words_


Hi everyone, I recently completed my google loop, unfortunatly i was rejected because i bombed the round where i was asked this question, i panicked and managed only a brute force with a couple of hints.

An arithmetic sequence is a list of numbers with a definite pattern. If you take any number in the sequence then subtract it from the previous one, the difference is always a constant.

A good arithmetic sequence is an arithmetic sequence with a common difference of either 1 or -1.

For example, \[4, 5, 6\] is a good arithmetic sequence. Any sequence that has only one element is a good arithmetic sequence.

For example, \[4\] is a good arithmetic sequence.

Given an integer array nums, return the sum of the sums of each subarray that is a good arithmetic sequence.

Example:

Given nums = \[7, 4, 5, 6, 5\]. Each of the following subarrays is a good arithmetic sequence:

\[7\], \[4\], \[5\], \[6\], \[5\],

\[4, 5\], \[5, 6\], \[6, 5\],

\[4, 5, 6\]

The sums of these subarrays are:

7, 4, 5, 6, 5,

4 + 5 = 9, 5 + 6 = 11, 6 + 5 = 11,

4 + 5 + 6 = 15

Thus, the answer is the sum of all the sums above, which is:

7 + 4 + 5 + 6 + 5 + 9 + 11 + 11 + 15 = 73.

Now I know that we can find the start and end of each sequence and calculate how many segments each number appears in. Unfortunatly I didn't know that pattern and math formula before this interview...

6

12

---

## [Google Recently Asked Coding Questions C 296M](https://leetcode.com/discuss/post/7701662/google-recently-asked-coding-questions-c-296m/)

_Crawled: 2026-05-24 · 1092 words_


* * *

# The Ultimate Questions List appeared on multiple platforms

### Arrays, Strings & Two Pointers

- [ ] **Find Longest Duplicated Substring:** Find the longest contiguous sequence of characters that appears more than once in a string. _(Difficulty: Level 4)_
- [ ] **Minimum Covering Substring:** Find the shortest substring of `s` that contains every character of `t`. _(Difficulty: Level 1)_
- [ ] **Dictionary Substring Check:** Verify if every contiguous substring of a given string is a valid word in a provided dictionary. _(Difficulty: Level 3)_
- [ ] **Prefix Duplicates Removal:** Delete elements from `listB` so that its first `k` elements share no value with `listA`. _(Difficulty: Level 5)_
- [ ] **Range Overwrite Queries:** Apply a list of `(left, right, value)` overwrite queries to an integer array. _(Difficulty: Level 2)_
- [ ] **Alternating Parity Subarrays:** Answer range queries to determine if a subarray has strictly alternating even and odd parities. _(Difficulty: Level 4)_
- [ ] **Largest Digit-Sharing Subset:** From a list of two-digit integers, find the largest subset where every integer shares at least one digit with another. _(Difficulty: Level 1)_
- [ ] **Median of RLE Arrays:** Find the median of two run-length encoded (RLE) arrays sorted by value. _(Difficulty: Level 5)_
- [ ] **Green-Only Wordle:** Choose optimal guesses from a dictionary to find a hidden 5-letter word using only exact-match feedback. _(Difficulty: Level 3)_
- [ ] **Decompress Nested Repeats:** Decompress an encoded string where parentheses denote groups and numbers dictate repetition counts. _(Difficulty: Level 2)_

### Graphs, Trees & Matrix Traversal

- [ ] **Minimax Grid Path:** Minimize the maximum terrain height you must traverse to get from the top-left to the bottom-right of a grid. _(Difficulty: Level 5)_
- [ ] **Distance to Nearest Taxi:** In a grid map, compute the distance from every empty cell to the nearest taxi. _(Difficulty: Level 2)_
- [ ] **Shortest Path with Blockers:** Compute the shortest distance between two nodes in an unweighted graph, avoiding a specific list of blocked nodes. _(Difficulty: Level 1)_
- [ ] **Distance-Sum from Tree Nodes:** In an undirected, cycle-free tree, compute the sum of distances from each node to all other nodes. _(Difficulty: Level 4)_
- [ ] **Chicken Genealogy (LCA):** Given parent-child relationships, determine if two specific nodes (chickens) are related. _(Difficulty: Level 3)_
- [ ] **Course Catalog Dependencies:** Validate an e-learning course catalog given a set of courses and prerequisite pairs (detect cycles/topological sort). _(Difficulty: Level 2)_
- [ ] **Trinary Tree Mode:** Find the most frequently occurring value in a search tree where nodes can have up to three children. _(Difficulty: Level 5)_
- [ ] **Movie Recommendation Graph:** Recommend top movies based on a set of movies and an undirected similarity graph. _(Difficulty: Level 1)_
- [ ] **Connected Crop Layout:** Construct a garden grid planted with `k` crops, ensuring all regions are connected and safe paths exist. _(Difficulty: Level 4)_

### Intervals & Scheduling

- [ ] **Minimum Rooms Needed:** Calculate the absolute minimum number of meeting rooms required to accommodate a list of overlapping meeting intervals. _(Difficulty: Level 3)_
- [ ] **Servers for Cyclic Tasks:** Compute the minimum servers needed to run a list of repeating/cyclic tasks represented by `(start, duration)`. _(Difficulty: Level 5)_
- [ ] **Circular Day Meetings:** Calculate minimum meeting rooms for intervals scheduled within a 24-hour cyclic day (where 23:59 wraps to 00:00). _(Difficulty: Level 1)_
- [ ] **Safe Space Travel:** Find safe travel intervals along an x-axis given a list of planets and their coordinates/zones of influence. _(Difficulty: Level 4)_
- [ ] **Assign Meetings with Delays:** Assign meetings to a fixed number of rooms while factoring in dynamic delays. _(Difficulty: Level 2)_

### Dynamic Programming, Greedy & Optimization

- [ ] **Tokens & Coins Board Game:** Maximize coins collected on a 1D board where tokens can only jump exactly 3 steps. _(Difficulty: Level 4)_
- [ ] **Bounded Knapsack DP:** Solve a variation of the knapsack problem and reconstruct the optimal set of chosen items. _(Difficulty: Level 1)_
- [ ] **Non-Adjacent Sum (House Robber):** Maximize the sum of a subset of an array such that no two selected indices are adjacent. _(Difficulty: Level 3)_
- [ ] **Winning Mahjong Hand:** Determine if a 14-tile integer array represents a valid winning configuration. _(Difficulty: Level 5)_
- [ ] **Delivery Route with Danger:** Compute the shortest delivery route across stops, factoring in specific nodes marked as dangerous. _(Difficulty: Level 2)_

### System Design & Architecture

- [ ] **O(1) Random Access Set:** Design a "FancySet" that supports adding, removing, and returning a random element in average O(1) time. _(Difficulty: Level 4)_
- [ ] **Stream K-th Largest:** Design a class to track the k-th largest element as a continuous stream of numbers arrives. _(Difficulty: Level 1)_
- [ ] **Multi-Type Server Allocation:** Design a service to manage 100,000 server nodes where clients request specific instance types. _(Difficulty: Level 5)_
- [ ] **Top-K Logger:** Design an in-memory logger that records events and can efficiently query the top K most frequent messages. _(Difficulty: Level 2)_
- [ ] **Elevator Control System:** Design software for a multi-elevator system in a high-rise, including scheduling and car assignment. _(Difficulty: Level 3)_
- [ ] **Autocomplete Trie:** Implement a service using a prefix tree that supports `insert`, `update`, and `delete` with word weights. _(Difficulty: Level 4)_

### Data Science, Math & Probability

- [ ] **1D Dice Walk Probability:** Compute the probability of landing on a specific target when repeatedly rolling a 1-to-K fair die on an infinite number line. _(Difficulty: Level 3)_
- [ ] **Simulate Uniform(0,1):** Use a provided `rand_bit()` function (returns 0 or 1) to generate a random float uniformly distributed between 0 and 1. _(Difficulty: Level 5)_
- [ ] **Invoice Reconciliation:** Build an algorithm to match a list of invoice records to payments based on memo text or exact amounts. _(Difficulty: Level 1)_
- [ ] **Imbalanced Precision-Recall:** Compute evaluation metrics and a PR curve for a highly imbalanced dataset (5% positive rate). _(Difficulty: Level 4)_
- [ ] **Two Sum-of-Squares:** Find all integers s<n that can be expressed as a sum of two squares in exactly two distinct unique ways. _(Difficulty: Level 2)_
- [ ] **Bootstrap Percentage RMSE:** Implement a function to calculate pRMSE and compute its confidence interval using bootstrapping. _(Difficulty: Level 3)_
- [ ] **Next-Word Predictor:** Build an NLP model over tokenized training sentences to predict the next word based on frequencies. _(Difficulty: Level 2)_

18

5

---

## [Google Interview For Pse Product Solutio Apwn](https://leetcode.com/discuss/post/7700921/google-interview-for-pse-product-solutio-apwn/)

_Crawled: 2026-05-24 · 18 words_


Hi, has anyone recently interviewed for google pse role? Wanted to know few details around it

2

3

---

## [Expected Ctc For Google Swe Iii L4 Banga Sanz](https://leetcode.com/discuss/post/7706811/expected-ctc-for-google-swe-iii-l4-banga-sanz/)

_Crawled: 2026-05-24 · 24 words_


Hi everyone,

What CTC can I expect for a SWE III (L4) role at Google, Bangalore? I have 2.3 years of experience.

1

5

---

## [Google Forward Deployed Engineer Fde](https://leetcode.com/discuss/post/7821696/google-forward-deployed-engineer-fde-by-l4th5/)

_Crawled: 2026-05-24 · 77 words_


Hi Leetcoder,

anyone came across FDE Forward Deployed Engineer opportunities at FAANMG,

1. how its different from MLE, DS?
2. how interviews differes for MLE/DS/FDE?
3. how the pay strucrture changes?( through its very hot jb in market right now just came across about it last week.)


one of Recuriter reached out for sepcific FDE requirement? they are selling it as very hot job in current market but whats the reality.

share your thoughts.

Thankyou.

10

1

---

## [Finally Solved Number Of Islands Felt Du 8Ca6](https://leetcode.com/discuss/post/7848975/finally-solved-number-of-islands-felt-du-8ca6/)

_Crawled: 2026-05-24 · 186 words_


Today I solved **Number of Islands**, and honestly… it was way harder for me than it should have been.

* * *

### What I already knew

- What BFS is
- How adjacency list / matrix works
- Basic traversal logic

* * *

### Where I got stuck

- How to actually use BFS on a grid
- How to move properly (up, down, left, right)
- How to think step-by-step instead of just knowing theory

* * *

For a long time, it just didn’t click.

It felt confusing and honestly a bit frustrating.

* * *

### What finally clicked

- Treating the grid like a graph
- Understanding how BFS expands level by level
- Marking visited cells properly to avoid revisiting

* * *

It might be a basic problem for many, but for me, this was a real breakthrough.

I don’t know why, but I feel proud of this one 🙂

**Going to sleep with a small win today.**

* * *

### Question for others

Did anyone else struggle with grid + BFS problems like this?

2

2

---

## [Google Web Solutions Engineer Need Help Rhubf](https://leetcode.com/discuss/post/7870214/google-web-solutions-engineer-need-help-rhubf/)

_Crawled: 2026-05-24 · 84 words_


I answered interview for the Google WSE (Web Solutions Engineer) role.

Rounds:

Screening

Coding

Coding+ Web Tech

SQL+ Behavioral + Googliness

After the last round, the recruiter didn't get back. I contacted the recruiter multiple times and later got an email that the **'hiring for this role is currently on hold'**

What can I expect now?

Is this something common Google does?

Did anyone else appear for WSE interview at google?

How much time does this take, if anyone has experienced this?

0

4

---

## [Google Application Need Help](https://leetcode.com/discuss/post/7895971/google-application-need-help-by-anand004-pe44/)

_Crawled: 2026-05-24 · 145 words_


I applied for the Google WSE role and SWE I (University Hiring) off- campus role, along with many other relevant positions, all with referrals. However, I haven’t received any response.

I’m from a tier-3 but well-known university in Chennai, and I’m an MCA graduate with a strong profile, including internships, projects, and competitive programming.

I recently applied again for the Application Engineer role at Google with a referral, but still no reply.

Why is this happening? Does college tier matter that much, or is it because I have an MCA degree? Do they not consider MCA graduates?

Am i missing out anything ??? should i need to do something great to get into googlle ? please be honest with me guys dont be nice.

This is not just Google, i have also applied to Microsoft, Oracle, Salesforce, Smartsheet, and Intuit, all with referrals.

2

3

---

## [Google Interview Retake Do Interviewers 24928](https://leetcode.com/discuss/post/7882921/google-interview-retake-do-interviewers-24928/)

_Crawled: 2026-05-24 · 137 words_


Hi everyone,

I have a question about Google interviews and how they are structured across attempts.

Last year, I went through the full process and passed all technical rounds, but was not selected in the end. During my interviews, I mostly got problems related to strings/stack (e.g., similar to Decode String) also dp and backtracking and did not encounter graph problems.

Now I’m preparing again and I’m wondering:

Do interviewers have access to the types of problems I was asked or how I performed previously?

Do they intentionally vary the problem types in a new interview cycle (e.g., if I didn’t get graphs before, should I expect graphs this time)?

Or is each interview completely independent with randomly selected questions?

Would really appreciate insights from anyone who has gone through multiple Google interview loops.

Thanks!

0

3

---

## [Google L3 Team Matching 11 Months And Ex Xwiq](https://leetcode.com/discuss/post/7819881/google-l3-team-matching-11-months-and-ex-xwiq/)

_Crawled: 2026-05-24 · 120 words_


Timeline: Cleared all onsites & behavioral in May 2025.

Updates: Only one team match call in October 2025.

My recruiter consistently says there are "no updates." I am now entering the 12th month, which means my packet is probably going to expire in a few weeks.

To be honest, I feel incredibly demoralized. It's exhausting to have prepared so hard, cleared the bar, and stayed hopeful for a year, just to end up with nothing.

Has anyone else experienced this timeline recently?

1. Did your recruiter let you extend the packet, or did you have to re-interview from scratch?

2. How did you mentally bounce back from this?


Any advice, similar experiences, or motivation would be deeply appreciated.


2

5

---

## [Stuck In Google Team Match 4 Months](https://leetcode.com/discuss/post/7845117/stuck-in-google-team-match-4-months-by-a-aa4e/)

_Crawled: 2026-05-24 · 117 words_


Hi all,

I passed my Google L4 interviews in Dec 2025 (UK). After 4 months in team matching limbo, my recruiter emailed me this:

> I don't have any updates... please feel free to apply directly through our website if you see any other positions that interest you.

Is this a soft rejection? Does "apply directly" mean the recruiter has stopped actively searching for me?

How should I apply? If I find a role on the careers site, do I apply blindly, or should I reach out to the hiring manager?

Does anyone have tips for finding active Hiring Managers in the UK on LinkedIn who actually hold headcount?

Any advice or harsh truths appreciated!

1

4

---

## [Applied Scientist At Microsoft Vs Softwa Vq8G](https://leetcode.com/discuss/post/7803324/applied-scientist-at-microsoft-vs-softwa-vq8g/)

_Crawled: 2026-05-24 · 24 words_


which option is better to choose in terms of long term perspective ?

having 4 YOE. Compensation is almost same for both.

0

7

---

## [Road Traffic Monitoring System Stripe](https://leetcode.com/discuss/post/7854799/road-traffic-monitoring-system-stripe-by-4nj9/)

_Crawled: 2026-05-24 · 21 words_


Hello folks,

Can some expert in HLD provide solution for HLD of Road traffic monitoring system.

Thanks in Advance.

1

1

---

## [Google Team Match Round With Tech Lead B 3Frb](https://leetcode.com/discuss/post/7742939/google-team-match-round-with-tech-lead-b-3frb/)

_Crawled: 2026-05-24 · 177 words_


Hi everyone,

I’m currently in the team matching phase for Google L3 (London). I had a team fit call with the Hiring Manager (HM) this past Monday, which I felt went quite well.

Today, my recruiter reached out and informed me that I have another round scheduled—this time with the Tech Lead (TL) of the same team.

I had a few questions for this round:

- What should I expect in this round? Since the HM call is already done, what is the typical focus for a TL-specific match call?
- Has anyone else faced two separate calls for the same team? Is this a common part of the process?
- Will the Tech Lead deep dive into technicals? Should I expect a technical grilling or project deep-dives, or is it still largely a "fit" conversation?

Any guidance or insights from those who have been through the L3 matching process would be greatly appreciated!

* * *

PS: I’ve already posted my full interview experience and questions on Leetcode so please don't ask for it.

2

6

---

## [I Have Rotting Oranges Now 994 Rotten Or T4Bw](https://leetcode.com/discuss/post/7883464/i-have-rotting-oranges-now-994-rotten-or-t4bw/)

_Crawled: 2026-05-24 · 137 words_


# Finally got Rotten Oranges after 3 days of struggling with BFS

Spent days stuck on Number of Islands, then this problem hit me again like _**wtf**_.

* * *

But the whole thing clicked with just one line:

CPP

```cpp
int sz = q.size();
```

This line freezes which oranges spread this minute. Newly rotted ones wait for next minute. Without this-time tracking is completely wrong.

* * *

The only other new idea vs Islands is multi-source BFS — you don't seed one cell, you throw ALL rotten cells into the queue before the loop even starts.

That's literally it. Two ideas. One problem.

**Trying Walls and Gates tomorrow. If you've solved it — does the same pattern hold? Upvote if you read this, shows me someone out there is grinding too 🙌**

4

2

---

## [Amazon Sde I Contract1 Year Expectations Mc10](https://leetcode.com/discuss/post/7926825/amazon-sde-i-contract1-year-expectations-mc10/)

_Crawled: 2026-05-24 · 62 words_


Hi Community, i have a interview scheduled for sde-I (contract 1 year)

Can someone pls tell about

1. expectations in lld
2. what are the most faq lld and hld
3. tips for dsa specific to amazon if they particularly follow a pattern or if anyone has any list of asked ques recently
4. is running code expected in dsa?

0

1

---

## [Just Got Amazon 6M Internhip Offer](https://leetcode.com/discuss/post/7945762/just-got-amazon-6m-internhip-offer-by-an-brp9/)

_Crawled: 2026-05-24 · 84 words_


Hi everyone, I just want to share my interview experience for the SDE internship at Amazon that happened recently on campus. The internship will be from July–December 2026.

This year, they have slightly changed the pattern. There was an additional Gen AI round, in which I was asked about my ML and RAG-based project. It was conducted in person.

**DSA Round:** This round had 2 DSA problems based on DP and strings.

U can read my complete interview exp here: [Link](https://leetcode.com/link/?target=https%3A%2F%2Fwww.codinzhub.com%2Fquestion%2Famazon-sde-6-month-intern-july-dec-2026-on-campus-interview-experience)

[https://www.codinzhub.com/question/amazon-sde-6-month-intern-july-dec-2026-on-campus-interview-experience](https://leetcode.com/link/?target=https%3A%2F%2Fwww.codinzhub.com%2Fquestion%2Famazon-sde-6-month-intern-july-dec-2026-on-campus-interview-experience)

3

0

---

## [Notice Period Doubts](https://leetcode.com/discuss/post/7787293/notice-period-doubts-by-anonymous_user-mwno/)

_Crawled: 2026-05-24 · 27 words_


What are best ways to get more calls while serving notice period.

Can we mention it in resume .

Anything we can mention on linkedin.

0

3

---

## [Google Web Solutions Engineer Delay Afte Pmz3](https://leetcode.com/discuss/post/7889060/google-web-solutions-engineer-delay-afte-pmz3/)

_Crawled: 2026-05-24 · 135 words_


Hi all, I interviewed for a Google Web Solutions Engineer role (India).

Timeline:

- Jan 30: Recruiter reached out
- Feb 9: Screening
- Feb 17–18: Technical rounds (DSA + web/system)
- Late Feb: SQL + System Design + Behavioral
- Director round (~5-10 min)

Recruiter said my technical performance was good, but communication could be more confident, the feedback I asked before director round.

Since then, (HR never ghosted me, used to reply quick for my follow up emails and called to explain delays)

I got responses like:

- feedback pending from an interviewer
- in hiring pool
- hiring team busy with campus hiring

Last update was on April 1 (asked to wait 2–3 weeks). No update after that.

Is this normal? Am I still under consideration or likely rejected?

Thanks!

0

5

---

## [Google L4 Dsa Phone Screen India 5 Yoe B 8Umr](https://leetcode.com/discuss/post/7785661/google-l4-dsa-phone-screen-india-5-yoe-b-8umr/)

_Crawled: 2026-05-24 · 84 words_


Hi everyone,

I have my Google SDE-L4 DSA phonescreen/virtual round scheduled for tomorrow (India region), and I have ~5 years of experience.

The interview is 45 minutes total, including introductions and discussion.

I wanted to get a sense from folks who’ve gone through this recently:

What difficulty level should I expect (LeetCode Easy/Medium/Hard)?

Is it usually one question or multiple?

How deep do they go into optimizations and edge cases given the time constraint?

Any last-day tips would also be really appreciated!

5

11

---

## [Google L5 Screening Reject](https://leetcode.com/discuss/post/7855988/google-l5-screening-reject-by-anonymous_-4a2i/)

_Crawled: 2026-05-24 · 201 words_


I recently got a call directly from a recruiter at Google since I had interviewed with them in the past (and declined an offer back then).

This was a screening stage with:

1 DSA round

1 Googliness round

Followed by onsite rounds (if cleared)

Round 1: DSA

Problem:

A user has a faulty keyboard where some keys get stuck, causing characters to repeat more than intended.

Given a dictionary of valid words, return all possible words the user intended to type.

Approach:

Built a Trie from the dictionary

Used backtracking to explore valid matches by collapsing repeated characters

The idea was:

Treat repeated characters as a flexible match (e.g., "heeellooo" → "hello")

Traverse the Trie while deciding whether to:

Consume multiple same chars

Or move forward

Verdict: Rejected

Reason:

I solved the main problem

But the interviewer wanted to go deeper with follow-ups

Unfortunately, we ran out of time before that

Solving the base problem is not enough — always leave time for follow-ups

Round 2: Googliness

Question:

Give an instance of self-improvement

I talked about a real example from my experience where I:

Identified a gap

Took structured steps to improve

Measured the impact

Verdict: Hire

Overall: Rejected

9

6

---

## [Google L4 Onsite Strong Dsa Failed Codin Bed9](https://leetcode.com/discuss/post/7909727/google-l4-onsite-strong-dsa-failed-codin-bed9/)

_Crawled: 2026-05-24 · 349 words_


Hi there, this one hurts, so I’m writing it out partly to process it and partly because I’d genuinely appreciate advice.

A Google recruiter found me through LinkedIn and reached out saying my profile stood out, that my education and experience looked impressive, and that I should absolutely go through the process. This role is honestly a dream job for me, and for years I never even applied because I thought I’d get filtered before I had a chance.

I just got the feedback call.

She said I passed the Googliness / leadership part very strongly.

She also said "they thought my data structures and algorithms knowledge was outstanding."

But they failed me on the coding round for L4 because, in her words, “the solution and follow ups were correct, but there were some areas for improvement in code comprehension and programming skills.” She also said I was close enough that I do not have to wait out the full cooldown, and that I should reach back out in October 1st to interview again and retake the coding round and if i didn't they will generally check to see if i'm still interested or if my situation's changed.

So now I’m trying to understand what this actually means in practice.

What confuses me is that I know that I had a correct solution. So if the algorithmic thinking was strong and the solution itself was basically right, what does “code comprehension / programming skills” usually refer to at Google L4?

Is this typically about:

- writing code that is cleaner and easier to follow?
- making correctness more obvious while coding?
- handling all edge cases in the implementation, not just verbally?
- needing too much guidance while turning the idea into code?
- code quality / polish rather than algorithmic ability?

I’m trying to use this as a roadmap instead of just feeling terrible about it.

So for anyone who has interviewed with Google, interviewed candidates, or gotten similar feedback before eventually passing:

what concrete changes helped you bridge that gap?

I’d really appreciate direct advice.

3

5

---

## [Google Recruitment Process 2 Weeks And N Vosh](https://leetcode.com/discuss/post/7911003/google-recruitment-process-2-weeks-and-n-vosh/)

_Crawled: 2026-05-24 · 101 words_


I had two technical interviews at Google two weeks ago (virtual on-site via Google Meet). This was the second stage of the process, following an initial technical interview and a Googleyness interview which I had already passed.

I still haven’t received an update on whether I passed or not. Is this delay usually a bad sign, or could it just be normal due to the holiday season?

I sent a follow-up email to the recruiter yesterday afternoon (It's been nore than 24 hours) but haven’t heard back yet.

Would love to hear about your experience with Google’s timelines. Thanks!

1

8

---

## [Study Mate For Sde 2 Sde 3 Prep Faangfaa 3Yyc](https://leetcode.com/discuss/post/7929482/study-mate-for-sde-2-sde-3-prep-faangfaa-3yyc/)

_Crawled: 2026-05-24 · 127 words_


Hey Guys

I am looking for few people with whom i can connect 1-2 times in a week for discussion & mock for System Design + DSA. We can make weekly target and plan accordingly for visibility. We can also share HR contact details with each other.

I am targeting FAANG/ FAANG+ companies for SDE-2 / SDE-3 role, even foreign also.

If interested & you can remain consistent, please fill out the below form I will ping you.

Link: [https://docs.google.com/forms/d/1BGbtrzV6LG9VTRCt-1sEzPlZpA1WEVgEfex5YTsWcKk/edit](https://docs.google.com/forms/d/1BGbtrzV6LG9VTRCt-1sEzPlZpA1WEVgEfex5YTsWcKk/edit)

About me:

Working at one of the FAANG(2022 passout), India.

I am in really good touch with DSA since i prepared for Google recently and currently want to focus more on designing part with DSA.

If you are in same boat then let's connect.

Thanks

1

3

---

## [Google Interview Update](https://leetcode.com/discuss/post/7939900/google-interview-update-by-anonymous_use-7q3a/)

_Crawled: 2026-05-24 · 92 words_


Had an interview on Apr 6. The question was around graphs.

Initially went in the DSU direction and spent some time there, then realized it wasn’t the right fit and pivoted to DFS. Managed to get the main part working, but ran out of time before fully attempting the follow-up (which was an optimization variant).

Overall felt decent about the discussion but not sure how it’ll be evaluated. Still waiting to hear back on the result.

Anyone else who interviewed around Apr 6 — have you received any feedback yet?

3

3

---

## [Google L4 Bengaluru Reject](https://leetcode.com/discuss/post/7867127/google-l4-bengaluru-reject-by-anonymous_-vho0/)

_Crawled: 2026-05-24 · 173 words_


I interviewed for Google's L4 SWE position last December.

YOE: 3.8

## Time Line

### Phone Screen:

(Via Referrel) October 2025

Simple knapsack DP variation - able to solve with memoization but no time for tabulation.

### Onsite

December 2025

##### Round 1 (DSA)

Similar to Designing Orderbook/Auction system (bid price and execute lowest bid)

##### Round 2 (DSA)

Variant of Merge Intervals and Overlapping Intervals (Line Sweep & Priority Queue)

##### Round 3 (Googlyness)

Standard behavioural Questions

### Team Matching

January 2026

Recruiter told me feedback for R1 and R2 were strong and for R3 it's neutral. Recruiter decided to move forward.

### Verdict

February 2026

Recruiter told me Hiring managers were not showing interest for my profile and so will be closing the loop and not moving forward. Sent multiple followup mails for waiting 2 more months to increase chance, but no reply from recruiter. Application moved to Not proceeding in the jobs portal, but didn't get the rejection mail.

Never seen such a scenario before in leetcode discussion.

8

8

---

## [Google Onsite Swe Ii](https://leetcode.com/discuss/post/8019003/google-onsite-swe-ii-by-anonymous_user-yd0w/)

_Crawled: 2026-05-24 · 23 words_


Upcoming onsite DSA round for SWE-II at Google.

~1.10 years of full-time experience (excluding internship).

Open to any tips or guidance!

2

1

---

## [Google L4 Chances](https://leetcode.com/discuss/post/7881477/google-l4-chances-by-anonymous_user-ik8e/)

_Crawled: 2026-05-24 · 307 words_


Hi all,

I had my Google preliminary rounds today and feeling a bit uneasy about how it went.

DSA Round:

I was given a question similar to “Count Visible People” but with a twist in visibility rules.

In this version, if the observer is taller, shorter people in between don’t block the view.

Example:

Array: 1, 10, 6, 7, 9, 2, 4, 5

For 5, visible people are: 4, 2, 9, 10

(In the usual LeetCode version, 2 wouldn’t be visible, but here it is.)

For the initial part, I was able to write an optimal O(n) solution.

Then the interviewer asked a follow-up to compute it for the entire array.

I gave a brute force solution (O(n²)) verbally.

When asked to optimize, I tried a few approaches but couldn’t reach a correct solution in time.

Toward the end, I wrote a monotonic stack based pseudocode, but later realized it was incorrect.

After the interview, I tried to upsolve it. One alternative I found was using a segment tree, but that would be around O(n² log n), which is actually worse than my brute force. So now I feel my initial verbal solution might have been the best possible here.

Honestly, this round didn’t feel that strong. I feel interviewer wasn’t very impressed.

Googlyness Round: This went really well. The discussion felt natural, and I was able to answer everything confidently. This is the only part I feel good about.

For Google, is it still possible to move to next (on-site) rounds with one average DSA round but strong googlyness round?

How long does Google usually take to get back after prelim rounds?

Right now it just feels like I missed it by a small margin, which is kind of hard to shake off.

Would really appreciate honest insights from people who’ve gone through loop.

9

9

---

## [Google L4](https://leetcode.com/discuss/post/7869055/google-l4-by-anonymous_user-i3e3/)

_Crawled: 2026-05-24 · 86 words_


Hey everyone,

I had a question for those who’ve recently interviewed with Google.

I’ve been using Google Docs, and honestly, the coding experience isn’t great—indentation is clunky, no auto-closing brackets/parentheses, etc.

Since Google interviews are conducted using Google Docs, I wanted to ask:

👉 Is the interview environment exactly the same as regular Google Docs?

👉 Or do they provide any improved/internal editor with better coding support (indentation, syntax help, etc.)?

Would really appreciate insights from people who’ve gone through the process recently 🙏

0

5

---

## [Help Needed For The Coming Google Onsite Ps8Y](https://leetcode.com/discuss/post/8008818/help-needed-for-the-coming-google-onsite-ps8y/)

_Crawled: 2026-05-24 · 108 words_


Hello All,

Need some guidance, I have a google full loop on-site interview(2 DSA and 1 system design) in 10 days. The thing is I feel very unprepared for the system design part, I don't have very in depth knowledge of things asked in interviews, and I also don't want to make a fool of myself there sitting in front of the interviewer. So experienced folks of this platform please share how or what I should study in the coming days so that at least I feel that I gave my best shot at the end of the interview.

Thanks in advance.

PS Its for L5

3

6

---

## [Advice For Google L4 Rounds](https://leetcode.com/discuss/post/7967734/advice-for-google-l4-rounds-by-anonymous-5dzr/)

_Crawled: 2026-05-24 · 104 words_


Hi everyone,

I have a Google L4 interview coming up and wanted to get a better sense of what to expect.

How difficult are the DSA questions typically in these rounds? I’ve completed Striver’s SDE sheet, but I’m still unsure about the patterns I should focus on and the overall level of complexity I should be prepared for.

It would also be really helpful if someone could share insights on how to prepare for the “Googlyness” (behavioral) round. I want to make sure I don’t mess that up.

Any advice, preparation strategies, or personal experiences would be really helpful. Thanks in advance!

2

5

---

## [Google Getting Team Call With Tl Is A Go Z9Au](https://leetcode.com/discuss/post/7920939/google-getting-team-call-with-tl-is-a-go-z9au/)

_Crawled: 2026-05-24 · 120 words_


hi, I'm in team matching with Google for L3 position.

I had one team call with HM and after 2 days recruiter told me that I had a call with Tech lead of the same team. Meeting with Tech Lead was very informal and seems like he was trying hard to sell the team to me.

Also it seems like to be a soft offer.

But it's been 12 days since my call with Tech Lead and I didn't get any update yet.

Does anyone face similar situation??

Getting team call with Tech Lead is positive sign or just a normal process. (in my previous team calls I had only calls with HMs).

Can I still be rejected??

4

3

---

## [Google Hiring Manager Round Gemini Appli Mb5K](https://leetcode.com/discuss/post/7936329/google-hiring-manager-round-gemini-appli-mb5k/)

_Crawled: 2026-05-24 · 431 words_


# Google Hiring Manager Round (Gemini Applications Team)

Recently, I gave the Hiring Manager round for **SWE III (ML)** at Google for the Gemini Applications team.

I have ~4.5 years of experience as a Data Scientist in a mid-size company.

The interview lasted around 30 minutes and focused on introduction followed by questions around building and deploying scalable systems.

* * *

## Interview Questions & Discussion

### Q1. Can you introduce yourself and walk me through one project?

**My Answer:**

Introduction and brief discussion about one project

* * *

### Q2. How is evaluation done for such systems?

**My Answer:**

Answered relevant to the project

* * *

### Q3. How would you design a multi-task system that handles varying domains?

**My Answer:**

Given constraints like limited resources and business pressure, and assuming access to a new model from the Gemini team:

- Use golden datasets to evaluate performance across different tasks
- Apply prompt enhancements instead of fine-tuning due to time constraints
- Highlighted that a single model may not effectively handle all domains

* * *

### Q4. How would you develop or improve the model over time?

**My Answer:**

With the help of golden datasets and stakeholders

* * *

### Q5. What would you do if no additional data is available?

**My Answer:**

Could not give a satisfactory answer

(Expected: agentic-based evaluation on top of golden datasets to iterate faster)

* * *

## My Questions to the Interviewer

### Q1. How do you ensure systems are reliable across so many domains?

### Q2. Do you use internal frameworks, or is there a dedicated team building solutions for new agentic workflows while others focus on implementation?

* * *

# Other Interviews:

### Google

- [First Round \| SWE III ML \| Bengaluru](https://leetcode.com/discuss/post/6973035/google-first-round-swe-iii-ml-bengaluru-d9rdx/)
- [Googleyness Round \| SWE III ML](https://leetcode.com/discuss/post/7093123/google-gl-googleyness-round-swe-iii-ml-b-0fe9/)
- [Hiring Manager Round \| Gemini Applications Team](https://leetcode.com/discuss/post/7936329/google-hiring-manager-round-gemini-appli-mb5k/)

### Other Tech Firms

- [Amazon \| Interview (1st Round) \| Applied Data Scientist \| Bengaluru](http://leetcode.com/discuss/post/6871782/amazon-online-1st-round-bengaluru-applie-uiwk/)
- [Freshworks \| OA (1st Round) \| Data Scientist \| Bengaluru](https://leetcode.com/discuss/post/6872463/freshworks-oa-data-scientist-jan-2025-be-97v4/)
- [Razorpay \| OA (1st Round) \| Senior MLE \| Bengaluru](https://leetcode.com/discuss/post/6889780/razorpay-oa-1st-round-senior-mle-bengalu-47vj/)
- [Avaamo \| Interview \| Senior MLE \| Bengaluru](https://leetcode.com/discuss/post/6879712/interview-senior-mle-avaamo-bengaluru-by-l9sy/)
- [Visa \| Coding Round \| Senior Data Role \| Bengaluru](https://leetcode.com/discuss/post/6937441/visa-coding-round-bengaluru-senior-data-t3zk2/)

* * *

## Compensation

### Offer / Compensation Discussions

- [Gallagher (GCoE) \| Offer Summary \| Senior Gen AI Engineer](https://leetcode.com/discuss/post/6871661/offer-summary-senior-gen-ai-engineer-gal-xqo1/)
- [Samya AI (Fractal) \| Compensation \| Data Scientist](https://leetcode.com/discuss/post/6877450/compensation-samya-ai-fractal-data-scien-qoox/)
- [Avaamo \| Machine Learning Engineer \| Compensation](https://leetcode.com/discuss/post/6877472/compensation-machine-learning-engineer-a-vxh4/)
- [ElasticRun \| Compensation \| AI Engineer \| Bengaluru](https://leetcode.com/discuss/post/7012559/compensation-ai-engineer-elasticrun-beng-i0du/)
- [Compensation \| Searce \| Machine Learning Engineer \| Pune](https://leetcode.com/discuss/post/8286166/compensation-searce-machine-learning-eng-1v4o/)

6

3

---

## [Team Match Result On Hold](https://leetcode.com/discuss/post/7949330/team-match-result-on-hold-by-anonymous_u-hesd/)

_Crawled: 2026-05-24 · 60 words_


I recently appeared for team match at Google,

manager said a yes to me on the call. 2 days later HR told me I have been put on hold, then she stopped replying to my emails, stopped picking up my calls. Looks like she has ghosted me.

Anyone who has similar experience? What to do in such cases?

1

5

---

## [Onsite Interviews In May First Week](https://leetcode.com/discuss/post/8095461/onsite-interviews-in-may-first-week-by-a-18s8/)

_Crawled: 2026-05-24 · 89 words_


Hi everyone, I have Google onsite interviews scheduled in the first week of May for SWE role. I’m currently focusing on DSA prep and wanted to ask the community:

- Any must-solve sheets / curated lists for final revision?
- Any recently asked question banks or patterns that are trending in onsite rounds?
- Any high-yield topics I should prioritize in the last stretch?
- General tips for performing well in onsite coding rounds?

Would really appreciate any suggestions from people who interviewed recently. Thanks in advance!

2

3

---

## [Google Bangalore Onsite L4 Final 2 Dsa R Okwd](https://leetcode.com/discuss/post/8052794/google-bangalore-onsite-l4-final-2-dsa-r-okwd/)

_Crawled: 2026-05-24 · 38 words_


Hi everyone,

I have my last 2 onsite rounds coming up at Google Bangalore (L4) both are DSA rounds, in-person, back-to-back, and I wanted to understand what kind of questions are typically asked at this stage.

2

5

---

## [Google L4 Team Matching Looker Team](https://leetcode.com/discuss/post/8102178/google-l4-team-matching-looker-team-by-a-lhav/)

_Crawled: 2026-05-24 · 76 words_


Hi Folks, after 4 months of my last interview at Google i finally got a team matching call at **Looker Team** Hyderabad (Flutter - L4 Mobile Developer). If anyone knows about the team culture and growth opportunities, please do share with me as i have to decide if i should choose the team or wait for other teams to match. Also how risky it is to wait for another team to get matched?

Thanks

4

4

---

## [Google Sdeiii Interview Experience](https://leetcode.com/discuss/post/8096071/google-sdeiii-interview-experience-by-an-67tm/)

_Crawled: 2026-05-24 · 349 words_


I recently went through the interview process for an SDE3 L4 role at Google.

There were four rounds in total — two virtual rounds followed by two back-to-back onsite rounds.

Round 1 (Phone Screening):

This was a DSA round. The problem was based on arrays — given an array, we had to check whether it could be divided into groups of size 5 such that each group contains consecutive increasing numbers. The output was a boolean (true/false).

The discussion mainly revolved around handling duplicates properly and ensuring all elements are used exactly once.

Round 2 (Behavioral / Team Fit):

This round was more conversational. Questions were around past experiences — times when I took ownership, made mistakes, handled disagreements, etc.

One situational question was about planning a team outing where people have different preferences and are not aligned — how to handle that and reach a decision.

Overall positive feedback so moved to onsite interviews.

Round 3 (Onsite – DSA):

I was given a set of points on a 2D plane (array of \[x, y\] pairs). The task was to find the maximum area of a rectangle that can be formed using those points.

The challenge here was not just identifying rectangles but doing it efficiently. I discussed multiple approaches and reached an optimized solution, but due to time constraints, I couldn’t fully complete the code. Most of the time went into reasoning about the geometry and optimizing the approach.

Round 4 (Onsite – DSA):

This round was based on task scheduling.

First part: Given multiple tasks (all with equal execution time) and a set of machines, determine the earliest time by which all tasks can be completed.

Second part: Given the number of tasks and execution time, find the minimum number of CPUs required to achieve that earliest completion time.

The key idea here involved combining scheduling logic with binary search to optimize resource usage.

Overall, the interviews were heavily focused on problem-solving, optimization, and clarity of thought. Communication played a big role, especially in explaining approaches and trade-offs.

Verdict: Not positive

Cool-off period: 12 months

10

7

---

## [Dsa Group For Faang Preparations Serious Qu6E](https://leetcode.com/discuss/post/8110216/dsa-group-for-faang-preparations-serious-qu6e/)

_Crawled: 2026-05-24 · 80 words_


I've been practicing **DSA** for a while, but honestly I struggle with **discipline and procrastination** sometimes.

I’m sure many people face the same issue.

So I thought — instead of struggling alone, why not **work together and stay accountable**?

If you're also learning **Data Structures & Algorithms** and want a small group to:

• Stay consistent

• Discuss problems

• Share resources

• Motivate each other

Fill this form and let's build a small **DSA accountability group**.

[https://docs.google.com/forms/d/e/1FAIpQLSdbZo5NrOaZmF4AIzkfLkqN1i9ZcaPicVjJ8foSipWefwKLKQ/viewform?usp=publish-editor](https://docs.google.com/forms/d/e/1FAIpQLSdbZo5NrOaZmF4AIzkfLkqN1i9ZcaPicVjJ8foSipWefwKLKQ/viewform?usp=publish-editor)

0

8

---

## [Preparation Strategy For Google L4](https://leetcode.com/discuss/post/8155455/preparation-strategy-for-google-l4-by-an-ny79/)

_Crawled: 2026-05-24 · 158 words_


Hii everyone.

Just resumed the DSA preparation again. Deleted the old account and this is a new account 5-6 months old.

I am doing good in life, as a SDE-2, and now I think is the time to revive that old dream of getting into Google.

Slow and steady, I have given myself a time of 11 months and next year this time, I want to crack Google.

A lot of you are here, preparing with dedication, so I thought it would be best to ask you guys for a preparation strategy.

I have office (Hybrid), but mostly 10-6. So for a time period of **6-10 months**, how should I prepare.

DSA Language - **Python** (as my office tech stack is also Python Backend & AI/ML pipelines, so would be better to stay with python)

Assume, after working and all, I am not in touch with DSA, so will be completely new (theoritically).

Thanks & Regards

1

1

---

## [Google L4](https://leetcode.com/discuss/post/8113604/google-l4-by-anonymous_user-y9xg/)

_Crawled: 2026-05-24 · 52 words_


I had a recruiter connect, and have been invited for 2 virtual rounds focussed on DSA and behaviour rounds.

1. What topics should I focus on for DSA ?
2. Any resources that I can refer to ? Open to premium resources as well.
3. Would Leetcode Premium help ?

2

6

---

## [Google Senior Software Engineer Preparat B4Fw](https://leetcode.com/discuss/post/8140583/google-senior-software-engineer-preparat-b4fw/)

_Crawled: 2026-05-24 · 99 words_


I'm beginning my preparation for a Senior Software Engineer role at Google and would appreciate guidance on a few areas:

- Coding Rounds
  - What’s the most effective way to prepare without resorting to randomly solving problems?
  - Beyond LeetCode’s company-specific lists, are there any well-curated resources or structured problem sets you would recommend?
- System Design & Behavioral Rounds
  - Could you suggest high-quality resources specifically relevant to Google’s interview style?
- General Advice
  - Any additional tips or strategies that could improve my preparation would be greatly appreciated.

Thank you for your time and guidance.

1

4

---

## [Onsite Google Interview L4 Bangalore](https://leetcode.com/discuss/post/8133843/onsite-google-interview-l4-bangalore-by-czhvf/)

_Crawled: 2026-05-24 · 163 words_


Hi everyone,

I have my Google onsite coming up soon and I’ve been doing a last round of graph prep. While going through problems, I noticed some topics like Kosaraju’s algorithm, Tarjan’s algorithm, strongly connected components (SCC), and Euler paths/circuits showing up.

The issue is that I’ve never studied these topics in depth only have a very high level idea (vague idea). Given the time constraints, I’m unsure whether it’s worth diving deep into them now or if it’s reasonable to skip them and focus on more common graph patterns like BFS/DFS, shortest paths, topological sort, DSU, etc.

For those who have recently interviewed (especially at Google), how relevant are these topics? Do they come up often in interviews, or are they more niche? Would it be risky to skip them at this stage?

Also, if you think they are important, any concise resources or ways to quickly get interview ready for these topics would be really helpful.

Thanks in advance.

0

1

---

## [How Hard Is To Get A Team In Google Lond Oc5C](https://leetcode.com/discuss/post/8133990/how-hard-is-to-get-a-team-in-google-lond-oc5c/)

_Crawled: 2026-05-24 · 93 words_


hi,

I'm in team matching for Google London since December 2025. I had two team calls so far and both the times HM ended up selecting internal candidates.

I have few questions

1. Can I get a team in London as a external candidate? (Indian)
2. Just because I need visa, HM hesitate to select me?
3. Any tips how to convert team calls into offer. I believe both calls went very well.
4. Why Google HM gives false hope. I had experience this in my previous two team calls?

Thanks!!

0

3

---

## [Sde 2 Sde 3 Prep Mock Lld Hld Discussion 22Bz](https://leetcode.com/discuss/post/8153766/sde-2-sde-3-prep-mock-lld-hld-discussion-22bz/)

_Crawled: 2026-05-24 · 109 words_


Hi Everyone

I want to connect with few people who are serious about switch for SDE-2 / SDE-3 role (FAANG / FAANG+) in coming few months and can remain consistent.

We can practice mock together and discuss (LLD + HLD) for better clarity & avoid rejection in interview.

We can also share contact details of HR to increase the interview calls.

If interested, please fill out the below form to get connected.

Link: [https://docs.google.com/forms/d/1Sg7rYYDyMOUxBzo-UllZxQFNNLJo\_xbufDmI4QqT02g/edit](https://docs.google.com/forms/d/1Sg7rYYDyMOUxBzo-UllZxQFNNLJo_xbufDmI4QqT02g/edit)

About me:

Working at FAANGMULA(2022 passout)

I am in really good touch with DSA and paticising more Designing Questions to get confidence.

If you are also on similar track then let's connect.

Thanks

0

4

---

## [Google L4 Oa Interviews](https://leetcode.com/discuss/post/8159666/google-l4-oa-interviews-by-anonymous_use-6mmf/)

_Crawled: 2026-05-24 · 51 words_


I have my interviews scheduled for L4 level. I received confirmation last week, and just today received an invite for an OA from Google.

Are the two related or are they part of separate processes ?

Also, what DSA topics should I emphasize on ?

Any particular patterns ?

4

1

---

## [Google Compensation Advice L3 Bangalore Ibjqb](https://leetcode.com/discuss/post/8154463/google-compensation-advice-l3-bangalore-ibjqb/)

_Crawled: 2026-05-24 · 175 words_


I am currently in offer discussion phase at Google (L3) for Bengaluru location. I want to seek advice about what should be my expected CTC ?

Years of Experience: 1 year 10 months

College: DTU / NSIT / IIITD (don't know which tier they belong to as per Leetcode community)

Branch: CSE

Role / Level: L3

Location: Bengaluru

Current Company: Product based MNC

Current Compensaton: around 16.5 lpa (15 base + 1.5 variable)

I want to ask the following questions:

1. I want to know what CTC (Base + RSU) should I quote to HR ?
2. One of my friend told me that RSUs are distributed across 4 years of vesting (40% + 40 + 10 + 10). Is it true for all L3 joiners or does it depend on discussion with HR and may vary as per discussion ?
3. If 2nd point is true, what should be my expected CTC/year ?
4. May sounds funny, but pls tell how to negotiate ? (never negotiated earlier, its my first switch !!)

1

10

---

## [Google L4 Team Matching](https://leetcode.com/discuss/post/8167765/google-l4-team-matching-by-vk_kr-18eq/)

_Crawled: 2026-05-24 · 51 words_


I had my google team matching on 13th april. After that i haven't received the feedback of team matching yet. Till 1-2 weeks back the recruiter was saying that she is waiting for feedback. After that she isn't replying to my mail now.Does anyone else also encountered this situation?

2

5

---

## [Part 2 100 Interviews 50 Companies 1 Off Cjdq](https://leetcode.com/discuss/post/8162098/part-2-100-interviews-50-companies-1-off-cjdq/)

_Crawled: 2026-05-24 · 253 words_


I made a post last year:

[https://leetcode.com/discuss/post/7176708/100-interviews-50-companies-0-offers-by-dbhmq/](https://leetcode.com/discuss/post/7176708/100-interviews-50-companies-0-offers-by-dbhmq/)

After that post, I interviewed with 7 more companies including Oracle, Twilio, Salesforce, etc., and finally received an offer from Oracle.

I finally joined Oracle, but due to my bad time, I was one among the 30,000 in the massacre done by Oracle.

Below are my experiences post layoff.

| # | Company | Role | Result |
| --- | --- | --- | --- |
| 1 | Kotak | SDE 2 | Rejected in 2nd round (DSA) |
| 2 | Kgen | SDE 2 | Rejected in 1st round (System Design) |
| 3 | Impact Analytics | SDE 2 | Rejected in 3rd round (Tech Python) |
| 4 | Amazon | SDE 2 | 4 rounds completed(Loop) - rejected because of LPs |
| 5 | HealthEdge | SDE 2 | Rejected in 2nd round (Technical) |
| 6 | Google | SWE III | Rejected in Screening (DSA) |
| 7 | Kotak (Fullstack) | SDE 2 | Rejected in 1st round: React, Node.js |
| 8 | Redpin | SDE 2 | Ghosted after 1st round |
| 9 | Photon | SDE 2 | Rejected in 1st round (Technical) |
| 10 | Arrise | SDE 2 | Rejected in 3rd round (Java) |
| 11 | Uber | SDE 2 | Rejected in 3rd round (LLD) |

**Again the same rejection story, I'm planning to leave the Software industry. Its not working for me..**

17

11

---

## [Google Interview Experience 2 Rounds Swe Ku5D](https://leetcode.com/discuss/post/8173874/google-interview-experience-2-rounds-swe-ku5d/)

_Crawled: 2026-05-24 · 191 words_


I recently had the opportunity to interview with Google, and I wanted to share my experience.

Round 1: DSA (Graphs)

The round focused on a graph-based problem (easy–medium level).

Problem Summary:

Given a weighted graph and a node, remove that node along with all its connected edges, and return the maximum edge weight remaining in the graph.

I explored multiple solutions during the discussion:

Priority Queue Approach:

Stored all edges in a max-heap and kept popping until I found an edge not connected to the removed node.

Multiset Approach:

Used a sorted structure to maintain edges and efficiently retrieve the maximum valid edge.

Optimized Preprocessing Approach (Final Solution):

Built an auxiliary structure to precompute the maximum edge weight for each node after its removal.

This allowed answering queries in O(1) time.

💡 The interviewer seemed reasonably satisfied, especially with the progression from brute-force to optimized thinking.

💬 Round 2: Googliness (Behavioral Round)

This round focused on:

Past projects

Problem-solving approaches

Real-life situations

Ownership and decision-making

Overall, it was a great learning experience. The process really tests both technical depth and problem-solving mindset, along with how you approach real-world challenges.

1

6

---

## [Google Phone Interview Questions](https://leetcode.com/discuss/post/8195929/google-phone-interview-questions-by-anon-mk7j/)

_Crawled: 2026-05-24 · 238 words_


Hello all,

I compiled a list of Google interview questions from discuss section and recent interview experiences. Hope it helps!!

Also was checking some recent 6 months /company tagged lists on [Codolio company kit](https://leetcode.com/link/?target=https%3A%2F%2Fcodolio.com%2Fquestion-tracker%2Fsheet%2Fpremium%2Fgoogle_all) while preparing and saw many of these repeated there too.

Here is the list:

- Median of Two Sorted Arrays [#4](https://leetcode.com/problems/median-of-two-sorted-arrays/)

- Trapping Rain Water [#42](https://leetcode.com/problems/trapping-rain-water/)

- Longest Substring Without Repeating Characters [#3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

- Longest Palindromic Substring [#5](https://leetcode.com/problems/longest-palindromic-substring/)

- Longest Consecutive Sequence [#128](https://leetcode.com/problems/longest-consecutive-sequence/)

- Subarray Sum Equals K [#560](https://leetcode.com/problems/subarray-sum-equals-k/)

- Russian Doll Envelopes [#354](https://leetcode.com/problems/russian-doll-envelopes/)

- Number of Islands [#200](https://leetcode.com/problems/number-of-islands/)

- Koko Eating Bananas [#875](https://leetcode.com/problems/koko-eating-bananas/)

- Next Permutation [#31](https://leetcode.com/problems/next-permutation/)

- Search in Rotated Sorted Array [#33](https://leetcode.com/problems/search-in-rotated-sorted-array/)

- Decode String [#394](https://leetcode.com/problems/decode-string/)

- Number of Visible People in a Queue [#1944](https://leetcode.com/problems/number-of-visible-people-in-a-queue/)

- LRU Cache [#146](https://leetcode.com/problems/lru-cache/)

- Meeting Rooms II [#253](https://leetcode.com/problems/meeting-rooms-ii/)

- Longest Repeating Character Replacement [#424](https://leetcode.com/problems/longest-repeating-character-replacement/)

- Find First and Last Position of Element in Sorted Array [#34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

- Maximal Rectangle [#85](https://leetcode.com/problems/maximal-rectangle/)

- Largest Rectangle in Histogram [#84](https://leetcode.com/problems/largest-rectangle-in-histogram/)

- Rotate Image [#48](https://leetcode.com/problems/rotate-image/)

- Course Schedule [#207](https://leetcode.com/problems/course-schedule/)

- Regular Expression Matching [#10](https://leetcode.com/problems/regular-expression-matching/)

- Sudoku Solver [#37](https://leetcode.com/problems/sudoku-solver/)

- Edit Distance [#72](https://leetcode.com/problems/edit-distance/)

- Longest Increasing Subsequence [#300](https://leetcode.com/problems/longest-increasing-subsequence/)

- Split Array Largest Sum [#410](https://leetcode.com/problems/split-array-largest-sum/)

- Sliding Window Maximum [#239](https://leetcode.com/problems/sliding-window-maximum/)

- Merge k Sorted Lists [#23](https://leetcode.com/problems/merge-k-sorted-lists/)


Some questions are the closest that it can get to the actual question. Especially LRU Cache, Sliding Window Maximum, Median of Two Sorted Arrays and Russian Doll Envelopes.

Hope it helps someone preparing :)

4

1

---

## [Next Steps After Onsite Interviews](https://leetcode.com/discuss/post/8198530/next-steps-after-onsite-interviews-by-an-4jnw/)

_Crawled: 2026-05-24 · 53 words_


Had my onsite recently for a Google L4 SWE position. Curious about current timelines after onsite.

How long did it take for you to:

- get onsite feedback
- move to team matching
- receive final decision/offer

Would be helpful to know recent experiences since processes seem to vary a lot.

2

3

---

## [Urgent Google Onsite Interview](https://leetcode.com/discuss/post/8193404/urgent-google-onsite-interview-by-anonym-wi2v/)

_Crawled: 2026-05-24 · 66 words_


Hey Guys,

I've upcoming Google Onsite Interview Scheduled for L4. I'm done with virtual 2 rounds and left with 2 offline rounds. It will be really helpful for me if you can suggest what to expect and any tips and trickes to keep in mind.

PS: Once done with the process, will be more than happay to share the entire end to end experience.

2

5

---

## [Google L4 In Person Interview](https://leetcode.com/discuss/post/8218498/google-l4-in-person-interview-by-anonymo-eqbq/)

_Crawled: 2026-05-24 · 211 words_


Location : BLR

Role : L4

I gave my Google in-person interview today. I wanted to know as per the mistakes what kind of rating \[ ie NH/LH/H \] I could get according to you guys.

It was a mapping question where provided a key-value pair and source string, I was supposed to return the output. In the source string anything that was present between 2 % signs were supposed to be taken as a key.

My mistakes :

1. I pointed out all keys might not be present so we will return "-1" as response. The interview said that could also be a valid response. I took a couple of secs to think and till the interviewer said "How about returning an error ?" I went with his idea and implemented that.

2. I totally missed that a key's value could have another key present inside it. Eg : X--> "%y%/home". I simply needed to add a recursive call after finding the key and I did that.

3. After doing the recursive call, I told him that we might have cycles. I stored earlier occuring keys in a vector and he suggested why not use a unordered\_map to save time and space.


What do you guys think ?

3

3

---

## [My Relationship With My Manager Is Destr Jzw0](https://leetcode.com/discuss/post/8229968/my-relationship-with-my-manager-is-destr-jzw0/)

_Crawled: 2026-05-24 · 45 words_


My manager just tries to find ways to put me down, these days he doesn't even try to listen to my points. he might be even thinking of laying off me. Urgent! any EM or senior dev who could help me out here?

0

1

---

## [Google L4 Interview](https://leetcode.com/discuss/post/8217371/google-l4-interview-by-anonymous_user-n071/)

_Crawled: 2026-05-24 · 225 words_


Hi All I gave my last onsite coding interviews. I have given 3 coding rounds and 1 googlyness round . I gave it on 9 April . In last week I reached to recruiter for closure on interview process. Followed after 2 days ( honestly was desperate for result ). Now today on 13 May I got call scheduled for 30 mins Google recruitment process update for 26 May. Honestly my 2 rounds in onsite I felt was not so great while googlyness and first codibg round was good as recruiter told before onsite . 1st coding round did null pointer exception and return type mismatch. Didnt have time for followup . In 2nd onsite codibg interviewer asked question which was really v hard like in all the rounds I wrote 30 lines of code in this I wrote almost 100 line of code. He was continuously saying me you will not get time for followup .Followup was actually harder I wrote some code but didnt have time left .

Now I have got this google recruitment process update call on 26 May ,mail for call on 13 May.Interview was done on 9 April.

I am ok with rejection but I dont want to go to call and get rejected there.

Pls advice all what It could be. Anyone has any experience .

6

6

---

## [Amazon Sde I In Person Interview At Blr 7Drz2](https://leetcode.com/discuss/post/8241486/amazon-sde-i-in-person-interview-at-blr-7drz2/)

_Crawled: 2026-05-24 · 127 words_


Hi everyone,

I have an interview scheduled for SDE-I at Amazon on 21st May and would really appreciate any insights or guidance from those who’ve recently gone through the process.

I have a few specific questions:

1. What level of depth is expected in Low-Level Design (LLD)?
2. What are the most frequently asked topics or questions in LLD and High-Level Design (HLD)?
3. Any tips for DSA preparation specific to Amazon? Do they tend to follow any pattern, or are there commonly repeated questions?
4. Is writing fully runnable code expected during DSA or LLD rounds?
5. Are there any questions related to Gen AI or AI concepts in the interviews?

Any recent experiences, tips, or resources would be really helpful. Thanks in advance!

3

9

---

## [Targeting L5Senior Google Meta Hft Uklon 5Pvr](https://leetcode.com/discuss/post/8252864/targeting-l5senior-google-meta-hft-uklon-5pvr/)

_Crawled: 2026-05-24 · 61 words_


Hi Everyone, I am keen on grinding LC-Hard DSA and advanced System Design for the next 3-6 months and looking for a senior-level partner to stay consistent, run intense mock interviews, and crack the roles we want. I'm a Software Engineer in Glasgow (3.5+ YOE) aiming for the L5 bar—if anyone's up for a disciplined, long-term grind, let's connect!

0

13

---

## [Onsite Feedback Delay](https://leetcode.com/discuss/post/8263531/onsite-feedback-delay-by-anonymous_user-co18/)

_Crawled: 2026-05-24 · 64 words_


Gave Google L4 onsite in the first week of May and haven’t heard back yet. Followed up twice with the recruiter so far, but no update yet.

Just wanted to check if anyone else is in a similar situation — is this kind of delay/no response after follow-ups normal in the current process?

Would appreciate hearing timelines from others who interviewed recently.

0

1

---

## [Google L4 Interview Reject](https://leetcode.com/discuss/post/8265899/google-l4-interview-reject-by-anonymous_-xsc3/)

_Crawled: 2026-05-24 · 289 words_


# Google L4 Interview

Location : Bengaluru

Role : L4

YOE : 2.9 yrs

## Round 1 :

Standard Topo Sort Question very similar to the below problems.

Question 1 : [https://leetcode.com/problems/course-schedule/description/](https://leetcode.com/problems/course-schedule/description/)

Question 2 : [https://leetcode.com/problems/course-schedule-ii/description/](https://leetcode.com/problems/course-schedule-ii/description/)

## Round 2 :

Standard Behavioral questions. The below link helped me a lot. Hope this helps you too.

[https://leetcode.com/discuss/post/5963463/googlyness-frequently-asked-questions-by-55sh/](https://leetcode.com/discuss/post/5963463/googlyness-frequently-asked-questions-by-55sh/)

* * *

The recruiter reached out to me in mid March. My R1 and R2 were scheduled after 1 month. 3 days after my R2, my recruiter reached out to me again and she said the response is +ve and she would like to move ahead with the next rounds.

* * *

## Round 3 \[Onsite\]

A question very similar to designing LFU cache was asked. The only difference was there were changes in key-value eviction property. Keys were numbers. Values were in the format \[ Content : String, Score : INT\]. Once we have accessed a key-value pair, the score was supposed to increase by 1. While evicting I need to follow the standard pattern but I was supposed to evict only those values whose score was even.

## Round 4 \[Onsite\]

I have already explained the question here. Please do checkout this link.

[https://leetcode.com/discuss/post/8218498/google-l4-in-person-interview-by-anonymo-eqbq/](https://leetcode.com/discuss/post/8218498/google-l4-in-person-interview-by-anonymo-eqbq/)

* * *

## Result :

Though I was expecting a positive response, the recruiter told me after considering the feedback from all the rounds, she can't move ahead with my applicaiton. My round 3 went excellent but when I asked her what went wrong in R3 and R4 she said, in R3 I wasn't able to consider all the edge cases and didn't make proper use of Classes.

**Please do upvote this if you think it might help you or someone else.**

14

4

---

## [Google Application Engineer Upcoming Cod Ndk6](https://leetcode.com/discuss/post/8277469/google-application-engineer-upcoming-cod-ndk6/)

_Crawled: 2026-05-24 · 158 words_


Hi everyone,

I have my first two coding rounds scheduled next week for the Application Engineer role at Google.

I’ve been grinding LeetCode and received a basic prep doc from my recruiter, but I know the AE track can differ slightly from the standard SWE track. Has anyone recently gone through the AE coding rounds? I’d love to get some ground-level insights.

Specifically, I’m looking for:

- Difficulty Level: Is it primarily LeetCode Mediums, or should I expect Hards?

- Frequent Topics: I’ve heard rumors of 2D Matrix (DFS/BFS), Strings, and HashMaps being common for AE. Is there anything else I should heavily index on?

- Environment & Expectations: Did you code in a plain text editor, and how much emphasis was placed on writing modular/helper functions vs. sheer algorithmic optimization?


Any recent experiences, specific problem types, or general suggestions for the final week of prep would be incredibly appreciated.

Thanks in advance for the help!

0

4

---

## [Google L3 Bangalore India Interview Expe Dt1H](https://leetcode.com/discuss/post/8268786/google-l3-bangalore-india-interview-expe-dt1h/)

_Crawled: 2026-05-24 · 579 words_


Hi community,

I recently completed 4 interview rounds with \[Google\] — 2 online rounds followed by 2 onsite rounds. I’m still waiting for the final result, so I wanted to share my experience and get your thoughts on my chances.

### Round 1

The questions were based on easy-medium level string manipulation. I was able to solve them, but the interviewer focused more on clean and concise code rather than just optimization.

One mistake from my side was initializing:

```cpp
vector<char> v;
```

without resizing it beforehand. The interviewer asked how this would behave for a large database and hinted toward memory optimization. I understood the concern, but the specific improvement he expected was using `v.resize()`.

Overall, that was the only major thing I lacked in this round.

**My verdict:** Hire

### Round 2 — Googliness

This round went well overall. The discussion was smooth, and I was able to communicate my thoughts clearly.

**My verdict:** Hire / Strong Hire

### Onsite (after 2 weeks)

### Round 3 — Graph Question

The problem involved a list of airports with flight arrival and departure times. I solved it using BFS.

Where I struggled was in representing the graph cleanly. I started overcomplicating things using nested pairs, maps of vectors, etc. The interviewer suggested using a `struct`, which was definitely a cleaner approach. He also suggested using tuples for storing time-related data.

So one weakness I noticed was choosing the right data structure quickly.

Another issue was around visited nodes. I initially argued that visited tracking was unnecessary because the traversal depended on time comparisons, but later the interviewer pointed out a missing case and hinted toward maintaining visited states.

Overall, I was able to explain and code the solution, though I did need a few hints during the discussion.

**My verdict:** Hire / Lean Hire

### Round 4 — Rook Placement Problem

This was the hardest round for me.

Problem statement:

There was an `n x n` chessboard with `n-1` rooks already placed such that no two rooks shared the same row or column. The matrix itself was hidden, and the only API available was:

```cpp
countRook(a, b, c, d)
```

which returned the number of rooks inside a rectangle.

I initially approached it with a backtracking-based solution. However, the interviewer was heavily focused on reducing the number of API calls.

My first solution required around `2 * n * n` API calls. After using memoization, I reduced it to around `2 * n`.

I was able to code this version successfully, but the interviewer seemed more interested in problem-solving ability and optimization thinking rather than just implementation.

I also proposed another approach, but it became overly complex. The interviewer kept hinting toward a better search strategy, which eventually led me toward binary search. However, I reached that idea only after hints and did not have enough time left to fully code it.

I found this problem genuinely difficult because it was not a standard pattern I had seen before. Initially, I approached it more like a queen-placement/backtracking problem.

**My verdict:** Lean Hire / Lean No Hire

* * *

It has now been around 20 days since my onsite interviews. The recruiter mentioned they were waiting for feedback from one panelist, but for the last 4–5 days I haven’t received any response to my follow-up emails.

According to you, what would my overall verdict likely be, and what do you think my chances of selection are?

Thanks

8

14

---

## [Google L4 Banglore](https://leetcode.com/discuss/post/8276966/google-l4-banglore-by-anonymous_user-97gh/)

_Crawled: 2026-05-24 · 269 words_


Recently interviewed with Google for an L4 role (4 YOE). Sharing my experience and would love to hear thoughts from people who’ve gone through similar rounds recently.

### Online Rounds

**Round 1 (DSA)**

Given:

- Movies with ratings
- Similarity graph between movies

Task:

Return the top K movies similar to a given movie.

Follow-up:

Optimize the solution to achieve close to **O(log K)** time complexity and **O(K)** space complexity.

* * *

**Round 2 — Googliness / Behavioural**

Mostly standard behavioural questions around collaboration, conflict resolution, ownership, etc.

* * *

### Onsite Rounds

**Round 3 (Design + Coding)**

Given APIs:

- `insertAd(string content, int score)`
- `getAd()`

Requirements:

- `getAd()` should always return the highest scored ad
- After returning an ad, decrease its score
- Consecutive same ads should not appear

Follow-up:

Introduce a cooldown/gap before the same ad can appear again while keeping operations close to **O(1)**.

I was able to code the follow-up as well.

* * *

**Round 4 (Graphs/Grid)**

Find all lakes in a grid given one land cell.

Initial version was straightforward (water surrounded by land), but interviewer added a twist:

- What if there is land inside the lake?

I explained the approach verbally, but due to time constraints interviewer didn’t ask me to code it.

* * *

My verdicts according to me:

1st: SH

2nd: H/SH

3rd: SH

4th: H/LH

With 4 years of experience, what do you think are the chances for L4 at Google?

Would really appreciate insights from people who’ve recently gone through the process.

Final Verdict : Positive (Moving to team match)

7

10

---

## [Google Application Engineer Upcoming Cod 99Aa](https://leetcode.com/discuss/post/8286412/google-application-engineer-upcoming-cod-99aa/)

_Crawled: 2026-05-24 · 163 words_


Hi everyone,

I have my first two coding rounds scheduled next week for the Application Engineer role at Google.

I’ve been grinding LeetCode and received a basic prep doc from my recruiter, but I know the AE track can differ slightly from the standard SWE track. Has anyone recently gone through the AE coding rounds? I’d love to get some ground-level insights.

Specifically, I’m looking for:

Difficulty Level: Is it primarily LeetCode Mediums, or should I expect Hards?

Frequent Topics: I’ve heard rumors of 2D Matrix (DFS/BFS), Strings, and HashMaps being common for AE. Is there anything else I should heavily index on?

Environment & Expectations: Did you code in a plain text editor, and how much emphasis was placed on writing modular/helper functions vs. sheer algorithmic optimization?

Any recent experiences, specific problem types, or general suggestions for the final week of prep would be incredibly appreciated. Prep Doc is also attached with this.

Thanks in advance for the help!

![sthsfn.jpeg](https://assets.leetcode.com/users/images/ed2cbaf9-c12b-47d2-9659-575baec9bea4_1779453244.419293.jpeg)

0

0

---

## [Onsite feedback delay](https://leetcode.com/discuss/post/8285817/onsite-feedback-delay-by-anonymous_user-tfw4/)

_Crawled: 2026-05-24 · 48 words_


Hi all,

Those who attended onsite interviews in May first week, did you get the feedback?

Its getting delayed for me without acknowledgement, I'm getting a bad feeling on this,

any info if i can still wait or can check with someone else like a mailer?

2

1

---

## [Google \| Amazon \| SDE-2 \| Bangalore](https://leetcode.com/discuss/post/8287855/google-amazon-sde-2-bangalore-by-anonymo-8qew/)

_Crawled: 2026-05-24 · 164 words_


Recently cleared my Google interviews (got the positive feedback 2 days back 🎉).

Current situation:

- Serving notice period in my current company
- Already have an Amazon SDE-2 offer
- Joining Amazon in ~8 days

But honestly, Google is my first preference and I would strongly prefer joining Google directly if possible.

I know the next step is team matching, and I’ve heard timelines can vary a lot. Since I’m on a tight timeline before joining Amazon, I wanted advice from people who’ve been in a similar situation.

What can I do to speed up the team matching process?

- Should I actively reach out to recruiters/hiring managers?
- Is there a way to improve visibility for matching?
- Does joining another company impact matching urgency?
- Any tips that genuinely helped you get matched faster?

Would really appreciate any advice or experiences from people who went through Google HC/team match recently.

Thanks!

Interview Experience

Google - [https://leetcode.com/discuss/post/8276966/google-l4-banglore-by-anonymous\_user-97gh/](https://leetcode.com/discuss/post/8276966/google-l4-banglore-by-anonymous_user-97gh/)

Amazon - [https://leetcode.com/discuss/post/7754949/amazon-l5-bengaluru-retail-team-by-anony-kb92/](https://leetcode.com/discuss/post/7754949/amazon-l5-bengaluru-retail-team-by-anony-kb92/)

3

3

---

## [Node(1,n\\
\\
2\\
\\
520\\
\\
2](https://leetcode.com/discuss/post/7873505/reverser-ll-nodes-with-verifying-hash-va-wng3/)

_Crawled: 2026-05-24 · 155 words_


reverser LL nodes with verifying hashvalues

Given LL => \[1,3,6,8,0\]. => \[0,8,6,3,1\] espected output

class Node:

def **init**(self,val,next=None):

self.val=val

self.next=None

NEWNODE -> NODE \[VAL\] -> NULL

HASH -> 0

HASH - \[HASH(NXTNODE VAL) + VAL\]

\[Node(1,next=> 3, hash=>(18)),\
\
Node(3,next=>6,Hash(17)\
\
Node(6,Next=>8,hash(14),\
\
Node(8,next=>0,hash(8)\
\
original Node(0,None,Hash(0))\
\
\[1,3,6,8,0\]. => head => \[0,8,6,3,1\] output\
\
\[18,17,15,8,0\] reversal => hashvalue=>\[0,8,14,17,18\]\
\
1 => 18 => 18-1>=0 => prefix=17\
\
3=> 17-3 =>14 >=0 \[prefix=14\]\
\
6=>\
\
node x ->{\
\
hash(x) == val + hash(next)\
\
pointer to the head node\
\
}\
\
\[0,8,6,3,1\]\
\
\[None <-1 \]\
\
prev cur=head,\
\
None \[Node(1,next=> 3),nxt\
\
cur.next Node(3,next=>6)\
\
<\-\-\- Node(6,Next=>8),\
\
Node(8,next=>0)\
\
Node(0,Next=> Null). 0 prefix= 0\
\
head\
\
reverse logic\
\
// prev,nxt,cur => None,None,head\
\
// while cur:\
\
// nxt=cur.next\
\
// cur.next=prev\
\
// prev=cur\
\
// cur=nxt\
\
// return prev\
\
2\
\
2\
\

---
