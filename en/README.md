# How I teach AI to source candidates

Daria Ivanova's workshop materials for [SPb IT Recruiter Meetup](https://proit-fest.timepad.ru/event/4273243/), November 19, 2026. Use a Lead Data Engineer brief to build LinkedIn and Google searches and test your query on sample profiles in Codex. Save those checks as a sourcing skill. On your next search, give Codex your new brief and ask it to apply the same rules to your query.

**[Try the exercise on your own role](participant-guide.md#my-first-sourcing-skill)** · [Claude Code adaptation](#adapting-the-exercise-to-claude-code) · [Русская версия](../README.md#русский)

1. Start with the [workshop slides (PDF)](slides.pdf) and open the [two-sided A4 handout (PDF)](handout.pdf).
2. Open the [sample job description](lead-data-engineer.md), the [Talent Intel market map (PDF)](talent-intel-lead-data-engineer.pdf) and [Sasha's sample resume](sasha.md).
3. Copy the [Codex demo prompts](participant-guide.md#codex-demo).

The [participant guide](participant-guide.md) includes a hiring brief template, example searches and source links. Pay figures in the [market map](talent-intel-lead-data-engineer.md) reflect the research available on the meetup date.

## Adapting the exercise to Claude Code

Work through the first four steps of the [exercise](participant-guide.md#my-first-sourcing-skill) in Claude Code. Pick one requirement from your brief and use three anonymized profiles. Two describe the experience you want in different words. The third uses similar words for different work. Check the phrases Claude cites against the profiles.

In step 5, ask Claude to interview you about your checks, show you the rules it inferred, and save the rules after your edits to `.claude/skills/my-sourcing-search/SKILL.md` in your project. Add `name: my-sourcing-search` and a `description` in the YAML frontmatter. Start a fresh Claude Code session in the same project and invoke `/my-sourcing-search` with your brief, query and a fourth anonymized profile. Decide in advance whether the query should find that profile, then compare your prediction with the result.

[Claude Code skills documentation](https://code.claude.com/docs/en/skills)

## For presenters

The [presenter guide](presenter-guide.md) includes the running order and links used during the demo. See the [changelog](CHANGELOG.md) for earlier updates.

The [web version of the slides](https://ta-meetup-ai-sourcing.vercel.app/) is in Russian.
