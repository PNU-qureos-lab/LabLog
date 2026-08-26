#!/usr/bin/env python3
"""Generate LabLog agro_brdf.html (UTF-8, no BOM, no null bytes)."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "agro_brdf.html"


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Agro BRDF - Project Page</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg0: #0f1c24;
      --bg1: #162a35;
      --bg2: #1d3644;
      --panel: rgba(245, 248, 250, 0.96);
      --ink: #13232c;
      --muted: #5b6f7a;
      --line: #d5dee4;
      --accent: #1f7a6c;
      --accent-soft: #d7efe9;
      --head: #e8eef2;
      --shadow: 0 10px 28px rgba(8, 20, 28, 0.18);
      --radius: 12px;
      --font-ui: "IBM Plex Sans", sans-serif;
      --font-display: "Source Serif 4", Georgia, serif;
    }

    * { box-sizing: border-box; }

    html, body {
      margin: 0;
      min-height: 100%;
      font-family: var(--font-ui);
      color: var(--ink);
      background:
        radial-gradient(1100px 560px at 8% -8%, #2a5d55 0%, transparent 55%),
        radial-gradient(900px 480px at 100% 0%, #3a4f6b 0%, transparent 50%),
        linear-gradient(160deg, var(--bg0), var(--bg1) 45%, var(--bg2));
    }

    body { padding: 18px; }

    .app {
      max-width: 1480px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .banner {
      display: none;
      padding: 12px 14px;
      border-radius: var(--radius);
      background: #fff7ed;
      border: 1px solid #fdba74;
      color: #9a3412;
      font-size: 0.86rem;
      line-height: 1.45;
      box-shadow: var(--shadow);
    }
    .banner.show { display: block; }
    .banner code {
      font-family: ui-monospace, Consolas, monospace;
      font-size: 0.82em;
    }

    .topbar {
      display: flex;
      flex-wrap: wrap;
      align-items: flex-end;
      justify-content: space-between;
      gap: 12px;
      padding: 18px 20px;
      border-radius: var(--radius);
      background: var(--panel);
      box-shadow: var(--shadow);
      border: 1px solid rgba(22, 42, 53, 0.1);
    }

    .brand h1 {
      margin: 0;
      font-family: var(--font-display);
      font-size: 1.55rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #0f2a30;
    }

    .brand p {
      margin: 4px 0 0;
      color: var(--muted);
      font-size: 0.86rem;
    }

    .back-link {
      display: inline-block;
      margin-bottom: 6px;
      color: var(--accent);
      font-size: 0.82rem;
      font-weight: 600;
      text-decoration: none;
    }
    .back-link:hover { text-decoration: underline; }

    .top-actions {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
    }

    .sync-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 999px;
      border: 1px solid var(--line);
      background: #fff;
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--muted);
    }
    .sync-pill .dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #94a3b8;
    }
    .sync-pill.live .dot { background: #16a34a; }
    .sync-pill.saving .dot { background: #ca8a04; }
    .sync-pill.error .dot { background: #dc2626; }
    .sync-pill.local .dot { background: #ea580c; }

    .panel {
      background: var(--panel);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid rgba(22, 42, 53, 0.1);
      padding: 16px 18px 18px;
    }

    .panel-head {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 12px;
    }

    .panel-head h2 {
      margin: 0;
      font-family: var(--font-display);
      font-size: 1.12rem;
      font-weight: 700;
      color: #123038;
    }

    .panel-head .meta {
      font-size: 0.78rem;
      color: var(--muted);
    }

    .row-actions {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }

    button {
      font-family: var(--font-ui);
      font-size: 0.78rem;
      font-weight: 600;
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      border-radius: 8px;
      padding: 6px 10px;
      cursor: pointer;
    }
    button:hover { background: var(--accent-soft); border-color: #9bc4bb; }
    button.primary {
      background: var(--accent);
      border-color: var(--accent);
      color: #fff;
    }
    button.primary:hover { filter: brightness(1.05); }
    button.danger {
      color: #b42318;
      border-color: #f0c7c3;
      background: #fff5f4;
    }

    .meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 12px;
    }

    .field-label {
      display: block;
      margin-bottom: 5px;
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--muted);
    }

    .field-input {
      width: 100%;
      min-height: 40px;
      padding: 8px 10px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fff;
      font-family: var(--font-ui);
      font-size: 0.92rem;
      color: var(--ink);
      outline: none;
    }
    .field-input:focus {
      border-color: #9bc4bb;
      box-shadow: 0 0 0 3px rgba(31, 122, 108, 0.12);
    }

    .rich-box {
      min-height: 72px;
      padding: 10px 12px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fff;
      line-height: 1.5;
      font-size: 0.9rem;
      outline: none;
    }
    .rich-box:focus {
      border-color: #9bc4bb;
      box-shadow: 0 0 0 3px rgba(31, 122, 108, 0.12);
    }

    .final-block { margin-bottom: 14px; }

    .goals-table {
      width: 100%;
      border-collapse: collapse;
    }
    .goals-table th,
    .goals-table td {
      border: 1px solid var(--line);
      padding: 8px;
      vertical-align: top;
      background: #fff;
    }
    .goals-table th {
      background: #edf3f6;
      font-size: 0.76rem;
      font-weight: 700;
      color: #35505a;
      text-align: left;
    }
    .goal-idx {
      width: 56px;
      text-align: center;
      font-weight: 700;
      color: var(--accent);
      background: #f4faf8 !important;
    }
    .goal-text {
      min-height: 42px;
      outline: none;
    }
    .goal-progress {
      width: 110px;
    }
    .goal-progress input {
      width: 100%;
      border: 1px solid transparent;
      background: transparent;
      font-family: var(--font-ui);
      font-size: 0.88rem;
      padding: 4px 6px;
      outline: none;
    }
    .goal-progress input:focus {
      border-color: #9bc4bb;
      border-radius: 6px;
      background: #fff;
    }
    .goal-del {
      width: 70px;
      text-align: center;
    }

    .graph-layout {
      display: grid;
      grid-template-columns: 1fr 118px;
      gap: 10px;
      min-height: 420px;
    }

    .graph-stage {
      position: relative;
      min-height: 420px;
      border: 1px solid var(--line);
      border-radius: 10px;
      background:
        linear-gradient(90deg, rgba(31, 122, 108, 0.05) 0, rgba(31, 122, 108, 0.05) 220px, transparent 220px),
        repeating-linear-gradient(0deg, transparent, transparent 23px, rgba(213, 222, 228, 0.55) 24px),
        repeating-linear-gradient(90deg, transparent, transparent 23px, rgba(213, 222, 228, 0.55) 24px),
        #f7fafb;
      overflow: hidden;
      user-select: none;
    }

    .graph-svg {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
    }
    .graph-svg .edge-group {
      pointer-events: none;
    }
    .graph-svg .edge-group .edge-hit {
      pointer-events: stroke;
      cursor: pointer;
    }
    .graph-svg .edge-line {
      fill: none;
      stroke: #3d6573;
      stroke-width: 2;
      pointer-events: none;
    }
    .graph-svg .edge-line.selected {
      stroke: #b42318;
      stroke-width: 2.6;
    }
    .graph-svg .edge-arrow {
      fill: none;
      stroke: #3d6573;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
      pointer-events: none;
    }
    .graph-svg .edge-arrow.selected {
      stroke: #b42318;
      stroke-width: 2.6;
    }
    .graph-svg .edge-temp {
      fill: none;
      stroke: #1f7a6c;
      stroke-width: 2;
      stroke-dasharray: 5 4;
      pointer-events: none;
    }
    .graph-svg .edge-temp-arrow {
      fill: none;
      stroke: #1f7a6c;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
      pointer-events: none;
    }
    .graph-svg .edge-x-g {
      opacity: 0;
      pointer-events: none;
    }
    .graph-svg .edge-group:hover .edge-x-g {
      opacity: 1;
      pointer-events: all;
    }
    .edge-x {
      pointer-events: all;
      cursor: pointer;
      fill: #fff;
      stroke: #b42318;
      stroke-width: 1.5;
    }
    .edge-x-mark {
      pointer-events: none;
      stroke: #b42318;
      stroke-width: 1.6;
    }

    .graph-nodes {
      position: absolute;
      inset: 0;
      z-index: 2;
    }

    .gnode {
      position: absolute;
      width: 190px;
      min-height: 54px;
      padding: 8px 28px 10px 12px;
      border-radius: 10px;
      border: 1px solid #b9cdd4;
      background: #fff;
      box-shadow: 0 4px 12px rgba(15, 28, 36, 0.08);
      cursor: grab;
      z-index: 3;
    }
    .gnode.dragging { cursor: grabbing; z-index: 5; opacity: 0.95; }
    .gnode.resizing { z-index: 5; }
    .gnode.goal {
      background: linear-gradient(180deg, #e8f6f2, #fff);
      border-color: #8ebfb4;
    }
    .gnode.task {
      background: #fff;
      border-color: #c2d0d7;
    }
    .gnode .node-title {
      min-height: 1.35em;
      padding-right: 2px;
      font-size: 0.82rem;
      line-height: 1.35;
      outline: none;
      word-break: break-word;
      cursor: text;
    }
    .gnode .node-title a {
      color: #0b5fff;
      text-decoration: underline;
      cursor: pointer;
    }
    .gnode .node-badge {
      display: inline-block;
      margin-bottom: 4px;
      font-size: 0.68rem;
      font-weight: 700;
      color: var(--accent);
      letter-spacing: 0.02em;
    }
    .gnode .node-del {
      position: absolute;
      top: 4px;
      right: 4px;
      width: 22px;
      height: 22px;
      padding: 0;
      border-radius: 6px;
      font-size: 0.72rem;
      line-height: 1;
      opacity: 0;
      pointer-events: none;
      z-index: 5;
    }
    .gnode:hover .node-del,
    .gnode:focus-within .node-del {
      opacity: 1;
      pointer-events: auto;
    }
    .node-resize {
      position: absolute;
      right: 1px;
      bottom: 1px;
      width: 12px;
      height: 12px;
      cursor: se-resize;
      z-index: 6;
      background:
        linear-gradient(135deg, transparent 0 45%, #7a93a0 45% 55%, transparent 55% 70%, #7a93a0 70% 80%, transparent 80%);
    }
    .port {
      position: absolute;
      top: 50%;
      width: 12px;
      height: 12px;
      margin-top: -6px;
      border-radius: 50%;
      border: 2px solid #fff;
      background: var(--accent);
      box-shadow: 0 0 0 1px #7aa89f;
      cursor: crosshair;
      z-index: 4;
    }
    .port.out { right: -7px; }
    .port.in { left: -7px; background: #3d6573; box-shadow: 0 0 0 1px #7a93a0; }

    .title-ctx-menu {
      position: fixed;
      z-index: 9999;
      min-width: 120px;
      padding: 4px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fff;
      box-shadow: var(--shadow);
    }
    .title-ctx-menu button {
      display: block;
      width: 100%;
      text-align: left;
      border: 0;
      background: transparent;
      padding: 8px 10px;
      border-radius: 6px;
      cursor: pointer;
      font: inherit;
      font-size: 0.82rem;
      color: var(--ink);
    }
    .title-ctx-menu button:hover {
      background: var(--accent-soft);
    }

    .graph-toolbar {
      display: flex;
      flex-direction: column;
      gap: 8px;
      padding: 10px;
      border: 1px solid var(--line);
      border-radius: 10px;
      background: #f4f8fa;
    }
    .graph-toolbar .hint {
      font-size: 0.72rem;
      color: var(--muted);
      line-height: 1.4;
    }

    @media (max-width: 860px) {
      .graph-layout {
        grid-template-columns: 1fr;
      }
      .graph-toolbar {
        flex-direction: row;
        align-items: center;
        flex-wrap: wrap;
      }
    }
  </style>
</head>
<body>
  <div class="app">
    <div id="setup-banner" class="banner" role="status"></div>

    <div class="topbar">
      <div class="brand">
        <a class="back-link" href="index.html">&larr; Back to Lab Research Plan</a>
        <h1>Agro BRDF</h1>
        <p>Project page with goals and hierarchy graph</p>
      </div>
      <div class="top-actions">
        <div id="sync-pill" class="sync-pill local" title="Sync status">
          <span class="dot" aria-hidden="true"></span>
          <span id="sync-text">Local only</span>
        </div>
      </div>
    </div>

    <section class="panel" id="pane-meta">
      <div class="panel-head">
        <h2>Project header</h2>
        <span class="meta">Pane 1</span>
      </div>
      <div class="meta-grid">
        <div>
          <label class="field-label" for="meta-title">과제명</label>
          <div id="meta-title" class="field-input" contenteditable="true" spellcheck="false"></div>
        </div>
        <div>
          <label class="field-label" for="meta-period">연구개발기간</label>
          <div id="meta-period" class="field-input" contenteditable="true" spellcheck="false"></div>
        </div>
        <div>
          <label class="field-label" for="meta-year-period">당해년도 개발기간</label>
          <div id="meta-year-period" class="field-input" contenteditable="true" spellcheck="false"></div>
        </div>
      </div>
    </section>

    <section class="panel" id="pane-goals">
      <div class="panel-head">
        <h2>당해년도 과업목표</h2>
        <div class="row-actions">
          <button type="button" id="btn-add-goal" class="primary">Add goal</button>
          <button type="button" id="btn-del-goal" class="danger">Delete goal row</button>
        </div>
      </div>

      <div class="final-block">
        <label class="field-label" for="final-goal">최종목표</label>
        <div id="final-goal" class="rich-box" contenteditable="true" spellcheck="false"></div>
      </div>

      <table class="goals-table" id="tbl-goals">
        <thead>
          <tr>
            <th style="width:56px">#</th>
            <th>Detail goal</th>
            <th style="width:110px">진행율</th>
            <th style="width:70px"></th>
          </tr>
        </thead>
        <tbody></tbody>
      </table>
    </section>

    <section class="panel" id="pane-graph">
      <div class="panel-head">
        <h2>Hierarchy / structure</h2>
        <span class="meta">Pane 3 - drag nodes, connect ports</span>
      </div>
      <div class="graph-layout">
        <div class="graph-stage" id="graph-stage">
          <svg class="graph-svg" id="graph-svg" xmlns="http://www.w3.org/2000/svg"></svg>
          <div class="graph-nodes" id="graph-nodes"></div>
        </div>
        <aside class="graph-toolbar">
          <button type="button" id="btn-add-item" class="primary">Add item</button>
          <div class="hint">Drag ports to link (arrows at input). Resize via SE corner. Hover edge for X to delete (or Del). Task title: select text, right-click Add link.</div>
        </aside>
      </div>
    </section>
  </div>

  <script src="https://www.gstatic.com/firebasejs/10.14.1/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.14.1/firebase-database-compat.js"></script>
  <script src="firebase-config.js"></script>
  <script>
    (function () {
      var LOCAL_KEY = "lab_project_agro_brdf_v1";
      var DB_PATH = "labManagement/projectPages/agro_brdf";
      var SAVE_DEBOUNCE_MS = 400;
      var NODE_W = 190;
      var NODE_H_MIN = 54;
      var GOAL_LEFT = 24;
      var GOAL_TOP0 = 28;
      var GOAL_GAP = 78;
      var PORT_HIT_PX = 18;
      var ARROW_LEN = 15;
      var ARROW_WING_DEG = 25;

      var state = null;
      var dbRef = null;
      var cloudEnabled = false;
      var applyingRemote = false;
      var saveTimer = null;
      var lastWrittenJson = "";
      var selectedEdgeId = null;
      var dragNode = null;
      var dragOffset = { x: 0, y: 0 };
      var resizeDrag = null;
      var linkDrag = null;
      var suppressClick = false;
      var titleCtxMenu = null;

      function uid(prefix) {
        return (prefix || "id") + "_" + Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);
      }

      function cloneData(obj) {
        return JSON.parse(JSON.stringify(obj || {}));
      }

      function asArray(v) {
        return Array.isArray(v) ? v : [];
      }

      function makeSeed() {
        var goals = [];
        var i;
        for (i = 0; i < 4; i++) {
          goals.push({ id: "goal_" + (i + 1), text: "", progress: "" });
        }
        return {
          meta: {
            title: "농림 BRDF",
            period: "",
            yearPeriod: ""
          },
          finalGoal: "",
          goals: goals,
          graphNodes: [],
          edges: []
        };
      }

      function isSafeHref(href) {
        var h = (href != null ? String(href) : "").trim();
        if (!h) return false;
        var lower = h.toLowerCase();
        if (lower.indexOf("javascript:") === 0) return false;
        if (lower.indexOf("data:") === 0) return false;
        if (lower.indexOf("vbscript:") === 0) return false;
        if (/^https?:\/\//i.test(h) || h.charAt(0) === "/" || h.charAt(0) === "#" || h.charAt(0) === "?" || h.indexOf("://") < 0) {
          return true;
        }
        return false;
      }

      function sanitizeHtml(html) {
        var s = html != null ? String(html) : "";
        var box = document.createElement("div");
        box.innerHTML = s;
        box.querySelectorAll("script,iframe,object,embed,link,meta,style").forEach(function (n) {
          n.remove();
        });
        box.querySelectorAll("*").forEach(function (el) {
          var tag = (el.tagName || "").toLowerCase();
          var attrs = Array.prototype.slice.call(el.attributes || []);
          attrs.forEach(function (attr) {
            var name = attr.name.toLowerCase();
            if (name.indexOf("on") === 0 || name === "srcdoc") {
              el.removeAttribute(attr.name);
              return;
            }
            if (tag === "a") {
              if (name !== "href" && name !== "target" && name !== "rel") {
                el.removeAttribute(attr.name);
              }
            } else if (name === "href" || name === "src") {
              el.removeAttribute(attr.name);
            }
          });
          if (tag === "a") {
            var href = el.getAttribute("href");
            if (!isSafeHref(href)) {
              el.removeAttribute("href");
            } else {
              el.setAttribute("target", "_blank");
              el.setAttribute("rel", "noopener noreferrer");
            }
          }
        });
        return box.innerHTML;
      }

      function setRichHtml(el, value) {
        var s = value != null ? String(value) : "";
        if (/<[a-z][\s\S]*>/i.test(s)) {
          el.innerHTML = sanitizeHtml(s);
        } else {
          el.textContent = s;
        }
      }

      function getRichHtml(el) {
        return sanitizeHtml(el.innerHTML);
      }

      function plainText(html) {
        var box = document.createElement("div");
        box.innerHTML = sanitizeHtml(html || "");
        return (box.textContent || "").replace(/\s+/g, " ").trim();
      }

      function syncGoalNodesOn(obj) {
        var goals = obj.goals || [];
        var keep = {};
        var nodes = asArray(obj.graphNodes);
        var next = [];
        var i;
        for (i = 0; i < goals.length; i++) {
          var g = goals[i];
          var found = null;
          var j;
          for (j = 0; j < nodes.length; j++) {
            if (nodes[j].type === "goal" && nodes[j].id === g.id) {
              found = nodes[j];
              break;
            }
          }
          if (!found) {
            for (j = 0; j < nodes.length; j++) {
              if (nodes[j].type === "goal" && Number(nodes[j].goalIndex) === i && !keep[nodes[j].id]) {
                found = nodes[j];
                break;
              }
            }
          }
          var title = plainText(g.text) || ("[" + (i + 1) + "]");
          if (found) {
            found.id = g.id;
            found.type = "goal";
            found.goalIndex = i;
            found.title = title;
            if (typeof found.x !== "number") found.x = GOAL_LEFT;
            if (typeof found.y !== "number") found.y = GOAL_TOP0 + i * GOAL_GAP;
            next.push(found);
            keep[found.id] = true;
          } else {
            next.push({
              id: g.id,
              type: "goal",
              goalIndex: i,
              title: title,
              x: GOAL_LEFT,
              y: GOAL_TOP0 + i * GOAL_GAP,
              w: NODE_W,
              h: null
            });
            keep[g.id] = true;
          }
        }
        for (i = 0; i < nodes.length; i++) {
          if (nodes[i].type !== "goal") next.push(nodes[i]);
        }
        obj.graphNodes = next;
        var valid = {};
        next.forEach(function (n) { valid[n.id] = true; });
        obj.edges = asArray(obj.edges).filter(function (e) {
          return e && valid[e.from] && valid[e.to] && e.from !== e.to;
        });
      }

      function syncGoalNodes() {
        if (!state) return;
        syncGoalNodesOn(state);
      }

      function normalizePayload(data) {
        data = data || {};
        var meta = data.meta && typeof data.meta === "object" ? data.meta : {};
        var out = {
          meta: {
            title: meta.title != null ? String(meta.title) : "농림 BRDF",
            period: meta.period != null ? String(meta.period) : "",
            yearPeriod: meta.yearPeriod != null ? String(meta.yearPeriod) : ""
          },
          finalGoal: data.finalGoal != null ? String(data.finalGoal) : "",
          goals: asArray(data.goals).map(function (g, idx) {
            g = g || {};
            return {
              id: g.id != null ? String(g.id) : ("goal_" + (idx + 1)),
              text: g.text != null ? String(g.text) : "",
              progress: g.progress != null ? String(g.progress) : ""
            };
          }),
          graphNodes: asArray(data.graphNodes).map(function (n) {
            n = n || {};
            var w = typeof n.w === "number" && n.w > 0 ? n.w : NODE_W;
            var h = typeof n.h === "number" && n.h >= NODE_H_MIN ? n.h : null;
            return {
              id: n.id != null ? String(n.id) : uid("node"),
              type: n.type === "goal" ? "goal" : "task",
              goalIndex: n.goalIndex != null ? Number(n.goalIndex) : null,
              title: n.title != null ? String(n.title) : "",
              x: typeof n.x === "number" ? n.x : 0,
              y: typeof n.y === "number" ? n.y : 0,
              w: w,
              h: h
            };
          }),
          edges: asArray(data.edges).map(function (e) {
            e = e || {};
            return {
              id: e.id != null ? String(e.id) : uid("edge"),
              from: e.from != null ? String(e.from) : "",
              to: e.to != null ? String(e.to) : ""
            };
          }).filter(function (e) { return e.from && e.to && e.from !== e.to; })
        };
        if (!out.goals.length) {
          out.goals = makeSeed().goals;
        }
        syncGoalNodesOn(out);
        return out;
      }

      function payloadFromState() {
        syncGoalNodes();
        var p = normalizePayload(state);
        state = cloneData(p);
        p.updatedAt = Date.now();
        return p;
      }

      function coreJson(payload) {
        var n = normalizePayload(payload);
        return JSON.stringify({
          meta: n.meta,
          finalGoal: n.finalGoal,
          goals: n.goals,
          graphNodes: n.graphNodes,
          edges: n.edges
        });
      }

      function setSync(mode, text) {
        var pill = document.getElementById("sync-pill");
        var label = document.getElementById("sync-text");
        pill.className = "sync-pill " + mode;
        label.textContent = text;
      }

      function showSetupBanner(msg) {
        var el = document.getElementById("setup-banner");
        el.innerHTML = msg;
        el.classList.add("show");
      }

      function readLocal() {
        try {
          var raw = localStorage.getItem(LOCAL_KEY);
          if (!raw) return null;
          return normalizePayload(JSON.parse(raw));
        } catch (e) {
          return null;
        }
      }

      function writeLocal(payload) {
        try {
          localStorage.setItem(LOCAL_KEY, JSON.stringify(normalizePayload(payload)));
        } catch (e) {}
      }

      function isConfigReady(cfg) {
        if (!cfg || typeof cfg !== "object") return false;
        return !!(cfg.apiKey && cfg.databaseURL && cfg.projectId);
      }

      function hasContent(payload) {
        var n = normalizePayload(payload);
        if ((n.meta.title || "").trim() && n.meta.title !== "농림 BRDF") return true;
        if ((n.meta.period || "").trim() || (n.meta.yearPeriod || "").trim()) return true;
        if ((n.finalGoal || "").trim()) return true;
        var i;
        for (i = 0; i < n.goals.length; i++) {
          if ((n.goals[i].text || "").trim() || (n.goals[i].progress || "").trim()) return true;
        }
        if (n.graphNodes.some(function (x) { return x.type === "task"; })) return true;
        if (n.edges.length) return true;
        return false;
      }

      function queueSave() {
        if (applyingRemote) return;
        var payload = payloadFromState();
        writeLocal(payload);
        if (!cloudEnabled || !dbRef) {
          setSync("local", "Local only");
          return;
        }
        setSync("saving", "Saving...");
        clearTimeout(saveTimer);
        saveTimer = setTimeout(function () {
          var json = JSON.stringify(payload);
          if (json === lastWrittenJson) {
            setSync("live", "Live sync");
            return;
          }
          dbRef.set(payload)
            .then(function () {
              lastWrittenJson = json;
              setSync("live", "Live sync");
            })
            .catch(function (err) {
              console.error(err);
              setSync("error", "Save failed");
            });
        }, SAVE_DEBOUNCE_MS);
      }

      function applyPayload(payload) {
        state = normalizePayload(payload);
        writeLocal(state);
        renderAll();
      }

      function readDomIntoState() {
        state.meta.title = getRichHtml(document.getElementById("meta-title"));
        state.meta.period = getRichHtml(document.getElementById("meta-period"));
        state.meta.yearPeriod = getRichHtml(document.getElementById("meta-year-period"));
        state.finalGoal = getRichHtml(document.getElementById("final-goal"));

        var rows = document.querySelectorAll("#tbl-goals tbody tr");
        rows.forEach(function (tr) {
          var idx = Number(tr.dataset.index);
          if (!state.goals[idx]) return;
          var textEl = tr.querySelector(".goal-text");
          var progEl = tr.querySelector(".goal-progress input");
          if (textEl) state.goals[idx].text = getRichHtml(textEl);
          if (progEl) state.goals[idx].progress = String(progEl.value || "");
        });

        document.querySelectorAll(".gnode").forEach(function (el) {
          var id = el.dataset.id;
          var node = findNode(id);
          if (!node) return;
          var titleEl = el.querySelector(".node-title");
          if (titleEl && node.type === "task") {
            node.title = getRichHtml(titleEl);
          }
          node.x = parseFloat(el.style.left) || node.x || 0;
          node.y = parseFloat(el.style.top) || node.y || 0;
          var bw = parseFloat(el.style.width);
          if (!isNaN(bw) && bw > 0) node.w = bw;
          var bh = parseFloat(el.style.height);
          if (!isNaN(bh) && bh >= NODE_H_MIN) node.h = bh;
        });

        syncGoalNodes();
      }

      function findNode(id) {
        var i;
        for (i = 0; i < state.graphNodes.length; i++) {
          if (state.graphNodes[i].id === id) return state.graphNodes[i];
        }
        return null;
      }

      function renderMeta() {
        setRichHtml(document.getElementById("meta-title"), state.meta.title || "");
        setRichHtml(document.getElementById("meta-period"), state.meta.period || "");
        setRichHtml(document.getElementById("meta-year-period"), state.meta.yearPeriod || "");
        setRichHtml(document.getElementById("final-goal"), state.finalGoal || "");
      }

      function renderGoals() {
        var tbody = document.querySelector("#tbl-goals tbody");
        tbody.innerHTML = "";
        state.goals.forEach(function (g, idx) {
          var tr = document.createElement("tr");
          tr.dataset.index = String(idx);
          tr.dataset.id = g.id;

          var tdIdx = document.createElement("td");
          tdIdx.className = "goal-idx";
          tdIdx.textContent = "[" + (idx + 1) + "]";
          tr.appendChild(tdIdx);

          var tdText = document.createElement("td");
          var textEl = document.createElement("div");
          textEl.className = "goal-text";
          textEl.contentEditable = "true";
          textEl.spellcheck = false;
          setRichHtml(textEl, g.text || "");
          tdText.appendChild(textEl);
          tr.appendChild(tdText);

          var tdProg = document.createElement("td");
          tdProg.className = "goal-progress";
          var inp = document.createElement("input");
          inp.type = "text";
          inp.value = g.progress || "";
          inp.placeholder = "30%";
          tdProg.appendChild(inp);
          tr.appendChild(tdProg);

          var tdDel = document.createElement("td");
          tdDel.className = "goal-del";
          var btn = document.createElement("button");
          btn.type = "button";
          btn.className = "danger";
          btn.textContent = "Del";
          btn.addEventListener("click", function () {
            readDomIntoState();
            if (state.goals.length <= 1) {
              state.goals[0].text = "";
              state.goals[0].progress = "";
            } else {
              var gid = state.goals[idx].id;
              state.goals.splice(idx, 1);
              state.edges = state.edges.filter(function (e) {
                return e.from !== gid && e.to !== gid;
              });
            }
            syncGoalNodes();
            renderGoals();
            renderGraph();
            queueSave();
          });
          tdDel.appendChild(btn);
          tr.appendChild(tdDel);

          tbody.appendChild(tr);
        });
      }

      function nodeSize(node) {
        var w = node && typeof node.w === "number" && node.w > 0 ? node.w : NODE_W;
        var h = node && typeof node.h === "number" && node.h >= NODE_H_MIN ? node.h : NODE_H_MIN;
        return { w: w, h: h };
      }

      function portPoint(nodeId, side) {
        var stage = document.getElementById("graph-stage");
        var stageRect = stage.getBoundingClientRect();
        var nodeEl = null;
        var nodes = document.querySelectorAll(".gnode");
        var i;
        for (i = 0; i < nodes.length; i++) {
          if (nodes[i].dataset.id === nodeId) {
            nodeEl = nodes[i];
            break;
          }
        }
        if (nodeEl) {
          var port = nodeEl.querySelector(side === "out" ? ".port.out" : ".port.in");
          if (port) {
            var r = port.getBoundingClientRect();
            return {
              x: r.left + r.width / 2 - stageRect.left,
              y: r.top + r.height / 2 - stageRect.top
            };
          }
        }
        var node = findNode(nodeId);
        if (!node) return { x: 0, y: 0 };
        var x = Number(node.x) || 0;
        var y = Number(node.y) || 0;
        var sz = nodeSize(node);
        var cy = y + sz.h / 2;
        if (side === "out") return { x: x + sz.w, y: cy };
        return { x: x, y: cy };
      }

      function edgeCurve(x1, y1, x2, y2) {
        var dx = Math.max(40, Math.abs(x2 - x1) * 0.45);
        return {
          d: "M " + x1 + " " + y1 + " C " + (x1 + dx) + " " + y1 + ", " + (x2 - dx) + " " + y2 + ", " + x2 + " " + y2,
          c2x: x2 - dx,
          c2y: y2,
          x2: x2,
          y2: y2
        };
      }

      function edgePath(x1, y1, x2, y2) {
        return edgeCurve(x1, y1, x2, y2).d;
      }

      function openArrowPath(c2x, c2y, ex, ey) {
        var ang = Math.atan2(ey - c2y, ex - c2x);
        var wing = (ARROW_WING_DEG * Math.PI) / 180;
        var back = ang + Math.PI;
        var xA = ex + ARROW_LEN * Math.cos(back + wing);
        var yA = ey + ARROW_LEN * Math.sin(back + wing);
        var xB = ex + ARROW_LEN * Math.cos(back - wing);
        var yB = ey + ARROW_LEN * Math.sin(back - wing);
        return "M " + xA + " " + yA + " L " + ex + " " + ey + " L " + xB + " " + yB;
      }

      function midPoint(x1, y1, x2, y2) {
        return { x: (x1 + x2) / 2, y: (y1 + y2) / 2 };
      }

      function renderEdges() {
        var svg = document.getElementById("graph-svg");
        var stage = document.getElementById("graph-stage");
        svg.setAttribute("width", String(stage.clientWidth || 800));
        svg.setAttribute("height", String(stage.clientHeight || 420));
        while (svg.firstChild) svg.removeChild(svg.firstChild);

        state.edges.forEach(function (edge) {
          var from = findNode(edge.from);
          var to = findNode(edge.to);
          if (!from || !to) return;
          var a = portPoint(edge.from, "out");
          var b = portPoint(edge.to, "in");
          var curve = edgeCurve(a.x, a.y, b.x, b.y);
          var d = curve.d;
          var mid = midPoint(a.x, a.y, b.x, b.y);
          var sel = selectedEdgeId === edge.id;

          var g = document.createElementNS("http://www.w3.org/2000/svg", "g");
          g.setAttribute("class", "edge-group");
          g.dataset.edgeId = edge.id;

          var hit = document.createElementNS("http://www.w3.org/2000/svg", "path");
          hit.setAttribute("d", d);
          hit.setAttribute("class", "edge-hit");
          hit.setAttribute("stroke", "transparent");
          hit.setAttribute("stroke-width", "14");
          hit.setAttribute("fill", "none");
          hit.dataset.edgeId = edge.id;
          hit.addEventListener("click", function (ev) {
            ev.stopPropagation();
            selectedEdgeId = edge.id;
            renderEdges();
          });
          g.appendChild(hit);

          var line = document.createElementNS("http://www.w3.org/2000/svg", "path");
          line.setAttribute("d", d);
          line.setAttribute("class", "edge-line" + (sel ? " selected" : ""));
          g.appendChild(line);

          var arrow = document.createElementNS("http://www.w3.org/2000/svg", "path");
          arrow.setAttribute("d", openArrowPath(curve.c2x, curve.c2y, curve.x2, curve.y2));
          arrow.setAttribute("class", "edge-arrow" + (sel ? " selected" : ""));
          g.appendChild(arrow);

          var bx = mid.x;
          var by = mid.y;
          var xg = document.createElementNS("http://www.w3.org/2000/svg", "g");
          xg.setAttribute("class", "edge-x-g");
          xg.dataset.edgeId = edge.id;

          var del = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          del.setAttribute("cx", String(bx));
          del.setAttribute("cy", String(by));
          del.setAttribute("r", "8");
          del.setAttribute("class", "edge-x");
          del.dataset.edgeId = edge.id;
          xg.appendChild(del);

          var m1 = document.createElementNS("http://www.w3.org/2000/svg", "path");
          m1.setAttribute("d", "M " + (bx - 3.5) + " " + (by - 3.5) + " L " + (bx + 3.5) + " " + (by + 3.5));
          m1.setAttribute("class", "edge-x-mark");
          xg.appendChild(m1);
          var m2 = document.createElementNS("http://www.w3.org/2000/svg", "path");
          m2.setAttribute("d", "M " + (bx + 3.5) + " " + (by - 3.5) + " L " + (bx - 3.5) + " " + (by + 3.5));
          m2.setAttribute("class", "edge-x-mark");
          xg.appendChild(m2);

          xg.addEventListener("click", function (ev) {
            ev.preventDefault();
            ev.stopPropagation();
            removeEdge(edge.id);
          });
          xg.addEventListener("mousedown", function (ev) {
            ev.stopPropagation();
          });
          g.appendChild(xg);
          svg.appendChild(g);
        });

        if (linkDrag) {
          var curveT = edgeCurve(linkDrag.x1, linkDrag.y1, linkDrag.x2, linkDrag.y2);
          var temp = document.createElementNS("http://www.w3.org/2000/svg", "path");
          temp.setAttribute("d", curveT.d);
          temp.setAttribute("class", "edge-temp");
          svg.appendChild(temp);
          var tempArrow = document.createElementNS("http://www.w3.org/2000/svg", "path");
          tempArrow.setAttribute("d", openArrowPath(curveT.c2x, curveT.c2y, curveT.x2, curveT.y2));
          tempArrow.setAttribute("class", "edge-temp-arrow");
          svg.appendChild(tempArrow);
        }
      }

      function removeEdge(edgeId) {
        state.edges = state.edges.filter(function (e) { return e.id !== edgeId; });
        if (selectedEdgeId === edgeId) selectedEdgeId = null;
        renderEdges();
        queueSave();
      }

      function hideTitleCtxMenu() {
        if (titleCtxMenu && titleCtxMenu.parentNode) {
          titleCtxMenu.parentNode.removeChild(titleCtxMenu);
        }
        titleCtxMenu = null;
      }

      function wrapSelectionWithLink(titleEl, url) {
        var sel = window.getSelection();
        if (!sel || sel.rangeCount < 1 || sel.isCollapsed) return false;
        var range = sel.getRangeAt(0);
        if (!titleEl.contains(range.commonAncestorContainer)) return false;
        var a = document.createElement("a");
        a.href = url;
        a.target = "_blank";
        a.rel = "noopener noreferrer";
        try {
          range.surroundContents(a);
        } catch (err) {
          var frag = range.extractContents();
          a.appendChild(frag);
          range.insertNode(a);
        }
        sel.removeAllRanges();
        return true;
      }

      function showTitleLinkMenu(clientX, clientY, titleEl) {
        hideTitleCtxMenu();
        var menu = document.createElement("div");
        menu.className = "title-ctx-menu";
        menu.style.left = clientX + "px";
        menu.style.top = clientY + "px";
        var btn = document.createElement("button");
        btn.type = "button";
        btn.textContent = "Add link";
        btn.addEventListener("click", function (ev) {
          ev.preventDefault();
          ev.stopPropagation();
          hideTitleCtxMenu();
          var url = window.prompt("URL", "https://");
          if (!url) return;
          url = String(url).trim();
          if (!isSafeHref(url)) {
            window.alert("Only http(s) or relative URLs are allowed.");
            return;
          }
          if (!wrapSelectionWithLink(titleEl, url)) return;
          titleEl.innerHTML = sanitizeHtml(titleEl.innerHTML);
          var n = findNode(titleEl.parentElement ? titleEl.parentElement.dataset.id : "");
          if (n && n.type === "task") {
            n.title = getRichHtml(titleEl);
            queueSave();
          }
        });
        menu.appendChild(btn);
        document.body.appendChild(menu);
        titleCtxMenu = menu;
      }

      function renderGraph() {
        syncGoalNodes();
        hideTitleCtxMenu();
        var host = document.getElementById("graph-nodes");
        host.innerHTML = "";
        state.graphNodes.forEach(function (node) {
          var el = document.createElement("div");
          el.className = "gnode " + (node.type === "goal" ? "goal" : "task");
          el.dataset.id = node.id;
          el.dataset.type = node.type;
          el.style.left = (Number(node.x) || 0) + "px";
          el.style.top = (Number(node.y) || 0) + "px";
          var w = typeof node.w === "number" && node.w > 0 ? node.w : NODE_W;
          el.style.width = w + "px";
          if (typeof node.h === "number" && node.h >= NODE_H_MIN) {
            el.style.height = node.h + "px";
          } else {
            el.style.height = "auto";
            el.style.minHeight = NODE_H_MIN + "px";
          }

          if (node.type === "goal") {
            var badge = document.createElement("div");
            badge.className = "node-badge";
            badge.textContent = "[" + ((Number(node.goalIndex) || 0) + 1) + "]";
            el.appendChild(badge);
          } else {
            var delBtn = document.createElement("button");
            delBtn.type = "button";
            delBtn.className = "danger node-del";
            delBtn.textContent = "x";
            delBtn.title = "Delete task";
            delBtn.addEventListener("click", function (ev) {
              ev.stopPropagation();
              readDomIntoState();
              state.graphNodes = state.graphNodes.filter(function (n) { return n.id !== node.id; });
              state.edges = state.edges.filter(function (e) {
                return e.from !== node.id && e.to !== node.id;
              });
              renderGraph();
              queueSave();
            });
            el.appendChild(delBtn);
          }

          var title = document.createElement("div");
          title.className = "node-title";
          if (node.type === "task") {
            title.contentEditable = "true";
            title.spellcheck = false;
            setRichHtml(title, node.title || "New item");
          } else {
            title.textContent = node.title || "";
          }
          title.addEventListener("mousedown", function (ev) {
            if (ev.target && ev.target.closest && ev.target.closest("a")) {
              ev.stopPropagation();
              return;
            }
            if (node.type === "task") ev.stopPropagation();
          });
          title.addEventListener("click", function (ev) {
            var a = ev.target && ev.target.closest ? ev.target.closest("a") : null;
            if (a && title.contains(a) && a.getAttribute("href")) {
              ev.preventDefault();
              ev.stopPropagation();
              window.open(a.href, "_blank", "noopener,noreferrer");
            }
          });
          title.addEventListener("contextmenu", function (ev) {
            if (node.type !== "task") return;
            var sel = window.getSelection();
            if (!sel || sel.isCollapsed || sel.rangeCount < 1) return;
            if (!title.contains(sel.anchorNode) && !title.contains(sel.focusNode)) return;
            ev.preventDefault();
            ev.stopPropagation();
            showTitleLinkMenu(ev.clientX, ev.clientY, title);
          });
          title.addEventListener("input", function () {
            if (applyingRemote) return;
            var n = findNode(node.id);
            if (!n || n.type !== "task") return;
            n.title = getRichHtml(title);
            queueSave();
          });
          el.appendChild(title);

          var portOut = document.createElement("div");
          portOut.className = "port out";
          portOut.dataset.side = "out";
          portOut.title = "Output";
          el.appendChild(portOut);

          var portIn = document.createElement("div");
          portIn.className = "port in";
          portIn.dataset.side = "in";
          portIn.title = "Input";
          el.appendChild(portIn);

          var resize = document.createElement("div");
          resize.className = "node-resize";
          resize.title = "Resize";
          resize.addEventListener("mousedown", onResizeMouseDown);
          el.appendChild(resize);

          el.addEventListener("mousedown", onNodeMouseDown);
          portOut.addEventListener("mousedown", onPortMouseDown);
          portIn.addEventListener("mousedown", function (ev) { ev.stopPropagation(); });

          host.appendChild(el);
        });
        renderEdges();
      }

      function renderAll() {
        renderMeta();
        renderGoals();
        renderGraph();
      }

      function stagePoint(ev) {
        var stage = document.getElementById("graph-stage");
        var rect = stage.getBoundingClientRect();
        return { x: ev.clientX - rect.left, y: ev.clientY - rect.top };
      }

      function onNodeMouseDown(ev) {
        if (ev.button !== 0) return;
        if (ev.target.classList.contains("port")) return;
        if (ev.target.classList.contains("node-del")) return;
        if (ev.target.classList.contains("node-resize")) return;
        if (ev.target.classList.contains("node-title") && ev.target.isContentEditable) return;
        if (ev.target.closest && ev.target.closest("a")) return;
        ev.preventDefault();
        hideTitleCtxMenu();
        var el = ev.currentTarget;
        var id = el.dataset.id;
        var node = findNode(id);
        if (!node) return;
        var pt = stagePoint(ev);
        dragNode = {
          id: id,
          el: el,
          startX: pt.x,
          startY: pt.y,
          origX: Number(node.x) || 0,
          origY: Number(node.y) || 0
        };
        el.classList.add("dragging");
        suppressClick = false;
      }

      function onResizeMouseDown(ev) {
        if (ev.button !== 0) return;
        ev.preventDefault();
        ev.stopPropagation();
        hideTitleCtxMenu();
        var handle = ev.currentTarget;
        var el = handle.parentElement;
        var id = el.dataset.id;
        var node = findNode(id);
        if (!node) return;
        var curW = typeof node.w === "number" && node.w > 0 ? node.w : (el.offsetWidth || NODE_W);
        var curH = typeof node.h === "number" && node.h >= NODE_H_MIN ? node.h : Math.max(NODE_H_MIN, el.offsetHeight || NODE_H_MIN);
        resizeDrag = {
          id: id,
          el: el,
          startX: ev.clientX,
          startY: ev.clientY,
          origW: curW,
          origH: curH
        };
        el.classList.add("resizing");
        suppressClick = true;
      }

      function onPortMouseDown(ev) {
        if (ev.button !== 0) return;
        ev.preventDefault();
        ev.stopPropagation();
        hideTitleCtxMenu();
        var port = ev.currentTarget;
        var el = port.parentElement;
        var id = el.dataset.id;
        var node = findNode(id);
        if (!node) return;
        var a = portPoint(id, "out");
        var pt = stagePoint(ev);
        linkDrag = {
          fromId: id,
          x1: a.x,
          y1: a.y,
          x2: pt.x,
          y2: pt.y
        };
        selectedEdgeId = null;
        renderEdges();
      }

      function onMouseMove(ev) {
        if (resizeDrag) {
          var dw = ev.clientX - resizeDrag.startX;
          var dh = ev.clientY - resizeDrag.startY;
          var nw = Math.max(120, resizeDrag.origW + dw);
          var nh = Math.max(NODE_H_MIN, resizeDrag.origH + dh);
          var rnode = findNode(resizeDrag.id);
          if (rnode) {
            rnode.w = nw;
            rnode.h = nh;
          }
          resizeDrag.el.style.width = nw + "px";
          resizeDrag.el.style.height = nh + "px";
          renderEdges();
          return;
        }
        if (dragNode) {
          var pt = stagePoint(ev);
          var dx = pt.x - dragNode.startX;
          var dy = pt.y - dragNode.startY;
          if (Math.abs(dx) + Math.abs(dy) > 3) suppressClick = true;
          var nx = Math.max(0, dragNode.origX + dx);
          var ny = Math.max(0, dragNode.origY + dy);
          var node = findNode(dragNode.id);
          if (node) {
            node.x = nx;
            node.y = ny;
          }
          dragNode.el.style.left = nx + "px";
          dragNode.el.style.top = ny + "px";
          renderEdges();
          return;
        }
        if (linkDrag) {
          var p2 = stagePoint(ev);
          linkDrag.x2 = p2.x;
          linkDrag.y2 = p2.y;
          renderEdges();
        }
      }

      function hitInputPort(ev) {
        var bestId = null;
        var bestDist = PORT_HIT_PX;
        var ports = document.querySelectorAll(".gnode .port.in");
        var i;
        for (i = 0; i < ports.length; i++) {
          var port = ports[i];
          var r = port.getBoundingClientRect();
          var cx = r.left + r.width / 2;
          var cy = r.top + r.height / 2;
          var dist = Math.sqrt(Math.pow(ev.clientX - cx, 2) + Math.pow(ev.clientY - cy, 2));
          if (dist <= bestDist) {
            bestDist = dist;
            bestId = port.parentElement ? port.parentElement.dataset.id : null;
          }
        }
        if (bestId) return bestId;
        var el = document.elementFromPoint(ev.clientX, ev.clientY);
        if (!el) return null;
        if (el.classList && el.classList.contains("port") && el.dataset.side === "in") {
          return el.parentElement ? el.parentElement.dataset.id : null;
        }
        var near = el.closest ? el.closest(".port.in") : null;
        if (near && near.parentElement) return near.parentElement.dataset.id;
        return null;
      }

      function wouldCreateCycle(fromId, toId) {
        var stack = [toId];
        var seen = {};
        while (stack.length) {
          var cur = stack.pop();
          if (cur === fromId) return true;
          if (seen[cur]) continue;
          seen[cur] = true;
          state.edges.forEach(function (e) {
            if (e.from === cur) stack.push(e.to);
          });
        }
        return false;
      }

      function onMouseUp(ev) {
        if (resizeDrag) {
          resizeDrag.el.classList.remove("resizing");
          resizeDrag = null;
          if (!applyingRemote) queueSave();
          return;
        }
        if (dragNode) {
          dragNode.el.classList.remove("dragging");
          dragNode = null;
          if (!applyingRemote) queueSave();
          return;
        }
        if (linkDrag) {
          var toId = hitInputPort(ev);
          var fromId = linkDrag.fromId;
          linkDrag = null;
          renderEdges();
          if (toId && toId !== fromId) {
            var exists = state.edges.some(function (e) {
              return e.from === fromId && e.to === toId;
            });
            if (!exists && !wouldCreateCycle(fromId, toId)) {
              state.edges.push({ id: uid("edge"), from: fromId, to: toId });
              renderEdges();
              queueSave();
            }
          }
        }
      }

      function onEditableInput(ev) {
        var t = ev.target;
        if (!t) return;
        if (applyingRemote) return;
        var isEdit = t.contentEditable === "true" || t.tagName === "INPUT";
        if (!isEdit) return;
        readDomIntoState();
        if (t.classList.contains("goal-text") || (t.tagName === "INPUT" && t.closest("#tbl-goals"))) {
          syncGoalNodes();
          renderGraph();
        }
        queueSave();
      }

      function initFirebase() {
        var cfg = window.LAB_FIREBASE_CONFIG;
        if (!isConfigReady(cfg)) {
          setSync("local", "Local only");
          showSetupBanner(
            "Shared sync is not configured yet. Edit <code>firebase-config.js</code> with your Firebase Realtime Database settings, then reopen this page. Until then, data stays in this browser only."
          );
          return false;
        }
        try {
          if (!firebase.apps.length) firebase.initializeApp(cfg);
          dbRef = firebase.database().ref(DB_PATH);
          cloudEnabled = true;
          setSync("saving", "Connecting...");
          dbRef.on("value", function (snap) {
            var remote = snap.val();
            if (!remote) {
              var local = readLocal();
              var upload = hasContent(local) ? local : normalizePayload(makeSeed());
              applyingRemote = true;
              applyPayload(upload);
              applyingRemote = false;
              var payload = payloadFromState();
              dbRef.set(payload).then(function () {
                lastWrittenJson = JSON.stringify(payload);
                setSync("live", "Live sync");
              }).catch(function (err) {
                console.error(err);
                setSync("error", "Upload failed");
              });
              return;
            }
            var normalized = normalizePayload(remote);
            var remoteJson = coreJson(normalized);
            var localJson = coreJson(state);
            if (remoteJson === localJson) {
              lastWrittenJson = JSON.stringify(payloadFromState());
              setSync("live", "Live sync");
              return;
            }
            applyingRemote = true;
            applyPayload(normalized);
            applyingRemote = false;
            lastWrittenJson = JSON.stringify(payloadFromState());
            setSync("live", "Live sync");
          }, function (err) {
            console.error(err);
            setSync("error", "Sync error");
            showSetupBanner(
              "Could not connect to Firebase. Check Realtime Database rules (read/write allowed) and <code>firebase-config.js</code>."
            );
          });
          return true;
        } catch (e) {
          console.error(e);
          setSync("error", "Config error");
          showSetupBanner("Firebase init failed. Check <code>firebase-config.js</code>.");
          return false;
        }
      }

      function wireButtons() {
        document.getElementById("btn-add-goal").addEventListener("click", function () {
          readDomIntoState();
          state.goals.push({ id: uid("goal"), text: "", progress: "" });
          syncGoalNodes();
          renderGoals();
          renderGraph();
          queueSave();
        });

        document.getElementById("btn-del-goal").addEventListener("click", function () {
          readDomIntoState();
          if (!state.goals.length) return;
          var last = state.goals[state.goals.length - 1];
          var gid = last.id;
          if (state.goals.length <= 1) {
            state.goals[0].text = "";
            state.goals[0].progress = "";
          } else {
            state.goals.pop();
            state.edges = state.edges.filter(function (e) {
              return e.from !== gid && e.to !== gid;
            });
          }
          syncGoalNodes();
          renderGoals();
          renderGraph();
          queueSave();
        });

        document.getElementById("btn-add-item").addEventListener("click", function () {
          readDomIntoState();
          var stage = document.getElementById("graph-stage");
          var x = Math.max(260, Math.floor((stage.clientWidth || 700) * 0.45));
          var y = 40 + state.graphNodes.filter(function (n) { return n.type === "task"; }).length * 70;
          state.graphNodes.push({
            id: uid("task"),
            type: "task",
            goalIndex: null,
            title: "New item",
            x: x,
            y: y,
            w: NODE_W,
            h: null
          });
          renderGraph();
          queueSave();
        });

        document.getElementById("graph-stage").addEventListener("click", function () {
          hideTitleCtxMenu();
          if (suppressClick) {
            suppressClick = false;
            return;
          }
          if (selectedEdgeId) {
            selectedEdgeId = null;
            renderEdges();
          }
        });

        document.addEventListener("mousedown", function (ev) {
          if (titleCtxMenu && !titleCtxMenu.contains(ev.target)) {
            hideTitleCtxMenu();
          }
        });

        document.addEventListener("keydown", function (ev) {
          if (ev.key !== "Delete" && ev.key !== "Del" && ev.key !== "Backspace") return;
          var tag = (ev.target && ev.target.tagName) || "";
          if (tag === "INPUT" || tag === "TEXTAREA") return;
          if (ev.target && ev.target.isContentEditable) return;
          if (!selectedEdgeId) return;
          ev.preventDefault();
          removeEdge(selectedEdgeId);
        });

        window.addEventListener("resize", function () {
          renderEdges();
        });
      }

      function boot() {
        var local = readLocal();
        if (local && hasContent(local)) {
          state = normalizePayload(local);
        } else {
          state = normalizePayload(makeSeed());
          writeLocal(state);
        }
        renderAll();
        wireButtons();
        document.addEventListener("input", onEditableInput);
        document.addEventListener("mousemove", onMouseMove);
        document.addEventListener("mouseup", onMouseUp);
        if (!initFirebase()) {
          setSync("local", "Local only");
        }
      }

      boot();
    })();
  </script>
</body>
</html>
"""


def write_utf8_no_bom(path: Path, text: str) -> None:
    data = text.encode("utf-8")
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    if b"\x00" in data:
        raise RuntimeError("Refusing to write file containing null bytes: " + str(path))
    path.write_bytes(data)


def main() -> None:
    write_utf8_no_bom(OUTPUT, HTML_TEMPLATE)
    print("Wrote", OUTPUT)
    print("Bytes", OUTPUT.stat().st_size)


if __name__ == "__main__":
    main()
