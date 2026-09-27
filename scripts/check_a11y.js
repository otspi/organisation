#!/usr/bin/env node
// SPDX-License-Identifier: EUPL-1.2
// Contrôle d'accessibilité (WCAG 2 AA, moteur axe) de toutes les pages du site construit, listées par
// son sitemap.xml. Le site est servi localement par ce script.
//
// axe distingue les violations confirmées des cas qu'il ne sait pas trancher (texte des schémas SVG,
// libellés tronqués…) : seules les premières font échouer le contrôle, les secondes sont listées.
//
// Usage :
//     npm install --no-save pa11y@9
//     node scripts/check_a11y.js [site]
//
// La variable d'environnement CHROME permet d'imposer le navigateur (sinon celui de Puppeteer).

const fs = require("fs");
const http = require("http");
const path = require("path");
const pa11y = require("pa11y");

const SITE = path.resolve(process.argv[2] || "site");
const TYPES = {
  ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript", ".json": "application/json",
  ".svg": "image/svg+xml", ".png": "image/png", ".woff2": "font/woff2", ".xml": "application/xml",
  ".pdf": "application/pdf",
};

function serve() {
  const server = http.createServer((req, res) => {
    let file = path.join(SITE, decodeURIComponent(new URL(req.url, "http://x").pathname));
    if (!file.startsWith(SITE)) {
      res.writeHead(403).end();
      return;
    }
    if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, "index.html");
    fs.readFile(file, (error, data) => {
      if (error) {
        res.writeHead(404).end();
        return;
      }
      res.writeHead(200, { "Content-Type": TYPES[path.extname(file)] || "application/octet-stream" }).end(data);
    });
  });
  return new Promise((resolve) => server.listen(0, "127.0.0.1", () => resolve(server)));
}

(async () => {
  const sitemap = fs.readFileSync(path.join(SITE, "sitemap.xml"), "utf-8");
  const pages = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => new URL(m[1]).pathname);
  const server = await serve();
  const base = `http://127.0.0.1:${server.address().port}`;
  const launch = { args: ["--no-sandbox"] };
  if (process.env.CHROME) launch.executablePath = process.env.CHROME;

  let confirmed = 0;
  const review = new Map();
  try {
    for (const page of pages) {
      const result = await pa11y(base + page, { runners: ["axe"], standard: "WCAG2AA", timeout: 60000, chromeLaunchConfig: launch });
      for (const issue of result.issues) {
        const context = issue.context.replace(/\s+/g, " ").slice(0, 90);
        if (issue.runnerExtras && issue.runnerExtras.needsFurtherReview) {
          review.set(`${issue.code} : ${page}`, (review.get(`${issue.code} : ${page}`) || 0) + 1);
          continue;
        }
        confirmed += 1;
        console.log(`ÉCHEC ${page} — ${issue.code} : ${issue.message.split(" (")[0]}\n      ${issue.selector}\n      ${context}`);
      }
    }
  } finally {
    server.close();
  }

  if (review.size) {
    console.log("\nÀ examiner (axe n'a pas pu trancher, sans effet sur le résultat) :");
    for (const [key, count] of review) console.log(`  ${key} (${count})`);
  }
  console.log(`\n${pages.length} pages contrôlées, ${confirmed} violation(s) confirmée(s).`);
  process.exit(confirmed ? 1 : 0);
})().catch((error) => {
  console.error(error);
  process.exit(2);
});
