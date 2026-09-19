SKILLS_DICTIONARY.update({
    # =========================================================
    # TECHNOLOGY, IT & SOFTWARE - BATCH 2 (10 Courses)
    # =========================================================
    "cybersecurity": {
        "name": "Cybersecurity and Information Security",
        "track": "Technology, IT & Software",
        "level": "ADVANCED",
        "stage": "SPECIALIZED",
        "prerequisites": ["network-administration", "system-administration"],
        "subtopics": ["Security Principles (CIA Triad)", "Threat Modeling", "Authentication & IAM", "Network Security (Firewalls/IDS)", "App Security (OWASP Top 10)", "Risk Assessment"],
        "project": "Perform a vulnerability assessment on a controlled lab environment and write a remediation report."
    },
    "machine-learning": {
        "name": "Machine Learning Algorithms",
        "track": "Technology, IT & Software",
        "level": "ADVANCED",
        "stage": "SPECIALIZED",
        "prerequisites": ["programming", "statistical-analysis"],
        "subtopics": ["Supervised Learning (Regression/Classification)", "Unsupervised Learning (Clustering)", "Decision Trees & Random Forests", "Model Evaluation (F1, Recall, Precision)", "Overfitting vs Underfitting", "Scikit-Learn Basics"],
        "project": "Build, train, and evaluate a predictive classification model using a Kaggle dataset."
    },
    "devops": {
        "name": "DevOps Practices",
        "track": "Technology, IT & Software",
        "level": "ADVANCED",
        "stage": "ADVANCED",
        "prerequisites": ["version-control", "cloud-computing"],
        "subtopics": ["DevOps Culture & Agile", "CI/CD Pipelines (GitHub Actions/Jenkins)", "Containerization (Docker)", "Orchestration (Kubernetes basics)", "Infrastructure as Code (Terraform)", "Monitoring (Prometheus/Grafana)"],
        "project": "Create a fully automated CI/CD pipeline that builds and deploys a Dockerized application."
    },
    "mobile-development": {
        "name": "Mobile App Development (iOS/Android)",
        "track": "Technology, IT & Software",
        "level": "INTERMEDIATE",
        "stage": "CORE",
        "prerequisites": ["programming"],
        "subtopics": ["Mobile UI/UX Principles", "Cross-Platform (Flutter/React Native) vs Native", "Navigation & Routing", "State Management", "Consuming APIs on Mobile", "App Store Deployment Basics"],
        "project": "Build a functional cross-platform mobile application with a working API backend."
    },
    "qa-testing": {
        "name": "Quality Assurance (QA) and Testing",
        "track": "Technology, IT & Software",
        "level": "INTERMEDIATE",
        "stage": "CORE",
        "prerequisites": ["programming"],
        "subtopics": ["Testing Fundamentals (Manual vs Auto)", "Unit Testing", "Integration Testing", "Writing Test Cases", "Test Automation Frameworks (Selenium/Cypress)", "Bug Reporting (Jira)"],
        "project": "Write a comprehensive test plan and create automated end-to-end tests for a web application."
    },
    "blockchain": {
        "name": "Blockchain Technology",
        "track": "Technology, IT & Software",
        "level": "SPECIALIZED",
        "stage": "SPECIALIZED",
        "prerequisites": ["programming"],
        "subtopics": ["Distributed Ledgers", "Hashing & Cryptography", "Consensus Mechanisms (PoW/PoS)", "Smart Contracts (Solidity)", "Wallets & Transactions", "Web3 Basics"],
        "project": "Deploy a basic Smart Contract to an Ethereum test network."
    },
    "iot": {
        "name": "Internet of Things (IoT) Development",
        "track": "Technology, IT & Software",
        "level": "SPECIALIZED",
        "stage": "SPECIALIZED",
        "prerequisites": ["programming", "network-administration"],
        "subtopics": ["IoT Architecture", "Sensors & Actuators", "Microcontrollers (Arduino/Raspberry Pi)", "IoT Protocols (MQTT, CoAP)", "Edge Computing", "IoT Security"],
        "project": "Build a simulated sensor-based IoT data collection pipeline."
    },
    "prompt-engineering": {
        "name": "Prompt Engineering (for Generative AI)",
        "track": "Technology, IT & Software",
        "level": "INTERMEDIATE",
        "stage": "SPECIALIZED",
        "prerequisites": ["ai-literacy"],
        "subtopics": ["LLM Architecture Basics", "Zero-shot vs Few-shot Prompting", "Chain of Thought (CoT)", "System Prompts & Context Windows", "Preventing Prompt Injection", "Output Formatting (JSON/XML)"],
        "project": "Build a structured prompt library for automating three distinct business workflows."
    },
    "server-maintenance": {
        "name": "Server Maintenance",
        "track": "Technology, IT & Software",
        "level": "ADVANCED",
        "stage": "ADVANCED",
        "prerequisites": ["system-administration", "network-administration"],
        "subtopics": ["Server Hardening", "Patch Management", "Log Aggregation", "Load Balancing", "High Availability (HA)", "Disaster Recovery Planning"],
        "project": "Design a High Availability server architecture diagram and write a Disaster Recovery runbook."
    },
    "software-architecture": {
        "name": "Software Architecture",
        "track": "Technology, IT & Software",
        "level": "ADVANCED",
        "stage": "ADVANCED",
        "prerequisites": ["programming", "api-development"],
        "subtopics": ["Monolith vs Microservices", "Event-Driven Architecture", "Caching Strategies (Redis)", "Database Sharding", "System Scalability", "Design Patterns"],
        "project": "Design and document the system architecture for a scalable, high-traffic web application."
    },

    # =========================================================
    # DATA & ANALYTICS (10 Courses)
    # =========================================================
    "quantitative-research": {
        "name": "Quantitative Research",
        "track": "Data & Analytics",
        "level": "FOUNDATION",
        "stage": "FOUNDATION",
        "prerequisites": [],
        "subtopics": ["Research Methodology", "Variable Types (Discrete/Continuous)", "Sampling Methods", "Data Collection Tools", "Survey Design", "Basic Descriptive Stats"],
        "project": "Design a quantitative survey, collect 50+ responses, and summarize the findings."
    },
    "sql": {
        "name": "SQL (Structured Query Language)",
        "track": "Data & Analytics",
        "level": "FOUNDATION",
        "stage": "CORE",
        "prerequisites": ["quantitative-research"],
        "subtopics": ["RDBMS Basics & SELECT", "Filtering (WHERE, AND/OR)", "Aggregation (GROUP BY, HAVING)", "Multi-table (INNER/LEFT JOIN)", "Subqueries", "CTEs & Window Functions"],
        "project": "Extract business insights from a multi-table E-commerce database using complex JOINs and CTEs."
    },
    "data-analysis": {
        "name": "Data Analysis",
        "track": "Data & Analytics",
        "level": "INTERMEDIATE",
        "stage": "CORE",
        "prerequisites": ["sql", "quantitative-research"],
        "subtopics": ["Data Cleaning (Handling Missing Vals)", "Exploratory Data Analysis (EDA)", "Pivot Tables (Excel/Python)", "Trend Identification", "Cohort Analysis", "Data Storytelling"],
        "project": "Clean a messy dataset and produce a written analytical report on customer churn."
    },
    "statistical-analysis": {
        "name": "Statistical Analysis",
        "track": "Data & Analytics",
        "level": "INTERMEDIATE",
        "stage": "CORE",
        "prerequisites": ["quantitative-research"],
        "subtopics": ["Probability Distributions", "Central Limit Theorem", "Hypothesis Testing (Null/Alt)", "P-Values & Confidence Intervals", "T-Tests & ANOVA", "Correlation vs Causation"],
        "project": "Perform an A/B test analysis using statistical significance formulas."
    },
    "data-visualization": {
        "name": "Data Visualization (Tableau, Power BI)",
        "track": "Data & Analytics",
        "level": "INTERMEDIATE",
        "stage": "CORE",
        "prerequisites": ["data-analysis"],
        "subtopics": ["Visual Best Practices", "Choosing the Right Chart", "Connecting Data Sources", "Building Interactive Dashboards", "Calculated Fields", "Publishing Dashboards"],
        "project": "Build an interactive global sales dashboard in Tableau or Power BI."
    },
    "data-engineering": {
        "name": "Data Engineering",
        "track": "Data & Analytics",
        "level": "ADVANCED",
        "stage": "ADVANCED",
        "prerequisites": ["sql", "data-analysis"],
        "subtopics": ["ETL / ELT Processes", "Data Warehouses (Snowflake/BigQuery)", "Data Lakes", "Pipeline Orchestration (Airflow)", "Data Modeling (Star Schema)", "Data Quality Checks"],
        "project": "Design an automated ETL pipeline architecture for a SaaS company."
    },
    "business-intelligence": {
        "name": "Business Intelligence (BI)",
        "track": "Data & Analytics",
        "level": "INTERMEDIATE",
        "stage": "ADVANCED",
        "prerequisites": ["data-analysis", "data-visualization"],
        "subtopics": ["Defining KPIs", "Business Metrics (CAC, LTV, Churn)", "Executive Reporting", "Self-Service BI", "Translating Data to Strategy", "BI Governance"],
        "project": "Create a unified BI dashboard for the executive team of a fictional retail chain."
    },
    "data-mining": {
        "name": "Data Mining",
        "track": "Data & Analytics",
        "level": "ADVANCED",
        "stage": "ADVANCED",
        "prerequisites": ["statistical-analysis", "data-analysis"],
        "subtopics": ["Pattern Discovery", "Association Rules (Market Basket)", "Anomaly Detection", "Text Mining Basics", "Web Scraping", "Dimensionality Reduction"],
        "project": "Perform market basket analysis to recommend products frequently bought together."
    },
    "big-data": {
        "name": "Big Data Processing (Hadoop, Spark)",
        "track": "Data & Analytics",
        "level": "ADVANCED",
        "stage": "SPECIALIZED",
        "prerequisites": ["data-engineering"],
        "subtopics": ["Distributed Computing Concepts", "Hadoop Ecosystem (HDFS)", "Apache Spark Architecture", "Spark DataFrames", "Stream Processing (Kafka)", "NoSQL at Scale"],
        "project": "Write a PySpark script to aggregate and process a large-scale (10GB+) simulated dataset."
    },
    "predictive-modeling": {
        "name": "Predictive Modeling",
        "track": "Data & Analytics",
        "level": "ADVANCED",
        "stage": "SPECIALIZED",
        "prerequisites": ["statistical-analysis", "data-analysis"],
        "subtopics": ["Linear & Logistic Regression", "Feature Engineering", "Training vs Test Sets", "Cross-Validation", "Time Series Forecasting", "Model Deployment Basics"],
        "project": "Build a time-series model forecasting quarterly sales based on historical data."
    },

    # =========================================================
    # MARKETING, SALES & CONTENT (15 Courses)
    # =========================================================
    "content-marketing": { "name": "Content Marketing", "track": "Marketing", "level": "FOUNDATION", "stage": "CORE", "prerequisites": [], "subtopics": ["Audience Personas", "Content Funnels", "Blogging & Articles", "Editorial Calendars", "Content Distribution", "Content Analytics"], "project": "Develop a 3-month content marketing calendar." },
    "copywriting": { "name": "Copywriting", "track": "Marketing", "level": "FOUNDATION", "stage": "FOUNDATION", "prerequisites": [], "subtopics": ["Persuasive Writing Frameworks (AIDA/PAS)", "Headlines & Hooks", "Calls to Action (CTAs)", "Landing Page Copy", "Ad Copy", "Email Copy"], "project": "Write the complete copy for a high-converting landing page." },
    "social-media": { "name": "Social Media Management", "track": "Marketing", "level": "FOUNDATION", "stage": "CORE", "prerequisites": [], "subtopics": ["Platform Algorithms (IG, LinkedIn, X)", "Community Engagement", "Social Listening", "Scheduling Tools", "Visual Storytelling", "Social Analytics"], "project": "Manage a simulated 30-day social media launch campaign." },
    "market-research": { "name": "Market Research", "track": "Marketing", "level": "FOUNDATION", "stage": "FOUNDATION", "prerequisites": [], "subtopics": ["Competitor Analysis", "Primary vs Secondary Research", "Focus Groups", "Survey Tools", "Market Segmentation", "Trend Forecasting"], "project": "Conduct a comprehensive competitor analysis for a new product launch." },
    "seo": { "name": "Search Engine Optimization (SEO)", "track": "Marketing", "level": "INTERMEDIATE", "stage": "CORE", "prerequisites": ["content-marketing"], "subtopics": ["Keyword Research", "On-Page Optimization", "Technical SEO (Site Speed/Structure)", "Backlink Strategies", "Local SEO", "Google Search Console"], "project": "Perform an SEO audit on an existing website." },
    "sem-ppc": { "name": "Search Engine Marketing (SEM/PPC)", "track": "Marketing", "level": "INTERMEDIATE", "stage": "CORE", "prerequisites": [], "subtopics": ["Google Ads Interface", "Bidding Strategies", "Keyword Match Types", "Quality Score", "Ad Extensions", "Conversion Tracking"], "project": "Design and budget a $5,000 Google Search Ad campaign." },
    "email-marketing": { "name": "Email Marketing", "track": "Marketing", "level": "INTERMEDIATE", "stage": "CORE", "prerequisites": ["copywriting"], "subtopics": ["List Building & Hygiene", "Segmentation", "Drip Campaigns", "A/B Testing Subject Lines", "Email Design Basics", "Deliverability & Spam Laws"], "project": "Design a 5-part automated welcome email sequence." },
    "crm": { "name": "Customer Relationship Management (CRM)", "track": "Marketing", "level": "INTERMEDIATE", "stage": "CORE", "prerequisites": [], "subtopics": ["CRM Architecture (Salesforce/HubSpot)", "Lead Status Management", "Pipeline Stages", "Task Automation", "Contact Lifecycle", "CRM Reporting"], "project": "Configure a sales pipeline workflow in a free CRM tool." },
    "lead-generation": { "name": "Lead Generation", "track": "Marketing", "level": "INTERMEDIATE", "stage": "CORE", "prerequisites": ["content-marketing"], "subtopics": ["Inbound vs Outbound", "Lead Magnets", "Gated Content", "Webinars", "Lead Scoring", "MQL vs SQL Definitions"], "project": "Create a lead magnet and map out the acquisition funnel." },
    "brand-management": { "name": "Brand Management", "track": "Marketing", "level": "INTERMEDIATE", "stage": "CORE", "prerequisites": ["market-research"], "subtopics": ["Brand Identity", "Brand Voice & Tone", "Brand Positioning", "Style Guides", "Brand Equity", "Rebranding Strategies"], "project": "Create a comprehensive brand style guide for a startup." },
    "video-marketing": { "name": "Video Marketing", "track": "Marketing", "level": "INTERMEDIATE", "stage": "CORE", "prerequisites": [], "subtopics": ["Video Strategy", "Short-form (TikTok/Reels) vs Long-form", "Scripting", "Thumbnail Psychology", "YouTube SEO", "Video Analytics"], "project": "Write, storyboard, and optimize a video marketing campaign." },
    "digital-marketing-strategy": { "name": "Digital Marketing Strategy", "track": "Marketing", "level": "ADVANCED", "stage": "ADVANCED", "prerequisites": ["seo", "content-marketing", "market-research"], "subtopics": ["Omnichannel Strategy", "Customer Journey Mapping", "Budget Allocation", "CAC vs LTV", "Marketing Mix Modeling", "Campaign ROI"], "project": "Draft a multi-channel annual digital marketing strategy." },
    "ecommerce": { "name": "E-commerce Management", "track": "Marketing", "level": "INTERMEDIATE", "stage": "CAREER", "prerequisites": [], "subtopics": ["Storefront Platforms (Shopify)", "Product Page Optimization", "Cart Abandonment", "Payment Gateways", "Fulfillment Basics", "E-com Analytics"], "project": "Design a conversion-optimized e-commerce product page layout." },
    "public-relations": { "name": "Public Relations (PR)", "track": "Marketing", "level": "INTERMEDIATE", "stage": "CAREER", "prerequisites": [], "subtopics": ["Media Relations", "Press Releases", "Pitching Journalists", "Crisis Communication", "Influencer Partnerships", "Earned Media"], "project": "Write a press release and media pitch for a product launch." },
    "sales": { "name": "B2B / B2C Sales", "track": "Marketing", "level": "INTERMEDIATE", "stage": "CAREER", "prerequisites": ["crm"], "subtopics": ["Prospecting & Cold Outreach", "Discovery Calls", "Objection Handling", "Closing Techniques", "Account Management", "Sales Psychology"], "project": "Conduct a simulated B2B sales discovery call and write a follow-up proposal." },

    # =========================================================
    # BUSINESS, FINANCE & OPERATIONS (10 Courses)
    # =========================================================
    "financial-accounting": { "name": "Financial Accounting (GAAP, IFRS)", "track": "Business", "level": "FOUNDATION", "stage": "FOUNDATION", "prerequisites": [], "subtopics": ["Double-Entry Bookkeeping", "Income Statements", "Balance Sheets", "Cash Flow Statements", "Accrual vs Cash Basis", "Depreciation"], "project": "Prepare three core financial statements from a raw ledger." },
    "inventory-control": { "name": "Inventory Control", "track": "Business", "level": "FOUNDATION", "stage": "CORE", "prerequisites": [], "subtopics": ["FIFO vs LIFO", "Economic Order Quantity (EOQ)", "Reorder Points", "Safety Stock", "Shrinkage", "Inventory Turnover"], "project": "Calculate EOQ and reorder points for a simulated retail business." },
    "budgeting": { "name": "Budgeting and Cost Management", "track": "Business", "level": "INTERMEDIATE", "stage": "CORE", "prerequisites": ["financial-accounting"], "subtopics": ["Operating Budgets", "Capital Budgets", "Zero-Based Budgeting", "Fixed vs Variable Costs", "Break-Even Analysis", "Variance Analysis"], "project": "Create a departmental operating budget and run a variance report." },
    "supply-chain": { "name": "Supply Chain Management", "track": "Business", "level": "INTERMEDIATE", "stage": "CORE", "prerequisites": ["inventory-control"], "subtopics": ["Procurement", "Vendor Management", "Logistics & Freight", "Just-In-Time (JIT)", "Supply Chain Risks", "Reverse Logistics"], "project": "Map the end-to-end supply chain process for a physical product." },
    "quality-control": { "name": "Quality Control and Assurance", "track": "Business", "level": "INTERMEDIATE", "stage": "CORE", "prerequisites": [], "subtopics": ["QA vs QC", "Six Sigma Basics", "Total Quality Management (TQM)", "ISO Standards", "Root Cause Analysis (Fishbone)", "Continuous Improvement"], "project": "Develop a standard operating procedure (SOP) for product quality inspection." },
    "financial-modeling": { "name": "Financial Modeling and Forecasting", "track": "Business", "level": "ADVANCED", "stage": "ADVANCED", "prerequisites": ["financial-accounting", "budgeting"], "subtopics": ["3-Statement Models", "DCF (Discounted Cash Flow)", "Revenue Forecasting", "Sensitivity Analysis", "Scenario Planning", "Excel/Sheets Mastery"], "project": "Build a 3-year financial forecast model in Excel." },
    "risk-management": { "name": "Risk Management", "track": "Business", "level": "ADVANCED", "stage": "ADVANCED", "prerequisites": ["financial-modeling"], "subtopics": ["Risk Identification", "Risk Matrices", "Financial Hedging", "Operational Risk", "Cyber Risk in Business", "Business Continuity Planning"], "project": "Create a corporate risk matrix and mitigation strategy." },
    "business-analysis": { "name": "Business Analysis", "track": "Business", "level": "INTERMEDIATE", "stage": "ADVANCED", "prerequisites": [], "subtopics": ["Requirements Gathering", "Process Mapping (BPMN)", "Stakeholder Management", "SWOT Analysis", "Gap Analysis", "Creating Business Cases"], "project": "Draft a formal Business Requirements Document (BRD)." },
    "contract-negotiation": { "name": "Contract Negotiation", "track": "Business", "level": "ADVANCED", "stage": "CAREER", "prerequisites": [], "subtopics": ["Contract Law Basics", "Terms and Conditions", "SLAs", "BATNA Strategies", "Win-Win Negotiation", "Managing Scope Creep"], "project": "Redline a vendor contract and negotiate terms in a simulation." },
    "compliance": { "name": "Compliance and Regulatory Knowledge", "track": "Business", "level": "ADVANCED", "stage": "CAREER", "prerequisites": [], "subtopics": ["Corporate Governance", "Data Privacy (GDPR/CCPA)", "Financial Regulations (SOX)", "Workplace Safety (OSHA)", "Internal Audits", "Whistleblower Policies"], "project": "Draft a GDPR-compliant data privacy policy for an online business." }
})