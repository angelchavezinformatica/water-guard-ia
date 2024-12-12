window.onload = function () {
  actualizarEstado();
  obtenerDatosSensores(); // Cargar los datos de los sensores al inicio
  document
    .getElementById("onButton")
    .addEventListener("click", () => controlBomba("on"));
  document
    .getElementById("offButton")
    .addEventListener("click", () => controlBomba("off"));
  document.getElementById("themeToggle").addEventListener("click", toggleTheme);
};

function controlBomba(action) {
  document.getElementById("loader").style.display = "inline-block";
  const onButton = document.getElementById("onButton");
  const offButton = document.getElementById("offButton");
  onButton.style.display = "none";
  offButton.style.display = "none";

  const url = `/bomb/${action}`;
  fetch(url)
    .then((response) => {
      if (response.ok) {
        actualizarEstado();
      } else {
        alert("Hubo un error al intentar controlar la bomba.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("Hubo un problema con la solicitud.");
    });
}

function actualizarEstado() {
  document.getElementById("loader").style.display = "inline-block";

  fetch("/bomb/state")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("loader").style.display = "none";
      const statusElement = document.getElementById("pumpStatus");
      const onButton = document.getElementById("onButton");
      const offButton = document.getElementById("offButton");

      if (data.state === "true") {
        statusElement.textContent = "Encendida";
        onButton.style.display = "none";
        offButton.style.display = "inline-block";
      } else {
        statusElement.textContent = "Apagada";
        onButton.style.display = "inline-block";
        offButton.style.display = "none";
      }
    })
    .catch((error) => {
      document.getElementById("loader").style.display = "none";
      console.error("Error al obtener el estado:", error);
    });
}

function obtenerDatosSensores() {
  fetch("/sensors/data")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("humidityValue").textContent = `Humedad: ${data.humidity.toFixed(2)}%`;
      document.getElementById("temperatureValue").textContent = `Temperatura: ${data.temperature.toFixed(2)}°C`;
    })
    .catch((error) => {
      console.error("Error al obtener los datos de los sensores:", error);
    });
}

function toggleTheme() {
  const isChecked = document.getElementById("themeToggle").checked;
  document.body.classList.toggle("dark-theme", isChecked);

  const themeLabel = document.getElementById("themeLabel");
  themeLabel.textContent = isChecked
    ? "Cambiar a Tema Claro"
    : "Cambiar a Tema Oscuro";
}

document.body.classList.remove("dark-theme");
