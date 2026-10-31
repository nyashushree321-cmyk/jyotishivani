import re

with open('c:/Users/Admin/Desktop/jotishvani 2/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Navbar Links
old_navbar = re.search(r'<nav class="navbar">.*?</nav>', content, re.DOTALL)
if old_navbar:
    new_navbar = '''<nav class="navbar">
                    <ul class="navbar-links">
                        <li class="navbar-dropdown"><a href="#pricing"> Consult </a></li>
                        <li class="navbar-dropdown"><a href="#about"> Services </a></li>
                        <li class="navbar-dropdown"><a href="#services"> How It Works </a></li>
                        <li class="navbar-dropdown"><a href="#app-screens"> App </a></li>
                        <li class="navbar-dropdown"><a href="#contact"> Contact </a></li>
                    </ul>
                </nav>'''
    content = content[:old_navbar.start()] + new_navbar + content[old_navbar.end():]
    print('1. Navbar updated successfully')
else:
    print('Warning: Navbar not found')

# 2. Update Pricing Section (<section id="pricing" ... </section>)
pricing_pattern = re.compile(r'<section id="pricing".*?</section>', re.DOTALL)
m_pricing = pricing_pattern.search(content)
if m_pricing:
    new_pricing = '''<section id="pricing" class="pricing-section-wrap">
        <div class="container">
            <div class="text-center mb-4">
                <span class="pricing-header-pill"><i class="fa-solid fa-sparkles"></i> Instant Consultations &amp; Vedic Services</span>
            </div>
            <div class="row g-4">
                <!-- Card 1: Chat with Jyotishi -->
                <div class="col-lg-3 col-md-6 col-12">
                    <a class="pricing-card-link" href="/chat">
                        <div class="consult-card consult-card-chat">
                            <div>
                                <div class="consult-top-bar">
                                    <span class="consult-tag"><i class="fa-solid fa-comments"></i> Chat</span>
                                    <span class="consult-tag consult-badge-offer"><i class="fa-solid fa-gift"></i> 5 Mins Free</span>
                                </div>
                                <div class="consult-icon-box">
                                    <i class="fa-solid fa-comments"></i>
                                </div>
                                <h3 class="consult-title">Chat with Jyotishi</h3>
                                <p class="consult-desc">Instant 1-on-1 private chat for quick answers on Love, Career &amp; Kundli.</p>
                            </div>
                            <div>
                                <div class="consult-price-wrap">
                                    <span class="consult-price-current">₹10<small>/min</small></span>
                                    <span class="consult-price-old">₹25/min</span>
                                    <span class="consult-rate-chip">60% OFF</span>
                                </div>
                                <div class="consult-btn">
                                    <span>Start Chat</span>
                                    <i class="fa-solid fa-arrow-right"></i>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>

                <!-- Card 2: Talk to Jyotishi (Featured / Hot) -->
                <div class="col-lg-3 col-md-6 col-12">
                    <a class="pricing-card-link" href="/call">
                        <div class="consult-card consult-card-call">
                            <div>
                                <div class="consult-top-bar">
                                    <span class="consult-tag text-white bg-white-10"><i class="fa-solid fa-bolt text-warning"></i> Call</span>
                                    <span class="consult-tag consult-badge-hot"><i class="fa-solid fa-fire"></i> Instant Call</span>
                                </div>
                                <div class="consult-icon-box">
                                    <i class="fa-solid fa-phone-volume"></i>
                                </div>
                                <h3 class="consult-title">Talk to Jyotishi</h3>
                                <p class="consult-desc">Direct voice consultation with verified top astrologers in under 60 secs.</p>
                            </div>
                            <div>
                                <div class="consult-price-wrap">
                                    <span class="consult-price-current">₹15<small>/min</small></span>
                                    <span class="consult-price-old">₹35/min</span>
                                    <span class="consult-rate-chip bg-warning text-dark font-weight-bold">Popular</span>
                                </div>
                                <div class="consult-btn">
                                    <span>Call Now</span>
                                    <i class="fa-solid fa-arrow-right"></i>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>

                <!-- Card 3: Astromall Shop -->
                <div class="col-lg-3 col-md-6 col-12">
                    <a class="pricing-card-link" href="/astromall">
                        <div class="consult-card consult-card-mall">
                            <div>
                                <div class="consult-top-bar">
                                    <span class="consult-tag"><i class="fa-solid fa-store"></i> Store</span>
                                    <span class="consult-tag consult-badge-cert"><i class="fa-solid fa-certificate"></i> Certified</span>
                                </div>
                                <div class="consult-icon-box">
                                    <i class="fa-solid fa-cart-shopping"></i>
                                </div>
                                <h3 class="consult-title">Astromall Shop</h3>
                                <p class="consult-desc">Original energized gemstones, Rudraksha &amp; Yantras with lab certificates.</p>
                            </div>
                            <div>
                                <div class="consult-price-wrap">
                                    <span class="consult-price-current">₹299<small> onw.</small></span>
                                    <span class="consult-price-old">₹699</span>
                                    <span class="consult-rate-chip">Free Check</span>
                                </div>
                                <div class="consult-btn">
                                    <span>Explore Shop</span>
                                    <i class="fa-solid fa-arrow-right"></i>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>

                <!-- Card 4: Book A Pooja -->
                <div class="col-lg-3 col-md-6 col-12">
                    <a class="pricing-card-link" href="/bookpoja">
                        <div class="consult-card consult-card-pooja">
                            <div>
                                <div class="consult-top-bar">
                                    <span class="consult-tag"><i class="fa-solid fa-om"></i> Ritual</span>
                                    <span class="consult-tag consult-badge-live"><i class="fa-solid fa-video"></i> Live e-Pooja</span>
                                </div>
                                <div class="consult-icon-box">
                                    <i class="fa-solid fa-book-open-reader"></i>
                                </div>
                                <h3 class="consult-title">Book A Pooja</h3>
                                <p class="consult-desc">Personalized Vedic rituals &amp; Hawan conducted with your Sankalp by Pandits.</p>
                            </div>
                            <div>
                                <div class="consult-price-wrap">
                                    <span class="consult-price-current">₹501<small> onw.</small></span>
                                    <span class="consult-price-old">₹1,100</span>
                                    <span class="consult-rate-chip">Prasad Deliv.</span>
                                </div>
                                <div class="consult-btn">
                                    <span>Book Ritual</span>
                                    <i class="fa-solid fa-arrow-right"></i>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </section>'''
    content = content[:m_pricing.start()] + new_pricing + content[m_pricing.end():]
    print('2. Pricing section updated successfully')
else:
    print('Warning: Pricing section not found')

# 3. Update Services Section (<section id="about" ... </section>)
about_pattern = re.compile(r'<section id="about".*?</section>', re.DOTALL)
m_about = about_pattern.search(content)
if m_about:
    new_about = '''<section id="about" class="gap">
      <div class="container">
        <div class="services-header sec-title-animation animation-style2">
          <span class="services-badge-pill"><i class="fa-solid fa-dharmachakra"></i> Sacred Vedic Solutions</span>
          <h2 class="title-animation">Our Expert Jyotishi Services</h2>
          <p>Ancient astrological wisdom combined with modern guidance. Select a specialized service to connect with verified astrologers for accurate predictions and remedial solutions.</p>
        </div>

        <div class="row g-4">
          <!-- Service 1: Janam Kundli -->
          <div class="col-lg-4 col-md-6 col-12">
            <div class="service-grid-card">
              <div>
                <div class="service-card-top">
                  <div class="service-card-icon service-icon-kundli">
                    <i class="fa-solid fa-scroll"></i>
                  </div>
                  <span class="service-card-badge">Kundli Report</span>
                </div>
                <h3>Janam Kundli &amp; Birth Chart</h3>
                <p>Complete planetary positions, Lagna chart, Bhavas, and life roadmap analysis with remedies for Manglik &amp; Kaal Sarp doshas.</p>
              </div>
              <a href="/call" class="service-card-link">
                <span>Get Kundli Analysis</span>
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- Service 2: Kundli Matching -->
          <div class="col-lg-4 col-md-6 col-12">
            <div class="service-grid-card">
              <div>
                <div class="service-card-top">
                  <div class="service-card-icon service-icon-milan">
                    <i class="fa-solid fa-heart-circle-check"></i>
                  </div>
                  <span class="service-card-badge">Matchmaking</span>
                </div>
                <h3>Kundli Matching (Milan)</h3>
                <p>Detailed 36 Guna Milan, Ashta Koota assessment, marital compatibility, and relationship harmony remedies for lasting union.</p>
              </div>
              <a href="/chat" class="service-card-link">
                <span>Check Compatibility</span>
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- Service 3: Daily & Yearly Horoscope -->
          <div class="col-lg-4 col-md-6 col-12">
            <div class="service-grid-card">
              <div>
                <div class="service-card-top">
                  <div class="service-card-icon service-icon-horoscope">
                    <i class="fa-solid fa-sun"></i>
                  </div>
                  <span class="service-card-badge">Daily Predictions</span>
                </div>
                <h3>Today's Horoscope &amp; Rashifal</h3>
                <p>Accurate daily, monthly, and annual horoscope predictions for all 12 Zodiac signs covering health, finance, career &amp; love life.</p>
              </div>
              <a href="/chat" class="service-card-link">
                <span>Read Your Horoscope</span>
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- Service 4: Career & Wealth -->
          <div class="col-lg-4 col-md-6 col-12">
            <div class="service-grid-card">
              <div>
                <div class="service-card-top">
                  <div class="service-card-icon service-icon-career">
                    <i class="fa-solid fa-chart-line"></i>
                  </div>
                  <span class="service-card-badge">Career &amp; Wealth</span>
                </div>
                <h3>Career &amp; Financial Guidance</h3>
                <p>Uncover wealth yogas (Dhana Yoga), auspicious business investment timings, job promotion milestones, and financial stability.</p>
              </div>
              <a href="/call" class="service-card-link">
                <span>Consult Career Expert</span>
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- Service 5: Love & Relationships -->
          <div class="col-lg-4 col-md-6 col-12">
            <div class="service-grid-card">
              <div>
                <div class="service-card-top">
                  <div class="service-card-icon service-icon-love">
                    <i class="fa-solid fa-hands-holding-circle"></i>
                  </div>
                  <span class="service-card-badge">Confidential</span>
                </div>
                <h3>Love &amp; Relationship Advice</h3>
                <p>Resolve emotional distance, overcome relationship hurdles, discover marriage timing, and ignite lasting companionship.</p>
              </div>
              <a href="/call" class="service-card-link">
                <span>Talk to Relationship Guru</span>
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          </div>

          <!-- Service 6: Panchang & Muhurat -->
          <div class="col-lg-4 col-md-6 col-12">
            <div class="service-grid-card">
              <div>
                <div class="service-card-top">
                  <div class="service-card-icon service-icon-panchang">
                    <i class="fa-solid fa-calendar-days"></i>
                  </div>
                  <span class="service-card-badge">Auspicious Dates</span>
                </div>
                <h3>Today Panchang &amp; Shubh Muhurat</h3>
                <p>Accurate Tithi, Nakshatra, Yoga, Karana, Choghadiya, and Rahu Kaal to plan auspicious events, weddings, and business launches.</p>
              </div>
              <a href="/chat" class="service-card-link">
                <span>Find Shubh Muhurat</span>
                <i class="fa-solid fa-arrow-right"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>'''
    content = content[:m_about.start()] + new_about + content[m_about.end():]
    print('3. Services section (#about) updated successfully')
else:
    print('Warning: Services section (#about) not found')

# 4. Update How It Works and App Screens sections (Fixing nested section bug and updating Store Badges)
# Find from <section id="services" to </section> before <section class="gap no-top section-client">
services_to_client_pattern = re.compile(
    r'<section\s+id="services".*?(?=<section class="gap no-top section-client">)',
    re.DOTALL
)
m_serv = services_to_client_pattern.search(content)
if m_serv:
    new_services_and_app = '''<section
      id="services"
      class="gap how-it-works"
      style="background-image: url(assets/img/shaps-bg.png)"
    >
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-6">
            <div class="heading two sec-title-animation animation-style2">
              <span class="title-animation">How do you get started?</span>
              <h2 class="title-animation">Live Consultation Sessions</h2>
              <p>Bring Peace, Prosperity, And Positivity Into Your Life with 3 Easy Steps!</p>
            </div>
            <ul class="chek">
              <li>
                <img src="assets/img/chek.png" alt="img" />Now you can Call,
                Chat &amp; have a Live Session with our Best in Class Jyotishi in
                an Instant.
              </li>
              <li>
                <img src="assets/img/chek.png" alt="img" />Astrological
                compatibility: Discuss compatibility between two Vedic Charts to
                understand strengths and challenges in your relationships.
              </li>
              <li>
                <img src="assets/img/chek.png" alt="img" />Birth chart analysis:
                Personalized insights into your astrological profile based on your
                date, time, and place of birth.
              </li>
              <li>
                <img src="assets/img/chek.png" alt="img" />Live Stream Connect:
                Participate in real-time Q&amp;A sessions via Live Stream and get all
                your life clarifications answered.
              </li>
            </ul>
          </div>
          <div class="col-lg-6">
            <div class="hiw-step-card">
              <div class="hiw-step-num">1</div>
              <div class="hiw-step-content">
                <h4>Select Your Verified Jyotishi</h4>
                <p>Browse 500+ certified Vedic astrologers, check their specialties, user reviews, languages, and ratings.</p>
              </div>
            </div>

            <div class="hiw-step-card">
              <div class="hiw-step-num">2</div>
              <div class="hiw-step-content">
                <h4>Choose Consultation Mode</h4>
                <p>Connect instantly in under 60 seconds via 1-on-1 private voice call or live chat. First 5 mins are free!</p>
              </div>
            </div>

            <div class="hiw-step-card">
              <div class="hiw-step-num">3</div>
              <div class="hiw-step-content">
                <h4>Receive Predictions &amp; Vedic Remedies</h4>
                <p>Get accurate life answers, actionable guidance, and personalized remedial solutions for peace and prosperity.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Our Mobile App Section with Upgraded Official Google Play & App Store Badges -->
    <section class="gap" id="app-screens" style="background-image: url(assets/img/shaps-bg.png)">
      <div class="container">
        <div class="heading sec-title-animation animation-style2 text-center">
          <span class="title-animation">Our Mobile App</span>
          <h2 class="title-animation">Download &amp; Explore Our App</h2>
          <p>Consult, chat, call, and connect with trusted astrologers — anytime, anywhere, right from your phone.</p>
        </div>

        <div class="row align-items-center">
          <!-- Left: feature highlights -->
          <div class="col-lg-5">
            <ul class="chek">
              <li>
                <img src="assets/img/chek.png" alt="img" />Chat, Call &amp; Video with expert Jyotishi instantly.
              </li>
              <li>
                <img src="assets/img/chek.png" alt="img" />Get your Free Kundli &amp; personalized birth chart analysis.
              </li>
              <li>
                <img src="assets/img/chek.png" alt="img" />Simple wallet recharge — pay only for what you use.
              </li>
              <li>
                <img src="assets/img/chek.png" alt="img" />Daily Horoscope &amp; Panchang updates, right on your home screen.
              </li>
            </ul>

            <!-- Upgraded Google Play & App Store Badges with Authentic Vector Icons -->
            <div class="store-badges">
              <!-- Official Google Play Badge -->
              <a class="store-badge store-badge-google" href="https://play.google.com/store" target="_blank" rel="noopener" aria-label="Get it on Google Play">
                <div class="store-badge-icon">
                  <svg class="store-svg play-svg" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <defs>
                      <linearGradient id="gpGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="#00A0FF"/>
                        <stop offset="100%" stop-color="#00D7FF"/>
                      </linearGradient>
                      <linearGradient id="gpGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#FF3A44"/>
                        <stop offset="100%" stop-color="#C31162"/>
                      </linearGradient>
                      <linearGradient id="gpGrad3" x1="0%" y1="100%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#00E676"/>
                        <stop offset="100%" stop-color="#00D05A"/>
                      </linearGradient>
                      <linearGradient id="gpGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="#FFE000"/>
                        <stop offset="100%" stop-color="#FF9C00"/>
                      </linearGradient>
                    </defs>
                    <path fill="url(#gpGrad1)" d="M54.1 36.9C51.5 45.4 50 56.4 50 70.3v371.4c0 13.9 1.5 24.9 4.1 33.4l1.8 1.8 208.5-208.5v-4.9L55.9 35.1l-1.8 1.8z"/>
                    <path fill="url(#gpGrad4)" d="M333.6 231.8l-69.2-69.2v-4.9l69.2-69.2 1.6.9 82.2 46.7c23.5 13.3 23.5 35.2 0 48.6l-82.2 46.7-1.6.4z"/>
                    <path fill="url(#gpGrad2)" d="M335.2 279.7L264.4 209 54.1 419.3c7.7 8.2 20.4 9.2 34.6 1.1l246.5-140.7z"/>
                    <path fill="url(#gpGrad3)" d="M335.2 138.3L88.7 9.6C74.5 1.5 61.8 2.5 54.1 10.7L264.4 221l70.8-70.7-0.0 -12z"/>
                  </svg>
                </div>
                <div class="store-badge-text">
                  <small>GET IT ON</small>
                  <strong>Google Play</strong>
                </div>
              </a>

              <!-- Official Apple App Store Badge with Iconic App Store 'A' Emblem -->
              <a class="store-badge store-badge-apple" href="https://www.apple.com/app-store/" target="_blank" rel="noopener" aria-label="Download on the App Store">
                <div class="store-badge-icon">
                  <svg class="store-svg appstore-svg" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <path fill="#0D84F8" d="M400 32H48C21.5 32 0 53.5 0 80v352c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V80c0-26.5-21.5-48-48-48z"/>
                    <path fill="#FFFFFF" d="M127 384.5c-5.5 9.6-17.8 12.8-27.3 7.3-9.6-5.5-12.8-17.8-7.3-27.3l14.3-24.7c16.1-4.9 29.3-1.1 39.6 11.4L127 384.5zm138.9-53.9H84c-11 0-20-9-20-20s9-20 20-20h51l65.4-113.2-20.5-35.4c-5.5-9.6-2.2-21.8 7.3-27.3 9.6-5.5 21.8-2.2 27.3 7.3l8.9 15.4 8.9-15.4c5.5-9.6 17.8-12.8 27.3-7.3 9.6 5.5 12.8 17.8 7.3 27.3l-85.8 148.6h62.1c20.2 0 31.5 23.7 22.7 40zm98.1 0h-29l19.6 33.9c5.5 9.6 2.2 21.8-7.3 27.3-9.6 5.5-21.8 2.2-27.3-7.3-32.9-56.9-57.5-99.7-74-128.1-16.7-29-4.8-58 7.1-67.8 13.1 22.7 32.7 56.7 58.9 102h52c11 0 20 9 20 20 0 11.1-9 20-20 20z"/>
                  </svg>
                </div>
                <div class="store-badge-text">
                  <small>Download on the</small>
                  <strong>App Store</strong>
                </div>
              </a>
            </div>
            <div class="store-trust-meta">
              <span class="store-stars"><i class="fa-solid fa-star"></i> 4.8 Rating</span>
              <span class="store-meta-divider">•</span>
              <span>50K+ Downloads</span>
              <span class="store-meta-divider">•</span>
              <span>100% Free App</span>
            </div>
          </div>

          <!-- Right: app screenshots -->
          <div class="col-lg-7 mt-5 mt-lg-0">
            <div class="row justify-content-center app-screens-row">
              <div class="col-6 col-md-3">
                <div class="app-screen-card">
                  <img src="assets/img/screenshot1.jpeg" alt="App Screen 1" class="img-fluid" />
                </div>
              </div>
              <div class="col-6 col-md-3">
                <div class="app-screen-card app-screen-mid">
                  <img src="assets/img/screenshot2.jpeg" alt="App Screen 2" class="img-fluid" />
                </div>
              </div>
              <div class="col-6 col-md-3">
                <div class="app-screen-card app-screen-mid">
                  <img src="assets/img/screenshot3.jpeg" alt="App Screen 3" class="img-fluid" />
                </div>
              </div>
              <div class="col-6 col-md-3">
                <div class="app-screen-card">
                  <img src="assets/img/screenshot4.jpeg" alt="App Screen 4" class="img-fluid" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <ul class="shaps-img">
        <li><img src="assets/img/shaps-2.png" alt="img" /></li>
      </ul>
    </section>

    '''
    content = content[:m_serv.start()] + new_services_and_app + content[m_serv.end():]
    print('4. How It Works and App Screens (including Store Badges) updated successfully')
else:
    print('Warning: services_to_client_pattern not found')

# 5. Fix Contact ID in footer widget so #contact navigates smoothly
content = re.sub(r'<div class="col-lg-4 col-md-6">\s*<div class="widget-title">\s*<h3>Contact Us</h3>',
                 r'<div class="col-lg-4 col-md-6" id="contact">\n            <div class="widget-title">\n              <h3>Contact Us</h3>',
                 content)

with open('c:/Users/Admin/Desktop/jotishvani 2/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('All updates completed successfully!')
