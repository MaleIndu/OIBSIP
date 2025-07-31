function getWeather() {
  const city = document.getElementById("cityInput").value;
  const apiKey = "8fc5c39db61af83b70c68d1ad3137f72"; // Replace with your actual API key
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const weatherInfo = `
        <h3>${data.name}</h3>
        <p>Temperature: ${data.main.temp}°C</p>
        <p>Weather: ${data.weather[0].description}</p>
        <p>Humidity: ${data.main.humidity}%</p>
      `;
      document.getElementById("weatherResult").innerHTML = weatherInfo;
    })
    .catch((error) => {
      document.getElementById("weatherResult").innerHTML = `<p>City not found.</p>`;
    });
}
