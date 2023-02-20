---
layout: page
title: Home
id: home
permalink: /
---

# 你好，陌生人 👀

<p style="padding: 3em 1em; background: #f5f7ff; border-radius: 4px;">
  我的收获都来自于这些清单，希望你从这些 <span style="font-weight: bold">[[阅读目录]]</span> 也有所收获!
</p>

- 💡[[卡片笔记与内化知识]]
- 🌴[[历史、地理知识收集]]

<strong>Recently updated notes</strong>

<ul>
  {% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
  {% for note in recent_notes | limit: 5 %}
    <li>
      {{ note.last_modified_at | date: "%Y-%m-%d" }} — <a class="internal-link" href="{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>

<style>
  .wrapper {
    max-width: 46em;
  }
</style>

