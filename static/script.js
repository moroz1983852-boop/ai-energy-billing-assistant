async function checkStatus() {
    const email = document.getElementById("search-email").value;
    const responseBox = document.getElementById("status-result");

    if (!email) {
        responseBox.innerText = "Bitte geben Sie eine E-Mail-Adresse ein.";
        return;
    }

    responseBox.innerHTML = '<span class="loading">In Verbindung mit KI... Bitte warten...</span>';

    try {
        const response = await fetch(`/ask-ai/${email}`);
        const data = await response.json();

        if (data.error) {
            responseBox.innerText = data.error;
        } else {
            responseBox.innerText = data.assistant_response;
        }
    } catch (error) {
        responseBox.innerText = "Fehler bei der Verbindung zum Server.";
    }
}

async function registerUser() {
    const name = document.getElementById("reg-name").value;
    const email = document.getElementById("reg-email").value;
    const responseBox = document.getElementById("reg-result");

    if (!name || !email) {
        responseBox.innerText = "Bitte füllen Sie alle Felder aus.";
        return;
    }

    responseBox.innerText = "Wird geladen...";

    try {
        const response = await fetch("/add-customer", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name: name, email: email })
        });

        const data = await response.json();

        if (data.error) {
            responseBox.innerText = data.error;
            responseBox.style.color = "#ef4444";
        } else {
            responseBox.innerText = data.message || data.success || "Kunde erfolgreich registriert!";
            responseBox.style.color = "#10b981";
            document.getElementById("reg-name").value = "";
            document.getElementById("reg-email").value = "";
        }
    } catch (error) {
        responseBox.innerText = "Fehler bei der Verbindung zum Server.";
    }
}