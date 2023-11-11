import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Web Browser with Selenium")
        self.setGeometry(100, 100, 1024, 768)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.browser_widget = QWebEngineView()
        self.layout.addWidget(self.browser_widget)

        self.init_selenium_browser()

    def init_selenium_browser(self):
        # Set up a Selenium-controlled browser
        chrome_driver_path = (
            "path_to_chromedriver"  # Replace with the path to your ChromeDriver
        )
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--enable-automation")
        options.add_argument("--enable-infobars")
        options.add_argument("--enable-web-security")
        options.add_argument("--enable-site-isolation-trials")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--enable-features=IsolateOrigins,site-per-process")
        options.add_argument("--no-sandbox")
        options.add_argument("--enable-features=site-per-process")
        options.add_argument("--enable-dev-shm-usage")
        options.add_argument("--start-maximized")
        options.add_argument("--enable-precise-memory-info")
        options.add_argument("--enable-popup-blocking")
        options.add_argument("--enable-default-apps")
        options.add_argument("--enable-logging")
        options.add_argument("--log-level=0")
        options.add_argument("--enable-notifications")
        options.add_argument("--enable-password-autofill-public-suffix-domain-matching")
        options.add_argument("--enable-password-separate-domains")
        options.add_argument("--enable-password-generation")
        options.add_argument("--enable-save-password-bubble")
        options.add_argument("--enable-save-password-for-http-forms")
        options.add_argument("--enable-extensions")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--ignore-urlfetcher-cert-requests")
        options.add_argument("--enable-popup-blocking")
        options.add_argument("--enable-software-rasterizer")
        options.add_argument("--enable-dev-shm-usage")
        options.add_argument("--enable-gpu")
        options.add_argument("--enable-canvas-aa")
        options.add_argument("--enable-2d-canvas-aa")
        options.add_argument("--enable-remote-fonts")
        options.add_argument("--enable-software-draw-with-physical-pixel-quad-ops")
        options.add_argument("--enable-features=NetworkService,NetworkServiceInProcess")
        options.add_argument("--enable-sandbox")
        options.add_argument("--enable-setuid-sandbox")
        options.add_argument("--enable-webgl")
        options.add_argument("--enable-xss-auditor")
        options.add_argument("--enable-client-side-phishing-detection")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--enable-webgl-image-chromium")
        options.add_argument("--enable-webgl-image-chromium-drawing-buffers")
        options.add_argument("--enable-webgl-image-chromium-mailbox")
        options.add_argument("--enable-3d-apis")
        options.add_argument("--enable-databases")
        options.add_argument("--enable-key-system-support")
        options.add_argument("--enable-presentation-api")
        options.add_argument("--enable-renderer-accessibility")
        options.add_argument("--safebrowsing-enable-auto-update")
        options.add_argument("--remote-debugging-port=0")
        options.add_argument("--no-first-run")
        options.add_argument("--no-service-autorun")
        options.add_argument("--enable-extensions")
        options.add_argument("--enable-component-extensions-with-background-pages")
        options.add_argument("--enable-default-apps")
        options.add_argument("--no-sandbox")
        options.add_argument("--enable-sync")
        options.add_argument("--enable-setuid-sandbox")
        options.add_argument("--enable-background-networking")
        options.add_argument("--enable-default-apps")
        options.add_argument("--enable-translate")
        options.add_argument("--enable-extensions")
        options.add_argument("--enable-accelerated-video-decode")
        options.add_argument("--enable-app-list-dismiss-on-blur")
        options.add_argument("--enable-accelerated-video-decode")
        options.add_argument("--enable-accelerated-video-encode")
        options.add_argument("--enable-software-rasterizer")
        options.add_argument("--enable-software-draw-with-physical-pixel-quad-ops")
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(service=service, options=options)

        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("https://member.daraz.lk/user/login")  # Load a webpage

        # Wait for the page to load
        time.sleep(5)  # Adjust the waiting time as needed

        # Get the HTML content from Selenium and display it in the QWebEngineView
        page_content = self.driver.page_source
        self.browser_widget.setHtml(page_content)

        btniID = ".mod-third-party-login-google"
        googleLogBtn = self.driver.find_element(By.CSS_SELECTOR, value=btniID)
        googleLogBtn.click()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebBrowser()
    window.show()
    sys.exit(app.exec_())
