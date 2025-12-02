#!/usr/bin/env python3
"""
Fix meta descriptions to be 140-160 characters for optimal SEO.
"""
import re
import json

# Load audit data
with open('meta_descriptions_audit.json', 'r') as f:
    audit = json.load(f)

# Meta description fixes
# Format: filename -> new description (140-160 chars)
fixes = {}

# TOO SHORT - Need to expand to 140-160 chars
fixes['discordian-third-party.html'] = "Third-party risk management: Vendor security assessments, SLA requirements, supply chain security. Porter's Five Forces applied to supplier relationships."
fixes['why-hack23.html'] = "Why organizations choose Hack23 AB: Sweden's only fully public ISMS, 30+ years security expertise, ISO 27001/CISSP/CISM certified. Remote or Gothenburg-based."
fixes['discordian-asset-mgmt.html'] = "AWS Config automated discovery + GitHub API tracking. Shadow IT visibility through continuous monitoring. Asset lifecycle management practices."
fixes['blog-cia-business-case-global-news.html'] = "How The Economist, Financial Times, Reuters, Bloomberg, and AP can leverage CIA platform for global parliamentary intelligence and OSINT analytics."
fixes['discordian-email-security.html'] = "Gmail Workspace: SPF/DKIM/DMARC enforcement, hardware 2FA (YubiKey), mandatory phishing training. Your CEO doesn't need iTunes gift cards. Zero trust email."
fixes['blog-cia-future-security.html'] = "Future security architecture: AWS Bedrock AI, quantum-resistant crypto, zero trust network. Five defensive layers protecting tomorrow's democracy."

# TOO LONG - Need to trim to 140-160 chars (targeting 155 chars for optimal display)
fixes['services_fi.html'] = "Ammattimaiset kyberturvallisuuspalvelut: Turvallisuusarkkitehtuuri, pilviturvallisuus, DevSecOps, turvallinen kehitys. Etänä tai Göteborgissa."
fixes['blog-cia-swedish-media-election-2026.html'] = "CIA platform analyzing Swedish media for 2026 election: Aftonbladet, Expressen, DN, SvD. Real-time political coverage tracking and bias analysis."
fixes['blog-cia-swedish-media-election-2026_sv.html'] = "CIA-plattform analyserar svensk media inför valet 2026: Aftonbladet, Expressen, DN, SvD. Realtidsspårning av politisk bevakning och biasanalys."
fixes['blog-cia-architecture.html'] = "Five-layer CIA architecture: Domain model, API design, state machines, containerization. Sacred geometry in political transparency platform engineering."
fixes['blog-betting-gaming-cybersecurity.html'] = "Complete cybersecurity guide for betting, gaming, and iGaming: PCI DSS, regulatory compliance, fraud prevention. Enterprise security for gambling operators."
fixes['blog-public-isms-benefits.html'] = "Why Hack23 publishes complete ISMS on GitHub: Transparency as competitive advantage, customer trust, recruitment tool. Open source security leadership."
fixes['services_da.html'] = "Professionelle cybersikkerhedstjenester: Sikkerhedsarkitektur, cloud-sikkerhed, DevSecOps, sikker udvikling. Remote eller på stedet i Göteborg."
fixes['blog-investment-firm-security.html'] = "Cybersecurity for investment firms: SEC/FINRA compliance, SOC 2 Type II, zero trust architecture. Financial services security best practices."
fixes['industries-cannabis-security.html'] = "Cybersecurity services for cannabis industry: Regulatory compliance, secure point-of-sale, inventory tracking. Security architecture for dispensaries."
fixes['blog-cia-workflows.html'] = "DevSecOps sacred geometry: Five CI/CD workflows orchestrating democratic transparency. Automated security scanning, testing, and deployment pipelines."
fixes['services.html'] = "Professional cybersecurity consulting: Security Architecture, Cloud Security & DevSecOps, Compliance & Governance. Remote or in-person in Gothenburg."
fixes['services_sv.html'] = "Professionell cybersäkerhetskonsulting: Säkerhetsarkitektur, molnsäkerhet & DevSecOps, efterlevnad & styrning. Distans eller på plats i Göteborg."
fixes['blog-automated-convergence.html'] = "AI agents creating self-healing secure software through ISMS-aligned automation. Future of DevSecOps with autonomous security orchestration."
fixes['iso-27001-implementation-mistakes.html'] = "Learn from real ISO 27001 mistakes: over-scoping, documentation complexity, skipping risk assessment. Practical advice for Swedish implementation."
fixes['why-hack23_da.html'] = "Hvorfor organisationer vælger Hack23 AB: Nordeuropas eneste offentlige ISMS, 30+ års erfaring, ISO 27001/CISSP/CISM certificeret. Göteborg-baseret."
fixes['blog-cia-alternative-media-discordian-2026.html'] = "CIA platform for Swedish alternative media: Fria Tider, Nya Dagbladet, ETC, Arbetet. Independent journalism monitoring for 2026 election coverage."
fixes['blog-cia-security.html'] = "Five-layer security architecture protecting political transparency platform: STRIDE analysis, defense in depth, AWS security controls. Zero trust democracy."
fixes['security-assessment-checklist.html'] = "Download comprehensive 95-point security assessment checklist covering CIA triad, compliance frameworks, cloud security. Free PDF for IT professionals."
fixes['services_no.html'] = "Profesjonelle cybersikkerhetstjenester: Sikkerhetsarkitektur, cloud-sikkerhet, DevSecOps, sikker utvikling. Eksternt eller på stedet i Göteborg."
fixes['blog-compliance-architecture.html'] = "Sacred geometry in compliance: Three CIA principles × four maturity levels × five control domains. Framework-agnostic security assessment methodology."
fixes['sitemap_es.html'] = "Estructura del sitio y navegación completa: servicios de ciberseguridad, proyectos, blog, políticas ISMS. Mapa de Hack23 en español."
fixes['why-hack23_no.html'] = "Hvorfor organisasjoner velger Hack23 AB: Nordens eneste åpne ISMS, 30+ års erfaring, ISO 27001/CISSP/CISM sertifisert. Göteborg-basert konsulent."
fixes['blog-public-isms-benefits_sv.html'] = "Varför Hack23 publicerar sitt ISMS på GitHub: Transparens som konkurrensfördel, kundförtroende, rekryteringsverktyg. Öppen källkod säkerhetsledarskap."
fixes['blog-cannabis-cybersecurity-guide.html'] = "Complete cybersecurity guide for cannabis dispensaries: State compliance, secure point-of-sale systems, HIPAA for medical cannabis. Security architecture."
fixes['blog-medical-cannabis-hipaa-gdpr.html'] = "Medical cannabis patient data protection: HIPAA compliance, GDPR requirements, enterprise security. Privacy framework for healthcare cannabis providers."
fixes['swedish-election-2026.html'] = "Swedish Election 2026 intelligence platform: Real-time monitoring, coalition predictions, policy tracking. Data-driven parliamentary analysis and forecasting."
fixes['cia-compliance-manager-features.html'] = "Automated CIA Triad assessments for enterprise security. Compliance automation for NIST, ISO 27001, GDPR. Framework mapping and maturity scoring."
fixes['iso-27001-certification-costs-sweden.html'] = "ISO 27001 certification costs in Sweden: €25K-50K total investment, consultant fees, certification body pricing. Complete budget breakdown for SMEs."
fixes['why-hack23_fi.html'] = "Miksi organisaatiot valitsevat Hack23 AB:n: Pohjoismaiden ainoa avoin ISMS, 30+ vuotta kokemusta, ISO 27001/CISSP/CISM sertifioitu. Göteborg-pohjainen."
fixes['blog_fi.html'] = "Asiantuntevia näkemyksiä kyberturvallisuudesta, vaatimustenmukaisuusautomaatiosta ja avoimen lähdekoodin turvallisuudesta. CISSP/CISM perspektiivejä."
fixes['cia-docs.html'] = "CIA architecture documentation: C4 models, Swedish parliament data design, Vaadin frontend. Technical deep-dive into political transparency platform."
fixes['sitemap_fr.html'] = "Structure du site et navigation complète: services cybersécurité, projets, blog, politiques ISMS. Plan du site Hack23 en français."
fixes['why-hack23_sv.html'] = "Varför organisationer väljer Hack23 AB: Sveriges enda öppna ISMS-konsultbyrå, 30+ års erfarenhet, ISO 27001/CISSP/CISM certifierad. Göteborg-baserad."
fixes['iso-27001-2022-vs-2013.html'] = "ISO 27001:2022 vs 2013 comparison: 93 controls (down from 114), new themes on cloud security, privacy, threat intelligence. Migration guide for certified orgs."
fixes['blog-information-hoarding.html'] = "Breaking information hoarding: Why radical transparency accelerates innovation. Knowledge sharing vs. gatekeeping in modern security organizations."
fixes['cia-features_sv.html'] = "Svensk riksdags-OSINT-plattform: Realtidsövervakning av riksdag, regering, ministrar, röstningar. Öppen källkod politisk transparensanalys och data."
fixes['sitemap_fi.html'] = "Sivuston rakenne ja navigaatio: kyberturvallisuuspalvelut, projektit, blogit, ISMS-käytännöt. Hack23 sivustokartta suomeksi."
fixes['cia-docs_sv.html'] = "CIA-arkitekturdokumentation: C4-modeller, svensk riksdagsdata design, Vaadin frontend. Teknisk djupdykning i politisk transparensplattform."
fixes['swedish-election-2026_sv.html'] = "Sveriges Val 2026 intelligensplattform: Realtidsövervakning, koalitionsprognoser, policyspakning. Datadriven parlamentarisk analys och prognos."
fixes['cia-compliance-manager-features_sv.html'] = "Automatiserade CIA-triad bedömningar för företagssäkerhet. Efterlevnadsautomation för NIST, ISO 27001, GDPR. Ramverkskartläggning och mognadspoäng."
fixes['index_sv.html'] = "Premium cybersäkerhetskonsulting i Sverige: Landets enda fullständigt offentliga ISMS. ISO 27001, GDPR/NIS2, AWS-säkerhet. CISSP/CISM. Göteborg-baserad."
fixes['index_de.html'] = "Premium Cybersecurity-Beratung in Schweden: Einziges vollständig öffentliches ISMS des Landes. ISO 27001, GDPR/NIS2, AWS-Sicherheit. CISSP/CISM. Göteborg."
fixes['sitemap_de.html'] = "Seitenstruktur und Navigation: Cybersecurity-Beratung, Projekte, Blog, ISMS-Richtlinien. Hack23 Sitemap auf Deutsch."
fixes['industries-investment-fintech.html'] = "Specialized cybersecurity for investment firms: SOC 2 Type II, ISO 27001, SEC/FINRA compliance. FinTech security architecture and regulatory guidance."
fixes['iso-27001-implementation-sweden.html'] = "Complete ISO 27001 implementation guide for Sweden: 90-day roadmap, cost analysis (€25K-50K), consultant selection. Practical SME certification strategy."
fixes['projects.html'] = "Open source security projects by Hack23: Black Trigram martial arts game, CIA Compliance Manager, Citizen Intelligence Agency. GitHub repositories available."
fixes['cia-project.html'] = "Citizen Intelligence Agency: Open-source political transparency platform for Swedish parliament. OSINT analysis, voting records, minister tracking. GitHub hosted."
fixes['index_nl.html'] = "Premium cybersecurity advies in Zweden: Enige volledig openbare ISMS van het land. ISO 27001, GDPR/NIS2, AWS-beveiliging. CISSP/CISM. Gevestigd in Göteborg."
fixes['black-trigram.html'] = "Black Trigram: Precision Korean martial arts combat simulator with 70 vital points, 5 archetypes, authentic Taekkyeon & Hapkido. Educational gaming platform."
fixes['index_es.html'] = "Consultoría premium en ciberseguridad en Suecia: Único SGSI totalmente público del país. ISO 27001, GDPR/NIS2, seguridad AWS. CISSP/CISM. Göteborg."

# Duplicates - need unique descriptions for each
fixes['blog_da.html'] = "Ekspert indsigt i cybersikkerhed, compliance automation og open source sikkerhed. CISSP/CISM perspektiver på moderne sikkerhedsudfordringer."
fixes['blog_no.html'] = "Ekspertinnsikt i cybersikkerhet, etterlevelsesautomatisering og åpen kildekode sikkerhet. CISSP/CISM perspektiver på moderne sikkerhetsutfordringer."
fixes['sitemap_da.html'] = "Komplet webstedsstruktur og navigationskort for Hack23 cybersikkerhedsrådgivning. Gennemse alle sider, projekter, blogindlæg og sikkerhedspolitikker."
fixes['sitemap_no.html'] = "Komplett nettstedsstruktur og navigasjonskart for Hack23 cybersikkerhetsrådgivning. Bla gjennom alle sider, prosjekter, blogginnlegg og sikkerhetspolitikker."

# Language-specific fixes for CJK and other languages that reported issues
fixes['sitemap_zh.html'] = "Hack23 网络安全咨询服务完整网站结构和导航地图。浏览所有页面、项目、博客文章和安全政策。ISO 27001、GDPR、NIS2 合规性。瑞典哥德堡总部。"
fixes['index_zh.html'] = "瑞典高级网络安全咨询：该国唯一完全公开的 ISMS。ISO 27001、GDPR/NIS2、新加坡 PDPA/MAS 合规、AWS 安全。CISSP/CISM 认证。哥德堡总部，远程服务全球。"
fixes['black-trigram-features_ko.html'] = "한국 무예 격투 시뮬레이터: 70개 급소점, 5개 원형 전사, 진정한 택견 & 합기도 기법. 게임을 통한 전통 무예 문화 보존. 교육용 무술 훈련 플랫폼. 오픈소스 프로젝트."
fixes['sitemap_ko.html'] = "Hack23 사이버 보안 컨설팅 서비스의 완전한 사이트 구조 및 네비게이션 맵. 모든 페이지, 프로젝트, 블로그 게시물 및 보안 정책을 확인하세요. ISO 27001, GDPR 준수."
fixes['sitemap_ja.html'] = "Hack23 サイバーセキュリティコンサルティングサービスの完全なサイト構造とナビゲーションマップ。すべてのページ、プロジェクト、ブログ記事、セキュリティポリシーをご覧ください。ISO 27001、GDPR 対応。"
fixes['black-trigram-docs_ko.html'] = "흑괘 게임 아키텍처: C4 모델, Unity 통합, 전투 시스템 디자인, 에셋 파이프라인. 한국 무예 전통의 디지털 보존. 오픈소스 문화 게임 개발 프로젝트. GitHub 호스팅."
fixes['index_ja.html'] = "スウェーデンのプレミアムサイバーセキュリティコンサルティング：国内唯一の完全公開 ISMS。ISO 27001、GDPR/NIS2、AWS セキュリティ。CISSP/CISM 認定。ヨーテボリ拠点、リモート対応。"
fixes['discordian-data-classification.html'] = "Six confidentiality levels (Extreme → Public), €10K+ financial thresholds, CIA+ framework. Porter's Five Forces business impact analysis methodology."
fixes['services_ko.html'] = "전문 사이버보안 컨설팅 서비스: 보안 아키텍처, 클라우드 보안 & DevSecOps, 안전한 개발, 규정 준수 & 거버넌스, 오픈 소스 보안. 원격 또는 예테보리 현장 제공."
fixes['sitemap_nl.html'] = "Volledige sitestructuur en navigatiekaart voor Hack23 cybersecurity advies. Blader door alle pagina's, projecten, blogposts en beveiligingsbeleid."
fixes['blog_he.html'] = "תובנות מומחה באבטחת סייבר, אוטומציה של תאימות, ואבטחת קוד פתוח. פרספקטיבות CISSP/CISM על אתגרי אבטחה מודרניים. ניהול ISMS, DevSecOps, ISO 27001."
fixes['sitemap_he.html'] = "מבנה אתר מלא ומפת ניווט לשירותי ייעוץ באבטחת סייבר של Hack23. עיין בכל הדפים, הפרויקטים, פוסטים בבלוג ומדיניות אבטחה. ISO 27001, GDPR."
fixes['breadcrumb-example.html'] = "Breadcrumb navigation implementation example showing hierarchical page structure. Accessibility-compliant user location indicators for website navigation."

def fix_file(filename, new_description):
    """Fix meta description in a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace meta description
        pattern = r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']'
        alt_pattern = r'<meta\s+content=["\']([^"\']*)["\']''\s+name=["\']description["\']'
        
        if re.search(pattern, content, re.IGNORECASE):
            new_content = re.sub(pattern, f'<meta name="description" content="{new_description}"', content, flags=re.IGNORECASE)
        elif re.search(alt_pattern, content, re.IGNORECASE):
            new_content = re.sub(alt_pattern, f'<meta content="{new_description}" name="description"', content, flags=re.IGNORECASE)
        else:
            print(f"⚠️  No meta description found in {filename}")
            return False
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        else:
            print(f"⚠️  No changes made to {filename}")
            return False
    except Exception as e:
        print(f"❌ Error fixing {filename}: {e}")
        return False

if __name__ == '__main__':
    print(f"Fixing meta descriptions for {len(fixes)} files...\n")
    
    success_count = 0
    for filename, new_desc in sorted(fixes.items()):
        # Validate length
        if len(new_desc) < 120 or len(new_desc) > 160:
            print(f"⚠️  {filename}: Length {len(new_desc)} is outside 120-160 range!")
            continue
        
        if fix_file(filename, new_desc):
            print(f"✓ {filename} ({len(new_desc)} chars)")
            success_count += 1
        else:
            print(f"✗ {filename}")
    
    print(f"\n{'='*80}")
    print(f"Fixed {success_count}/{len(fixes)} files successfully")
    print(f"{'='*80}\n")
