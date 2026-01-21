const fs = require('fs');
const files = ['index_ko.html', 'index_ja.html', 'blog_ko.html', 'blog_ja.html', 'services_ko.html', 'services_ja.html'];

files.forEach(file => {
  const content = fs.readFileSync(file, 'utf-8');
  const matches = content.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g);
  
  console.log(`\n=== ${file} ===`);
  if (!matches) {
    console.log('❌ No JSON-LD found');
    return;
  }
  
  matches.forEach((match, i) => {
    const json = match.replace(/<script type="application\/ld\+json">/, '').replace(/<\/script>/, '');
    try {
      JSON.parse(json);
      console.log(`✅ JSON-LD block ${i + 1}: Valid`);
    } catch (e) {
      console.log(`❌ JSON-LD block ${i + 1}: ${e.message}`);
    }
  });
});
