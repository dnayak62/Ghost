pip install Flask
mkdir copernic-space-landing
cd copernic-space-landing
mkdir static
mkdir static/css
mkdir templates
touch app.py
touch templates/index.html
touch static/css/styles.css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Copernic Space - To the Moon…literally!</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>

    <div class="hero">
        <div class="hero-content">
            <h1>To the Moon…literally!</h1>
            <h2>Prepare for Lift-Off: The Future of Space Assets Awaits!</h2>
        </div>
    </div>

    <div class="content">
        <section class="introduction">
            <p>The Copernic Space platform is undergoing a major upgrade as we gear up for the historic 2024 Moon Mission and the first-ever lunar asset sale. Get ready for new features across the platform, including Spaceibles, that will redefine your experience with space assets.</p>
        </section>

        <section class="exclusive-access">
            <h3>Exclusive Access for Registered Users and Passport Holders</h3>
            <p>The current Copernic Space platform is now exclusively available to our passport holders and registered user wallets. This ensures current users can still access their assets and listings while enhancing security and creating a seamless transition for the upgrade of the platform and experience for our monumental 2024 Moon Mission.</p>
        </section>

        <section class="access-instructions">
            <h3>How to Access:</h3>
            <ul>
                <li>Log in here with your previously registered wallet tied to your account.</li>
                <li>Or use your wallet holding your Copernic Space passport(s).</li>
            </ul>
        </section>

        <section class="moon-mission">
            <h3>Be Part of History: 2024 Moon Mission</h3>
            <p>Join us on an extraordinary journey as Copernic Space leads the charge in creating the democratized marketplace for space. Our 2024 Moon Mission will make history and open unprecedented opportunities in space commerce. Participate in the lunar asset sale and own a piece of the Moon! (Sign up for the reserve list to access assets before the public)</p>
            <blockquote>“Embark on an unparalleled voyage with Copernic Space at the forefront of revolutionizing the space market. Our upcoming 2024 Moon Mission isn't just a historic event; it's a gateway to limitless opportunities in space commerce. Secure your place in cosmic history by participating in our lunar asset sale and claiming your very own lunar legacy! Join the reserve list now to seize exclusive access to assets before they're available to the public.”</blockquote>
        </section>

        <section class="contact-info">
            <h3>Need Assistance?</h3>
            <p>Have questions or need assistance? <a href="mailto:contact@copernicspace.com">Contact us here</a> to learn more and stay updated on our exciting journey.</p>
        </section>
    </div>

    <div class="footer">
        <a href="#">Terms of Service</a> | 
        <a href="#">Privacy Policy</a> | 
        <a href="#">Twitter</a> | 
        <a href="#">LinkedIn</a> | 
        <a href="#">Discord</a> | 
        contact@copernicspace.com
    </div>

</body>
</html>
