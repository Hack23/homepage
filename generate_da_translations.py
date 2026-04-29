#!/usr/bin/env python3
"""Generate Danish (_da.html) translations for 9 new product pages."""

import re

# =============================================================================
# Common Danish translations dictionary
# =============================================================================

COMMON_DA = {
    # HTML lang attribute
    '<html lang="en">': '<html lang="da">',
    
    # Locale
    'content="en_US"': 'content="da_DK"',
    '"inLanguage": "en"': '"inLanguage": "da"',
    
    # Nav
    '>Services<': '>Tjenester<',
    '>Projects<': '>Projekter<',
    'title="Services">Services': 'title="Services">Tjenester',
    'title="Projects">Projects': 'title="Projects">Projekter',
    'title="Why Hack23">Why Hack23': 'title="Why Hack23">Hvorfor Hack23',
    'title="Blog">Blog': 'title="Blog">Blog',
    'title="Public ISMS">ISMS': 'title="Public ISMS">ISMS',
    'title="Home">🏠 Hack23': 'title="Home">🏠 Hack23',
    
    # Breadcrumb Home/Projects
    '<a href="index.html">Home</a>': '<a href="index.html">Hjem</a>',
    '<a href="projects.html">Projects</a>': '<a href="projects.html">Projekter</a>',
    
    # JSON-LD breadcrumb
    '"name": "Home",': '"name": "Hjem",',
    '"name": "Projects",': '"name": "Projekter",',
    
    # Footer company info
    'Cybersecurity Consulting<br>': 'Cybersikkerhedsrådgivning<br>',
    'Gothenburg, Sweden | Remote': 'Göteborg, Sverige | Fjernarbejde',
    '>LinkedIn Company Page<': '>LinkedIn-virksomhedsside<',
    'CEO: James Pether Sörling': 'Adm. direktør: James Pether Sörling',
    
    # Footer columns
    '<h3>Services</h3>': '<h3>Tjenester</h3>',
    '<h3>Products</h3>': '<h3>Produkter</h3>',
    '<h3>Resources</h3>': '<h3>Ressourcer</h3>',
    '<h3>Company</h3>': '<h3>Virksomhed</h3>',
    
    # Footer services
    '>Security Consulting<': '>Sikkerhedsrådgivning<',
    '>Security Architecture<': '>Sikkerhedsarkitektur<',
    '>Cloud Security<': '>Cloud-sikkerhed<',
    '>DevSecOps Integration<': '>DevSecOps-integration<',
    '>Compliance &amp; ISMS<': '>Compliance og ISMS<',
    
    # Footer resources
    '>Security Blog<': '>Sikkerhedsblog<',
    '>Public ISMS<': '>Offentligt ISMS<',
    '>Sitemap<': '>Sitemap<',
    
    # Footer company
    '>About Hack23<': '>Om Hack23<',
    '>Security Policy<': '>Sikkerhedspolitik<',
    '>Report Security Issue<': '>Rapportér sikkerhedsproblem<',
    '>GitHub Organization<': '>GitHub-organisation<',
    '>Accessibility<': '>Tilgængelighed<',
    
    # Footer copyright
    'All rights reserved.': 'Alle rettigheder forbeholdes.',
    
    # Common section headings
    '>🎯 Key Features</h2>': '>🎯 Nøglefunktioner</h2>',
    '>⚙️ Platform Capabilities</h2>': '>⚙️ Platformkapaciteter</h2>',
    '>🛡️ Security &amp; Quality</h2>': '>🛡️ Sikkerhed og kvalitet</h2>',
    '>🛡️ Security & Quality</h2>': '>🛡️ Sikkerhed og kvalitet</h2>',
    '>💼 Use Cases</h2>': '>💼 Anvendelsesscenarier</h2>',
    '>🔗 Related Projects</h2>': '>🔗 Relaterede projekter</h2>',
    '>🌐 Live Resources</h2>': '>🌐 Live-ressourcer</h2>',
    '>🌐 Live Resources<': '>🌐 Live-ressourcer<',
    '>📊 Statistics</h2>': '>📊 Statistikker</h2>',
    '>🔐 ISMS Compliance</h2>': '>🔐 ISMS-overensstemmelse</h2>',
    '>📋 ISMS Compliance</h2>': '>📋 ISMS-overensstemmelse</h2>',
    '>🎯 Platform Overview</h2>': '>🎯 Platformoversigt</h2>',
    '>🛠️ Technology Stack</h2>': '>🛠️ Teknologistak</h2>',
    '>🚀 Getting Started</h2>': '>🚀 Kom i gang</h2>',
    '>🎯 Mission & Impact</h2>': '>🎯 Mission og indvirkning</h2>',
    
    # Common card content
    '>View All Documentation →<': '>Se al dokumentation →<',
    '>Learn More →<': '>Læs mere →<',
    '>View on GitHub →<': '>Se på GitHub →<',
    
    # Ecosystem section
    'Part of the Hack23 Political Intelligence Ecosystem</h2>': 'Del af Hack23 Politisk Efterretnings-Økosystem</h2>',
    'All projects: Apache-2.0 licensed • OpenSSF Scorecard 7.0+ • SLSA Level 3 provenance • CodeQL clean':
        'Alle projekter: Apache-2.0-licenseret • OpenSSF Scorecard 7.0+ • SLSA Level 3 provenance • CodeQL ren',
    
    # CTA
    '← Back to Projects</a>': '← Tilbage til projekter</a>',
    
    # Compliance cards
    '>📋 Compliance Frameworks</h3>': '>📋 Overensstemmelsesrammer</h3>',
    '>🎯 Data Classification</h3>': '>🎯 Dataklassificering</h3>',
    '>📚 Full Documentation</h3>': '>📚 Fuld dokumentation</h3>',
    'Full alignment with ISO 27001:2022, NIST CSF 2.0, CIS Controls v8.1, GDPR (public official data), and NIS2 requirements.':
        'Fuld overensstemmelse med ISO 27001:2022, NIST CSF 2.0, CIS Controls v8.1, GDPR (offentlige officielle data) og NIS2-krav.',
    '<strong>Confidentiality:</strong> Public | <strong>Integrity:</strong> High | <strong>Availability:</strong> High. Processes only public official data from Swedish Riksdag open data sources.':
        '<strong>Fortrolighed:</strong> Offentlig | <strong>Integritet:</strong> Høj | <strong>Tilgængelighed:</strong> Høj. Behandler kun offentlige officielle data fra det svenske Riksdags åbne datakilder.',
    'Comprehensive ISMS documentation including architecture diagrams, threat models, security assessments, and CRA compliance assessment publicly available on GitHub.':
        'Omfattende ISMS-dokumentation inkl. arkitekturdiagrammer, trusselmodeller, sikkerhedsvurderinger og CRA-overensstemmelsesvurdering offentligt tilgængeligt på GitHub.',
    
    # Common use case card text
    'Make informed voting decisions based on actual parliamentary behavior, not just campaign promises. Track your representatives\' activity and accountability.':
        'Træf informerede valgbeslutninger baseret på faktisk parlamentarisk adfærd, ikke blot valgkampagneløfter. Følg dine repræsentanters aktivitet og ansvarlighed.',
    'Access comprehensive parliamentary data for investigative journalism and academic research. Evidence-based reporting on Riksdag political behavior and trends.':
        'Få adgang til omfattende parlamentariske data til undersøgende journalistik og akademisk forskning. Faktubaseret rapportering om Riksdags politiske adfærd og tendenser.',
    'Monitor specific policy areas and hold politicians accountable. Track legislative progress on issues that matter to your organization.':
        'Overvåg specifikke politikområder og hold politikere ansvarlige. Følg lovgivningsmæssige fremskridt inden for spørgsmål, der er vigtige for din organisation.',
    'Teaching tool for political science, civics education, and Swedish democratic processes. Real-world data for academic study of Riksdag operations.':
        'Undervisningsværktøj til statskundskab, samfundsfag og svenske demokratiske processer. Virkelighedsdata til akademisk studie af Riksdags funktioner.',
    
    # Security section text
    '>📋 Compliance Frameworks</h3>\n                     <p>Full alignment with ISO 27001:2022': 
        '>📋 Overensstemmelsesrammer</h3>\n                     <p>Fuld overensstemmelse med ISO 27001:2022',
    
    # Availability
    '"availability": "https://schema.org/OnlineOnly"': '"availability": "https://schema.org/OnlineOnly"',
}

# =============================================================================
# File-specific translations
# =============================================================================

RIKSDAGSMONITOR_DA = {
    # Title & Meta
    '<title>Riksdagsmonitor | AI-Powered Swedish Parliament Intelligence | Hack23</title>':
        '<title>Riksdagsmonitor | AI-drevet Svensk Parlamentsintelligens | Hack23</title>',
    'content="Riksdagsmonitor: AI-powered Swedish Parliament intelligence with 11 agentic workflows, 349 MPs, 2,494 historical politicians, 3.5M+ votes, 109,000+ documents, and 14 languages. World\'s first fully autonomous political newsroom."':
        'content="Riksdagsmonitor: AI-drevet svensk parlamentsintelligens med 11 agentiske arbejdsgange, 349 parlamentsmedlemmer, 2.494 historiske politikere, 3,5M+ stemmer, 109.000+ dokumenter og 14 sprog. Verdens første fuldt autonome politiske nyhedsrum."',
    'content="AI-powered Swedish Parliament intelligence: 11 agentic workflows, 349 MPs, 3.5M+ votes, 45-rule risk heat map. Zero human editors — fully autonomous news generation."':
        'content="AI-drevet svensk parlamentsintelligens: 11 agentiske arbejdsgange, 349 parlamentsmedlemmer, 3,5M+ stemmer, 45-regel risikovarmekort. Nul menneskelige redaktører — fuldt autonom nyhedsgenerering."',
    'content="Swedish parliament monitoring, AI political intelligence, Riksdag transparency, agentic AI newsroom, 11 workflows, 349 MPs, 3.5M votes, parliamentary analytics, open data Sweden, Swedish democracy, OSINT Sweden, autonomous news generation"':
        'content="Overvågning af det svenske parlament, AI politisk efterretning, Riksdag-gennemsigtighed, agentisk AI-nyhedsrum, 11 arbejdsgange, 349 parlamentsmedlemmer, 3,5M stemmer, parlamentarisk analyse, åbne data Sverige, svensk demokrati, OSINT Sverige, autonom nyhedsgenerering"',
    
    # OG tags
    'content="Riksdagsmonitor | AI-Powered Swedish Parliament Intelligence"':
        'content="Riksdagsmonitor | AI-drevet Svensk Parlamentsintelligens"',
    'content="World\'s first fully autonomous AI political newsroom: 11 agentic workflows, 349 MPs, 3.5M+ votes, 109,000+ documents in 14 languages."':
        'content="Verdens første fuldt autonome AI-politiske nyhedsrum: 11 agentiske arbejdsgange, 349 parlamentsmedlemmer, 3,5M+ stemmer, 109.000+ dokumenter på 14 sprog."',
    
    # Canonical
    '<link rel="canonical" href="https://hack23.com/riksdagsmonitor.html">':
        '<link rel="canonical" href="https://hack23.com/riksdagsmonitor_da.html">',
    
    # Breadcrumb
    'aria-current="page">\n                Riksdagsmonitor\n            </li>':
        'aria-current="page">\n                Riksdagsmonitor\n            </li>',
    
    # Hero section
    '<p style="font-size: 1.3rem; margin: 0.5rem 0 0; font-weight: 500;">AI-Powered Swedish Parliament Intelligence</p>':
        '<p style="font-size: 1.3rem; margin: 0.5rem 0 0; font-weight: 500;">AI-drevet Svensk Parlamentsintelligens</p>',
    'The world\'s first fully autonomous AI political newsroom for Swedish Parliament. <strong>11 agentic workflows</strong> produce deep political analysis — not shallow summaries, but structured OSINT intelligence covering 349 MPs, 2,494 historical politicians, 3.5M+ votes, and 109,000+ documents in 14 languages. Zero human editors required.':
        'Verdens første fuldt autonome AI-politiske nyhedsrum for det svenske parlament. <strong>11 agentiske arbejdsgange</strong> producerer dyb politisk analyse — ikke overfladiske resuméer, men struktureret OSINT-efterretning om 349 parlamentsmedlemmer, 2.494 historiske politikere, 3,5M+ stemmer og 109.000+ dokumenter på 14 sprog. Nul menneskelige redaktører påkrævet.',
    
    # Buttons
    '>🌐 Visit Riksdagsmonitor</a>': '>🌐 Besøg Riksdagsmonitor</a>',
    '>�� View on GitHub</a>': '>📂 Se på GitHub</a>',
    '>✨ Features</a>': '>✨ Funktioner</a>',
    '>📚 Documentation</a>': '>📚 Dokumentation</a>',
    
    # Live resources
    '>📰 <span>AI News Feed</span>': '>📰 <span>AI-nyhedsfeed</span>',
    '>🎯 <span>Political Intelligence</span>': '>🎯 <span>Politisk efterretning</span>',
    '>📊 <span>Live Dashboard</span>': '>📊 <span>Live-dashboard</span>',
    '>🗺️ <span>Sitemap</span>': '>🗺️ <span>Sitemap</span>',
    '>📡 <span>RSS Feed</span>': '>📡 <span>RSS-feed</span>',
    '>📖 <span>API JavaDocs</span>': '>📖 <span>API JavaDocs</span>',
    '>📈 <span>Code Coverage</span>': '>�� <span>Kodedækning</span>',
    '>📚 <span>DeepWiki Docs</span>': '>📚 <span>DeepWiki Dokumentation</span>',
    
    # Key Features
    '<h3>🤖 11 Agentic AI Workflows</h3>':
        '<h3>🤖 11 Agentiske AI-arbejdsgange</h3>',
    'Fully autonomous news generation with 91 skills. AI workflows produce deep political analysis including daily summaries, MP profiles, party analyses, committee reports, and Tidö coalition tracking — zero human editors in the loop.':
        'Fuldt autonom nyhedsgenerering med 91 færdigheder. AI-arbejdsgange producerer dyb politisk analyse inkl. daglige resuméer, parlamentsmedlemsprofiler, partianalyser, udvalgsrapporter og Tidö-koalitionssporing — nul menneskelige redaktører involveret.',
    
    '<h3>🗳️ 3.5M+ Vote Records</h3>':
        '<h3>🗳️ 3,5M+ Stemmejournaler</h3>',
    'Comprehensive analysis of 3.5M+ parliamentary votes with 349 current MPs and 2,494 historical politicians. Party alignment tracking, voting anomaly detection, and 45-rule × 349-MP risk heat map.':
        'Omfattende analyse af 3,5M+ parlamentariske stemmer med 349 nuværende parlamentsmedlemmer og 2.494 historiske politikere. Sporing af partitilpasning, opdagelse af stemmeanomalier og 45-regel × 349-MP risikovarmekort.',
    
    '<h3>📄 109,000+ Documents</h3>':
        '<h3>📄 109.000+ Dokumenter</h3>',
    'Full-text analysis of 109,000+ parliamentary documents including motions, interpellations, committee reports, and legislation. AI-powered summarization and cross-referencing.':
        'Fuldtekstanalyse af 109.000+ parlamentariske dokumenter inkl. forslag, interpellationer, udvalgsrapporter og lovgivning. AI-drevet resumé og krydshenvigning.',
    
    '<h3>🌍 14 Language Support</h3>':
        '<h3>🌍 14 Sprogunderstøttelse</h3>',
    'Full multi-language AI news generation supporting 14 languages (Swedish, English, Arabic, Hebrew RTL, Japanese, Korean, Chinese, and 7 European languages) for global democratic transparency.':
        'Fuld flersproget AI-nyhedsgenerering med 14 sprog (svensk, engelsk, arabisk, hebraisk RTL, japansk, koreansk, kinesisk og 7 europæiske sprog) for global demokratisk gennemsigtighed.',
    
    '<h3>📊 45-Rule Risk Heat Map</h3>':
        '<h3>📊 45-Regel Risikovarmekort</h3>',
    'Advanced political risk scoring with 45 compliance/behavior rules applied across 349 MPs. Anomaly detection, early warning system, and accountability tracking dashboards.':
        'Avanceret politisk risikoscoring med 45 overholdelse-/adfærdsregler anvendt på 349 parlamentsmedlemmer. Anomalidetektion, tidlig advarselssystem og ansvarligheds-sporings-dashboards.',
    
    '<h3>🏛️ Tidö Coalition Tracker</h3>':
        '<h3>🏛️ Tidö-koalitionssporer</h3>',
    'Specialized monitoring of the Tidö Agreement coalition dynamics, voting cohesion analysis, and policy implementation tracking for Sweden\'s current government configuration.':
        'Specialiseret overvågning af Tidö-aftalens koalitionsdynamik, analyse af stemmekohæsion og sporing af politikimplementering for Sveriges nuværende regeringskonfiguration.',
    
    # Platform Overview
    '<h3>🌟 Autonomous Political Intelligence</h3>':
        '<h3>🌟 Autonom Politisk Efterretning</h3>',
    'Disrupting parliamentary journalism with AI-generated intelligence. What used to require a team of analysts can now be done by any citizen with an AI assistant.':
        'Forstyrrer parlamentarisk journalistik med AI-genereret efterretning. Hvad der tidligere krævede et team af analytikere, kan nu udføres af enhver borger med en AI-assistent.',
    '<strong>Impact:</strong> Democratising access to political intelligence — non-partisan, open-source, architecturally designed for equal treatment of all political groups.':
        '<strong>Indvirkning:</strong> Demokratisering af adgangen til politisk efterretning — upartisk, open-source, arkitektonisk designet til ligelig behandling af alle politiske grupper.',
    
    '<h3>🔄 Built on CIA Data Backbone</h3>':
        '<h3>🔄 Bygget på CIA Data-rygrad</h3>',
    'Powered by the <a href="cia-project.html" title="Citizen Intelligence Agency">Citizen Intelligence Agency</a> — 6 analysis frameworks, 50 risk rules, 110 database views (77 politicians + 33 documents), and 4 OSINT sources with OpenSSF Scorecard 7.2/10.':
        'Drevet af <a href="cia-project.html" title="Citizen Intelligence Agency">Citizen Intelligence Agency</a> — 6 analyserammer, 50 risikoregeler, 110 databasevisninger (77 politikere + 33 dokumenter) og 4 OSINT-kilder med OpenSSF Scorecard 7.2/10.',
    '<strong>Foundation:</strong> Enterprise-grade open-source platform with SLSA Level 3 supply chain security, zero critical CVEs for 5+ years.':
        '<strong>Fundament:</strong> Enterprise-grade open-source platform med SLSA Level 3 supply chain sikkerhed, nul kritiske CVE\'er i 5+ år.',
    
    '<h3>🔍 OSINT Tradecraft Applied</h3>':
        '<h3>🔍 OSINT-metodik Anvendt</h3>',
    'Structured open-source intelligence methodology applied to public legislative data. Source verification via official Riksdag APIs, not scraped social media.':
        'Struktureret open-source efterretningsmetodologi anvendt på offentlige lovgivningsdata. Kildeverifikation via officielle Riksdag-API\'er, ikke social medie-skrabning.',
    '<strong>Trust:</strong> GDPR-by-design, public-data only, no user accounts, no ads, no tracking. Cannot be weaponised for partisan influence.':
        '<strong>Tillid:</strong> GDPR-by-design, kun offentlige data, ingen brugerkonti, ingen annoncer, ingen sporing. Kan ikke bruges som våben til partisk indflydelse.',
    
    # Platform Capabilities
    '<h3>👤 MP Profiles</h3>':
        '<h3>👤 Parlamentsmedlemsprofiler</h3>',
    'Comprehensive profiles for all Riksdag members including voting history, party affiliation, committee memberships, interpellations, and activity metrics.':
        'Omfattende profiler for alle Riksdag-medlemmer inkl. stemmehistorik, partimedlemskab, udvalgsmedlemskab, interpellationer og aktivitetsmålinger.',
    
    '<h3>🏛️ Party Analysis</h3>':
        '<h3>🏛️ Partianalyse</h3>',
    'Party-level statistics and coalition analysis. Track party cohesion, voting discipline, and strategic positioning across issues and legislative periods.':
        'Partiniveaustatistikker og koalitionsanalyse. Følg partikohæsion, stemmedisciplin og strategisk positionering på tværs af sager og lovgivningsperioder.',
    
    '<h3>📋 Committee Tracking</h3>':
        '<h3>📋 Udvalgsovervågning</h3>',
    'Follow committee work, proposals, and decisions through the legislative process. Track committee composition, activity levels, and policy influence.':
        'Følg udvalgsarbejde, forslag og beslutninger gennem lovgivningsprocessen. Spor udvalgssammensætning, aktivitetsniveauer og politisk indflydelse.',
    
    '<h3>💬 Interpellation Monitoring</h3>':
        '<h3>💬 Interpellationsovervågning</h3>',
    'Track all interpellations (parliamentary questions) to ministers with full response history. Monitor accountability mechanisms and government responsiveness.':
        'Spor alle interpellationer (parlamentariske spørgsmål) til ministre med fuld svarhistorik. Overvåg ansvarligheds-mekanismer og regeringens reaktionsevne.',
    
    '<h3>📊 Custom Reports</h3>':
        '<h3>📊 Brugerdefinerede Rapporter</h3>',
    'Generate custom reports for specific time periods, politicians, or issues. Export data for research and analysis purposes.':
        'Generer brugerdefinerede rapporter for specifikke tidsperioder, politikere eller sager. Eksportér data til forsknings- og analyseformål.',
    
    '<h3>🔗 Open Data Integration</h3>':
        '<h3>🔗 Åbne Data Integration</h3>',
    'Integration with official Swedish Riksdag open data sources. Automated updates and real-time synchronization with parliamentary systems.':
        'Integration med officielle svenske Riksdag åbne datakilder. Automatiserede opdateringer og realtidssynkronisering med parlamentariske systemer.',
    
    # Security & Quality
    'Riksdagsmonitor demonstrates enterprise security practices with 99.998% availability target, comprehensive ISMS documentation, and full compliance with ISO 27001:2022, NIST CSF 2.0, and CIS Controls v8.1.':
        'Riksdagsmonitor demonstrerer enterprise-sikkerhedspraksisser med 99,998% tilgængelighed som mål, omfattende ISMS-dokumentation og fuld overholdelse af ISO 27001:2022, NIST CSF 2.0 og CIS Controls v8.1.',
    
    # Use Cases
    '<h3>👥 Citizens &amp; Voters</h3>':
        '<h3>👥 Borgere og Vælgere</h3>',
    '<h3>📰 Journalists &amp; Researchers</h3>':
        '<h3>📰 Journalister og Forskere</h3>',
    '<h3>🏛️ Civil Society Organizations</h3>':
        '<h3>🏛️ Civilsamfundsorganisationer</h3>',
    '<h3>🎓 Educators &amp; Students</h3>':
        '<h3>🎓 Undervisere og Studerende</h3>',
    
    # Related Projects
    '<h3>🔍 Citizen Intelligence Agency</h3>\n                    <p>The foundational open-source OSINT platform for Swedish political transparency that powers Riksdagsmonitor.</p>':
        '<h3>🔍 Citizen Intelligence Agency</h3>\n                    <p>Den grundlæggende open-source OSINT-platform for svensk politisk gennemsigtighed, der driver Riksdagsmonitor.</p>',
    '<h3>🔐 CIA Compliance Manager</h3>\n                    <p>Security assessment platform demonstrating data integrity and compliance practices used in the platform.</p>':
        '<h3>🔐 CIA Compliance Manager</h3>\n                    <p>Sikkerhedsvurderingsplatform, der demonstrerer dataintegritet og overholdelsespraksisser brugt i platformen.</p>',
    '<h3>🥋 Black Trigram</h3>\n                    <p>Educational gaming project showcasing secure development practices and quality assurance methodologies.</p>':
        '<h3>🥋 Black Trigram</h3>\n                    <p>Uddannelses-spilprojekt, der viser sikre udviklingspraksisser og kvalitetssikringsmetodologier.</p>',
    
    # Ecosystem section
    'Riksdagsmonitor is powered by open-source infrastructure designed for transparency, security, and democratic accountability.':
        'Riksdagsmonitor drives af open-source infrastruktur designet til gennemsigtighed, sikkerhed og demokratisk ansvarlighed.',
    
    # CTA
    '<h2>🎯 Explore Swedish Parliamentary Data</h2>':
        '<h2>🎯 Udforsk Svenske Parlamentariske Data</h2>',
    'Access comprehensive parliamentary data and analytics for Swedish democracy. Open source platform for informed citizenship and systematic transparency.':
        'Få adgang til omfattende parlamentariske data og analyser for det svenske demokrati. Open source platform for oplyst medborgerskab og systematisk gennemsigtighed.',
    '>🌐 Visit Riksdagsmonitor</a>\n                <a href="https://github.com/Hack23/riksdagsmonitor" title="GitHub Repository" class="cta-button">📂 View on GitHub</a>':
        '>🌐 Besøg Riksdagsmonitor</a>\n                <a href="https://github.com/Hack23/riksdagsmonitor" title="GitHub Repository" class="cta-button">📂 Se på GitHub</a>',
    '>✨ Features</a>\n                <a href="projects.html"':
        '>✨ Funktioner</a>\n                <a href="projects.html"',
    
    # Language switcher - footer
    '<a href="riksdagsmonitor.html" lang="en" aria-current="page">English</a>':
        '<a href="riksdagsmonitor.html" lang="en">English</a>',
    '<a href="index_da.html" lang="da">Dansk</a>':
        '<a href="riksdagsmonitor_da.html" lang="da" aria-current="page">Dansk</a>',
}

RIKSDAGSMONITOR_FEATURES_DA = {
    # Title & Meta
    '<title>Riksdagsmonitor Features | AI-Powered Swedish Parliament Intelligence | Hack23</title>':
        '<title>Riksdagsmonitor Funktioner | AI-drevet Svensk Parlamentsintelligens | Hack23</title>',
    'content="Riksdagsmonitor features: 11 agentic AI workflows, 349 MPs, 3.5M+ votes, 109,000+ documents, 45-rule risk heat map, Tidö coalition tracker, 14 languages — world\'s first autonomous political newsroom."':
        'content="Riksdagsmonitor funktioner: 11 agentiske AI-arbejdsgange, 349 parlamentsmedlemmer, 3,5M+ stemmer, 109.000+ dokumenter, 45-regel risikovarmekort, Tidö-koalitionssporer, 14 sprog — verdens første autonome politiske nyhedsrum."',
    'content="11 agentic AI workflows, 349 MPs, 3.5M+ votes, 45-rule risk heat map — fully autonomous political newsroom."':
        'content="11 agentiske AI-arbejdsgange, 349 parlamentsmedlemmer, 3,5M+ stemmer, 45-regel risikovarmekort — fuldt autonomt politisk nyhedsrum."',
    'content="11 agentic AI workflows, 349 MPs, 3.5M+ votes, 109,000+ documents, 45-rule risk heat map. Fully autonomous political intelligence."':
        'content="11 agentiske AI-arbejdsgange, 349 parlamentsmedlemmer, 3,5M+ stemmer, 109.000+ dokumenter, 45-regel risikovarmekort. Fuldt autonom politisk efterretning."',
    'content="Riksdagsmonitor features, Swedish parliament monitoring, Riksdag transparency, MP voting records, committee activity tracking, interpellation monitoring, historical parliamentary data Sweden, multi-language parliament platform, political analytics Sweden, Swedish democracy transparency, Riksdag open data, parliamentary intelligence platform, political accountability Sweden, Swedish MP profiles, party analysis Sweden, legislative tracking Sweden, democratic transparency tools, parliamentary data visualization, Swedish political analytics, Riksdag committee monitoring"':
        'content="Riksdagsmonitor funktioner, overvågning af det svenske parlament, Riksdag-gennemsigtighed, parlamentsmedlemmers stemmeregistre, udvalgsaktivitetssporing, interpellationsovervågning, historiske parlamentariske data Sverige, flersproget parlamentsplatform, politisk analyse Sverige, svensk demokratigennemsigtighed, Riksdag åbne data, parlamentarisk efterretningsplatform, politisk ansvarlighed Sverige, svenske parlamentsmedlemsprofiler, partianalyse Sverige, lovgivningssporing Sverige, demokratiske gennemsigtighedsværktøjer, visualisering af parlamentariske data, svenske politiske analyser, Riksdag-udvalgsovervågning"',
    
    'content="Riksdagsmonitor | AI-Powered Swedish Parliament Features"':
        'content="Riksdagsmonitor | AI-drevet Svenske Parlamentsfunktioner"',
    
    '<link rel="canonical" href="https://hack23.com/riksdagsmonitor-features.html">':
        '<link rel="canonical" href="https://hack23.com/riksdagsmonitor-features_da.html">',
    '"inLanguage": "en"': '"inLanguage": "da"',
    
    # Breadcrumb
    '"name": "Riksdagsmonitor Features",': '"name": "Riksdagsmonitor Funktioner",',
    
    # Lang switcher
    '<a href="riksdagsmonitor-features.html" lang="en" aria-current="page">English</a>':
        '<a href="riksdagsmonitor-features.html" lang="en">English</a>',
    '<a href="index_da.html" lang="da">Dansk</a>':
        '<a href="riksdagsmonitor-features_da.html" lang="da" aria-current="page">Dansk</a>',
}

RIKSDAGSMONITOR_DOCS_DA = {
    '<link rel="canonical" href="https://hack23.com/riksdagsmonitor-docs.html">':
        '<link rel="canonical" href="https://hack23.com/riksdagsmonitor-docs_da.html">',
    '"inLanguage": "en"': '"inLanguage": "da"',
    
    # Lang switcher
    '<a href="riksdagsmonitor-docs.html" lang="en" aria-current="page">English</a>':
        '<a href="riksdagsmonitor-docs.html" lang="en">English</a>',
    '<a href="index_da.html" lang="da">Dansk</a>':
        '<a href="riksdagsmonitor-docs_da.html" lang="da" aria-current="page">Dansk</a>',
}

EUPARLIAMENTMONITOR_DA = {
    # Title & Meta
    '<title>EU Parliament Monitor | AI-Powered European Parliament Intelligence | Hack23</title>':
        '<title>EU Parliament Monitor | AI-drevet Europaparlamentsintelligens | Hack23</title>',
    'content="EU Parliament Monitor: AI-powered European Parliament intelligence with 8 unified gh-aw workflows, 51-artifact analysis baseline, 17 methodologies, 52 templates, 170+ daily runs in 14 languages."':
        'content="EU Parliament Monitor: AI-drevet europaparlamentsintelligens med 8 unified gh-aw arbejdsgange, 51-artefakt analysegrundlinje, 17 metodologier, 52 skabeloner, 170+ daglige kørsler på 14 sprog."',
    'content="AI-powered EU Parliament intelligence: 8 workflows, 51-artifact baseline, 17 methodologies, 170+ daily runs, 1,700+ artifacts. Powered by 62 MCP tools."':
        'content="AI-drevet EU-parlamentsintelligens: 8 arbejdsgange, 51-artefakt grundlinje, 17 metodologier, 170+ daglige kørsler, 1.700+ artefakter. Drevet af 62 MCP-værktøjer."',
    'content="EU Parliament monitor, AI political intelligence, European Parliament transparency, agentic AI newsroom, 62 MCP tools, MEP monitoring, plenary sessions, autonomous news generation, civic technology Europe"':
        'content="EU-parlamentsmonitor, AI politisk efterretning, Europaparlamentets gennemsigtighed, agentisk AI-nyhedsrum, 62 MCP-værktøjer, MEP-overvågning, plenarsamlinger, autonom nyhedsgenerering, borgerteknologi Europa"',
    
    'content="EU Parliament Monitor | AI-Powered European Parliament Intelligence"':
        'content="EU Parliament Monitor | AI-drevet Europaparlamentsintelligens"',
    'content="AI-powered EU Parliament intelligence: 8 workflows, 51-artifact baseline, 170+ daily runs, 1,700+ artifacts in 14 languages. Powered by 62 MCP tools."':
        'content="AI-drevet EU-parlamentsintelligens: 8 arbejdsgange, 51-artefakt grundlinje, 170+ daglige kørsler, 1.700+ artefakter på 14 sprog. Drevet af 62 MCP-værktøjer."',
    
    '<link rel="canonical" href="https://hack23.com/euparliamentmonitor.html">':
        '<link rel="canonical" href="https://hack23.com/euparliamentmonitor_da.html">',
    
    # Breadcrumb
    'aria-current="page">\n                EU Parliament Monitor\n            </li>':
        'aria-current="page">\n                EU Parliament Monitor\n            </li>',
    '"name": "EU Parliament Monitor",': '"name": "EU Parliament Monitor",',
    
    # Hero
    '<p style="font-size: 1.3rem; margin: 0.5rem 0 0; font-weight: 500;">AI-Powered European Parliament Intelligence</p>':
        '<p style="font-size: 1.3rem; margin: 0.5rem 0 0; font-weight: 500;">AI-drevet Europaparlamentsintelligens</p>',
    'AI-powered European Parliament Intelligence Platform with <strong>8 unified gh-aw workflows</strong> + 1 translate, producing autonomous political news in 14 languages. 51-artifact analysis baseline, 17 methodologies, 52 templates, 19 tradecraft references — 170+ daily runs generating 1,700+ artifacts. Powered by the <a href="european-parliament-mcp.html">EP MCP Server</a> (62 tools).':
        'AI-drevet Europaparlaments Intelligens-platform med <strong>8 unified gh-aw arbejdsgange</strong> + 1 oversæt, der producerer autonome politiske nyheder på 14 sprog. 51-artefakt analysegrundlinje, 17 metodologier, 52 skabeloner, 19 efterretningsreferencer — 170+ daglige kørsler der genererer 1.700+ artefakter. Drevet af <a href="european-parliament-mcp.html">EP MCP Server</a> (62 værktøjer).',
    
    # Buttons
    '>🌐 Visit Platform</a>': '>🌐 Besøg Platformen</a>',
    
    # Live Resources
    '>📰 <span>AI News Platform</span>': '>📰 <span>AI-nyhedsplatform</span>',
    '>🎯 <span>Political Intelligence</span>': '>🎯 <span>Politisk efterretning</span>',
    '>🗺️ <span>Sitemap</span>': '>🗺️ <span>Sitemap</span>',
    '>📖 <span>MCP API Docs</span>': '>📖 <span>MCP API Dokumentation</span>',
    '>📈 <span>Code Coverage</span>': '>📈 <span>Kodedækning</span>',
    '>📚 <span>DeepWiki Docs</span>': '>📚 <span>DeepWiki Dokumentation</span>',
    
    # Key Features
    '<h3>🤖 8 Unified Agentic Workflows</h3>':
        '<h3>🤖 8 Unified Agentiske Arbejdsgange</h3>',
    'Fully autonomous news generation with 8 unified gh-aw workflows + 1 translate. AI workflows produce deep political analysis including daily summaries, MEP profiles, party analyses, committee reports — zero human editors in the loop.':
        'Fuldt autonom nyhedsgenerering med 8 unified gh-aw arbejdsgange + 1 oversæt. AI-arbejdsgange producerer dyb politisk analyse inkl. daglige resuméer, MEP-profiler, partianalyser, udvalgsrapporter — nul menneskelige redaktører involveret.',
    
    '<h3>📊 51-Artifact Analysis Baseline</h3>':
        '<h3>📊 51-Artefakt Analysegrundlinje</h3>',
    'Comprehensive analysis baseline with 17 methodologies and 52 templates. Structured OSINT tradecraft with 19 tradecraft references for intelligence-grade political analysis.':
        'Omfattende analysegrundlinje med 17 metodologier og 52 skabeloner. Struktureret OSINT-efterretningsmetodik med 19 efterretningsreferencer til efterretningsgraderet politisk analyse.',
    
    '<h3>⚡ 170+ Daily Runs</h3>':
        '<h3>⚡ 170+ Daglige Kørsler</h3>',
    'High-frequency autonomous operation generating 1,700+ artifacts. Continuous monitoring of European Parliament activities with real-time news production across 14 languages.':
        'Højfrekvent autonom drift der genererer 1.700+ artefakter. Kontinuerlig overvågning af Europaparlamentets aktiviteter med realtids nyhedsproduktion på 14 sprog.',
    
    '<h3>🔌 62 MCP Tools Integration</h3>':
        '<h3>🔌 62 MCP-Værktøjer Integration</h3>',
    'Powered by the <a href="european-parliament-mcp.html">European Parliament MCP Server</a> with 62 tools (15 OSINT intelligence + 47 data access). MEP influence scoring, coalition analysis, anomaly detection.':
        'Drevet af <a href="european-parliament-mcp.html">European Parliament MCP Server</a> med 62 værktøjer (15 OSINT efterretning + 47 dataadgang). MEP indflydelsescoring, koalitionsanalyse, anomalidetektion.',
    
    '<h3>🌍 14 Language Support</h3>':
        '<h3>🌍 14 Sprogunderstøttelse</h3>',
    'Full multi-language AI news generation supporting 14 languages (English, Swedish, Arabic, Hebrew RTL, Japanese, Korean, Chinese, and 7 European languages) for global democratic transparency.':
        'Fuld flersproget AI-nyhedsgenerering med 14 sprog (engelsk, svensk, arabisk, hebraisk RTL, japansk, koreansk, kinesisk og 7 europæiske sprog) for global demokratisk gennemsigtighed.',
    
    '<h3>📄 SEO-Optimized Output</h3>':
        '<h3>📄 SEO-optimeret Output</h3>',
    'Structured news output with SEO optimization, schema.org markup, and accessibility compliance. Published directly to static site with automated deployment.':
        'Struktureret nyhedsoutput med SEO-optimering, schema.org-markup og tilgængelighed. Publiceret direkte til statisk side med automatiseret udrulning.',
    
    # Mission
    '<h3>🌟 EU Democratic Transparency</h3>':
        '<h3>🌟 EU Demokratisk Gennemsigtighed</h3>',
    'Empowering European citizens with access to EU political information and accountability data. Making EU democracy more transparent and accessible to everyone across all 27 member states.':
        'Styrker europæiske borgere med adgang til EU politisk information og ansvarligheds-data. Gør EU-demokratiet mere gennemsigtigt og tilgængeligt for alle på tværs af alle 27 medlemsstater.',
    '<strong>Impact:</strong> Increased citizen engagement in EU democratic processes through better access to European Parliament information.':
        '<strong>Indvirkning:</strong> Øget borgerinddragelse i EU demokratiske processer gennem bedre adgang til Europaparlamentets information.',
    
    '<h3>📊 Open Data Integration</h3>':
        '<h3>📊 Åbne Data Integration</h3>',
    'Built on official <a href="https://data.europarl.europa.eu/" title="European Parliament Open Data">European Parliament open data</a>. All data sourced directly from authoritative EU institutions, ensuring accuracy and reliability.':
        'Bygget på officielle <a href="https://data.europarl.europa.eu/" title="European Parliament Open Data">Europaparlamentets åbne data</a>. Alle data hentet direkte fra autoritative EU-institutioner, der sikrer nøjagtighed og pålidelighed.',
    '<strong>Impact:</strong> Trustworthy, evidence-based political intelligence for researchers, journalists, and engaged citizens.':
        '<strong>Indvirkning:</strong> Troværdig, faktabaseret politisk efterretning for forskere, journalister og engagerede borgere.',
    
    '<h3>🔍 Evidence-Based EU Politics</h3>':
        '<h3>🔍 Faktabaseret EU Politik</h3>',
    'Providing objective data for researchers, journalists, and citizens to analyze EU political behavior and hold EU representatives accountable across all legislative areas.':
        'Tilbyder objektive data for forskere, journalister og borgere til at analysere EU politisk adfærd og holde EU-repræsentanter ansvarlige på tværs af alle lovgivningsområder.',
    '<strong>Impact:</strong> More informed public discourse on EU affairs based on facts from official parliamentary records.':
        '<strong>Indvirkning:</strong> Mere oplyst offentlig diskurs om EU-anliggender baseret på fakta fra officielle parlamentariske protokoller.',
    
    # Platform Capabilities
    '<h3>👥 MEP Profiles</h3>':
        '<h3>👥 MEP-profiler</h3>',
    'Comprehensive profiles for all MEPs including voting history, party affiliation, national delegation, committee memberships, and activity metrics.':
        'Omfattende profiler for alle MEP\'er inkl. stemmehistorik, partitilknytning, national delegation, udvalgsmedlemskab og aktivitetsmålinger.',
    
    '<h3>🏛️ Political Group Analysis</h3>':
        '<h3>🏛️ Politisk Gruppeanalyse</h3>',
    'Political group-level statistics and cross-group voting analysis. Track group cohesion, voting discipline, and coalition patterns across EU legislative issues.':
        'Politisk gruppeniveaustatistikker og stemmeanalyse på tværs af grupper. Spor gruppekohæsion, stemmedisciplin og koalitionsmønstre på tværs af EU lovgivningsspørgsmål.',
    
    '<h3>📋 Legislative Tracking</h3>':
        '<h3>📋 Lovgivningssporing</h3>',
    'Follow EU legislative proposals through the full legislative process. Track first reading, second reading, amendments, committee reports, and final votes with complete history.':
        'Følg EU lovgivningsforslag gennem hele lovgivningsprocessen. Spor første behandling, anden behandling, ændringer, udvalgsrapporter og endelige afstemninger med komplet historik.',
    
    '<h3>🔎 Advanced Search</h3>':
        '<h3>🔎 Avanceret Søgning</h3>',
    'Powerful search across EU Parliament documents, votes, debates, and MEP profiles. Filter by topic, date, committee, political group, or national delegation.':
        'Kraftfuld søgning på tværs af EU Parlamentets dokumenter, afstemninger, debatter og MEP-profiler. Filtrer efter emne, dato, udvalg, politisk gruppe eller national delegation.',
    
    '<h3>📊 Voting Analytics</h3>':
        '<h3>📊 Stemmeanalyser</h3>',
    'Detailed analysis of all European Parliament votes including party alignment tracking, individual voting patterns, and cross-party coalition analysis.':
        'Detaljeret analyse af alle Europaparlamentets afstemninger inkl. sporing af partitilpasning, individuelle stemmemønstre og tværgående koalitionsanalyse.',
    
    '<h3>🌍 Multi-Language Support</h3>':
        '<h3>🌍 Flersproglig Understøttelse</h3>',
    'Access EU Parliament data across all official EU languages. The platform supports the multilingual nature of the European Parliament\'s work and documentation.':
        'Tilgå EU Parlamentets data på alle officielle EU-sprog. Platformen understøtter den flersprogede karakter af Europaparlamentets arbejde og dokumentation.',
    
    # Technology Stack
    '<h3>🌐 Frontend</h3>':
        '<h3>🌐 Frontend</h3>',
    '<strong>HTML5, CSS3, JavaScript</strong> - Modern static web application with responsive design, accessible interface, and progressive enhancement.':
        '<strong>HTML5, CSS3, JavaScript</strong> — Moderne statisk webapplikation med responsivt design, tilgængeligt interface og progressiv forbedring.',
    
    '<h3>📡 Data Source</h3>':
        '<h3>📡 Datakilde</h3>',
    '<strong>European Parliament Open Data</strong> - Official data from <a href="https://data.europarl.europa.eu/" title="EP Open Data">data.europarl.europa.eu</a>. Automated updates from authoritative EU institutional sources.':
        '<strong>Europaparlamentets åbne data</strong> — Officielle data fra <a href="https://data.europarl.europa.eu/" title="EP Open Data">data.europarl.europa.eu</a>. Automatiserede opdateringer fra autoritative EU institutionelle kilder.',
    
    '<h3>🤖 AI Integration</h3>':
        '<h3>🤖 AI Integration</h3>',
    '<strong>MCP Server Protocol</strong> - European Parliament MCP Server enables AI assistants to query and analyze EP data. Integrates with Claude, GPT, and other AI systems.':
        '<strong>MCP Server Protocol</strong> — European Parliament MCP Server giver AI-assistenter mulighed for at forespørge og analysere EP data. Integrerer med Claude, GPT og andre AI-systemer.',
    
    '<h3>🔒 Security</h3>':
        '<h3>🔒 Sikkerhed</h3>',
    '<strong>ISMS Compliant</strong> - ISO 27001:2022, NIST CSF 2.0, CIS Controls v8.1, and GDPR compliant. Fully transparent security practices with public ISMS documentation.':
        '<strong>ISMS-kompatibel</strong> — ISO 27001:2022, NIST CSF 2.0, CIS Controls v8.1 og GDPR-kompatibel. Fuldt transparent sikkerhedspraksis med offentlig ISMS-dokumentation.',
    
    # Security & Quality
    'EU Parliament Monitor demonstrates enterprise security practices for handling EU political data with integrity and transparency.':
        'EU Parliament Monitor demonstrerer enterprise-sikkerhedspraksisser til håndtering af EU politiske data med integritet og gennemsigtighed.',
    
    # ISMS Compliance
    'EU Parliament Monitor is fully compliant with Hack23\'s public Information Security Management System (ISMS) framework.':
        'EU Parliament Monitor er fuldt kompatibel med Hack23\'s offentlige Information Security Management System (ISMS) ramme.',
    
    '<h3>🏛️ ISO 27001:2022</h3>':
        '<h3>🏛️ ISO 27001:2022</h3>',
    'Information security management system aligned with international standard. Full documentation available in public ISMS repository.':
        'Informationssikkerhedsstyringssystem i overensstemmelse med international standard. Fuld dokumentation tilgængelig i det offentlige ISMS repository.',
    
    '<h3>🔵 NIST CSF 2.0</h3>':
        '<h3>🔵 NIST CSF 2.0</h3>',
    'Cybersecurity framework covering Govern, Identify, Protect, Detect, Respond, and Recover functions for comprehensive security posture.':
        'Cybersikkerhedsramme der dækker Govern, Identify, Protect, Detect, Respond og Recover funktioner for en omfattende sikkerhedsholdning.',
    
    '<h3>✅ CIS Controls v8.1</h3>':
        '<h3>✅ CIS Controls v8.1</h3>',
    'Security best practices implemented across all control domains. Evidence-based security controls mapped to project architecture.':
        'Bedste sikkerhedspraksisser implementeret på tværs af alle kontroldomæner. Faktabaserede sikkerhedskontroller mappet til projektarkitektur.',
    
    '<h3>🔒 GDPR</h3>':
        '<h3>🔒 GDPR</h3>',
    'General Data Protection Regulation compliance for handling any personal data of EU citizens. Privacy-by-design approach throughout the platform.':
        'Overholdelse af persondataforordningen ved håndtering af EU-borgernes persondata. Privacy-by-design tilgang i hele platformen.',
    
    # Related Projects
    '<h3>🤖 European Parliament MCP Server</h3>\n                    <p>AI access to European Parliament data via Model Context Protocol. Enables AI assistants like Claude to query MEPs, votes, committees, and legislative documents programmatically.</p>':
        '<h3>🤖 European Parliament MCP Server</h3>\n                    <p>AI-adgang til Europaparlamentets data via Model Context Protocol. Giver AI-assistenter som Claude mulighed for programmatisk at forespørge MEP\'er, afstemninger, udvalg og lovgivningsdokumenter.</p>',
    '<h3>🔍 Citizen Intelligence Agency</h3>\n                    <p>Swedish Parliament monitoring platform. Similar approach applied to the Swedish Riksdag for comprehensive national political transparency.</p>':
        '<h3>🔍 Citizen Intelligence Agency</h3>\n                    <p>Svensk parlamentsovervågningsplatform. Tilsvarende tilgang anvendt på det svenske Riksdag for omfattende national politisk gennemsigtighed.</p>',
    '<h3>🔐 CIA Compliance Manager</h3>\n                    <p>Security assessment platform demonstrating data integrity and compliance practices used across Hack23\'s open source projects.</p>':
        '<h3>🔐 CIA Compliance Manager</h3>\n                    <p>Sikkerhedsvurderingsplatform, der demonstrerer dataintegritet og overholdelsespraksisser brugt på tværs af Hack23\'s open source projekter.</p>',
    
    # Use Cases
    '<h3>👥 EU Citizens &amp; Voters</h3>':
        '<h3>👥 EU-borgere og Vælgere</h3>',
    'Make informed decisions about EU politics based on actual MEP behavior, not just campaign promises. Track your EU representatives\' voting activity and legislative work.':
        'Træf informerede beslutninger om EU-politik baseret på faktisk MEP-adfærd, ikke blot valgkampagneløfter. Følg dine EU-repræsentanters stemmeaktivitet og lovgivningsarbejde.',
    
    '<h3>📰 Journalists &amp; Researchers</h3>':
        '<h3>📰 Journalister og Forskere</h3>',
    'Access comprehensive EU political data for investigative journalism and academic research. Evidence-based reporting on EU Parliament activity and MEP behavior.':
        'Få adgang til omfattende EU politiske data til undersøgende journalistik og akademisk forskning. Faktabaseret rapportering om EU Parlamentets aktivitet og MEP-adfærd.',
    
    '<h3>🏛️ Civil Society Organizations</h3>':
        '<h3>🏛️ Civilsamfundsorganisationer</h3>',
    'Monitor specific EU policy areas and hold MEPs accountable. Track legislative progress on issues like climate, digital rights, or social policy.':
        'Overvåg specifikke EU-politikområder og hold MEP\'er ansvarlige. Spor lovgivningsmæssige fremskridt inden for spørgsmål som klima, digitale rettigheder eller socialpolitik.',
    
    '<h3>🎓 Educators &amp; Students</h3>':
        '<h3>🎓 Undervisere og Studerende</h3>',
    'Teaching tool for European politics, EU institutions, and democratic processes. Real-world EP data for academic study of European integration.':
        'Undervisningsværktøj til europæisk politik, EU-institutioner og demokratiske processer. Virkelighedsdata fra EP til akademisk studie af europæisk integration.',
    
    # Ecosystem
    'EU Parliament Monitor is powered by open-source infrastructure designed for transparency, security, and democratic accountability.':
        'EU Parliament Monitor drives af open-source infrastruktur designet til gennemsigtighed, sikkerhed og demokratisk ansvarlighed.',
    
    # CTA
    '<h2>🎯 Explore EU Political Transparency</h2>':
        '<h2>🎯 Udforsk EU Politisk Gennemsigtighed</h2>',
    'Access comprehensive European Parliament data and analytics. Open source platform for informed EU citizenship and democratic accountability.':
        'Få adgang til omfattende Europaparlamentariske data og analyser. Open source platform for oplyst EU-medborgerskab og demokratisk ansvarlighed.',
    
    # Language switcher
    '<a href="euparliamentmonitor.html" lang="en" aria-current="page">English</a>':
        '<a href="euparliamentmonitor.html" lang="en">English</a>',
    '<a href="index_da.html" lang="da">Dansk</a>':
        '<a href="euparliamentmonitor_da.html" lang="da" aria-current="page">Dansk</a>',
}

EUPARLIAMENTMONITOR_FEATURES_DA = {
    '<link rel="canonical" href="https://hack23.com/euparliamentmonitor-features.html">':
        '<link rel="canonical" href="https://hack23.com/euparliamentmonitor-features_da.html">',
    '"inLanguage": "en"': '"inLanguage": "da"',
    '<a href="euparliamentmonitor-features.html" lang="en" aria-current="page">English</a>':
        '<a href="euparliamentmonitor-features.html" lang="en">English</a>',
    '<a href="index_da.html" lang="da">Dansk</a>':
        '<a href="euparliamentmonitor-features_da.html" lang="da" aria-current="page">Dansk</a>',
}

EUPARLIAMENTMONITOR_DOCS_DA = {
    '<link rel="canonical" href="https://hack23.com/euparliamentmonitor-docs.html">':
        '<link rel="canonical" href="https://hack23.com/euparliamentmonitor-docs_da.html">',
    '"inLanguage": "en"': '"inLanguage": "da"',
    '<a href="euparliamentmonitor-docs.html" lang="en" aria-current="page">English</a>':
        '<a href="euparliamentmonitor-docs.html" lang="en">English</a>',
    '<a href="index_da.html" lang="da">Dansk</a>':
        '<a href="euparliamentmonitor-docs_da.html" lang="da" aria-current="page">Dansk</a>',
}

EP_MCP_DA = {
    # Title & Meta
    '<title>European Parliament MCP Server | 62 AI Tools for EU Parliament Data | Hack23</title>':
        '<title>European Parliament MCP Server | 62 AI-Værktøjer til EU Parlamentsdata | Hack23</title>',
    'content="European Parliament MCP Server: 62 MCP tools (15 OSINT intelligence + 47 data access), 9 resources, 7 prompts. 1,130+ unit tests, 71 E2E tests, 80%+ coverage. SLSA Level 3, OpenSSF Scorecard 7.2/10."':
        'content="European Parliament MCP Server: 62 MCP-værktøjer (15 OSINT efterretning + 47 dataadgang), 9 ressourcer, 7 prompter. 1.130+ enhedstests, 71 E2E-tests, 80%+ dækning. SLSA Level 3, OpenSSF Scorecard 7.2/10."',
    'content="European Parliament MCP Server: 62 tools for AI access to EU Parliament data. 1,130+ unit tests, 71 E2E, SLSA Level 3, OpenSSF Scorecard 7.2/10."':
        'content="European Parliament MCP Server: 62 værktøjer til AI-adgang til EU Parlamentsdata. 1.130+ enhedstests, 71 E2E, SLSA Level 3, OpenSSF Scorecard 7.2/10."',
    'content="European Parliament MCP server, 62 MCP tools, Model Context Protocol, EU Parliament data, AI assistant integration, OSINT intelligence, MEP influence scoring, coalition analysis, SLSA Level 3"':
        'content="European Parliament MCP server, 62 MCP-værktøjer, Model Context Protocol, EU Parlamentsdata, AI-assistent integration, OSINT efterretning, MEP indflydelsescoring, koalitionsanalyse, SLSA Level 3"',
    
    'content="European Parliament MCP Server | 62 AI Tools for EU Parliament Data"':
        'content="European Parliament MCP Server | 62 AI-Værktøjer til EU Parlamentsdata"',
    'content="62 MCP tools (15 OSINT + 47 data access), 1,130+ unit tests, 71 E2E tests, 80%+ coverage. SLSA Level 3, OpenSSF Scorecard 7.2/10."':
        'content="62 MCP-værktøjer (15 OSINT + 47 dataadgang), 1.130+ enhedstests, 71 E2E-tests, 80%+ dækning. SLSA Level 3, OpenSSF Scorecard 7.2/10."',
    
    '<link rel="canonical" href="https://hack23.com/european-parliament-mcp.html">':
        '<link rel="canonical" href="https://hack23.com/european-parliament-mcp_da.html">',
    
    # Add hreflang for da
    '<link rel="alternate" hreflang="en" href="https://hack23.com/european-parliament-mcp.html">\n    <link rel="alternate" hreflang="x-default" href="https://hack23.com/european-parliament-mcp.html">':
        '<link rel="alternate" hreflang="en" href="https://hack23.com/european-parliament-mcp.html">\n    <link rel="alternate" hreflang="da" href="https://hack23.com/european-parliament-mcp_da.html">\n    <link rel="alternate" hreflang="x-default" href="https://hack23.com/european-parliament-mcp.html">',
    
    # Breadcrumb
    '"name": "European Parliament MCP Server",': '"name": "European Parliament MCP Server",',
    
    # Hero
    '<p style="font-size: 1.3rem; margin: 0.5rem 0 0; font-weight: 500;">62 MCP Tools • 9 Resources • 7 Prompts | OpenSSF Scorecard 7.2/10</p>':
        '<p style="font-size: 1.3rem; margin: 0.5rem 0 0; font-weight: 500;">62 MCP-Værktøjer • 9 Ressourcer • 7 Prompter | OpenSSF Scorecard 7.2/10</p>',
    'TypeScript/Node.js <strong>Model Context Protocol (MCP) server</strong> powering the EU Parliament Monitor with <strong>62 MCP tools</strong> (15 OSINT intelligence + 47 data access), <strong>9 resources</strong>, and <strong>7 prompts</strong>. <strong>1,130+ unit tests, 71 E2E tests, 80%+ coverage.</strong> SLSA Level 3 supply chain security.':
        'TypeScript/Node.js <strong>Model Context Protocol (MCP) server</strong> der driver EU Parliament Monitor med <strong>62 MCP-værktøjer</strong> (15 OSINT efterretning + 47 dataadgang), <strong>9 ressourcer</strong> og <strong>7 prompter</strong>. <strong>1.130+ enhedstests, 71 E2E-tests, 80%+ dækning.</strong> SLSA Level 3 supply chain sikkerhed.',
    
    # Buttons
    '>📦 npm Package</a>': '>📦 npm-pakke</a>',
    
    # Live Resources
    '>📦 <span>npm Package</span>': '>📦 <span>npm-pakke</span>',
    '>📂 <span>GitHub Repo</span>': '>📂 <span>GitHub Repo</span>',
    '>📖 <span>TypeDoc API</span>': '>📖 <span>TypeDoc API</span>',
    '>📈 <span>Code Coverage</span>': '>📈 <span>Kodedækning</span>',
    '>🎭 <span>E2E Report</span>': '>🎭 <span>E2E Rapport</span>',
    '>📚 <span>DeepWiki Docs</span>': '>📚 <span>DeepWiki Dokumentation</span>',
    
    # Key Features
    '<h3>🔌 62 MCP Tools</h3>':
        '<h3>🔌 62 MCP-Værktøjer</h3>',
    '<strong>15 OSINT intelligence tools</strong> (MEP influence scoring, coalition analysis, voting patterns) + <strong>47 data access tools</strong> for Claude, ChatGPT, and all MCP-compatible AI assistants.':
        '<strong>15 OSINT efterretningsværktøjer</strong> (MEP indflydelsescoring, koalitionsanalyse, stemmemønstre) + <strong>47 dataadgangsværktøjer</strong> til Claude, ChatGPT og alle MCP-kompatible AI-assistenter.',
    
    '<h3>🏛️ EU Parliament Data Access</h3>':
        '<h3>🏛️ EU Parlamentsdata Adgang</h3>',
    'Direct access to <strong>MEP profiles, plenary sessions, voting records, committee information, and parliamentary questions</strong> via the official European Parliament Open Data API.':
        'Direkte adgang til <strong>MEP-profiler, plenarsamlinger, afstemningsregistre, udvalgsinformation og parlamentariske spørgsmål</strong> via den officielle European Parliament Open Data API.',
    
    '<h3>📘 TypeScript & Zod Validation</h3>':
        '<h3>�� TypeScript og Zod-validering</h3>',
    'Written in <strong>TypeScript</strong> with strict type safety and <strong>Zod schema validation</strong> for all API inputs and outputs. Rate limiting and security headers included out of the box.':
        'Skrevet i <strong>TypeScript</strong> med streng type-sikkerhed og <strong>Zod schema-validering</strong> for alle API input og output. Rate limiting og sikkerhedsheadere inkluderet som standard.',
    
    '<h3>🛡️ SLSA Level 3 Security</h3>':
        '<h3>🛡️ SLSA Level 3 Sikkerhed</h3>',
    'Supply chain security with <strong>SLSA Level 3</strong> build provenance attestations, OpenSSF Scorecard validation, and comprehensive security scanning via GitHub Actions.':
        'Supply chain sikkerhed med <strong>SLSA Level 3</strong> build provenance attestationer, OpenSSF Scorecard validering og omfattende sikkerhedsscanning via GitHub Actions.',
    
    '<h3>🧪 1,130+ Unit Tests</h3>':
        '<h3>🧪 1.130+ Enhedstests</h3>',
    '<strong>1,130+ unit tests</strong> and <strong>71 E2E tests</strong> maintaining 80%+ code coverage. Automated CI/CD pipeline with SLSA Level 3 provenance attestations and quality gates.':
        '<strong>1.130+ enhedstests</strong> og <strong>71 E2E-tests</strong> der opretholder 80%+ kodedækning. Automatiseret CI/CD pipeline med SLSA Level 3 provenance attestationer og kvalitetsgates.',
    
    '<h3>🔒 OpenSSF Scorecard 7.2/10</h3>':
        '<h3>🔒 OpenSSF Scorecard 7.2/10</h3>',
    'Fully aligned with <strong>ISO 27001:2022, NIST CSF 2.0, CIS Controls v8.1, and GDPR</strong>. OpenSSF Scorecard <strong>7.2/10</strong>, SLSA Level 3, complete ISMS documentation.':
        'Fuldt i overensstemmelse med <strong>ISO 27001:2022, NIST CSF 2.0, CIS Controls v8.1 og GDPR</strong>. OpenSSF Scorecard <strong>7.2/10</strong>, SLSA Level 3, komplet ISMS dokumentation.',
    
    # MCP Tools section
    '<h2>🔧 Featured MCP Tools (62 Total)</h2>':
        '<h2>🔧 Udvalgte MCP-Værktøjer (62 i alt)</h2>',
    '<strong>15 OSINT intelligence tools</strong> for deep political analysis + <strong>47 data access tools</strong> for comprehensive EU Parliament data. Here are some highlights:':
        '<strong>15 OSINT efterretningsværktøjer</strong> til dyb politisk analyse + <strong>47 dataadgangsværktøjer</strong> til omfattende EU Parlamentsdata. Her er nogle højdepunkter:',
    
    '<h3>👤 get_meps</h3>':
        '<h3>👤 get_meps</h3>',
    'Retrieve <strong>Member of European Parliament (MEP)</strong> profiles with filtering by country, political group, and committee membership.':
        'Hent <strong>Europaparlamentets MEP</strong>-profiler med filtrering efter land, politisk gruppe og udvalgsmedlemskab.',
    
    '<h3>📅 get_plenary_sessions</h3>':
        '<h3>📅 get_plenary_sessions</h3>',
    'Access <strong>plenary session</strong> records, agendas, and proceedings with date-range filtering.':
        'Tilgå <strong>plenarsamlings</strong>-registre, dagsordener og forhandlinger med datointervalfiltrering.',
    
    '<h3>🗳️ get_voting_records</h3>':
        '<h3>🗳️ get_voting_records</h3>',
    'Query detailed <strong>voting records</strong> including individual MEP votes, vote summaries, and legislative context.':
        'Forespørg detaljerede <strong>afstemningsregistre</strong> inkl. individuelle MEP-stemmer, stemmeresumeer og lovgivningsmæssig kontekst.',
    
    '<h3>🔍 search_documents</h3>':
        '<h3>🔍 search_documents</h3>',
    'Full-text search across <strong>parliamentary documents</strong>, reports, opinions, and legislative texts.':
        'Fuldtekstsøgning på tværs af <strong>parlamentariske dokumenter</strong>, rapporter, udtalelser og lovgivningstekster.',
    
    '<h3>🏛️ get_committee_info</h3>':
        '<h3>🏛️ get_committee_info</h3>',
    'Access <strong>committee structures</strong>, membership, mandates, and recent activities.':
        'Tilgå <strong>udvalgsstrukturer</strong>, medlemskab, mandater og seneste aktiviteter.',
    
    '<h3>❓ get_parliamentary_questions</h3>':
        '<h3>❓ get_parliamentary_questions</h3>',
    'Retrieve <strong>parliamentary questions</strong> with answers from MEPs and the European Commission.':
        'Hent <strong>parlamentariske spørgsmål</strong> med svar fra MEP\'er og Europa-Kommissionen.',
    
    '<h3>📊 analyze_voting_patterns</h3>':
        '<h3>📊 analyze_voting_patterns</h3>',
    '<strong>Analyze voting patterns</strong> across political groups, countries, and legislative topics for deeper political intelligence.':
        '<strong>Analyser stemmemønstre</strong> på tværs af politiske grupper, lande og lovgivningsemner for dybere politisk efterretning.',
    
    '<h3>📋 track_legislation</h3>':
        '<h3>📋 track_legislation</h3>',
    '<strong>Track legislative procedures</strong> from proposal through committee review to final vote.':
        '<strong>Spor lovgivningsprocedurer</strong> fra forslag gennem udvalgsgennemgang til endelig afstemning.',
    
    '<h3>📄 generate_report</h3>':
        '<h3>📄 generate_report</h3>',
    'Generate structured <strong>AI-ready reports</strong> on parliamentary activity, voting summaries, and MEP profiles.':
        'Generer strukturerede <strong>AI-klare rapporter</strong> om parlamentarisk aktivitet, stemmeresumeer og MEP-profiler.',
    
    # Data Sources
    '<h3>🇪�� MEPs & Representatives</h3>':
        '<h3>🇪🇺 MEP\'er og Repræsentanter</h3>',
    'Complete profiles of all Members of the European Parliament including political group, country, committees, and contact information sourced from the official EU Parliament Open Data API.':
        'Komplette profiler for alle Europaparlamentets medlemmer inkl. politisk gruppe, land, udvalg og kontaktinformation hentet fra den officielle EU Parlamentets Open Data API.',
    
    '<h3>🏛️ Plenary Sessions</h3>':
        '<h3>🏛️ Plenarsamlinger</h3>',
    'Full plenary session records including agendas, debate transcripts, and outcomes from the European Parliament\'s open data portal.':
        'Komplette plenarsamlingsregistre inkl. dagsordener, debatudskrifter og resultater fra Europaparlamentets åbne dataportal.',
    
    '<h3>📁 Committees & Documents</h3>':
        '<h3>📁 Udvalg og Dokumenter</h3>',
    'Committee membership, reports, and opinions alongside the full parliamentary document repository for research and analysis.':
        'Udvalgsmedlemskab, rapporter og udtalelser sammen med det komplette parlamentariske dokumentlager til forskning og analyse.',
    
    '<h3>❓ Parliamentary Questions</h3>':
        '<h3>❓ Parlamentariske Spørgsmål</h3>',
    'Written and oral questions submitted by MEPs with official Commission and Council responses, enabling accountability tracking.':
        'Skriftlige og mundtlige spørgsmål indsendt af MEP\'er med officielle Kommissions- og Rådsvar, der muliggør ansvarlighedssporing.',
    
    # Technology Stack
    '<h3>💻 Runtime</h3>':
        '<h3>💻 Runtime</h3>',
    '<strong>TypeScript/Node.js</strong> — Type-safe implementation with full ES module support. Published to npm as <code>european-parliament-mcp-server</code>.':
        '<strong>TypeScript/Node.js</strong> — Type-sikker implementering med fuld ES module understøttelse. Publiceret til npm som <code>european-parliament-mcp-server</code>.',
    
    '<h3>📦 Protocol</h3>':
        '<h3>📦 Protokol</h3>',
    '<strong>Model Context Protocol (MCP)</strong> — Standard protocol for AI assistant integrations. Compatible with Claude, ChatGPT, and any MCP-compatible AI client.':
        '<strong>Model Context Protocol (MCP)</strong> — Standardprotokol til AI-assistent integrationer. Kompatibel med Claude, ChatGPT og enhver MCP-kompatibel AI-klient.',
    
    '<strong>SLSA Level 3</strong> — Supply chain security with build provenance, reproducible builds, and security scanning. OpenSSF Scorecard validated. Rate limiting and Zod input validation.':
        '<strong>SLSA Level 3</strong> — Supply chain sikkerhed med build provenance, reproducerbare builds og sikkerhedsscanning. OpenSSF Scorecard valideret. Rate limiting og Zod inputvalidering.',
    
    # Security & Quality
    'European Parliament MCP Server demonstrates enterprise-grade security practices for AI integration middleware.':
        'European Parliament MCP Server demonstrerer enterprise-grade sikkerhedspraksisser til AI integration middleware.',
    
    # Getting Started
    '<h3>1️⃣ Install via npm</h3>':
        '<h3>1️⃣ Installér via npm</h3>',
    'Install the package globally or as a project dependency. Requires Node.js 18+ and an MCP-compatible AI client.':
        'Installér pakken globalt eller som projektafhængighed. Kræver Node.js 18+ og en MCP-kompatibel AI-klient.',
    '>📦 View on npm</a>': '>📦 Se på npm</a>',
    
    '<h3>2️⃣ Configure AI Client</h3>':
        '<h3>2️⃣ Konfigurér AI-klient</h3>',
    'Add the MCP server to your AI client configuration (Claude Desktop, Continue, or any MCP-compatible client) to enable EU Parliament data queries.':
        'Tilføj MCP-serveren til din AI-klientkonfiguration (Claude Desktop, Continue eller enhver MCP-kompatibel klient) for at aktivere EU Parlamentsdata-forespørgsler.',
    '>📖 Installation Guide</a>': '>📖 Installationsguide</a>',
    
    '<h3>3️⃣ Query Parliament Data</h3>':
        '<h3>3️⃣ Forespørg Parlamentsdata</h3>',
    'Use natural language to query MEP profiles, voting records, plenary sessions, and more through your AI assistant. Fork and extend for custom workflows.':
        'Brug naturligt sprog til at forespørge MEP-profiler, afstemningsregistre, plenarsamlinger og mere gennem din AI-assistent. Fork og udvid til brugerdefinerede arbejdsgange.',
    
    # Use Cases
    '<h3>🔍 Political Research</h3>':
        '<h3>🔍 Politisk Forskning</h3>',
    'Academic and journalistic research on MEP voting patterns, political group alignment, and legislative activity using AI-powered analysis.':
        'Akademisk og journalistisk forskning i MEP-stemmemønstre, politisk gruppepositionering og lovgivningsaktivitet ved hjælp af AI-drevet analyse.',
    
    '<h3>📊 Transparency & Accountability</h3>':
        '<h3>📊 Gennemsigtighed og Ansvarlighed</h3>',
    'Track MEP performance, attendance, and voting consistency to hold representatives accountable to their constituents and campaign promises.':
        'Spor MEP-præstation, fremmøde og stemningskonsistens for at holde repræsentanter ansvarlige over for deres valgkreds og valgkampagneløfter.',
    
    '<h3>🏢 Policy Analysis</h3>':
        '<h3>🏢 Politikanalyse</h3>',
    'Monitor legislative developments, committee activity, and policy trends relevant to specific industries or interest areas.':
        'Overvåg lovgivningsmæssig udvikling, udvalgsaktivitet og politiktendenser relevant for specifikke brancher eller interesseområder.',
    
    '<h3>🎓 Education</h3>':
        '<h3>🎓 Uddannelse</h3>',
    'Teaching tool for European politics courses, demonstrating how open government data can be democratized through AI integration.':
        'Undervisningsværktøj til europæiske politikkurser, der demonstrerer, hvordan åbne offentlige data kan demokratiseres gennem AI integration.',
    
    # Related Projects
    '<h3>🔍 Citizen Intelligence Agency</h3>\n                    <p>Political transparency platform for Swedish parliamentary data, demonstrating data integrity and availability best practices at scale.</p>':
        '<h3>🔍 Citizen Intelligence Agency</h3>\n                    <p>Politisk gennemsigtighedsplatform til svenske parlamentariske data, der demonstrerer dataintegritet og tilgængelighed bedste praksisser i stor skala.</p>',
    '<h3>🔐 CIA Compliance Manager</h3>\n                    <p>Enterprise security assessment platform for the CIA triad with multi-framework compliance mapping and automated reporting.</p>':
        '<h3>🔐 CIA Compliance Manager</h3>\n                    <p>Enterprise sikkerhedsvurderingsplatform til CIA triaden med multi-ramme overensstemmelsesmapping og automatiseret rapportering.</p>',
    '<h3>🥋 Black Trigram</h3>\n                    <p>Educational gaming project showcasing secure software development lifecycle and quality assurance practices.</p>':
        '<h3>🥋 Black Trigram</h3>\n                    <p>Uddannelses-spilprojekt der viser sikker softwareudviklings livscyklus og kvalitetssikringspraksisser.</p>',
    
    # Ecosystem
    'EP MCP Server powers AI assistants with structured access to European Parliament data for the broader political intelligence ecosystem.':
        'EP MCP Server giver AI-assistenter struktureret adgang til Europaparlamentets data til det bredere politiske efterretningsøkosystem.',
    
    # CTA
    '<h2>🎯 Ready to Explore EU Parliament Data?</h2>':
        '<h2>🎯 Klar til at Udforske EU Parlamentsdata?</h2>',
    'Integrate AI-powered access to European Parliament open datasets into your research, journalism, or policy analysis workflow.':
        'Integrer AI-drevet adgang til Europaparlamentets åbne datasæt i din forsknings-, journalistik- eller politikanalyseworkflow.',
    
    # Language switcher
    '<a href="european-parliament-mcp.html" lang="en" aria-current="page">English</a>':
        '<a href="european-parliament-mcp.html" lang="en">English</a>',
    '<a href="index_da.html" lang="da">Dansk</a>':
        '<a href="european-parliament-mcp_da.html" lang="da" aria-current="page">Dansk</a>',
}

EP_MCP_FEATURES_DA = {
    '<link rel="canonical" href="https://hack23.com/european-parliament-mcp-features.html">':
        '<link rel="canonical" href="https://hack23.com/european-parliament-mcp-features_da.html">',
    '"inLanguage": "en"': '"inLanguage": "da"',
    '<a href="european-parliament-mcp-features.html" lang="en" aria-current="page">English</a>':
        '<a href="european-parliament-mcp-features.html" lang="en">English</a>',
    '<a href="index_da.html" lang="da">Dansk</a>':
        '<a href="european-parliament-mcp-features_da.html" lang="da" aria-current="page">Dansk</a>',
}

EP_MCP_DOCS_DA = {
    '<link rel="canonical" href="https://hack23.com/european-parliament-mcp-docs.html">':
        '<link rel="canonical" href="https://hack23.com/european-parliament-mcp-docs_da.html">',
    '"inLanguage": "en"': '"inLanguage": "da"',
    '<a href="european-parliament-mcp-docs.html" lang="en" aria-current="page">English</a>':
        '<a href="european-parliament-mcp-docs.html" lang="en">English</a>',
    '<a href="index_da.html" lang="da">Dansk</a>':
        '<a href="european-parliament-mcp-docs_da.html" lang="da" aria-current="page">Dansk</a>',
}

# =============================================================================
# Translation functions
# =============================================================================

def apply_translations(content, *translation_dicts):
    """Apply multiple translation dictionaries to content."""
    for td in translation_dicts:
        for src, dst in td.items():
            content = content.replace(src, dst)
    return content

def generate_file(src_path, dst_path, *extra_dicts):
    """Read source, apply translations, write destination."""
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = apply_translations(content, COMMON_DA, *extra_dicts)
    
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {dst_path}")

# =============================================================================
# Generate all 9 files
# =============================================================================

BASE = '/home/runner/work/homepage/homepage'

generate_file(
    f'{BASE}/riksdagsmonitor.html',
    f'{BASE}/riksdagsmonitor_da.html',
    RIKSDAGSMONITOR_DA
)

generate_file(
    f'{BASE}/riksdagsmonitor-features.html',
    f'{BASE}/riksdagsmonitor-features_da.html',
    RIKSDAGSMONITOR_FEATURES_DA
)

generate_file(
    f'{BASE}/riksdagsmonitor-docs.html',
    f'{BASE}/riksdagsmonitor-docs_da.html',
    RIKSDAGSMONITOR_DOCS_DA
)

generate_file(
    f'{BASE}/euparliamentmonitor.html',
    f'{BASE}/euparliamentmonitor_da.html',
    EUPARLIAMENTMONITOR_DA
)

generate_file(
    f'{BASE}/euparliamentmonitor-features.html',
    f'{BASE}/euparliamentmonitor-features_da.html',
    EUPARLIAMENTMONITOR_FEATURES_DA
)

generate_file(
    f'{BASE}/euparliamentmonitor-docs.html',
    f'{BASE}/euparliamentmonitor-docs_da.html',
    EUPARLIAMENTMONITOR_DOCS_DA
)

generate_file(
    f'{BASE}/european-parliament-mcp.html',
    f'{BASE}/european-parliament-mcp_da.html',
    EP_MCP_DA
)

generate_file(
    f'{BASE}/european-parliament-mcp-features.html',
    f'{BASE}/european-parliament-mcp-features_da.html',
    EP_MCP_FEATURES_DA
)

generate_file(
    f'{BASE}/european-parliament-mcp-docs.html',
    f'{BASE}/european-parliament-mcp-docs_da.html',
    EP_MCP_DOCS_DA
)

print("\nAll 9 Danish translation files created successfully!")
