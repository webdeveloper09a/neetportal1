<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Aakash NEET Test Papers 2025-2026</title>
  <style>
    /* Reset & basics */
    * {
      box-sizing: border-box;
    }
    body {
      margin: 0; 
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #f7f9fc; /* very light gray-blue */
      color: #222831;       /* almost black, soft */
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px 15px 50px;
      line-height: 1.5;
      letter-spacing: 0.02em;
    }

    header {
      width: 100%;
      max-width: 960px;
      background: linear-gradient(135deg, #283e59, #3a5068); /* darker blue-gray gradient */
      color: #eaeaea; /* very light */
      padding: 35px 25px;
      border-radius: 15px;
      text-align: center;
      box-shadow: 0 8px 24px rgba(40, 62, 89, 0.4);
      user-select: none;
      font-weight: 700;
      letter-spacing: 0.03em;
      transition: background 0.4s ease;
    }
    header:hover {
      background: linear-gradient(135deg, #1f2d43, #2e4050);
    }
    header h1 {
      margin: 0 0 10px;
      font-size: 2.4rem;
      line-height: 1.2;
    }
    header p {
      font-size: 1.15rem;
      opacity: 0.8;
      font-weight: 600;
      letter-spacing: 0.02em;
    }

    /* Quote section */
    .quote {
      max-width: 860px;
      margin: 30px auto 50px;
      font-style: italic;
      font-weight: 600;
      color: #475569; /* slate gray-blue */
      font-size: 1.2rem;
      border-left: 6px solid #3a5068;
      padding-left: 18px;
      user-select: text;
      box-shadow: 2px 2px 8px rgba(58, 80, 104, 0.1);
      background: #e3e9f1; /* very light blue-gray */
      border-radius: 8px;
      line-height: 1.45;
    }

    /* Search box */
    .search-container {
      margin: 20px auto 35px;
      width: 100%;
      max-width: 960px;
      text-align: center;
    }
    .search-container input {
      width: 92%;
      max-width: 520px;
      padding: 14px 20px;
      font-size: 1.1rem;
      border-radius: 30px;
      border: 2.5px solid #3a5068;
      outline-offset: 3px;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
      box-shadow: inset 0 0 8px #9bb3cc66;
      font-weight: 600;
      color: #222831;
      background-color: #fafbfc;
    }
    .search-container input::placeholder {
      color: #a1b0cc;
      font-style: italic;
    }
    .search-container input:focus {
      border-color: #1f2d43;
      box-shadow: 0 0 12px #1f2d43aa;
      background-color: #fff;
    }

    /* Batches container */
    .batches {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 22px;
      width: 100%;
      max-width: 960px;
      user-select: none;
    }

    .batch-card {
      background: #f9fafc;
      border-radius: 18px;
      padding: 28px 35px;
      min-width: 190px;
      max-width: 210px;
      box-shadow: 0 8px 28px rgba(58, 80, 104, 0.15);
      cursor: pointer;
      text-align: center;
      font-weight: 700;
      font-size: 1.3rem;
      color: #283e59;
      transition: background 0.35s ease, color 0.35s ease, transform 0.3s ease, box-shadow 0.3s ease;
      border: 2px solid transparent;
      user-select: none;
      letter-spacing: 0.015em;
      text-transform: uppercase;
    }
    .batch-card:hover {
      background: #dde4ef;
      color: #1f2d43;
      transform: translateY(-7px);
      border-color: #1f2d43;
      box-shadow: 0 12px 38px rgba(31, 45, 67, 0.35);
    }

    /* JEE card special */
    .batch-card.jee {
      cursor: default;
      background: #e4e7eb;
      color: #8892a3;
      border-color: #bcc4d4;
      font-style: italic;
      user-select: none;
      transition: background 0.3s ease, box-shadow 0.3s ease;
      box-shadow: none;
      text-transform: none;
    }
    .batch-card.jee:hover {
      background: #d0d5dd;
      color: #6a7280;
      transform: none;
      border-color: #9aa3b5;
      box-shadow: none;
    }

    /* Test container */
    .test-container {
      margin-top: 40px;
      width: 100%;
      max-width: 960px;
      display: flex;
      flex-wrap: wrap;
      gap: 28px;
      justify-content: center;
      user-select: none;
      min-height: 320px;
      background: #fff;
      border-radius: 20px;
      box-shadow: 0 6px 28px rgba(58, 80, 104, 0.12);
      padding: 25px 20px;
      transition: background 0.3s ease;
    }
    .test-container:empty::before {
      content: "Please select a batch above to view test papers.";
      color: #999ea7;
      font-style: italic;
      font-weight: 600;
      width: 100%;
      text-align: center;
      user-select: none;
      font-size: 1.1rem;
      padding: 40px 0;
      display: block;
    }

    .test-section {
      flex: 1 1 320px;
      background: #f4f7fc;
      border-radius: 16px;
      box-shadow: 0 4px 22px rgba(31, 45, 67, 0.08);
      padding: 28px 30px;
      display: flex;
      flex-direction: column;
      max-height: 540px;
      overflow-y: auto;
      transition: background 0.3s ease;
    }
    .test-section h2 {
      font-size: 1.4rem;
      font-weight: 700;
      color: #283e59;
      margin-bottom: 18px;
      border-bottom: 3px solid #3a5068;
      padding-bottom: 8px;
      user-select: text;
      letter-spacing: 0.02em;
    }

    /* PDF links */
    .pdf-link {
      text-decoration: none;
      padding: 10px 14px;
      margin-bottom: 14px;
      color: #1f2d43;
      font-weight: 600;
      border-radius: 10px;
      transition: background-color 0.3s ease, color 0.3s ease;
      user-select: text;
      display: block;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      box-shadow: 0 2px 6px rgba(58, 80, 104, 0.1);
    }
    .pdf-link:hover {
      background: #c4cddb;
      color: #0b1220;
      box-shadow: 0 4px 14px rgba(11, 18, 32, 0.2);
    }

    /* Message if no papers */
    .no-papers {
      color: #7a828d;
      font-style: italic;
      font-weight: 600;
      margin-top: 8px;
      user-select: text;
      font-size: 1rem;
      text-align: center;
      letter-spacing: 0.015em;
    }

    /* Why section */
    .why-section {
      max-width: 960px;
      background: #e3e9f1;
      border-radius: 18px;
      padding: 30px 40px;
      margin: 60px auto 0;
      box-shadow: 0 10px 30px rgba(58, 80, 104, 0.15);
      user-select: text;
    }
    .why-section h2 {
      font-size: 1.8rem;
      color: #283e59;
      font-weight: 700;
      margin-bottom: 22px;
      letter-spacing: 0.02em;
      text-align: center;
    }
    .why-section ul {
      list-style: none;
      padding-left: 0;
      font-size: 1.1rem;
      color: #222831;
      line-height: 1.55;
      max-width: 700px;
      margin: 0 auto;
    }
    .why-section ul li {
      margin-bottom: 14px;
      padding-left: 24px;
      position: relative;
      font-weight: 600;
    }
    .why-section ul li::before {
      content: '✔';
      color: #3a5068;
      position: absolute;
      left: 0;
      top: 2px;
      font-weight: 900;
      font-size: 1.1rem;
      user-select: none;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
      .test-container {
        flex-direction: column;
        max-width: 100%;
        padding: 20px 15px;
      }
      .test-section {
        max-height: none;
      }
      .batch-card {
        min-width: 140px;
        max-width: 160px;
        font-size: 1.1rem;
        padding: 20px 22px;
      }
      .why-section {
        padding: 25px 20px;
      }
    }
  </style>
</head>
<body>

  <header>
    <h1>Welcome to Aakash NEET & JEE Test Papers (2025–2026)</h1>
    <p>Batches: RM (Droppers), OYM (12th), TYM (11th) — JEE Coming Soon</p>
  </header>

  <div class="quote" aria-label="Inspirational quote">
    “Success in exams is not just about studying hard, but studying smart. Your journey starts here.”
  </div>

  <div class="search-container">
    <input type="search" id="searchInput" placeholder="Search test papers..." oninput="filterSearch()" />
  </div>

  <div class="batches" role="list" aria-label="Select batch">
    <div class="batch-card" data-batch="rm" onclick="showTests('rm')" role="listitem" tabindex="0" onkeypress="if(event.key==='Enter') showTests('rm')">RM (Droppers)</div>
    <div class="batch-card" data-batch="oym" onclick="showTests('oym')" role="listitem" tabindex="0" onkeypress="if(event.key==='Enter') showTests('oym')">OYM (12th)</div>
    <div class="batch-card" data-batch="tym" onclick="showTests('tym')" role="listitem" tabindex="0" onkeypress="if(event.key==='Enter') showTests('tym')">TYM (11th)</div>
    <div class="batch-card jee" onclick="alert('JEE Content Coming Soon!')" role="listitem" tabindex="0" onkeypress="if(event.key==='Enter') alert('JEE Content Coming Soon!')">JEE (Coming Soon)</div>
  </div>

  <div class="test-container" id="testContainer" aria-live="polite" aria-label="Test papers list"></div>

  <section class="why-section" aria-label="Why choose AakashPaper 2025-26">
    <h2>Why AakashPaper 25-26?</h2>
    <ul>
      <li>Comprehensive & updated test papers tailored for NEET aspirants.</li>
      <li>Organized batches covering droppers and school years with precise categorization.</li>
      <li>Easy search and navigation for quick access to your required papers.</li>
      <li>Trusted by thousands of students for consistent exam preparation.</li>
      <li>Future-ready updates including upcoming JEE content.</li>
    </ul>
  </section>

<script>
  const categories = {
    rm: [
      { name: "FTS Test 1 - 2025", link: "#" },
      { name: "AIATS Test 2 - 2025", link: "#" }
    ],
    oym: [
      { name: "PT Test 1 - 2025", link: "#" },
      { name: "AIATS Test 3 - 2025", link: "#" },
      { name: "TE Test 1 - 2025", link: "#" },
      { name: "NRT Test 1 - 2025", link: "#" }
    ],
    tym: [
      { name: "PT Test 1 - 2025", link: "#" },
      { name: "AIATS Test 2 - 2025", link: "#" },
      { name: "TE Test 1 - 2025", link: "#" },
      { name: "NRT Test 2 - 2025", link: "#" }
    ]
  };

  const testContainer = document.getElementById('testContainer');

  function showTests(batch) {
    testContainer.innerHTML = '';
    if (!categories[batch] || categories[batch].length === 0) {
      testContainer.innerHTML = '<p class="no-papers">No test papers available for this batch currently.</p>';
      return;
    }
    categories[batch].forEach(test => {
      const a = document.createElement('a');
      a.href = test.link;
      a.textContent = test.name;
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
      a.className = 'pdf-link';
      testContainer.appendChild(a);
    });
  }

  function filterSearch() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    const links = testContainer.querySelectorAll('.pdf-link');
    links.forEach(link => {
      if (link.textContent.toLowerCase().includes(input)) {
        link.style.display = 'block';
      } else {
        link.style.display = 'none';
      }
    });
  }
</script>

</body>
</html>
