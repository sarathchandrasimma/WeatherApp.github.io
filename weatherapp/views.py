from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
import requests
import datetime
import random


def get_random_image(query):
    unsplash_url = f"https://api.unsplash.com/photos/random?query={query}&client_id={settings.UNSPLASH_ACCESS_KEY}"
    response = requests.get(unsplash_url)
    data = response.json()
    return data['urls']['regular'] if 'urls' in data else ""

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Srikakulam'

    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.WEATHER_API_KEY}'
    weather_params = {'units': 'metric'}

    unsplash_access_key = 'DXm0k47uqZAYlpeGOtFFx49AJ65bVuVYfa8sTytYi9U'

    query = f"{city} landscape"
    image_url = None
    try:
        unsplash_search_url = f"https://api.unsplash.com/search/photos?query={query}&client_id={settings.UNSPLASH_ACCESS_KEY}&orientation=landscape&per_page=30"
        image_data = requests.get(unsplash_search_url).json()
        image_data = requests.get(unsplash_search_url).json()
        results = image_data.get('results')
        if results:
            image_url = random.choice(results)['urls']['regular']
        else:
            image_url = 'https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600'
    except Exception as e:
        print(f"Image fetch error: {e}")
        image_url = 'https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600'

    try:
        weather_data = requests.get(weather_url, params=weather_params).json()
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = datetime.date.today()

        # Affiliate links based on weather condition
        affiliate_links = []
        if 'rain' in description.lower():
            affiliate_links = [
                {'title': 'Buy an Umbrella', 'url': 'https://www.amazon.in/Rylan-Automatic-Umbrellas-Windproof-Umberalla/dp/B0D17WJLLH?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/41ka57bJK4L.jpg'},
                {'title': 'Get a Raincoat', 'url': 'https://www.amazon.in/HACER-Waterproof-Universal-Resistant-Portable/dp/B0C6QWCXJ1?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/41iXZ-+4wHL._SY300_SX300_.jpg'}
            ]
        elif 'clear' in description.lower() or 'sunny' in description.lower():
            affiliate_links = [
                {'title': 'Buy Sunscreen,and protect your beautiful face from sun tan!!', 'url': 'https://www.amazon.in/Derma-Co-Hyaluronic-Sunscreen-Protection/dp/B095CRM8NF?tag=sarath04c-21', 'image':'https://m.media-amazon.com/images/I/41NQN8irrVL._SX300_SY300_QL70_FMwebp_.jpg'}
            ]
        elif 'cold' in description.lower() or temp < 15:
            affiliate_links = [
                {'title': 'Get a Moisturizer', 'url': 'https://www.amazon.in/Moisturizer-Hyaluronic-Hydration-Non-Sticky-Instantly/dp/B09Z6TJP7Y?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/41cwfqxLL4L._SX300_SY300_QL70_FMwebp_.jpg'}
            ]
        elif 'cloud' in description.lower():
            affiliate_links = [
                {'title': 'Are you Feeling cold !!,Buy a Hoodie', 'url': 'https://amzn.to/4aFLfto?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/51-1Kq42BEL._SY879_.jpg'}
            ]
        elif 'snow' in description.lower():
            affiliate_links = [
                {'title': 'Buy Snow Boots', 'url': 'https://amzn.to/4dPvPpk?tag=sarath04c-21', 'image':'https://m.media-amazon.com/images/I/61LL-8KcciL._SY675_.jpg'}
            ]
        elif 'wind' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Windbreaker', 'url': 'https://amzn.to/3R3e5Nx?tag=sarath04c-21', 'image':'https://m.media-amazon.com/images/I/71683ZH6YIL._SX679_.jpg'}
            ]
        elif 'haze' in description.lower():
            affiliate_links = [
                {'title': 'Get an Air Purifier', 'url': 'https://amzn.to/3X10YQG?tag=sarath04c-21', 'image':'https://m.media-amazon.com/images/I/71kd66J0MlL._SY879_.jpg'},
                {'title': 'Wear Anti-Pollution Mask', 'url': 'https://www.amazon.in/OxiClear-OxiMask-Pollution-Mask/dp/B01N952VHF/ref=sr_1_1_sspa?crid=3ITM2GS5M28X8&dib=eyJ2IjoiMSJ9.g648tYGoWCOGbwZnwuxY3sY5Ix7ukc6eWtmLSNRUt_Hu78JMCvnNgmBJM2_vbB58kIetenXPI2CMk3K4LCgc50orskcxtG4USkH9BGVMooAcYZatgteWeb8goOnZ6Z7sB3w-wOA6NUPvK_jv-FBBkMPMcpuofvHyeZf8bag2PtV7Oyrr5QcqnPqKT2bHLBqcciPbZqU4M69o9RPH28w7kKklQZ_diENmVEonprv0O2wYW5leI_e2vxP6z_3lVlUD_6vbi7HtdQ2hAJ-UCuwU0lrRci9V62YlzIs4Y8EiUU4.7_KyMyDmouDGpifEhybz2DYk5cZX5YWJrFwVqi5kci8&dib_tag=se&keywords=anti-pollution+mask&qid=1716883730&sprefix=anti-pollution+mask%2Caps%2C961&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/41j6GUixh4L._SY445_SX342_QL70_FMwebp_.jpg'}
            ]
        elif 'mist' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Warm Jacket', 'url': 'https://amzn.to/4bCAF7M?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/51tlIIuJ3dL._SX679_.jpg'}
            ]
        elif 'drizzle' in description.lower():
            affiliate_links = [
                {'title': 'Get a Waterproof Backpack', 'url': 'https://amzn.to/3wIBsoQ?tag=sarath04c-21', 'image':'https://m.media-amazon.com/images/I/71EbaQCAOFL._SX679_.jpg'}
            ]
        elif 'thunderstorm' in description.lower():
            affiliate_links = [
                {'title': 'Buy Surge Protector', 'url': 'https://amzn.to/44YQKlT?tag=sarath04c-21', 'image':'https://m.media-amazon.com/images/I/313hBb+4rXL._SY300_SX300_.jpg'}
            ]
        elif 'fog' in description.lower():
            affiliate_links = [
                {'title': 'Buy a High Visibility Vest', 'url': 'https://amzn.to/4e0PBhJ?tag=sarath04c-21', 'image':'https://m.media-amazon.com/images/I/412OzF9vRCL._SY445_SX342_QL70_FMwebp_.jpg'}
            ]
        elif 'humid' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Dehumidifier', 'url': 'https://amzn.to/3UYEMUN?tag=sarath04c-21', 'image':' https://m.media-amazon.com/images/I/3103Dh74r5L._SX300_SY300_QL70_FMwebp_.jpg'}
            ]
        elif 'dust' in description.lower():
            affiliate_links = [
                {'title': 'Buy Safety Goggles', 'url': 'https://amzn.to/3Kkx95Z?tag=sarath04c-21', 'image': 'https://m.media-amazon.com/images/I/31nil8LpOtL._SY300_SX300_QL70_FMwebp_.jpg'}
            ]
        elif 'smoke' in description.lower():
            affiliate_links = [
                {'title': 'Buy an Air Quality Monitor', 'url': 'https://amzn.to/3UZJ8Li?tag=sarath04c-21', 'image':' https://m.media-amazon.com/images/I/41KO0vucj9L._SY445_SX342_QL70_FMwebp_.jpg'}
            ]
        elif 'sleet' in description.lower():
            affiliate_links = [
                {'title': 'Buy Insulated Gloves', 'url': 'https://amzn.to/4aHWdyP?tag=sarath04c-21', 'image': get_random_image('insulated gloves')}
            ]
        elif 'blizzard' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Snow Shovel', 'url': 'https://amzn.to/4bWPkun?tag=sarath04c-21', 'image': get_random_image('snow shovel')}
            ]
        elif 'sandstorm' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Dust Mask', 'url': 'https://amzn.to/3Vh8OEC?tag=sarath04c-21', 'image': get_random_image('dust mask')}
            ]
        elif 'tornado' in description.lower():
            affiliate_links = [
                {'title': 'Buy a Safety Helmet', 'url': 'https://amzn.to/4bXRfyN?tag=sarath04c-21', 'image': get_random_image('safety helmet')}
            ]
        elif 'thunder' in description.lower():
            affiliate_links = [
                {'title': 'Buy Ear Protection', 'url': 'https://amzn.to/3KlxoxG?tag=sarath04c-21', 'image':' https://m.media-amazon.com/images/I/51OGBLwDUfL._SX679_.jpg'}
            ]
        elif 'rainbow' in description.lower():
            affiliate_links = [
                {'title': 'Buy Rainbow Wall Decals', 'url': 'https://amzn.to/4dWCY7g?tag=sarath04c-21', 'image': get_random_image('rainbow wall decals')}
            ]
        elif 'northern lights' in description.lower():
            affiliate_links = [
                {'title': 'Get Northern Lights Projector', 'url': 'https://amzn.to/4bBmRdP?tag=sarath04c-21', 'image': get_random_image('northern lights projector')}
            ]
        elif 'frost' in description.lower():
            affiliate_links = [
                {'title': 'Buy Frost Guard Windshield Cover', 'url': 'https://amzn.to/44ZKPgo?tag=sarath04c-21', 'image': get_random_image('frost guard')}
            ]
        elif 'ice' in description.lower():
            affiliate_links = [
                {'title': 'Get Ice Scraper Mitt', 'url': 'https://amzn.to/4bViwlr?tag=sarath04c-21', 'image': get_random_image('ice scraper')}
            ]
        elif 'sunrise' in description.lower():
            affiliate_links = [
                {'title': 'Buy Sunrise Alarm Clock', 'url': 'https://amzn.to/3R4hV9f?tag=sarath04c-21', 'image': get_random_image('sunrise alarm clock')}
            ]
        elif 'sunset' in description.lower():
            affiliate_links = [
                {'title': 'Grab this wonderful sunset lamp ,Have an awesome Evening!', 'url': 'https://amzn.to/3KhMg08?tag=sarath04c-21', 'image': get_random_image('sunset lamp')}
            ]
        elif 'moon' in description.lower():
            affiliate_links = [
                {'title': 'Make some moonlight dinner with your Love!! ,Grab an interestind Moon lamp', 'url': 'https://www.amazon.in/REFULGIX-3D-Moon-Rechargeable-Lamp/dp/B09NRBHC8C?crid=I3LLS1C75DEO&dib=eyJ2IjoiMSJ9.XhmGN61bn8BMYR9H0V7VOfBMlvZbIa4G4T64jbXlGF6LgZzLur3E9LzRnEzmMopk1dm6YeTPD602UrLP6Ux4Sf_T45Tx0JMG4jBRC8whu1Qjd1jkQOVRNf5J2yTo4I8eGxh7VrcFpiXh7PuAXnuZqQomfvOLYysHq1Xf5Te5HCoqPCNc5hsYRGYOTkTGanMe-ZrW6YNEkk_yLIg9lFS2R08QQcwKm_1PDn9q_0R3qM_tcFYGvHZdQcHo8A9JMcNjIiCqzZhctFZz_iOmtHp8LCNNkf2rFSMCKBJxQu8SfQg.Sq8DbaU1FwEXS1rUdcyoNNeevuRkvlvzmWV5g42sk_o&dib_tag=se&keywords=moon+lamp&qid=1716880330&sprefix=moon+lamp%2Caps%2C382&sr=8-6&linkCode=ll1&tag=sarath04c-21&linkId=a18a389e72c668d2d035d7beef80fa04&language=en_IN&ref_=as_li_ss_tl', 'image': get_random_image('moon lamp')}
            ]

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url,
            'affiliate_links': affiliate_links
        })
    
    except KeyError:
        exception_occurred = True
        messages.error(request, 'City information is not available from the Weather API')
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'city': 'Srikakulam',
            'exception_occurred': exception_occurred,
            'image_url': image_url,
            'affiliate_links': []
        })