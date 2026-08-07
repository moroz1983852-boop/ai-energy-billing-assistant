# ⚡ AI Energy Billing Assistant

Full-Stack-Webanwendung zur Automatisierung der Kundenbetreuung eines Energieunternehmens. 
Das System berechnet die Ausstände von Nutzern über MySQL und generiert personalisierte Zahlungserinnerungen mithilfe der Gemini KI.

## 🛠 Technologiestack
* **Backend:** Python 3.13, FastAPI, Pydantic, Uvicorn
* **Datenbank:** MySQL, PyMySQL
* **KI-Integration:** Google Gemini API
* **Frontend:** HTML5, CSS3, JavaScript (Async/Await, Fetch API)

## 🚀 Funktionen
- 🔍 **Schuldenprüfung:** Automatische Berechnung von Rückständen mittels SQL-Abfrage (`SUM`).
- 🤖 **KI-Assistent:** Generierung von personalisierten E-Mails auf Deutsch via Gemini API.
- 👤 **Registrierung:** Anlegen neuer Kunden mit Validierung der E-Mail-Eindeutigkeit.

---

## 🚀 Installation & Start

1. **Repository klonen:**
   ```bash
   git clone [https://github.com/moroz1983852-boop/ai-energy-billing.git](https://github.com/moroz1983852-boop/ai-energy-billing.git)
   cd ai-energy-billing