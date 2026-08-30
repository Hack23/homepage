import { minify } from 'html-minifier-terser';
import CleanCSS from 'clean-css';
import { readFileSync, writeFileSync } from 'fs';
import { execSync } from 'child_process';

// Structural HTML minification only. minifyJS/minifyCSS are intentionally
// disabled: re-parsing every inline <script>/<style> with terser/clean-css is
// what made the previous Docker-based minify step take ~15 minutes.
const htmlOptions = {
  collapseWhitespace: true,
  removeComments: true,
};

const cleanCss = new CleanCSS({});

function gitFiles(pattern) {
  return execSync(`git ls-files '${pattern}'`)
    .toString()
    .trim()
    .split('\n')
    .filter(Boolean);
}

let htmlCount = 0;
for (const file of gitFiles('*.html')) {
  const src = readFileSync(file, 'utf8');
  writeFileSync(file, await minify(src, htmlOptions));
  htmlCount++;
}

let cssCount = 0;
for (const file of gitFiles('*.css')) {
  const src = readFileSync(file, 'utf8');
  const { styles, errors } = cleanCss.minify(src);
  if (errors && errors.length > 0) {
    console.error(`clean-css errors in ${file}:`, errors);
    process.exitCode = 1;
    continue;
  }
  writeFileSync(file, styles);
  cssCount++;
}

console.log(`Minified ${htmlCount} HTML and ${cssCount} CSS files`);
