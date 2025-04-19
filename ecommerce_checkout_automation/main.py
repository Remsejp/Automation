import time # Librería para poder usar el sleep o tiempo de espera antes de seguir la ejecución del programa o script
from selenium import webdriver # con webdriver puedo llamar al metodo ChromeOptions() que me permite darle opciones al navegador
from selenium.webdriver.chrome.service import Service # Con esto puedo instalar el driver de google chrome sin necesidad de hacer busqueda manual
from webdriver_manager.chrome import ChromeDriverManager # Se necesita una version de chrome para hacer toda la automatización
from selenium.webdriver import Chrome # Con esto puedo abrir el navegador de google chrome

from selenium.webdriver.common.by import By # Con esto puedo buscar un elemento por su id, clases, atributos, usando xpath sinstaxis de selenium
from selenium.webdriver.support import expected_conditions as EC # Con esto puedo esperar a que un elemento este disponible para poder interactuar con el
from selenium.webdriver.support.ui import WebDriverWait # Con esto puedo esperar a que un elemento este disponible para poder interactuar con el

# Definir variables globales
USER = "standard_user" # Usuario por defecto
PASSWORD = "secret_sauce" # Contraseña por defecto
URL = "https://www.saucedemo.com" # URL por defecto

# Definicimos la funcion main, que es la que se va a ejecutar al correr el programa
def main():
    service = Service(ChromeDriverManager().install())
    options  = webdriver.ChromeOptions() # Con esto puedo darle algunos parametros a mi navegador, como lo es automizar en un segundo plano
    # Agrego opciones para omitir un error que ocurría al momento que se abría una pestaña emergente que interrumpía las opciones de clics
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # Abrir sin sesión de Google activa
    options.add_argument("--guest")  
    # option.add_argument("--headless") # Con esto puedo abrir el navegador en segundo plano o no se va a abrir ninguna ventana
    options.add_argument("--window-size=1920,1080") # Con esto puedo darle un tamaño a la ventana del navegador
    
    # Ahora vamos a crear nuestro navegador con el servicio y las opciones que le dimos antes
    driver  = Chrome(service=service, options=options) # Con esto creamos el navegador y le pasamos el servicio y las opciones que le dimos antes
    

    try:
        driver.get(URL) # Con esto le decimos al navegador que abra la pagina de google
        # Ahora queremos que nuestro driver vaya a encontrar algun o algunos objetos
        # y que los almacene en una variable, para luego poder interactuar con ellos
        user_input     = driver.find_element(By.ID, "user-name").send_keys(USER) # Con esto le decimos al navegador que busque el elemento por su id y le enviamos el usuario; o rellenamos el input
        password_input = driver.find_element(By.ID, "password").send_keys(PASSWORD) # Con esto le decimos al navegador que busque el elemento por su id y le enviamos la contraseña; o rellenamos el input
        login_button   = driver.find_element(By.ID, "login-button").click() # Con esto le decimos al navegador que busque el elemento por su id y le enviamos el click; o hacemos click en el boton de login
        
        # Una vez ingresdos, procedemos a realizar la comrpa de dos articulos ubicados dentro de la tienda, agregamos 2 articulos al carrito
        buy1_button    = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        buy1_button    = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

        # Ahora abro lo contenido en el carrito
        shoppingcar_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()

        # Genero opción para ya pagar definitivamente, o conocido como checkout
        shoppingcar_button = driver.find_element(By.ID, "checkout").click()
        firstname_input    = driver.find_element(By.XPATH, '//input[@id="first-name"]').send_keys("Pedro")
        lastname_input     = driver.find_element(By.XPATH, '//input[@id="last-name"]').send_keys("Marino")
        postalcode_input   = driver.find_element(By.XPATH, '//input[@id="postal-code"]').send_keys("111131")
        continue_button    = driver.find_element(By.ID, "continue").click() #
        
        # Por ultimo se selecciona el boton FINISH
        finish_button    = driver.find_element(By.ID, "finish").click()
    except Exception as e:
        print("❌ Ocurrió un error durante la automatización:")
        print(f"Error: {e}")
    finally:
        driver.quit() # Con esto cerramos el navegador, si no lo hacemos se queda abierto y no se cierra nunca
        print("🧹 Navegador cerrado correctamente.")


    # time.sleep(14)
    

if __name__ == "__main__":
    main()