# 🇯🇵 Japanese (ja) Translation Guide

**Version 6.0 - Expanded Hack23 Edition**  
*Last Updated: January 2026*

---

## 📋 Quick Reference

| Attribute | Value |
|-----------|-------|
| **Language Code** | `ja` |
| **Locale** | `ja_JP` |
| **Text Direction** | LTR (Left-to-Right) → |
| **Currency** | JPY (¥) |
| **Date Format** | `YYYY年MM月DD日` or `2026年1月1日` |
| **Scripts** | Kanji (漢字), Hiragana (ひらがな), Katakana (カタカナ) |

---

## 🔄 Visual Translation Workflow

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph LR
    A[ファイル選択] --> B[用語確認]
    B --> C[コンテンツ翻訳]
    C --> D[品質検証]
    D --> E{承認?}
    E -->|はい| F[公開]
    E -->|いいえ| C

    classDef default fill:#e3f2fd,stroke:#1565C0,stroke-width:2px,color:#1a1a2e
    classDef primary fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#ffffff
    classDef success fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff
    classDef warning fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#ffffff
    classDef danger fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#ffffff
    classDef info fill:#455A64,stroke:#263238,stroke-width:2px,color:#ffffff
```

## 🔄 Quality Standards Pyramid

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#2196F3", "primaryTextColor": "#1a1a2e", "lineColor": "#455A64", "secondaryColor": "#e8f5e9", "tertiaryColor": "#fff8e1", "primaryBorderColor": "#1565C0"}}}%%
graph TD
    L1[基盤: 技術的正確性]
    L2[中間: 文法と流暢さ]
    L3[頂点: 文化的適合性]
    L1 --> L2 --> L3

    classDef default fill:#e3f2fd,stroke:#1565C0,stroke-width:2px,color:#1a1a2e
    classDef primary fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#ffffff
    classDef success fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff
    classDef warning fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#ffffff
    classDef danger fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#ffffff
    classDef info fill:#455A64,stroke:#263238,stroke-width:2px,color:#ffffff
```

---

## 📚 Comprehensive Vocabulary Reference

### 🔥 Brand & Key Entities (Never Translate)

| English | Japanese | Notes |
|---------|----------|-------|
| Hack23 | Hack23 | Company name – never translate |
| Hack23 AB | Hack23 AB | Swedish company designation |
| Citizen Intelligence Agency | Citizen Intelligence Agency | Project name – keep English |
| CIA Compliance Manager | CIA Compliance Manager | Product name – keep English |
| Black Trigram | Black Trigram / ブラックトライグラム | Game product |
| 흑괘 | 흑괘 (黒卦) | Korean name for Black Trigram |
| 黑卦 | 黒卦 | Chinese name for Black Trigram |
| James Pether Sörling | James Pether Sörling | Founder name |
| CISSP | CISSP | Certification |
| CISM | CISM | Certification |
| GitHub | GitHub | Platform name |
| LinkedIn | LinkedIn | Platform name |
| OpenSSF | OpenSSF | Open Source Security Foundation |
| CII Best Practices | CII Best Practices | Badge name |
| Riksdag | Riksdag | Swedish Parliament |

### 👔 Job Titles & Professional Roles

| English | Japanese | Notes |
|---------|----------|-------|
| CEO / Chief Executive Officer | CEO / 最高経営責任者 | |
| Founder | 創業者 | |
| CEO/Founder | CEO/創業者 | |
| Application Security Officer | アプリケーションセキュリティ責任者 | |
| Information Security Officer | 情報セキュリティ責任者 | |
| Senior Security Architect | シニアセキュリティアーキテクト | |
| Cloud Architect | クラウドアーキテクト | |
| Security Consultant | セキュリティコンサルタント | |
| CISO | CISO | Chief Information Security Officer |
| Compliance Officer | コンプライアンス責任者 | |
| Risk Manager | リスクマネージャー | |
| IT Security Manager | ITセキュリティマネージャー | |
| Security Auditor | セキュリティ監査人 | |
| Taekwondo Instructor | テコンドーインストラクター | |
| System Developer | システム開発者 | |
| Software Engineer | ソフトウェアエンジニア | |
| J2EE Developer | J2EE開発者 | |
| Unix Helpdesk | Unixヘルプデスク | |
| Teaching Assistant | ティーチングアシスタント | |
| NBC Defence Group Leader | NBC防護グループリーダー | Military role |

### 🏢 Hack23 Business & Services

| English | Japanese | Notes |
|---------|----------|-------|
| Cybersecurity Consulting Sweden | スウェーデンのサイバーセキュリティコンサルティング | Main tagline |
| Public ISMS | 公開ISMS | Core differentiator |
| Open ISMS Transparency | オープンISMS透明性 | |
| Security Architecture & Strategy | セキュリティアーキテクチャと戦略 | Service line |
| Cloud Security & DevSecOps | クラウドセキュリティとDevSecOps | Service line |
| Secure Development & Code Quality | セキュア開発とコード品質 | Service line |
| Compliance & Regulatory | コンプライアンスと規制 | Service line |
| Open Source Security | オープンソースセキュリティ | Service line |
| Security Culture & Training | セキュリティ文化とトレーニング | Service line |
| Full-Stack Security | フルスタックセキュリティ | |
| Current Practitioner | 現役プラクティショナー | Value proposition |
| Transparent Security | 透明性のあるセキュリティ | |
| Developer-Friendly Security | 開発者フレンドリーなセキュリティ | |
| Security Excellence Through Transparency | 透明性によるセキュリティエクセレンス | |
| OSPO | OSPO | Open Source Program Office |
| Gothenburg | ヨーテボリ | City in Sweden |
| Sweden | スウェーデン | |
| Nordic Region | 北欧地域 | |
| Europe | ヨーロッパ | |
| Singapore | シンガポール | |
| ASEAN Region | ASEAN地域 | |

### 🎮 Black Trigram Game Vocabulary

| English | Japanese | Notes |
|---------|----------|-------|
| Precision Combat Simulator | 精密戦闘シミュレーター | |
| Vital Points | 急所 | |
| 70 Anatomical Vital Points | 70の解剖学的急所 | |
| 70 Techniques | 70の技 | |
| Fighter Archetypes | 戦闘アーキタイプ | |
| Musa (Warrior) | 武士（戦士） | |
| Amsalja (Assassin) | 暗殺者 | |
| Hacker | ハッカー | |
| Jeongbo (Intelligence) | 情報員 | |
| Jojik (Organization) | 組織 | |
| Korean Martial Arts | 韓国武術 | |
| Taekkyeon | テッキョン | Korean martial art |
| Hapkido | ハプキドー | Korean martial art |
| Taekwondo | テコンドー | Korean martial art |
| Song Moo Kwan | 松武館 | Taekwondo school |
| Kukkiwon | 国技院 | World Taekwondo HQ |
| Black Belt | 黒帯 | |
| 3rd Dan | 三段 | Rank |
| Cultural Preservation | 文化保存 | |
| Educational Gaming | 教育ゲーム | |
| Unity Game | Unityゲーム | |
| Steam | Steam | Platform name |
| itch.io | itch.io | Platform name |
| Fighting | 格闘 | Game genre |
| Simulation | シミュレーション | Game genre |
| Educational | 教育的 | Game genre |
| Cultural | 文化的 | Game genre |
| Single-player | シングルプレイヤー | |
| Multiplayer | マルチプレイヤー | |
| Teen | 青少年向け | Content rating |
| Cross-platform | クロスプラットフォーム | |
| Open Source Game | オープンソースゲーム | |

### 🔍 Citizen Intelligence Agency Vocabulary

| English | Japanese | Notes |
|---------|----------|-------|
| Political Transparency | 政治的透明性 | |
| Political Intelligence Platform | 政治インテリジェンスプラットフォーム | |
| OSINT Platform | OSINTプラットフォーム | |
| Parliamentary Monitoring | 議会モニタリング | |
| Swedish Parliament Monitoring (Riksdag) | スウェーデン議会（リクスダーグ）モニタリング | |
| Political Decision Tracking | 政治的意思決定追跡 | |
| Governance Metrics & Rankings | ガバナンス指標とランキング | |
| Democratic Accountability Analysis | 民主的説明責任分析 | |
| Voting Records | 投票記録 | |
| Voting Pattern Analysis | 投票パターン分析 | |
| Party Performance Metrics | 政党パフォーマンス指標 | |
| Minister Activity Tracking | 大臣活動追跡 | |
| Committee Work Analysis | 委員会作業分析 | |
| Political Trend Visualization | 政治トレンド可視化 | |
| Open Data Integration | オープンデータ統合 | |
| World Bank | 世界銀行 | |
| Swedish Government | スウェーデン政府 | |
| Accountability Metrics | 説明責任指標 | |
| Open Data | オープンデータ | |
| Civic Technology | シビックテック | |
| Swedish Parliament | スウェーデン議会 | |
| Data Visualization | データ可視化 | |
| Political Analytics | 政治分析 | |
| Citizens | 市民 | Audience |
| Journalists | ジャーナリスト | Audience |
| Researchers | 研究者 | Audience |
| Policy Analysts | 政策アナリスト | Audience |
| Political Scientists | 政治学者 | Audience |
| Democracy Advocates | 民主主義提唱者 | Audience |
| Parliamentary Process Analysis | 議会プロセス分析 | |
| OSINT Methodology | OSINT方法論 | |
| Swedish Governance System | スウェーデン統治システム | |
| Data-Driven Political Analysis | データ駆動型政治分析 | |
| Open Government Data Usage | オープンガバメントデータ活用 | |

### 🔐 CIA Compliance Manager Vocabulary

| English | Japanese | Notes |
|---------|----------|-------|
| Security Assessment Platform | セキュリティ評価プラットフォーム | |
| Enterprise Security Management | エンタープライズセキュリティ管理 | |
| CIA Triad Assessment | CIAトライアド評価 | |
| Business Impact Analysis | ビジネスインパクト分析 | |
| Multi-Framework Compliance | マルチフレームワークコンプライアンス | |
| STRIDE Analysis | STRIDE分析 | Threat model |
| Threat Modeling | 脅威モデリング | |
| Evidence Collection | 証拠収集 | |
| Automated Compliance Reporting | 自動コンプライアンスレポート | |
| Risk Register | リスク登録簿 | |
| Controls Monitoring | コントロール監視 | |
| CRA Assessment | CRA評価 | Cyber Resilience Act |
| Security Level Selection | セキュリティレベル選択 | |
| Cost Estimation | コスト見積もり | |
| Implementation Guidance | 実装ガイダンス | |
| Gap Analysis | ギャップ分析 | |
| Security Visualization | セキュリティ可視化 | |
| Widget-Based Dashboard | ウィジェットベースダッシュボード | |
| Availability Impact Analysis | 可用性影響分析 | |
| Integrity Impact Analysis | 完全性影響分析 | |
| Confidentiality Impact Analysis | 機密性影響分析 | |
| Open Source Security Tool | オープンソースセキュリティツール | |

### 🎓 Education & Learning Terms

| English | Japanese | Notes |
|---------|----------|-------|
| Educational Use | 教育利用 | |
| Self-Directed Learning | 自己学習 | |
| Skill Development | スキル開発 | |
| Professional Development | 専門能力開発 | |
| Teaches | 教える | Schema.org property |
| Accessibility Features | アクセシビリティ機能 | |
| Keyboard Navigation | キーボードナビゲーション | |
| High Contrast Mode | ハイコントラストモード | |
| Closed Captions | 字幕 | |
| Screen Reader Compatible | スクリーンリーダー対応 | |

### 🍎 Discordian Philosophy & ISMS Blog

| English | Japanese | Notes |
|---------|----------|-------|
| Think for Yourself | 自分で考えろ | Core motto |
| Question Authority | 権威を疑え | |
| FNORD | FNORD | Never translate |
| Nothing is True | 何も真実ではない | |
| Everything is Permitted | すべては許される | |
| Security Theater | セキュリティ劇場 | Fake security |
| Radical Transparency | 徹底的な透明性 | |
| Chapel Perilous | 危険な礼拝堂 | Keep English or translate |
| Operation Mindfuck | Operation Mindfuck | Keep English |
| Illuminatus Trilogy | イルミナティ三部作 | |
| Eris | エリス | Goddess of Chaos |
| Discordia | ディスコルディア | |
| Law of Fives | 5の法則 | |
| Sacred Geometry | 神聖幾何学 | |
| Five-Layer Architecture | 5層アーキテクチャ | |
| Nation-State Surveillance | 国家監視 | |
| Crypto Backdoors | 暗号バックドア | |
| Security Through Obscurity | 隠蔽によるセキュリティ | Anti-pattern |
| Information Hoarding | 情報の囲い込み | |
| Knowledge Transparency | 知識の透明性 | |
| Simon Moon | サイモン・ムーン | Character reference |
| Hagbard Celine | ハグバード・セリーヌ | Character reference |
| George Dorn | ジョージ・ドーン | Character reference |

### 🧭 Navigation & UI Elements

| English | Japanese |
|---------|----------|
| Home | ホーム |
| About Us | 会社概要 |
| Services | サービス |
| Products | 製品 |
| Projects | プロジェクト |
| Contact | お問い合わせ |
| Blog | ブログ |
| Search | 検索 |
| Menu | メニュー |
| Close | 閉じる |
| Back | 戻る |
| Next | 次へ |
| Previous | 前へ |
| Submit | 送信 |
| Cancel | キャンセル |
| **Expand All** | **すべて展開** |
| **Collapse All** | **すべて折りたたむ** |
| Download | ダウンロード |
| Read More | 続きを読む |
| View Details | 詳細を見る |
| Privacy Policy | プライバシーポリシー |
| Terms of Service | 利用規約 |
| Copyright | 著作権 |
| Sitemap | サイトマップ |
| FAQ | よくある質問 |
| Why Hack23 | なぜHack23か |
| Accessibility Statement | アクセシビリティ声明 |
| Language | 言語 |
| Share | 共有 |
| Print | 印刷 |
| Save | 保存 |
| Edit | 編集 |
| Delete | 削除 |
| Confirm | 確認 |
| Loading | 読み込み中 |
| Error | エラー |
| Success | 成功 |
| Warning | 警告 |

### 🔐 CIA Triad & Core Security Principles

| English | Japanese | Notes |
|---------|----------|-------|
| CIA Triad | CIAトライアド | |
| CIA+ Framework | CIA+フレームワーク | Extended framework |
| **Confidentiality** | **機密性** | Data protection |
| **Integrity** | **完全性** | Data accuracy |
| **Availability** | **可用性** | System uptime |
| Non-Repudiation | 否認防止 | |
| Authentication | 認証 | |
| Authorization | 認可 | |

### 🔒 Security & Cybersecurity Terminology

| English | Japanese | Notes |
|---------|----------|-------|
| Cybersecurity | サイバーセキュリティ | |
| Information Security | 情報セキュリティ | |
| ISMS | 情報セキュリティマネジメントシステム | |
| Security Policy | セキュリティポリシー | |
| Risk Management | リスク管理 | |
| Risk Assessment | リスクアセスメント | |
| Threat | 脅威 | |
| Vulnerability | 脆弱性 | |
| Exploit | エクスプロイト | |
| Patch | パッチ | |
| Firewall | ファイアウォール | |
| Encryption | 暗号化 | |
| Decryption | 復号化 | |
| Access Control | アクセス制御 | |
| Multi-Factor Authentication (MFA) | 多要素認証 | |
| Single Sign-On (SSO) | シングルサインオン | |
| Phishing | フィッシング | |
| Ransomware | ランサムウェア | |
| Malware | マルウェア | |
| Zero Trust | ゼロトラスト | |
| Defense in Depth | 多層防御 | |
| Least Privilege | 最小権限 | |
| Incident Response | インシデント対応 | |
| Data Breach | データ侵害 | |
| Penetration Test | ペネトレーションテスト | |
| Audit | 監査 | |
| Compliance | コンプライアンス | |
| Governance | ガバナンス | |
| Security Awareness | セキュリティ意識 | |
| Backup | バックアップ | |
| Disaster Recovery | 災害復旧 | |
| Business Continuity | 事業継続 | |
| Supply Chain Security | サプライチェーンセキュリティ | |
| SLSA Level 3 | SLSAレベル3 | Supply chain security |
| Container Security | コンテナセキュリティ | |
| Serverless Security | サーバーレスセキュリティ | |
| API Security | APIセキュリティ | |
| Endpoint Security | エンドポイントセキュリティ | |

### 🏛️ Regulatory & Standards

| English | Japanese | Notes |
|---------|----------|-------|
| ISO 27001 | ISO 27001 | Keep as-is |
| ISO 27001:2022 | ISO 27001:2022 | |
| GDPR | GDPR / 一般データ保護規則 | EU regulation |
| NIS2 | NIS2指令 | EU directive |
| NIST CSF | NISTサイバーセキュリティフレームワーク | |
| CIS Controls | CISコントロール | |
| SOC2 | SOC2 | |
| HIPAA | HIPAA | US healthcare |
| EU Cyber Resilience Act (CRA) | EUサイバーレジリエンス法 | |
| Annex A Controls | 附属書Aの管理策 | ISO 27001 |
| Statement of Applicability | 適用宣言書 | |
| NISC | 内閣サイバーセキュリティセンター | Japanese regulator |
| JPCERT/CC | JPCERT/CC | Japanese CERT |

### 💼 Business & Professional Terms

| English | Japanese |
|---------|----------|
| Consulting | コンサルティング |
| Enterprise | エンタープライズ |
| Strategy | 戦略 |
| Certification | 認証 |
| Assessment | アセスメント |
| Implementation | 実装 |
| Audit | 監査 |
| Review | レビュー |
| Gap Analysis | ギャップ分析 |
| Roadmap | ロードマップ |
| Best Practices | ベストプラクティス |
| Case Study | ケーススタディ |
| ROI | 投資対効果 |
| KPI | 主要業績評価指標 |
| SLA | サービスレベル契約 |
| Stakeholder | ステークホルダー |
| Deliverable | 成果物 |
| Milestone | マイルストーン |

### 📝 Blog Post Categories

| English | Japanese |
|---------|----------|
| Security Architecture | セキュリティアーキテクチャ |
| ISMS Policies | ISMSポリシー |
| Compliance Frameworks | コンプライアンスフレームワーク |
| Threat Modeling | 脅威モデリング |
| Secure Development | セキュア開発 |
| Cloud Security | クラウドセキュリティ |
| Access Control | アクセス制御 |
| Cryptography | 暗号学 |
| Incident Response | インシデント対応 |
| Vulnerability Management | 脆弱性管理 |
| Asset Management | 資産管理 |
| Network Security | ネットワークセキュリティ |
| Email Security | メールセキュリティ |
| Physical Security | 物理セキュリティ |
| Mobile Device Security | モバイルデバイスセキュリティ |
| Remote Access Security | リモートアクセスセキュリティ |
| Monitoring & Logging | モニタリングとログ |
| Security Metrics | セキュリティ指標 |
| Third Party Risk | サードパーティリスク |
| Change Management | 変更管理 |

### 🏭 Industry-Specific Terms

| English | Japanese |
|---------|----------|
| Investment & FinTech | 投資とフィンテック |
| Betting & Gaming | ベッティングとゲーミング |
| Cannabis Security | 大麻セキュリティ |
| Healthcare | ヘルスケア |
| Government | 政府 |
| Critical Infrastructure | 重要インフラ |
| Financial Services | 金融サービス |
| E-commerce | Eコマース |

---

## 🔤 Japanese-Specific Guidelines

### Script Usage
- **Kanji (漢字)**: Used for most nouns, verbs, adjectives
- **Hiragana (ひらがな)**: Grammatical elements, native Japanese words
- **Katakana (カタカナ)**: Foreign loanwords, technical terms, brand names

### Formatting
- No spaces between words in Japanese text
- Use Japanese punctuation (。、！？)
- Full-width numbers for Japanese context, half-width for technical

### Honorifics
- Use です/ます form (polite) for professional content
- Avoid overly casual language

---

## ✅ Translation Checklist

- [ ] `<html lang="ja">` attribute set
- [ ] `<title>` translated
- [ ] `<meta name="description">` translated
- [ ] `og:locale` set to `ja_JP`
- [ ] All hreflang tags present (14 languages)
- [ ] Navigation menu translated
- [ ] Footer translated
- [ ] Brand names kept in English or Katakana
- [ ] Appropriate script usage (Kanji/Hiragana/Katakana)
- [ ] Japanese punctuation used correctly

---

## 📝 Notes

- Use **polite Japanese** (です/ます form)
- Many technical terms use Katakana transliteration
- NISC is the Japanese cybersecurity center
- Keep consistency in technical term translations

---

*23 FNORD 5*
