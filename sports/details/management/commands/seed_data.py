from django.core.management.base import BaseCommand
from details.models import Category, Product

class Command(BaseCommand):
    help = 'Seeds categories and products into the database'

    def handle(self, *args, **options):
        self.stdout.write("Seeding categories and products...")

        categories_data = [
            {
                'name': 'Jersey',
                'slug': 'jersey',
                'department': 'Football',
                'description': 'Official and replica football club jerseys engineered with breathable AEROREADY and Dri-FIT fabrics.',
                'banner_image': 'bg6.jpg'
            },
            {
                'name': 'Football Shoes',
                'slug': 'shoes',
                'department': 'Football',
                'description': 'Engineered football boots and studs for firm ground, turf, and indoor courts with high traction.',
                'banner_image': 'bgfemk.jpg'
            },
            {
                'name': 'Football Accessories',
                'slug': 'accessories',
                'department': 'Football',
                'description': 'Essential football accessories including match balls, gloves, training cones, bags, and protective gear.',
                'banner_image': 'bg4.jpg'
            },
            {
                'name': 'Male Running Shoes',
                'slug': 'male-running',
                'department': 'Running Shoes',
                'description': 'High-performance men’s running shoes with responsive cushioning, energy return, and ergonomic support.',
                'banner_image': 'bgmen.jpg'
            },
            {
                'name': 'Female Running Shoes',
                'slug': 'female-running',
                'department': 'Running Shoes',
                'description': 'Lightweight and supportive women’s running shoes crafted for maximum comfort, mileage, and speed.',
                'banner_image': 'bgwoman.jpg'
            },
            {
                'name': 'Training Men',
                'slug': 'training-men',
                'department': 'Training',
                'description': 'Men’s gym, cardio, and active training apparel made for sweat-wicking durability and freedom of motion.',
                'banner_image': 'bg2.jpg'
            },
            {
                'name': 'Training Women',
                'slug': 'training-women',
                'department': 'Training',
                'description': 'Women’s workout essentials including sports bras, high-waist leggings, tops, and active outer layers.',
                'banner_image': 'bg3.jpg'
            },
            {
                'name': 'Training Kids',
                'slug': 'training-kids',
                'department': 'Training',
                'description': 'Comfortable and rugged athletic wear for active boys and girls of all age groups.',
                'banner_image': 'bgkid.jpg'
            },
        ]

        cat_objs = {}
        for cdata in categories_data:
            cat, created = Category.objects.update_or_create(
                slug=cdata['slug'],
                defaults={
                    'name': cdata['name'],
                    'department': cdata['department'],
                    'description': cdata['description'],
                    'banner_image': cdata['banner_image'],
                }
            )
            cat_objs[cdata['slug']] = cat

        products_data = [
            # Jerseys
            {'category': 'jersey', 'name': 'Real Madrid Home Jersey 24/25', 'slug': 'real-madrid-jersey', 'brand': 'Adidas', 'price': 80.00, 'original_price': 110.00, 'image_name': 'RM.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': True, 'desc': 'Official Real Madrid home kit with iconic gold and white trim.'},
            {'category': 'jersey', 'name': 'Juventus Turin Home Jersey', 'slug': 'juventus-jersey', 'brand': 'Adidas', 'price': 80.00, 'original_price': 105.00, 'image_name': 'JUV.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': True, 'desc': 'Classic black and white striped Bianconeri kit with breathable mesh.'},
            {'category': 'jersey', 'name': 'Manchester United Home Jersey', 'slug': 'manchester-united-jersey', 'brand': 'Adidas', 'price': 80.00, 'original_price': 110.00, 'image_name': 'MU.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': True, 'desc': 'Red Devils authentic home match edition with moisture-wicking technology.'},
            {'category': 'jersey', 'name': 'Paris Saint-Germain Home Kit', 'slug': 'psg-jersey', 'brand': 'Nike', 'price': 80.00, 'original_price': 115.00, 'image_name': 'PSG.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': False, 'desc': 'Parisian style meets elite athletic performance with midnight navy fabric.'},
            {'category': 'jersey', 'name': 'Manchester City Sky Blue Jersey', 'slug': 'manchester-city-jersey', 'brand': 'Puma', 'price': 80.00, 'original_price': 100.00, 'image_name': 'MC.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': False, 'desc': 'Premier champions edition crafted with ultra-light dryCELL material.'},
            {'category': 'jersey', 'name': 'Tottenham Hotspur Home Jersey', 'slug': 'tottenham-jersey', 'brand': 'Nike', 'price': 80.00, 'original_price': 95.00, 'image_name': 'TOT.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': False, 'desc': 'Crisp Lilywhites jersey featuring contrast collar and ergonomic seams.'},
            {'category': 'jersey', 'name': 'Liverpool FC Stadium Jersey', 'slug': 'liverpool-jersey', 'brand': 'Nike', 'price': 80.00, 'original_price': 110.00, 'image_name': 'LIV.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': True, 'desc': 'You’ll Never Walk Alone in this bold crimson Liverpool stadium edition.'},
            {'category': 'jersey', 'name': 'Celtic FC Striped Kit', 'slug': 'celtic-jersey', 'brand': 'Adidas', 'price': 80.00, 'original_price': 90.00, 'image_name': 'CEL.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': False, 'desc': 'Timeless green and white hoops design engineered for matchday.'},
            {'category': 'jersey', 'name': 'Arsenal Gunners Home Jersey', 'slug': 'arsenal-jersey', 'brand': 'Adidas', 'price': 80.00, 'original_price': 110.00, 'image_name': 'ARS.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': True, 'desc': 'Gunners home jersey with gold cannon crest and AEROREADY fabric.'},
            {'category': 'jersey', 'name': 'FC Barcelona Blaugrana Jersey', 'slug': 'barcelona-jersey', 'brand': 'Nike', 'price': 85.00, 'original_price': 120.00, 'image_name': 'FCB.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': True, 'desc': 'Iconic deep royal blue and noble red Catalan crest edition.'},
            {'category': 'jersey', 'name': 'Chelsea FC Pride of London', 'slug': 'chelsea-jersey', 'brand': 'Nike', 'price': 80.00, 'original_price': 105.00, 'image_name': 'CHL.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': False, 'desc': 'Royal blue Chelsea jersey with sleek textured geometric pattern.'},
            {'category': 'jersey', 'name': 'Atletico Madrid Home Jersey', 'slug': 'atletico-madrid-jersey', 'brand': 'Nike', 'price': 80.00, 'original_price': 100.00, 'image_name': 'ATH.jpg', 'sizes': 'XS,S,M,L,XL', 'is_featured': False, 'desc': 'Rojiblancos red and white striped match jersey.'},

            # Football Shoes
            {'category': 'shoes', 'name': 'dSports Victory FG Boot', 'slug': 'dsports-victory-fg', 'brand': 'dSports', 'price': 347.56, 'original_price': 420.00, 'image_name': 'FS1.jpg', 'sizes': '8,9,10,11,12', 'is_featured': True, 'desc': 'Elite firm-ground football boots with carbon-fiber speed plate.'},
            {'category': 'shoes', 'name': 'dSports BigBang Strike', 'slug': 'dsports-bigbang-strike', 'brand': 'dSports', 'price': 260.25, 'original_price': 310.00, 'image_name': 'FS2.jpg', 'sizes': '8,9,10,11,12', 'is_featured': False, 'desc': 'Explosive acceleration studs with textured 3D touch control zone.'},
            {'category': 'shoes', 'name': 'dSports Vision Control', 'slug': 'dsports-vision-control', 'brand': 'dSports', 'price': 302.40, 'original_price': 380.00, 'image_name': 'FS3.jpg', 'sizes': '8,9,10,11,12', 'is_featured': True, 'desc': 'Playmaker cleat engineered for deadly precision and spin.'},
            {'category': 'shoes', 'name': 'dSports Dragon Elite', 'slug': 'dsports-dragon-elite', 'brand': 'dSports', 'price': 210.00, 'original_price': 260.00, 'image_name': 'FS4.jpg', 'sizes': '8,9,10,11,12', 'is_featured': False, 'desc': 'Aggressive traction studs for quick cuts and lightning speed.'},
            {'category': 'shoes', 'name': 'dSports King Classic Leather', 'slug': 'dsports-king-classic', 'brand': 'dSports', 'price': 371.76, 'original_price': 450.00, 'image_name': 'FS5.jpg', 'sizes': '8,9,10,11,12', 'is_featured': True, 'desc': 'Premium kangaroo leather upper with timeless comfort and soft touch.'},
            {'category': 'shoes', 'name': 'dSports Jaguar Speed Pro', 'slug': 'dsports-jaguar-speed', 'brand': 'dSports', 'price': 283.40, 'original_price': 340.00, 'image_name': 'FS6.jpg', 'sizes': '8,9,10,11,12', 'is_featured': False, 'desc': 'Ultra-lightweight sprint boots built for forwards and wingers.'},
            {'category': 'shoes', 'name': 'dSports Phantom Strike', 'slug': 'dsports-phantom-strike', 'brand': 'dSports', 'price': 295.00, 'original_price': 360.00, 'image_name': 'FS7.jpg', 'sizes': '8,9,10,11,12', 'is_featured': False, 'desc': 'Ghost lace system with all-weather control surface.'},
            {'category': 'shoes', 'name': 'dSports Mercurial Blade', 'slug': 'dsports-mercurial-blade', 'brand': 'dSports', 'price': 320.00, 'original_price': 399.00, 'image_name': 'FS8.jpg', 'sizes': '8,9,10,11,12', 'is_featured': False, 'desc': 'Aerodynamic contouring designed for pure velocity.'},
            {'category': 'shoes', 'name': 'dSports Predator Precision', 'slug': 'dsports-predator-precision', 'brand': 'dSports', 'price': 350.00, 'original_price': 430.00, 'image_name': 'FS9.jpg', 'sizes': '8,9,10,11,12', 'is_featured': True, 'desc': 'Rubber strike elements for ultimate swerve and power shots.'},

            # Football Accessories
            {'category': 'accessories', 'name': 'Nike Strike Match Ball', 'slug': 'nike-strike-match-ball', 'brand': 'Nike', 'price': 89.00, 'original_price': 120.00, 'image_name': 'nikefootball.jpg', 'sizes': 'Size 4,Size 5', 'is_featured': True, 'desc': 'FIFA Quality Pro certified match ball with textured casing.'},
            {'category': 'accessories', 'name': 'Adidas League Football', 'slug': 'adidas-league-football', 'brand': 'Adidas', 'price': 75.00, 'original_price': 95.00, 'image_name': 'football.jpg', 'sizes': 'Size 4,Size 5', 'is_featured': False, 'desc': 'Seamless thermally bonded surface for predictable trajectory.'},
            {'category': 'accessories', 'name': 'New Balance Elite Ball', 'slug': 'nb-elite-ball', 'brand': 'New Balance', 'price': 70.00, 'original_price': 88.00, 'image_name': 'nbfootball.jpg', 'sizes': 'Size 5', 'is_featured': False, 'desc': 'High-rebound rubber bladder and reinforced outer panels.'},
            {'category': 'accessories', 'name': 'dSports Pro Goalkeeper Gloves', 'slug': 'dsports-pro-gk-gloves', 'brand': 'dSports', 'price': 50.00, 'original_price': 65.00, 'image_name': 'keepinggloves.jpg', 'sizes': '7,8,9,10', 'is_featured': True, 'desc': '4mm Contact Latex palm for supreme grip in wet or dry conditions.'},
            {'category': 'accessories', 'name': 'Pro Athletic Sports Bag', 'slug': 'pro-athletic-sports-bag', 'brand': 'dSports', 'price': 45.00, 'original_price': 60.00, 'image_name': 'bag.jpg', 'sizes': 'One Size', 'is_featured': False, 'desc': 'Water-resistant duffel with dedicated ventilated shoe compartment.'},
            {'category': 'accessories', 'name': 'Hydration Squeeze Water Bottle', 'slug': 'hydration-squeeze-bottle', 'brand': 'dSports', 'price': 18.00, 'original_price': 25.00, 'image_name': 'waterbottle.jpg', 'sizes': '750ml,1000ml', 'is_featured': False, 'desc': 'BPA-free leakproof sports bottle with high-flow valve.'},
            {'category': 'accessories', 'name': 'Sweat Absorbing Wristbands (Pair)', 'slug': 'sweat-wristbands-pair', 'brand': 'dSports', 'price': 15.00, 'original_price': 20.00, 'image_name': 'wristband.jpg', 'sizes': 'Standard', 'is_featured': False, 'desc': 'Thick Terry-cloth cotton wristbands for maximum sweat absorption.'},
            {'category': 'accessories', 'name': 'Cushioned Football Crew Socks', 'slug': 'football-crew-socks', 'brand': 'dSports', 'price': 22.00, 'original_price': 30.00, 'image_name': 'socks.jpg', 'sizes': 'M,L', 'is_featured': False, 'desc': 'Anti-slip grip pads with arch compression support.'},
            {'category': 'accessories', 'name': 'Breathable Athletic Cap', 'slug': 'breathable-athletic-cap', 'brand': 'dSports', 'price': 28.00, 'original_price': 38.00, 'image_name': 'cap.jpg', 'sizes': 'Adjustable', 'is_featured': False, 'desc': 'Laser-perforated running & training cap with UV protection.'},

            # Male Running Shoes
            {'category': 'male-running', 'name': 'Air Speedster Pro Men', 'slug': 'air-speedster-pro-men', 'brand': 'dSports', 'price': 220.00, 'original_price': 280.00, 'image_name': 'MS1.jpg', 'sizes': '8,9,10,11,12', 'is_featured': True, 'desc': 'Dual-density foam cushioning with carbon infused stability plate.'},
            {'category': 'male-running', 'name': 'Sonic Stride Runner', 'slug': 'sonic-stride-runner', 'brand': 'dSports', 'price': 195.00, 'original_price': 240.00, 'image_name': 'MS2.jpg', 'sizes': '8,9,10,11,12', 'is_featured': True, 'desc': 'Breathable engineered mesh with ultra-responsive rebound.'},
            {'category': 'male-running', 'name': 'Aero Glide Velocity Men', 'slug': 'aero-glide-velocity-men', 'brand': 'dSports', 'price': 240.00, 'original_price': 300.00, 'image_name': 'MS3.jpg', 'sizes': '8,9,10,11,12', 'is_featured': False, 'desc': 'Long distance marathon road shoe with plush heel counter.'},
            {'category': 'male-running', 'name': 'Trail Storm Rugged Runner', 'slug': 'trail-storm-rugged-men', 'brand': 'dSports', 'price': 210.00, 'original_price': 260.00, 'image_name': 'MS4.jpg', 'sizes': '8,9,10,11,12', 'is_featured': False, 'desc': 'Deep lugged Vibram-style outsole for gravel, mud, and mountain trails.'},
            {'category': 'male-running', 'name': 'Flyknit Cloudstride Men', 'slug': 'flyknit-cloudstride-men', 'brand': 'dSports', 'price': 255.00, 'original_price': 320.00, 'image_name': 'MS5.jpg', 'sizes': '8,9,10,11,12', 'is_featured': True, 'desc': 'Sock-like woven fit with cloud foam maximum impact protection.'},
            {'category': 'male-running', 'name': 'Endurance Prime Road Shoes', 'slug': 'endurance-prime-road', 'brand': 'dSports', 'price': 180.00, 'original_price': 225.00, 'image_name': 'MS6.jpg', 'sizes': '8,9,10,11,12', 'is_featured': False, 'desc': 'Daily training companion with high abrasion rubber outsole.'},

            # Female Running Shoes
            {'category': 'female-running', 'name': 'Cloudfoam Aura Flow Women', 'slug': 'cloudfoam-aura-women', 'brand': 'dSports', 'price': 215.00, 'original_price': 270.00, 'image_name': 'FMS1.jpg', 'sizes': '5,6,7,8,9', 'is_featured': True, 'desc': 'Soft cushioned lightweight trainer tailored for women’s foot biomechanics.'},
            {'category': 'female-running', 'name': 'Swift Stride Blossom Pink', 'slug': 'swift-stride-pink', 'brand': 'dSports', 'price': 190.00, 'original_price': 235.00, 'image_name': 'FMS2.jpg', 'sizes': '5,6,7,8,9', 'is_featured': True, 'desc': 'Vibrant styling with energy returning EVA midsole and breathable mesh.'},
            {'category': 'female-running', 'name': 'Lunar Glide Comfort Women', 'slug': 'lunar-glide-women', 'brand': 'dSports', 'price': 230.00, 'original_price': 290.00, 'image_name': 'FMS3.jpg', 'sizes': '5,6,7,8,9', 'is_featured': False, 'desc': 'Dynamic arch support preventing overpronation during road runs.'},
            {'category': 'female-running', 'name': 'Infinity Float Runner Women', 'slug': 'infinity-float-women', 'brand': 'dSports', 'price': 245.00, 'original_price': 310.00, 'image_name': 'FMS4.jpg', 'sizes': '5,6,7,8,9', 'is_featured': True, 'desc': 'Maximum cushion rocker geometry for effortless mile transition.'},
            {'category': 'female-running', 'name': 'Flex Motion Trainer Women', 'slug': 'flex-motion-trainer-women', 'brand': 'dSports', 'price': 175.00, 'original_price': 210.00, 'image_name': 'FMS5.jpg', 'sizes': '5,6,7,8,9', 'is_featured': False, 'desc': 'Versatile hybrid shoe ideal for both 5K runs and HIIT workouts.'},
            {'category': 'female-running', 'name': 'Aero Pulse Speed Women', 'slug': 'aero-pulse-speed-women', 'brand': 'dSports', 'price': 205.00, 'original_price': 255.00, 'image_name': 'FMS6.jpg', 'sizes': '5,6,7,8,9', 'is_featured': False, 'desc': 'Featherweight racer engineered for rapid tempo runs and race days.'},

            # Training Men
            {'category': 'training-men', 'name': 'PowerTech Compression Top Men', 'slug': 'powertech-compression-top-men', 'brand': 'dSports', 'price': 65.00, 'original_price': 85.00, 'image_name': 'TS1.jpg', 'sizes': 'S,M,L,XL,XXL', 'is_featured': True, 'desc': 'Second-skin muscle support with 4-way stretch moisture management.'},
            {'category': 'training-men', 'name': 'Pro Athletic Training Shorts', 'slug': 'pro-training-shorts-men', 'brand': 'dSports', 'price': 50.00, 'original_price': 65.00, 'image_name': 'TS2.jpg', 'sizes': 'S,M,L,XL', 'is_featured': False, 'desc': 'Side slit mobility shorts with zippered phone pocket and liner.'},
            {'category': 'training-men', 'name': 'Core Muscle Tank Top', 'slug': 'core-muscle-tank-men', 'brand': 'dSports', 'price': 42.00, 'original_price': 55.00, 'image_name': 'TS3.jpg', 'sizes': 'S,M,L,XL', 'is_featured': False, 'desc': 'Deep cut armholes for full range of motion during heavy lifts.'},
            {'category': 'training-men', 'name': 'AirFlow Breathable Gym Tee', 'slug': 'airflow-gym-tee-men', 'brand': 'dSports', 'price': 48.00, 'original_price': 60.00, 'image_name': 'TS4.jpg', 'sizes': 'S,M,L,XL,XXL', 'is_featured': True, 'desc': 'Anti-odor treated lightweight performance fabric.'},
            {'category': 'training-men', 'name': 'Tapered Flex Training Pants', 'slug': 'tapered-flex-pants-men', 'brand': 'dSports', 'price': 78.00, 'original_price': 98.00, 'image_name': 'TS5.jpg', 'sizes': 'S,M,L,XL', 'is_featured': False, 'desc': 'Ankle-zip athletic sweatpants suitable for warmups and street style.'},
            {'category': 'training-men', 'name': 'StormShield Training Hoodie', 'slug': 'stormshield-training-hoodie', 'brand': 'dSports', 'price': 95.00, 'original_price': 130.00, 'image_name': 'TS6.jpg', 'sizes': 'S,M,L,XL,XXL', 'is_featured': True, 'desc': 'Thermal fleece lined workout hoodie with water-repellent coating.'},

            # Training Women
            {'category': 'training-women', 'name': 'Seamless Sculpt Workout Tee', 'slug': 'seamless-sculpt-tee-women', 'brand': 'dSports', 'price': 55.00, 'original_price': 70.00, 'image_name': 'TSF1.jpg', 'sizes': 'XS,S,M,L', 'is_featured': True, 'desc': 'Body-hugging seamless knit that eliminates chafing during intense routines.'},
            {'category': 'training-women', 'name': 'High-Rise Squat-Proof Leggings', 'slug': 'high-rise-leggings-women', 'brand': 'dSports', 'price': 72.00, 'original_price': 95.00, 'image_name': 'TSF2.jpg', 'sizes': 'XS,S,M,L', 'is_featured': True, 'desc': 'Buttery soft compressive feel with zero roll-down waistband.'},
            {'category': 'training-women', 'name': 'Aerobic Racerback Crop Tank', 'slug': 'aerobic-crop-tank-women', 'brand': 'dSports', 'price': 38.00, 'original_price': 50.00, 'image_name': 'TSF3.jpg', 'sizes': 'XS,S,M,L', 'is_featured': False, 'desc': 'Quick-drying stretch cropped workout tank.'},
            {'category': 'training-women', 'name': 'Active Flex 2-in-1 Shorts', 'slug': 'active-flex-shorts-women', 'brand': 'dSports', 'price': 48.00, 'original_price': 62.00, 'image_name': 'TSF4.jpg', 'sizes': 'XS,S,M,L', 'is_featured': False, 'desc': 'Built-in compression liner with flowing outer shell for maximum confidence.'},
            {'category': 'training-women', 'name': 'High-Impact Sports Bra', 'slug': 'high-impact-sports-bra', 'brand': 'dSports', 'price': 52.00, 'original_price': 68.00, 'image_name': 'TSF5.jpg', 'sizes': 'S,M,L', 'is_featured': True, 'desc': 'Molded cups and adjustable cross straps for high-intensity training.'},
            {'category': 'training-women', 'name': 'Elite Windbreaker Training Jacket', 'slug': 'elite-windbreaker-women', 'brand': 'dSports', 'price': 90.00, 'original_price': 120.00, 'image_name': 'TSF6.jpg', 'sizes': 'XS,S,M,L', 'is_featured': False, 'desc': 'Ultra-packable reflective windbreaker with ventilated back flap.'},

            # Training Kids
            {'category': 'training-kids', 'name': 'Junior Champion Active Tee', 'slug': 'junior-champion-tee', 'brand': 'dSports', 'price': 35.00, 'original_price': 45.00, 'image_name': 'KT1.jpg', 'sizes': 'YS,YM,YL,YXL', 'is_featured': True, 'desc': 'Durable and breathable jersey tee built for energetic young athletes.'},
            {'category': 'training-kids', 'name': 'Youth Athletic Play Shorts', 'slug': 'youth-play-shorts', 'brand': 'dSports', 'price': 30.00, 'original_price': 40.00, 'image_name': 'KT2.jpg', 'sizes': 'YS,YM,YL,YXL', 'is_featured': False, 'desc': 'Elastic drawstring waist with quick-drying lightweight fabric.'},
            {'category': 'training-kids', 'name': 'Kids All-Weather Tracksuit', 'slug': 'kids-tracksuit-set', 'brand': 'dSports', 'price': 75.00, 'original_price': 98.00, 'image_name': 'KT3.jpg', 'sizes': 'YS,YM,YL,YXL', 'is_featured': True, 'desc': 'Full zip jacket and matching pants set for school sports and practice.'},
            {'category': 'training-kids', 'name': 'QuickDry Junior Training Set', 'slug': 'quickdry-junior-set', 'brand': 'dSports', 'price': 58.00, 'original_price': 72.00, 'image_name': 'KT4.jpg', 'sizes': 'YS,YM,YL,YXL', 'is_featured': False, 'desc': 'Two-piece matching top and bottoms engineered for soccer and running.'},
            {'category': 'training-kids', 'name': 'Junior Speedster Long Sleeve', 'slug': 'junior-speedster-long-sleeve', 'brand': 'dSports', 'price': 40.00, 'original_price': 52.00, 'image_name': 'KT5.jpg', 'sizes': 'YS,YM,YL,YXL', 'is_featured': False, 'desc': 'UV sun protection rashguard and cool-weather training top.'},
            {'category': 'training-kids', 'name': 'All-Star Practice Jersey Kids', 'slug': 'all-star-practice-jersey-kids', 'brand': 'dSports', 'price': 38.00, 'original_price': 48.00, 'image_name': 'KT6.jpg', 'sizes': 'YS,YM,YL,YXL', 'is_featured': True, 'desc': 'Mesh ventilation with vibrant athletic trim and durable stitching.'},
        ]

        count = 0
        for pdata in products_data:
            cat = cat_objs.get(pdata['category'])
            if cat:
                Product.objects.update_or_create(
                    slug=pdata['slug'],
                    defaults={
                        'category': cat,
                        'name': pdata['name'],
                        'brand': pdata['brand'],
                        'price': pdata['price'],
                        'original_price': pdata.get('original_price'),
                        'image_name': pdata['image_name'],
                        'available_sizes': pdata['sizes'],
                        'is_featured': pdata['is_featured'],
                        'description': pdata['desc'],
                        'stock': 100,
                    }
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {len(categories_data)} categories and {count} products!"))
