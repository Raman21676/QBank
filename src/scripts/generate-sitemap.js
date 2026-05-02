const fs = require("fs");
const path = require("path");

const BASE_URL = "https://raman21676.github.io/QBank";

// Load manifests
const bca = require("../content/bca.json");
const ba = require("../content/ba.json");
const bit = require("../content/bit.json");

const faculties = [bca, ba, bit];

const urls = [
  { loc: "/", priority: "1.0", changefreq: "weekly" },
];

for (const faculty of faculties) {
  // Faculty page
  urls.push({
    loc: `/${faculty.slug}/`,
    priority: "0.9",
    changefreq: "weekly",
  });

  for (const sem of faculty.semesters) {
    // Semester page
    urls.push({
      loc: `/${faculty.slug}/${sem.slug}/`,
      priority: "0.8",
      changefreq: "weekly",
    });

    for (const sub of sem.subjects) {
      // Subject page
      urls.push({
        loc: `/${faculty.slug}/${sem.slug}/${sub.slug}/`,
        priority: "0.7",
        changefreq: "weekly",
      });

      for (const paper of sub.papers) {
        // Year page
        urls.push({
          loc: `/${faculty.slug}/${sem.slug}/${sub.slug}/${paper.year}/`,
          priority: paper.hasQuestions ? "0.6" : "0.3",
          changefreq: "monthly",
        });
      }
    }
  }
}

const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls
  .map(
    (url) => `  <url>
    <loc>${BASE_URL}${url.loc}</loc>
    <priority>${url.priority}</priority>
    <changefreq>${url.changefreq}</changefreq>
  </url>`
  )
  .join("\n")}
</urlset>
`;

const publicDir = path.join(__dirname, "../../public");
if (!fs.existsSync(publicDir)) {
  fs.mkdirSync(publicDir, { recursive: true });
}

fs.writeFileSync(path.join(publicDir, "sitemap.xml"), sitemap);

const robots = `User-agent: *
Allow: /

Sitemap: ${BASE_URL}/sitemap.xml
`;

fs.writeFileSync(path.join(publicDir, "robots.txt"), robots);

console.log(`Generated sitemap.xml with ${urls.length} URLs`);
console.log(`Generated robots.txt`);
