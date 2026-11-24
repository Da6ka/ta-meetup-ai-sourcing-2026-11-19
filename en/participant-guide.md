# Search by job title and company

[Download the two-sided A4 handout](handout.pdf)

### Sample brief (Lead Data Engineer)

- **Responsibilities.** Own the architecture on 2-3 client projects, explain the data model to the client, and launch the warehouse.
- **Where to look.** Data consulting. Start with Future Mind, then Datatonic. Look for Senior Data Engineers, Lead Data Engineers and Data Leads.
- **Required experience.** 5+ years. SQL, Python, BigQuery, and Airflow or equivalent. AI coding tools on a real project and English at B2 or above. A senior engineer qualifies if they made architecture decisions.
- **What to check.** Look for the engineer's role on the project. In conversation, ask about their decision, client work, use of AI and compensation expectations.
- **Terms.** Full-time, remote, B2B. Up to EUR 4,000 per month before personal taxes.
- **Questions for the hiring manager.** Why is the role open? When should the hire start? Which regions and companies should we exclude?

### Search example (Future Mind)

The team used BigQuery and Cloud Composer on a client project. The example budget was within the published mid-level range at the time of the meetup. Check lead compensation separately. Keep Datatonic as a backup.

On free LinkedIn, search for Data Engineer, select People, open All filters and set Current company to Future Mind. Try these queries one at a time:

```text
BigQuery AND ("data modeling" OR "data modelling")
BigQuery AND (migration OR "data warehouse")
```

In Google X-ray, test the same two ideas: data model selection and warehouse migration.

```text
site:linkedin.com/in "Future Mind" BigQuery ("data modeling" OR "data modelling")
site:linkedin.com/in "Future Mind" BigQuery (migration OR "data warehouse")
```

In the meetup example, Future Mind's website confirmed a Data Lead role. Skip the BigQuery mention in someone else's post. What warehouse decision did the person make themselves?

### Search example (Product Engineer)

Look for an engineer who took onboarding through launch and measured the outcome. Start with B2B SaaS teams that build their own onboarding.

Try these queries one at a time in LinkedIn's regular search bar, then select People.

```text
"Product Engineer" AND onboarding
"Full Stack Engineer" AND activation
```

Look for the person's own contribution in the profile. In conversation, ask what changed after launch.

# My first sourcing skill

Use a role you're working on or recently filled. You'll use Codex to broaden a narrow query and save your checks for future searches.

1. **Pick one criterion from your brief.** Open the job request or your hiring manager notes. Write down the title, one responsibility and the relevant experience. Add your search platform and usual query. If you need a starting query, combine the title with one phrase describing the experience.
2. **Collect three profile excerpts.** Use a shortlist, earlier search results or public resumes. Copy the headline and one line of experience. A uses your search terms. B describes the same experience differently and gets missed. C uses similar terms for a different task. Remove names and contacts. Set C aside.
3. **Ask Codex to broaden the query.** Open an empty folder as a Codex project. Send: "I'm sourcing [role] on [platform]. They'll own [task]. They need [experience]. My query is [query]. A: [excerpt]. B: [excerpt]. Change only the experience clause to find both. Show the query and the exact matches in A and B before and after."
4. **Test the query on profile C.** Send: "C: [excerpt]. This person did [task], and we need [required task]. Would your query find C? Show the matching words. If C matches, refine the query and check A, B and C again." Verify the quotes yourself. A and B should match. C should drop out.
5. **Create a skill through an interview.** In the same chat, send: "$skill-creator, use our A, B and C exercise to interview me. Ask one question at a time. Find out when I need search help, what inputs I provide, how I verify matches and which decision I make myself. Show me the rules you inferred. After my edits, create a skill named my-sourcing-search in this project and show me how to run it." Answer with examples from your role. When the rules are right, reply: "These rules look right. Create the skill."
6. **Try the skill on a fresh example.** Start a new chat in the same folder. Pick another profile and decide whether the query should find it. Send "Use $my-sourcing-search" with the inputs from step 3 and the new example. Compare the result with your prediction. If they differ, find out why and update the rule in the skill file.

## Hiring brief template

Copy the table for your role.

| Question for the hiring manager | Your answer |
|---|---|
| What's the urgent problem? What result do you expect from the lead, and how will you measure it? | |
| Who have you hired for similar roles? What experience would make you invite someone to interview? | |
| Which terms are mandatory? Include location, working hours, budget and contract type. | |
| Which teams solve this problem? Why search there? Which companies should we exclude? | |
| How might someone describe the work on their profile? Which other job titles should we try? | |
| What can we verify from public sources? What do we need to ask the person directly? | |

### Before the intake call

[Hiring brief skill](https://github.com/michaljuhas/recruiting-skills/blob/main/.claude/skills/job-requirement-analysis/SKILL.md)

"I'm preparing for a Lead Data Engineer intake. Based on the description below, write five questions for the hiring manager. What should the hire solve in the first three months? Which decisions will the lead own? Where should I look for people with that experience? Skip questions the brief already answers."

## Codex demo

Send the first prompt in a new chat. Once Codex replies, send the second prompt in the same chat.

### Slide 19. Broaden the query for A and B

```text
I'm sourcing a Lead Data Engineer for a consulting team that builds warehouses for international clients. A senior engineer who personally designed a warehouse for a client could fit. We're testing one criterion: making an architecture decision. Original query: "Senior Data Engineer" AND "designed a BigQuery warehouse".

A. Senior Data Engineer. Designed a BigQuery warehouse for a client.
B. Senior Data Engineer. Chose the BigQuery data model and defended it with the client.

Keep the job title and broaden the experience clause. Give me one Boolean query. Quote the words the query would match in A and B. What do we still need to clarify?
```

### Slide 20. Test the query on C

```text
C. Senior Data Engineer. Built dashboards on top of an existing BigQuery warehouse.

Test the new query on C. This profile shows work with an existing warehouse. If C matches, refine the experience clause and test all three profiles again. For each profile, quote the matching phrase or explain why there is no match.
```

A designed the warehouse. B chose the data model. C worked with an existing warehouse. Verify experience with AI coding tools separately. Use the excerpts to check phrase matches in the exercise. Test live search results separately.

## References

[Market map (PDF)](talent-intel-lead-data-engineer.pdf) · [Sample job description](lead-data-engineer.md) · [Sasha's sample resume](sasha.md)

**Map the market.** Give Talent Intel a role, an industry and a region. Ask, "Which teams solve similar problems? Show companies, project examples and published pay ranges with links." Verify the work each team did and the seniority behind each range.

**Start a conversation.** "Hi Sasha, you chose the data model during a BigQuery migration and defended the decision with the client. Our lead owns the architecture for 2-3 client projects. The B2B budget is up to EUR 4,000 per month before personal taxes. Would you be open to discussing the role?"

[Metaview Sourcing](https://www.metaview.ai/sourcing) · [Juicebox](https://juicebox.ai/)

**Check where to search.** Record the team name, a problem it solves that resembles yours, and a job ad or post where the team describes the work.

**Compare two queries.** Keep the title and change the experience clause. Open a profile that appeared after the change. Which line would make you reach out? What do you still need to check? [Query examples from Sourcing Sabra](https://github.com/gehtalexey/sourcing-sabra/blob/main/skills/talent-sourcer/SKILL.md)

Search syntax references include [LinkedIn Boolean search](https://www.linkedin.com/help/linkedin/answer/a524335) and [Google site search](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site).

[Talent Intel skill for Claude Code](https://github.com/SriniGundelli/talent-intel) · [Sample market map](https://github.com/SriniGundelli/talent-intel/blob/main/examples/sample-report.md)
