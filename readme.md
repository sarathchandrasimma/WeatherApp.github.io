````markdown
# Weather App 🌦️

Welcome to the Weather App, a Django application that provides weather updates based on the city input. This app also includes dynamically generated affiliate links for products relevant to the current weather conditions.

## Features ✨

- Fetches real-time weather data using the OpenWeatherMap API.
- Displays beautiful images related to the city's weather from Unsplash.
- Provides relevant affiliate links based on the current weather conditions.
- User-friendly interface with responsive design.

## Demo 🎥

![Weather App Demo](assests/demo.gif)

## Getting Started 🚀

Follow these instructions to set up and run the project on your local machine.

### Prerequisites 📋

- Python 3.8+
- Django 3.2+
- A virtual environment tool (like `venv`)

### Installation 🛠️

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/WeatherApp.git
   cd WeatherApp
   ```
````

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**

   - Create a `.env` file in the root directory of the project by copying the example file:

     ```sh
     cp .env.example .env
     ```

   - Open the `.env` file and add your own API keys:

     ```env
     WEATHER_API_KEY=your_actual_weather_api_key
     UNSPLASH_API_KEY=your_actual_unsplash_api_key
     ```

### Running the App ▶️

1. **Apply migrations:**

   ```sh
   python manage.py migrate
   ```

2. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

3. **Open your browser and navigate to:**

   ```
   http://localhost:8000
   ```

## Usage 📝

- Enter the name of a city in the input field and submit.
- View the weather information and related images.
- Check out the suggested affiliate products based on the current weather conditions.

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- [OpenWeatherMap](https://openweathermap.org/) for the weather data API.
- [Unsplash](https://unsplash.com/) for the beautiful images.
- Inspiration and guidance from the Django community.

---

Feel free to improve this project and share your feedback!
