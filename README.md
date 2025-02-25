<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CyHack – Cybersecurity Toolkit</title>
    <style>
        /* Cyberpunk Themed Styles */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #0a0a0a;
            color: #00ffcc;
            text-align: center;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 90%;
            max-width: 900px;
            margin: 20px auto;
            padding: 20px;
            border-radius: 10px;
            background: #121212;
            box-shadow: 0px 0px 20px rgba(0, 255, 204, 0.3);
        }

        h1, h2 {
            color: #ffcc00;
            text-shadow: 0px 0px 10px rgba(255, 204, 0, 0.8);
        }

        h1 {
            font-size: 2.5rem;
        }

        h2 {
            font-size: 1.8rem;
            border-bottom: 2px solid #00ffcc;
            padding-bottom: 5px;
            margin-top: 20px;
        }

        p {
            font-size: 1.2rem;
            line-height: 1.5;
        }

        .features, .installation, .usage, .config, .repo-structure, .contributing {
            text-align: left;
            margin-top: 20px;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        ul li {
            font-size: 1.2rem;
            background: rgba(0, 255, 204, 0.2);
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
        }

        code {
            background: #222;
            color: #ffcc00;
            padding: 5px;
            border-radius: 5px;
        }

        pre {
            background: #222;
            color: #ffcc00;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            text-align: left;
        }

        .footer {
            margin-top: 30px;
            font-size: 1rem;
            color: #999;
        }

        .images {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 20px;
        }

        .images img {
            width: 80%;
            max-width: 500px;
            border-radius: 10px;
            margin: 10px;
            box-shadow: 0px 0px 15px rgba(255, 204, 0, 0.5);
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>🔥 CyHack – Cybersecurity Toolkit</h1>
        <p>🚀 CyHack is a cybersecurity toolkit designed for ethical hackers, penetration testers, and security professionals to identify vulnerabilities, test exploits, and strengthen system defenses.</p>

        <h2>⚡ Features</h2>
        <ul class="features">
            <li>✅ <strong>Network Scanning</strong> – Identify open ports, services, and vulnerabilities.</li>
            <li>✅ <strong>Penetration Testing</strong> – Simulate real-world cyber attacks.</li>
            <li>✅ <strong>Exploit Testing</strong> – Deploy and test known exploits.</li>
            <li>✅ <strong>Forensic Tools</strong> – Analyze logs and track system anomalies.</li>
            <li>✅ <strong>Automation</strong> – Automate security assessments for efficiency.</li>
            <li>✅ <strong>Reporting</strong> – Generate detailed security reports.</li>
        </ul>

        <h2>📌 Installation</h2>
        <div class="installation">
            <p><strong>🔹 Prerequisites</strong></p>
            <ul>
                <li>🐍 Python 3.8+</li>
                <li>📦 pip (Python package manager)</li>
                <li>🔗 Git</li>
            </ul>

            <p><strong>🔹 Steps</strong></p>
            <pre>
git clone https://github.com/ravikirank2018/CYHACK.git
cd CYHACK
pip install -r requirements.txt
python cyhack.py
            </pre>
        </div>

        <h2>🎯 Usage</h2>
        <div class="usage">
            <pre>
python cyhack.py
# Choose a module (Network Scanning, Exploit Testing, etc.)
# Enter parameters and execute operations
# Review the results and take necessary actions
            </pre>
        </div>

        <h2>⚙️ Configuration</h2>
        <p>Modify <code>config.json</code> to customize:</p>
        <ul class="config">
            <li>Default scan targets</li>
            <li>Logging preferences</li>
            <li>API keys for external integrations</li>
        </ul>

        <h2>📂 Repository Structure</h2>
        <pre>
CYHACK/
│── .github/workflows/    # CI/CD automation (e.g., ngrok.yml)
│── cyber_incidents/      # Cybersecurity incident-related data and scripts
│── requirements.txt      # Required Python dependencies
│── cyhack.py             # Main script
│── config.json           # Configuration file
│── README.md             # Project documentation
        </pre>

        <h2>🚨 Disclaimer</h2>
        <p>❌ CyHack is strictly for ethical hacking and security research purposes. Unauthorized use is prohibited.</p>

        <h2>🤝 Contributing</h2>
        <p>💡 Contributions are welcome! Feel free to submit a <strong>Pull Request</strong> or open an <strong>Issue</strong>.</p>

        <h2>📌 Developed & Maintained by <strong>Ravi Kiran</strong> 🚀</h2>

        <div class="images">
            <img src="https://github.com/user-attachments/assets/8c327a6a-1829-4d0c-bd12-0d1c7e7f97fa" alt="Screenshot 1">
            <img src="https://github.com/user-attachments/assets/a49bb093-70ba-4131-a03c-a662cb489eea" alt="Screenshot 2">
            <img src="https://github.com/user-attachments/assets/15289e67-b61d-45cd-a5e4-0d7cf2adf186" alt="Screenshot 3">
        </div>

        <p class="footer">© 2025 CyHack | Developed by Ravi Kiran 🚀</p>
    </div>

</body>
</html>
